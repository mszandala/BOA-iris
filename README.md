<<<<<<< HEAD
# BOA + KNN (Iris)

Butterfly Optimization Algorithm (BOA) — projekt demonstracyjny optymalizacji parametru K dla klasyfikatora KNN na zbiorze Iris.

Pliki w repozytorium:
- `main.py` — główny skrypt implementujący BOA + KNN
- `requirements.txt` — zależności (numpy, scikit-learn, matplotlib itp.)
- `result.txt` — plik wynikowy generowany przez skrypt

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

6. Dodatkowe uwagi
- Nie przechowuj w repo danych osobowych ani kluczy API.
- Jeśli chcesz przyczynić się do projektu — otwórz issue lub wyślij pull request.

---

Jeśli chcesz, mogę dodać także plik `CONTRIBUTING.md` z zasadami kontrybucji lub sekcję opisującą licencję.
