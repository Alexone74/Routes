import os

# Cartella con i file .txt
cartella = "C:/AAA/Alex/Routes/percorsi-txt/Autostrade"  # Cambia con il percorso corretto

# Itera su tutti i file .txt nella cartella
for filename in os.listdir(cartella):
    if filename.endswith(".txt"):
        filepath = os.path.join(cartella, filename)
        
        # Leggi il contenuto del file
        with open(filepath, "r", encoding="utf-8") as file:
            contenuto = file.read()
        
        # Sostituisci Õ con '
        nuovo_contenuto = contenuto.replace("Õ", "'")
        
        # Scrivi il file corretto
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(nuovo_contenuto)

print("Sostituzione completata in tutti i file .txt!")
