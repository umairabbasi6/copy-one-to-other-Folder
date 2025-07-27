import os
import shutil

# === CONFIGURATION ===
list_file = 'list.txt'  # File with PDF names
source_dir = r'C:\Users\Special\Downloads\nssm-2.24\test_API\New folder\New folder'
destination_dir = r'C:\Users\Special\Downloads\nssm-2.24\test_API\New folder\New folder2'

# Create destination folder if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Read and clean PDF names from list.txt
with open(list_file, 'r') as file:
    raw_names = {line.strip() for line in file if line.strip()}

# Loop through cleaned list and copy
copied = 0
missing = []

for pdf_name in raw_names:
    pdf_name = pdf_name.strip()
    if not pdf_name.lower().endswith('.pdf'):
        pdf_name += '.pdf'

    source_path = os.path.join(source_dir, pdf_name)
    dest_path = os.path.join(destination_dir, pdf_name)

    if os.path.exists(source_path):
        shutil.copy2(source_path, dest_path)
        copied += 1
    else:
        missing.append(pdf_name)

print(f"✅ Copied {copied} PDF(s) to {destination_dir}")

if missing:
    print(f"⚠️ {len(missing)} file(s) were not found in source:")
    for name in missing:
        print(f" - {name}")
