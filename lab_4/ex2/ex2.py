def ersetzen(file_path, wort_zu_ersetzen, ersatzwort):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    count = 0
    replaced_lines = []

    for line in lines:
        if wort_zu_ersetzen in line:
            count += line.count(wort_zu_ersetzen)
            replaced_line = line.replace(wort_zu_ersetzen, ersatzwort)
            replaced_lines.append(replaced_line)
        else:
            replaced_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(replaced_lines)

    if count > 0:
        print(f"Ersetzt '{wort_zu_ersetzen}' durch '{ersatzwort}' an {count} Stellen.")
    else:
        print(f"{wort_zu_ersetzen} wurde nicht gefunden.")



def main():
    file_path = "meine_datei.txt"
    wort_zu_ersetzen = input("Wort zu ersetzen: ")
    ersatzwort = input("Ersatzwort: ")
    ersetzen(file_path, wort_zu_ersetzen, ersatzwort)

main()
