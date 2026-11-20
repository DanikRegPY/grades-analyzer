# Grades Analyzer

🇬🇧 English | 🇩🇪 [Deutsch](#deutsch)

## English

A small console program written in Python. You enter grades from 1 to 100 and get a short report.

### Features
- Enter grades one by one (1-100)
- Input validation: letters, empty input and out-of-range numbers are rejected
- Report: count, total, highest, lowest, average, number of passed grades (60 or higher)

### Commands
- a number from 1 to 100 adds a grade
- `show` prints the current list of grades
- `exit` finishes input and prints the report

### How to run
1. Install Python 3 from https://www.python.org
2. Download `grades.py` (or clone this repository)
3. Open a terminal in the project folder and run:

```
python grades.py
```

On some systems the command is `python3 grades.py`.

### Example
```
Enter a grade (1–100), 'show' or 'exit': 85
Enter a grade (1–100), 'show' or 'exit': 52
Enter a grade (1–100), 'show' or 'exit': exit
Goodbye.
count: 2
total: 137
highest: 85
lowest: 52
avg: 68.5
passed: 1
list: [85, 52]
```

---

## Deutsch

Ein kleines Konsolenprogramm in Python. Man gibt Noten von 1 bis 100 ein und bekommt einen kurzen Bericht.

### Funktionen
- Noten nacheinander eingeben (1-100)
- Eingabeprüfung: Buchstaben, leere Eingaben und Zahlen außerhalb des Bereichs werden abgelehnt
- Bericht: Anzahl, Summe, höchste, niedrigste, Durchschnitt, Anzahl bestandener Noten (ab 60)

### Befehle
- eine Zahl von 1 bis 100 fügt eine Note hinzu
- `show` zeigt die aktuelle Liste der Noten
- `exit` beendet die Eingabe und zeigt den Bericht

### So startest du das Programm
1. Python 3 installieren: https://www.python.org
2. `grades.py` herunterladen (oder das Repository klonen)
3. Terminal im Projektordner öffnen und eingeben:

```
python grades.py
```

Auf manchen Systemen lautet der Befehl `python3 grades.py`.

### Beispiel
Siehe das Beispiel im englischen Teil oben.
