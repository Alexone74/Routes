#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Script per convertire la codifica dei file TXT

import os
import sys
import shutil
import chardet

def detect_encoding(file_path):
    """Rileva la codifica di un file utilizzando chardet"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def convert_file(src_file, dst_file):
    """Converte un file dalla sua codifica originale a UTF-8"""
    try:
        # Rileva la codifica del file sorgente
        src_encoding = detect_encoding(src_file)
        if not src_encoding:
            print(f"Impossibile rilevare la codifica per: {src_file}")
            return False
        
        # Leggi il contenuto con la codifica rilevata
        with open(src_file, 'r', encoding=src_encoding, errors='replace') as f:
            content = f.read()
        
        # Scrivi il contenuto in UTF-8
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Convertito: {src_file} ({src_encoding} → UTF-8)")
        return True
    except Exception as e:
        print(f"Errore durante la conversione di {src_file}: {str(e)}")
        return False

def convert_directory(src_dir, dst_dir):
    """Converte tutti i file .txt in una directory e nelle sue sottodirectory"""
    # Conta i file convertiti
    converted_count = 0
    error_count = 0
    
    # Assicurati che la directory di destinazione esista
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Percorri tutte le sottocartelle
    for root, dirs, files in os.walk(src_dir):
        # Crea la stessa struttura di cartelle nella destinazione
        rel_path = os.path.relpath(root, src_dir)
        if rel_path == '.':
            current_dst_dir = dst_dir
        else:
            current_dst_dir = os.path.join(dst_dir, rel_path)
            if not os.path.exists(current_dst_dir):
                os.makedirs(current_dst_dir)
        
        # Converte tutti i file .txt nella cartella corrente
        for file in files:
            if file.lower().endswith('.txt'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(current_dst_dir, file)
                
                if convert_file(src_file, dst_file):
                    converted_count += 1
                else:
                    error_count += 1
            else:
                # Copia semplicemente i file non .txt
                src_file = os.path.join(root, file)
                dst_file = os.path.join(current_dst_dir, file)
                shutil.copy2(src_file, dst_file)
                print(f"Copiato: {src_file}")
    
    return converted_count, error_count

if __name__ == "__main__":
    # Definisci le cartelle di origine e destinazione
    source_dir = r"C:\AAA\Alex\Routes\EXP"
    target_dir = r"C:\AAA\Alex\Routes\EXP2"
    
    print(f"Inizio conversione dei file da {source_dir} a {target_dir}...")
    
    if not os.path.exists(source_dir):
        print(f"Errore: La cartella di origine {source_dir} non esiste.")
        sys.exit(1)
    
    # Esegui la conversione
    converted, errors = convert_directory(source_dir, target_dir)
    
    print("\nConversione completata!")
    print(f"File convertiti con successo: {converted}")
    print(f"File con errori: {errors}")
    print(f"I file convertiti sono stati salvati in: {target_dir}")