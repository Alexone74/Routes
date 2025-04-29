import os

# Inserisci il percorso della cartella
cartella = r"C:\AAA\Alex\Routes\percorsi-txt\Stazioni"

for nome_file in os.listdir(cartella):
    if nome_file.endswith(".txt"):
        percorso_file = os.path.join(cartella, nome_file)

        with open(percorso_file, 'r', encoding='utf-8') as file:
            contenuto = file.readlines()

        # Rimuove righe vuote all'inizio del file
        while contenuto and contenuto[0].strip() == "":
            contenuto.pop(0)

        nuovo_contenuto = [f"{nome_file}\n", "\n"] + contenuto

        with open(percorso_file, 'w', encoding='utf-8') as file:
            file.writelines(nuovo_contenuto)

print("✅ Tutti i file aggiornati correttamente senza riga vuota prima del titolo.")
