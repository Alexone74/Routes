#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Convertitore da file TXT a JSON per Percorsi Milano (versione con sottocartelle)

import os
import json
import sys

# Configurazione - modifica questi valori
CARTELLA_INPUT_TXT = 'percorsi-txt'  # Cartella principale dove si trovano le sottocartelle delle categorie
CARTELLA_INPUT_JPG = 'percorsi-img'  # Cartella principale delle immagini (stessa struttura a sottocartelle)
FILE_OUTPUT = 'percorsi.json'        # File JSON di output
SEPARATORE_NOME = ' - '              # Separatore tra origine e destinazione nel nome del file

def converti_percorsi():
    """Funzione principale per convertire i file TXT in JSON usando la struttura a sottocartelle"""
    print('Inizia conversione da TXT a JSON dei percorsi (usando struttura a sottocartelle)...')
    
    # Verifica che la cartella dei TXT esista
    if not os.path.exists(CARTELLA_INPUT_TXT):
        print(f'Errore: La cartella "{CARTELLA_INPUT_TXT}" non esiste.')
        return
    
    # Ottieni le sottocartelle (categorie)
    categorie = [nome for nome in os.listdir(CARTELLA_INPUT_TXT) 
                if os.path.isdir(os.path.join(CARTELLA_INPUT_TXT, nome))]
    
    if len(categorie) == 0:
        print(f'Nessuna sottocartella trovata in "{CARTELLA_INPUT_TXT}". Creare sottocartelle per le categorie.')
        return
    
    print(f'Trovate {len(categorie)} categorie: {", ".join(categorie)}')
    
    # Dizionario che conterrà tutti i percorsi organizzati per categoria
    percorsi_json = {}
    id_contatore = 1
    total_files_processed = 0
    
    # Elabora ogni categoria
    for categoria in categorie:
        percorsi_categoria = []  # Lista temporanea per i percorsi di questa categoria
        cartella_categoria = os.path.join(CARTELLA_INPUT_TXT, categoria)
        
        # Leggi tutti i file TXT nella cartella della categoria
        files = [f for f in os.listdir(cartella_categoria) if f.endswith('.txt')]
        
        if len(files) == 0:
            print(f'Nessun file .txt trovato nella categoria "{categoria}".')
            percorsi_json[categoria] = []  # Aggiungi comunque la categoria vuota
            continue
        
        print(f'Categoria "{categoria}": trovati {len(files)} file .txt da processare.')
        
        # Elabora ogni file della categoria
        for file in files:
            percorso_file = os.path.join(cartella_categoria, file)
            
            try:
                with open(percorso_file, 'r', encoding='utf-8') as f:
                    contenuto = f.read()
            except Exception as e:
                print(f'Errore nella lettura del file "{file}" (categoria {categoria}): {str(e)}')
                continue
            
            # Estrai le vie dal contenuto (una via per riga)
            vie = [riga.strip() for riga in contenuto.splitlines() if riga.strip()]
            
            if not vie:
                print(f'Il file "{file}" (categoria {categoria}) non contiene vie valide. Sarà saltato.')
                continue
            
            # Estrai nome del percorso dal nome del file (senza estensione .txt)
            nome_percorso = os.path.splitext(file)[0]
            
            # Cerca l'immagine corrispondente nelle sottocartelle delle immagini
            nome_base = os.path.splitext(file)[0]
            immagine = None
            
            # Controlla se esiste la sottocartella delle immagini per questa categoria
            cartella_immagini_categoria = os.path.join(CARTELLA_INPUT_JPG, categoria)
            if os.path.exists(cartella_immagini_categoria):
                immagini_categoria = [f for f in os.listdir(cartella_immagini_categoria) 
                                    if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                
                for img in immagini_categoria:
                    nome_img_base = os.path.splitext(img)[0]
                    if nome_img_base == nome_base:
                        # Percorso relativo all'immagine: 'categoria/nome_immagine.jpg'
                        immagine = f"{categoria}/{img}"
                        print(f'Trovata immagine "{img}" per il percorso "{nome_percorso}" (categoria {categoria})')
                        break
            
            # Crea il percorso
            percorso = {
                "id": id_contatore,
                "nome": nome_percorso,
                "vie": vie
            }
            
            # Aggiungi l'immagine solo se disponibile
            if immagine:
                percorso["immagine"] = immagine
            
            # Aggiungi il percorso alla lista temporanea
            percorsi_categoria.append(percorso)
            
            print(f'Elaborato: "{nome_percorso}" ({len(vie)} vie) - Categoria: {categoria}')
            id_contatore += 1
            total_files_processed += 1
        
        # Ordina i percorsi per nome prima di aggiungerli al dizionario JSON
        percorsi_categoria.sort(key=lambda x: x["nome"].lower())
        
        # Aggiungi la lista ordinata al dizionario JSON
        percorsi_json[categoria] = percorsi_categoria
    
    # Conta il numero totale di percorsi
    totale_percorsi = sum(len(percorsi) for percorsi in percorsi_json.values())
    
    # Salva il risultato nel file JSON
    with open(FILE_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(percorsi_json, f, ensure_ascii=False, indent=2)
    
    print('')
    print('Conversione completata!')
    print(f'Totale percorsi convertiti: {totale_percorsi}')
    print(f'File JSON salvato in: {FILE_OUTPUT}')

if __name__ == '__main__':
    try:
        converti_percorsi()
    except Exception as e:
        print(f'Si è verificato un errore durante la conversione: {str(e)}')
        sys.exit(1)
