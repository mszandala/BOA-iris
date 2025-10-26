<<<<<<< HEAD
# BOA + KNN (Iris)

Butterfly Optimization Algorithm (BOA) — projekt demonstracyjny optymalizacji parametru K dla klasyfikatora KNN na zbiorze Iris.

Pliki w repozytorium:
- `main.py` — główny skrypt implementujący BOA + KNN
- `requirements.txt` — zależności (numpy, scikit-learn, matplotlib itp.)
- `result.txt` — plik wynikowy generowany przez skrypt

## Jak działa program

Krótki opis działania krok po kroku:

1. Wczytanie danych: skrypt używa wbudowanego zbioru Iris (`sklearn.datasets.load_iris`) i dzieli dane na cechy `X` i etykiety `y`.
2. Baseline: uruchamiany jest klasyczny klasyfikator KNN z wybraną wartością K, by uzyskać punkt odniesienia (accuracy przy 5-fold CV).
3. BOA (Butterfly Optimization Algorithm): prosty algorytm optymalizacyjny przeszukuje przestrzeń wartości parametru K (liczba sąsiadów) i dla każdej kandydatki mierzy błąd klasyfikacji (1 - accuracy) przy użyciu walidacji krzyżowej.
4. Ograniczenia i poprawki: wartość K jest zaokrąglana do liczby nieparzystej, ograniczana do dozwolonego zakresu (np. nie większa niż rozmiar zbioru treningowego), a niepoprawne oceny traktowane są jako wysoki błąd.
5. Wyniki i wykresy: skrypt zapisuje podsumowanie do `result.txt` oraz generuje wykresy (zmiana najlepszego K w czasie, błąd w czasie, przedstawienie 3D ewolucji pozycji motyli).
6. Użyte biblioteki: numpy, scikit-learn, matplotlib.

Sekcja techniczna (wewnętrzne elementy):
- `evaluate_k()` — ocenia jedną kandydacką wartość K używając `cross_val_score`.
- `run_boa_for_k()` — implementacja pętli BOA (populacja, iteracje, eksploatacja/eksploracja, aktualizacja najlepszego rozwiązania).

Możesz zmienić parametry BOA (np. N, MaxIter, p, alpha, c_init, K_min, K_max) bezpośrednio w `main.py`.

## Tabela zmian parametrów 

| Parametr (z przykładem)| Co oznacza | Opis |
|---|---|---|
| N = 10 | Wielkość populacji | To liczba „motyli” – czyli ile różnych propozycji K jednocześnie bada algorytm. <br>🔹 Więcej motyli → więcej pomysłów → większa szansa na dobre rozwiązanie, ale dłuższy czas działania.  <br>Przykład: jeśli N=10, to algorytm jednocześnie testuje 10 różnych wartości K. |
| MaxIter = 35 | Liczba iteracji (rund)| To ile razy motyle będą latać po „świecie rozwiązań”. Każda iteracja to jedna runda, w której motyle próbują się przemieścić i znaleźć lepszy wynik.  <br>🔹 Więcej iteracji → dłuższe, dokładniejsze szukanie, ale większy czas obliczeń. | 
| p = 0.8 | Prawdopodobieństwo przełączania | To określa, czy motyl leci w stronę najlepszego motyla (eksploatacja), czy losowo w stronę innych (eksploracja).  <br>🔹 Jeśli p = 0.8 → 80% czasu motyle idą w stronę najlepszego rozwiązania, 20% czasu błądzą, szukając czegoś nowego.  <br>📘 Dzięki temu algorytm nie utknie w jednym miejscu. |
| alpha = 0.5 | Wykładnik mocy (siła zapachu)| Określa, jak bardzo „zapach” (czyli jakość rozwiązania) wpływa na ruch motyla.<br>🔹 Większe alpha → silniejszy wpływ dobrych rozwiązań (motyle szybciej zbliżają się do najlepszego).<br>🔹 Mniejsze alpha → ruchy są bardziej przypadkowe.|
| c_init = 0.1 | Współczynnik sensoryczny | To początkowa „czułość nosa motyla” 👃🦋 — określa, jak daleko motyl może polecieć.<br>🔹 Duże c_init → motyle latają daleko (więcej eksploracji). <br>🔹 Małe c_init → motyle robią krótkie kroki (dokładniejsze dopieszczanie). <br>📉 Zwykle c maleje z czasem (np. c = c_init * (1 - t/MaxIter)), by na końcu precyzyjnie zbliżyć się do najlepszego wyniku.|
| K_min = 1 | Minimalna wartość K (dolna granica)| To najniższa wartość, jaką może przyjąć K (liczba sąsiadów w KNN).<br>W KNN nie może być 0, więc zwykle zaczynamy od 1. |
| K_max = 70 | Maksymalna wartość K (górna granica) | To najwyższa wartość K, jaką może testować algorytm.<br>🔹 Jeśli dasz bardzo duże K, model KNN stanie się „leniwy” (będzie uśredniał zbyt wiele punktów).<br>🔹 Typowo ustawia się coś między 20 a 100 w zależności od liczby próbek.|



## Clone & run (szybkie kroki)

To repo jest publiczne — jeśli chcesz sklonować i uruchomić projekt lokalnie, wykonaj poniższe kroki.

1. Sklonuj repozytorium (HTTPS):

```bash
git clone https://github.com/mszandala/BOA-iris.git
```

Albo (jeśli wolisz SSH i masz skonfigurowane klucze):

```bash
git clone git@github.com:mszandala/BOA-iris.git
```

2. Przejdź do katalogu projektu:

```bash
cd BOA-iris
```

3. (Opcjonalnie) Utwórz i aktywuj wirtualne środowisko Python:

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

5. Uruchom skrypt:

```bash
python main.py
```

Skrypt wygeneruje (lub zaktualizuje) plik `result.txt` z krótkim podsumowaniem wyników.
