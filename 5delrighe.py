import os
import re

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if len(lines) < 2:
            return  # File troppo corto, lo saltiamo
        
        # Manteniamo la prima riga (titolo)
        result = [lines[0]]
        
        # Manteniamo la seconda riga solo se è vuota
        if len(lines) > 1:
            second_line = lines[1]
            if second_line.strip() == '':
                result.append(second_line)
        
        # Per le righe successive, aggiungiamo solo quelle non vuote
        for line in lines[2:]:
            if line.strip() != '':
                result.append(line)
        
        # Scriviamo il file modificato
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(result)
            
        return True
    except Exception as e:
        print(f"Errore nel processare il file {file_path}: {e}")
        return False

def process_directories(root_dir):
    processed_files = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(dirpath, filename)
                if process_file(file_path):
                    processed_files += 1
    
    return processed_files

if __name__ == "__main__":
    # Specifica qui il percorso della tua cartella principale
    root_directory = "C:\AAA\Alex\Routes\MAC_percorsi-txt"
    
    # Esegui l'elaborazione
    count = process_directories(root_directory)
    print(f"Elaborazione completata. Processati {count} file .txt.")