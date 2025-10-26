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

| Parametr | Co oznacza | Opis |
|---|---|---|
| N = 10 | To liczba „motyli” – czyli ile różnych propozycji K jednocześnie bada algorytm. 
🔹 Więcej motyli → więcej pomysłów → większa szansa na dobre rozwiązanie, ale dłuższy czas działania. 
Przykład: jeśli N=10, to algorytm jednocześnie testuje 10 różnych wartości K. | |
| MaxIter (iteracje) | | |
| p (prob. przełączenia) | | |


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
