import os

# Imposta il percorso della cartella principale
cartella_principale = "C:\\AAA\\Alex\\Routes\\percorsi-txt"  # <-- modifica questo

# Parole da sostituire: chiave = da sostituire, valore = sostituto
sostituzioni = {
    "P.za": "Piazza",
    "P.ta": "Porta",
    "Oro": "oro",
    "V.le": "Viale",
    "L.go": "Largo",
    "C.so": "Corso"
}

# Scansiona tutti i file .txt nelle sottocartelle
for radice, sottocartelle, files in os.walk(cartella_principale):
    for nome_file in files:
        if nome_file.endswith(".txt"):
            percorso_file = os.path.join(radice, nome_file)

            with open(percorso_file, "r", encoding="utf-8") as file:
                contenuto = file.read()

            # Esegui le sostituzioni
            for da_sostituire, sostituto in sostituzioni.items():
                contenuto = contenuto.replace(da_sostituire, sostituto)

            # Sovrascrivi il file con il nuovo contenuto
            with open(percorso_file, "w", encoding="utf-8") as file:
                file.write(contenuto)

print("Sostituzioni completate!")
