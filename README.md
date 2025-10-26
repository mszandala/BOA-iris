# Projekt: BOA + KNN (Iris)

Krótki skrypt Pythona używający algorytmu BOA do optymalizacji parametru K dla KNN na zbiorze Iris.

Pliki w repozytorium:
- `main.py` — główny skrypt
- `requirements.txt` — lista zależności
- `result.txt` — (generowany) wyniki po uruchomieniu

Co zrobić, żeby wysłać na GitHub (szybkie kroki):

1. Zainstaluj Git (jeśli jeszcze nie jest zainstalowany). Przykładowe sposoby:
   - Najszybciej (GUI): pobierz instalator z https://git-scm.com/download/win i zainstaluj.
   - Winget (Windows 10/11):

```powershell
winget install --id Git.Git -e --source winget
```

   - Chocolatey (jeśli masz):

```powershell
choco install git
```

2. Otwórz nowy PowerShell (zamknij stary), przejdź do folderu projektu:

```powershell
cd "C:\Matyna_C\Studia\Nowy folder"
```

3. Skonfiguruj dane użytkownika (tylko raz):

```powershell
git config --global user.name "Twoje Imię"
git config --global user.email "twoj@email.com"
```

4. Zainicjalizuj repo i zrób pierwszy commit:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
```

5. Utwórz repo na GitHub (ręcznie na github.com lub użyj GitHub CLI `gh`):

   - Ręcznie: https://github.com/new — utwórz repo i skopiuj URL.
   - `gh` (jeśli zainstalowane):

```powershell
gh repo create <nazwa-repo> --public --source=. --remote=origin --push
```

6. Dodaj remote i wypchnij (jeśli utworzyłeś repo ręcznie):

```powershell
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Uwaga nt. uwierzytelniania:
- Jeśli masz włączone 2FA, do HTTPS używaj Personal Access Token (PAT) zamiast hasła.
- Alternatywnie skonfiguruj SSH i używaj `git@github.com:username/repo.git`.

Jeśli chcesz, mogę:
- pomóc w instalacji Gita i/lub `gh` (instrukcje krok po kroku),
- po instalacji uruchomić `git init`, commit i wypchnąć repo (potrzebuję: URL z GitHub lub dostęp `gh`),
- albo tylko doradzić krok po kroku — wybierz co wolisz.
