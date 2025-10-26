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
