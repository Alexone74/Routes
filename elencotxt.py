import os
import sys

def list_txt_files(root_folder):
    """
    Elenca tutti i file .txt presenti nella cartella principale e nelle sottocartelle.
    Restituisce un dizionario dove le chiavi sono i percorsi delle cartelle e 
    i valori sono liste di nomi di file .txt presenti in ciascuna cartella.
    """
    result = {}
    
    # Controlla che la cartella esista
    if not os.path.exists(root_folder):
        print(f"Errore: La cartella '{root_folder}' non esiste.")
        return {}
    
    # Naviga attraverso tutte le cartelle e sottocartelle
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Filtra solo i file .txt
        txt_files = [file for file in filenames if file.lower().endswith('.txt')]
        
        # Se ci sono file .txt in questa cartella, aggiungili al risultato
        if txt_files:
            # Usa il percorso relativo come chiave nel dizionario
            relative_path = os.path.relpath(dirpath, root_folder)
            if relative_path == '.':
                relative_path = '(cartella principale)'
            result[relative_path] = txt_files
    
    return result

def print_results(results):
    """
    Stampa i risultati in formato leggibile
    """
    if not results:
        print("Nessun file .txt trovato.")
        return
    
    print("\nElenco dei file .txt trovati:\n")
    
    for folder, files in results.items():
        print(f"Cartella: {folder}")
        for i, file in enumerate(files, 1):
            print(f"  {i}. {file}")
        print()  # Linea vuota tra le cartelle

def main():
    # Prendi la cartella principale dagli argomenti della riga di comando o chiedi all'utente
    if len(sys.argv) > 1:
        root_folder = sys.argv[1]
    else:
        root_folder = input("Inserisci il percorso della cartella principale: ")
    
    # Ottieni l'elenco dei file .txt
    txt_files_by_folder = list_txt_files(root_folder)
    
    # Stampa i risultati
    print_results(txt_files_by_folder)
    
    # Opzionalmente, salva i risultati in un file
    save_to_file = input("Vuoi salvare i risultati in un file? (s/n): ").lower()
    if save_to_file == 's':
        output_file = input("Inserisci il nome del file di output (o premi invio per 'elenco_txt.txt'): ")
        if not output_file:
            output_file = "elenco_txt.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Elenco dei file .txt trovati:\n\n")
            for folder, files in txt_files_by_folder.items():
                f.write(f"Cartella: {folder}\n")
                for i, file in enumerate(files, 1):
                    f.write(f"  {i}. {file}\n")
                f.write("\n")  # Linea vuota tra le cartelle
                
        print(f"\nRisultati salvati in '{output_file}'")

if __name__ == "__main__":
    main()