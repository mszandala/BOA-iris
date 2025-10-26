<<<<<<< HEAD
# BOA + KNN (Iris)

Butterfly Optimization Algorithm (BOA) — projekt demonstracyjny optymalizacji parametru K dla klasyfikatora KNN na zbiorze Iris.

Pliki w repozytorium:
- `main.py` — główny skrypt implementujący BOA + KNN
- `requirements.txt` — zależności (numpy, scikit-learn, matplotlib itp.)
- `result.txt` — plik wynikowy generowany przez skrypt

Instrukcja szybkiego wysłania projektu na GitHub

1. Zainstaluj Git (jeśli jeszcze nie jest zainstalowany):
   - Pobierz instalator: https://git-scm.com/download/win i uruchom go.
   - Alternatywy: `winget install --id Git.Git -e --source winget` lub `choco install git` (jeśli masz te narzędzia).

2. Otwórz nowy PowerShell i przejdź do folderu projektu (zamień poniższą ścieżkę na swoją lokalną):

```powershell
# Przykład (zamień na ścieżkę do twojego projektu):
cd "<ścieżka\do\twojego\projektu>"
```

3. Skonfiguruj Git (tylko raz):

```powershell
# Ustaw swoje imię i email (wstaw tutaj swoje dane — nie zostawiaj cudzych danych w README)
git config --global user.name "Twoje Imię"
git config --global user.email "twoj@email.com"
```

4. Inicjalizacja, commit i ustawienie gałęzi `main`:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
```

5. Dodanie zdalnego repozytorium i wypchnięcie (HTTPS):

```powershell
git remote add origin https://github.com/mszandala/BOA-iris.git
git push -u origin main
```

Uwierzytelnianie:
- Jeśli masz włączone 2FA w GitHub użyj Personal Access Token (PAT) jako hasła przy push.
- Alternatywnie skonfiguruj SSH i użyj `git@github.com:mszandala/BOA-iris.git`.

Jeśli pojawią się konflikty (np. README istnieje już na GitHub), możesz pobrać zmiany i scalić je:

```powershell
git fetch origin
git pull origin main --allow-unrelated-histories
# rozwiąż konflikty, jeśli się pojawią, następnie:
git add README.md
git commit -m "Resolve merge conflict in README"
git push -u origin main
```

---

Jeśli chcesz, mogę rozwiązać konflikt README za Ciebie, wykonać commit i wypchnąć; właśnie to robię teraz.

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
