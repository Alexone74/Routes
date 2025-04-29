import os
import re

def process_txt_files(root_folder):
    # Conta i file elaborati
    files_processed = 0
    
    # Attraversa tutte le cartelle e sottocartelle
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # Verifica che sia un file .txt
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                
                try:
                    # Leggi il contenuto del file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # Verifica che ci sia almeno una riga
                    if lines:
                        # Rimuovi ".txt" dalla fine della prima riga
                        lines[0] = re.sub(r'\.txt$', '', lines[0])
                        
                        # Scrivi il contenuto modificato nel file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        
                        files_processed += 1
                        print(f"Modificato: {file_path}")
                except Exception as e:
                    print(f"Errore nel processare il file {file_path}: {e}")
    
    return files_processed

if __name__ == "__main__":
    # Usa direttamente il percorso (con uno dei metodi corretti)
    root_folder = r"C:\AAA\Alex\Routes\MAC_percorsi-txt"
    
    # Verifica che la cartella esista
    if not os.path.isdir(root_folder):
        print("Il percorso specificato non è una cartella valida.")
    else:
        # Processa i file
        count = process_txt_files(root_folder)
        print(f"Elaborati {count} file .txt.")