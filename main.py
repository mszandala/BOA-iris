# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import time
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Wczytanie danych
iris = load_iris()
X, y = iris.data, iris.target


def evaluate_k(k_value, X_local, y_local, cv=5):
    """Oblicza błąd klasyfikacji (1 - dokładność) dla podanej wartości K
    za pomocą walidacji krzyżowej.
    Zwraca korygowaną wartość K (nieparzystą) oraz błąd (1 - accuracy).
    """
    # Jeśli wejście nie jest liczbą (NaN, inf), zwracamy wysoki błąd
    if not np.isfinite(k_value):
        return 1.0, max(1, int(K_min))

    # Oblicz przybliżony rozmiar zbioru treningowego dla danego cv
    n_samples = len(y_local)
    # Dla cv=int zakładamy równy podział; rozmiar treningu to n_samples - (n_samples // cv)
    try:
        n_train = n_samples - (n_samples // int(cv))
    except Exception:
        n_train = max(1, n_samples - 1)

    # Konwersja i nałożenie granic
    k = max(1, int(round(k_value)))
    if k % 2 == 0:
        k += 1

    # Jeśli k jest większe niż prób treningowych, ograniczamy do możliwego maksimum
    if k > n_train:
        # Nie możemy użyć n_neighbors większego niż liczba próbek w zbiorze uczącym
        # Zwracamy wysoki błąd (unikamy wyjątku w cross_val_score)
        return 1.0, n_train if n_train >= 1 else 1

    knn = KNeighborsClassifier(n_neighbors=k)
    try:
        scores = cross_val_score(knn, X_local, y_local, cv=cv, scoring='accuracy')
        mean_accuracy = np.mean(scores)
        error_rate = 1 - mean_accuracy
        # Jeśli otrzymaliśmy NaN w score, potraktuj jako zły wynik
        if not np.isfinite(error_rate):
            return 1.0, k
        return error_rate, k
    except Exception:
        # Jeśli coś pójdzie nie tak (np. ValueError z powodu nieprawidłowego k),
        # zwracamy maksymalny błąd.
        return 1.0, k


# 1. Parametry BOA dla K-NN
N = 5          # Wielkość populacji (ilość mottyli)
MaxIter = 60    # Liczba iteracji BOA
p = 0.2         # Prawdopodobieństwo przełączania (To określa, czy motyl leci w stronę najlepszego motyla (eksploatacja), czy losowo w stronę innych (eksploracja))
alpha = 0.1     # Wykładnik mocy (siła zapachu)
c_init = 0.15   # Współczynnik sensoryczny
K_min = 1       # Minimalna wartość K (Dolna Granica)
K_max = 120      # Maksymalna wartość K (Górna Granica)

def run_boa_for_k(X_local, y_local, N, MaxIter, p, alpha, c_init, K_min, K_max):
    """Prosta implementacja BOA dla doboru parametru K dla KNN.
    Zwraca (best_K, best_error, history)
    """
    # Ustawiamy granicę górną K tak, aby nie przekraczać rozmiaru zbioru treningowego
    n_samples = len(y_local)
    n_train = n_samples - (n_samples // 5)
    safe_K_max = min(K_max, max(1, n_train))

    positions = np.random.uniform(K_min, safe_K_max, N)
    fitness = np.array([evaluate_k(pos, X_local, y_local, cv=5)[0] for pos in positions])
    # Zastąp NaN (np.inf) dużym błędem, by nie psuć wyboru najlepszego
    fitness = np.array([f if np.isfinite(f) else 1.0 for f in fitness])

    best_index = np.argmin(fitness)
    g_star = positions[best_index]
    best_fitness = fitness[best_index]
    best_K = evaluate_k(g_star, X_local, y_local, cv=5)[1]

    c = c_init
    history = []
    positions_history = []
    fitness_history = []


    print(f"\n=== START BOA ===")
    print(f"Początkowy najlepszy K: {best_K:.2f}, błąd: {best_fitness:.4f}\n")

    for t in range(MaxIter):
        c = c_init * (1 - t / MaxIter)  # c maleje z każdą iteracją
        for i in range(N):
            I_i = fitness[i]
            f_i = c * (I_i ** alpha)
            r = np.random.rand()
            x_i_t = positions[i]

            if r < p:
                x_i_next = x_i_t + (r ** 2 * g_star - x_i_t) * f_i
            else:
                candidates = list(range(N))
                candidates.pop(i)
                j, k = np.random.choice(candidates, 2, replace=False)
                x_j_t = positions[j]
                x_k_t = positions[k]
                x_i_next = x_i_t + (r ** 2 * x_j_t - x_k_t) * f_i

            x_i_next = np.clip(x_i_next, K_min, K_max)
            new_error_rate, new_k_value = evaluate_k(x_i_next, X_local, y_local, cv=5)
            if not np.isfinite(new_error_rate):
                new_error_rate = 1.0

            if new_error_rate < fitness[i]:
                positions[i] = x_i_next
                fitness[i] = new_error_rate
                if new_error_rate < best_fitness:
                    best_fitness = new_error_rate
                    g_star = x_i_next
                    best_K = new_k_value

        # 🔹 Komunikaty kontrolne co iterację:
        mean_fitness = np.mean(fitness)
        print(f"Iteracja {t+1}/{MaxIter}: najlepszy_K={best_K:.0f}, "
              f"najlepszy_błąd={best_fitness:.4f}, średni_błąd={mean_fitness:.4f}")

        positions_history.append(positions.copy())
        fitness_history.append(fitness.copy())

        history.append((t, best_K, best_fitness))      

    print("\n=== KONIEC BOA ===")
    print(f"Najlepszy znaleziony K: {best_K:.0f}, końcowy błąd: {best_fitness:.4f}\n")

    return best_K, best_fitness, history, positions_history, fitness_history


if __name__ == '__main__':
    # 1) Baseline: klasyczny KNN (domyślnie n_neighbors)
    baseline_k = 30
    knn_baseline = KNeighborsClassifier(n_neighbors=baseline_k)
    start = time.time()
    baseline_scores = cross_val_score(knn_baseline, X, y, cv=5, scoring='accuracy')
    baseline_mean = float(np.mean(baseline_scores))
    baseline_time = time.time() - start

    # 2) BOA: szukamy najlepszego K
    t0 = time.time()
    best_K, best_error, history, positions_history, fitness_history = run_boa_for_k(
    X, y, N=N, MaxIter=MaxIter, p=p, alpha=alpha, c_init=c_init, K_min=K_min, K_max=K_max
)
    boa_time = time.time() - t0
    best_accuracy = 1 - best_error

    # 3) Porównanie i zapis wyników
    summary_lines = []
    summary_lines.append("=== Porównanie: klasyczny KNN vs BOA-optymalizowany KNN ===")
    summary_lines.append(f"Dataset: Iris ({X.shape[0]} próbek, {X.shape[1]} cech)")
    summary_lines.append("")
    summary_lines.append("-- Klasyczny KNN (baseline)")
    summary_lines.append(f"K (domyślne): {baseline_k}")
    summary_lines.append(f"Średnia dokładność (5-fold CV): {baseline_mean * 100:.2f}%")
    summary_lines.append(f"Czas wykonania: {baseline_time:.2f} s")
    summary_lines.append("")
    summary_lines.append("-- BOA + KNN")
    summary_lines.append(f"Najlepsze K znalezione przez BOA: {best_K}")
    summary_lines.append(f"Średnia dokładność KNN (5-fold CV) z najlepszym K: {best_accuracy * 100:.2f}%")
    summary_lines.append(f"Czas optymalizacji BOA: {boa_time:.2f} s")
    summary_lines.append("")
    diff = (best_accuracy - baseline_mean) * 100
    summary_lines.append(f"Różnica (BOA - baseline): {diff:+.2f} punktów procentowych")

    print("\n".join(summary_lines))
    
    # ============================================
    # 🔹 WYKRESY KONWERGENCJI BOA
    # ============================================

    # Dane do 2D
    iterations = [h[0] for h in history]
    best_K_values = [h[1] for h in history]
    best_errors = [h[2] for h in history]

    # --- (1) K vs Iteracja ---
    plt.figure(figsize=(8, 5))
    plt.plot(iterations, best_K_values, marker='o', color='royalblue')
    plt.title("Zmiana najlepszego K w czasie (BOA)")
    plt.xlabel("Iteracja")
    plt.ylabel("Najlepsze K")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- (2) Błąd vs Iteracja ---
    plt.figure(figsize=(8, 5))
    plt.plot(iterations, best_errors, marker='o', color='tomato')
    plt.title("Zmiana najlepszego błędu w czasie (BOA)")
    plt.xlabel("Iteracja")
    plt.ylabel("Błąd (1 - accuracy)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- (3) 3D: Iteracja - K - Błąd ---
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(N):
        ax.plot(
            range(MaxIter),
            [positions_history[t][i] for t in range(MaxIter)],
            [fitness_history[t][i] for t in range(MaxIter)],
            alpha=0.6
        )

    ax.set_xlabel("Iteracja")
    ax.set_ylabel("Wartość K")
    ax.set_zlabel("Błąd (1 - accuracy)")
    ax.set_title("Ewolucja pozycji motyli (BOA 3D)")
    plt.show()


    try:
        with open("result.txt", "w", encoding="utf-8") as f:
            for ln in summary_lines:
                f.write(ln + "\n")
        print("Wyniki zapisano do result.txt")
    except Exception as e:
        print(f"Nie udało się zapisać wyników do pliku: {e}")