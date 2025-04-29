import os

# PERCORSI DA MODIFICARE
input_folder = "C:\\AAA\\Alex\\Routes\\MAC_percorsi-txt"
output_folder = "C:\\AAA\\Alex\\Routes\\EXP"
font_name = "Arial"
font_size = 24
title_size = 30

os.makedirs(output_folder, exist_ok=True)

def escape_rtf(text):
    # Escaping per RTF + converti newline in \par
    text = text.replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')
    text = text.replace('\r\n', '\n').replace('\r', '\n').replace('\n', r'\par ' + '\n')
    return text

def convert_to_rtf(title, body):
    title = escape_rtf(title)
    body = escape_rtf(body)

    rtf = [
        r"{\rtf1\ansi\ansicpg1252\deff0",
        rf"{{\fonttbl{{\f0 {font_name};}}}}",
        rf"\fs{title_size * 2} \b {title}\b0\par\par",
        rf"\fs{font_size * 2} {body}",
        r"}"
    ]
    return "\n".join(rtf)

for dirpath, _, filenames in os.walk(input_folder):
    for filename in filenames:
        if filename.lower().endswith(".txt"):
            txt_path = os.path.join(dirpath, filename)

            try:
                # ⚠️ Leggiamo come UTF-8 (come nel tuo file caricato, che è valido UTF-8)
                with open(txt_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except UnicodeDecodeError:
                # fallback in caso qualche file non sia utf-8
                with open(txt_path, "r", encoding="windows-1252") as f:
                    lines = f.readlines()

            if not lines:
                continue

            title = lines[0].strip()
            body = "".join(lines[1:]).strip()
            rtf_content = convert_to_rtf(title, body)

            relative_path = os.path.relpath(dirpath, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            rtf_filename = os.path.splitext(filename)[0] + ".rtf"
            rtf_path = os.path.join(output_dir, rtf_filename)

            with open(rtf_path, "w", encoding="utf-8") as f:
                f.write(rtf_content)

print("✅ Conversione RTF completata correttamente.")
