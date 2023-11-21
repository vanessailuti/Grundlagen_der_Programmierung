import random


# Die Funktion, um den Gewinner einer Runde zu bestimmen und die Punktzahlen zu aktualisieren
def spiel(user_choice, computer_choice, user, computer):
    if user_choice >= 3 or user_choice < 0:
        print("Ungültige Zahl.")
    elif user_choice == 0 and computer_choice == 2:
        user += 1
    elif user_choice == 2 and computer_choice == 0:
        computer += 1
    elif computer_choice > user_choice:
        computer += 1
    elif user_choice > computer_choice:
        user += 1
    elif user_choice == computer_choice:
        user += 1
        computer += 1

    return user, computer


# Funktion zum Anzeigen der Benutzerwahl, Bestimmen der Computerauswahl und Aktualisieren der Punktzahlen
def print_choices(user, computer):
    # Benutzereingabe für die Wahl (0 für Stein, 1 für Blatt, 2 für Schere)
    user_choice = -1  # Initialisiere user_choice mit einem ungültigen Wert
    while user_choice < 0 or user_choice > 2:
        try:
            user_choice = int(input("Welche wählst du? Schreibe 0 für Stein, 1 für Blatt oder 2 für Schere.\n"))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib 0, 1 oder 2 ein.")

    # Generiere eine zufällige Computerauswahl (0 für Stein, 1 für Blatt, 2 für Schere)
    computer_choice = random.randint(0, 2)

    # Konvertiere die numerische Computerauswahl in ihren entsprechenden Namen
    computer_name = name(computer_choice)
    print(f"Der Computer wählt: {computer_name}")

    # Aktualisiere die Punktzahlen basierend auf den Auswahlen
    user, computer = spiel(user_choice, computer_choice, user, computer)

    # Gebe den aktuellen Stand aus
    print(f"Aktueller Stand: Du - {user}, Computer - {computer}")
    return user, computer


# Funktion, um den Gewinner des Spiels zu bestimmen
def win(user, computer):
    if user > computer:
        print("Du gewinnst!")
    elif computer > user:
        print("Du verlierst!")
    else:
        print("Es ist Unentschieden.")


# Funktion, um die numerische Wahl in ihren entsprechenden Namen umzuwandeln
def name(random_num):
    if random_num == 0:
        return "Stein"
    elif random_num == 1:
        return "Blatt"
    elif random_num == 2:
        return "Schere"


# Die Hauptfunktion zur Steuerung des Spielablaufs
def main():
    spiele = 3  # Anzahl der Runden zu spielen
    user = 0  # Punktzahl des Benutzers
    computer = 0  # Punktzahl des Computers

    # Schleife durch die festgelegte Anzahl von Runden
    while spiele > 0:
        user, computer = print_choices(user, computer)
        spiele -= 1

    # Bestimme und gebe den Gewinner des Spiels aus
    win(user, computer)


# Rufe die Hauptfunktion auf, um das Spiel zu starten
main()
