#CREATE BY @meffking and @mishadsd
import pandas as pd
import time
import os
time.sleep(0.5)
print('''
 ███▄ ▄███▓▓█████   █████▒ █████▒    ██ ▄█▀ ██▓ ███▄    █   ▄████ 
▓██▒▀█▀ ██▒▓█   ▀ ▓██   ▒▓██   ▒     ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
▓██    ▓██░▒███   ▒████ ░▒████ ░    ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██    ▒██ ▒▓█  ▄ ░▓█▒  ░░▓█▒  ░    ▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓
▒██▒   ░██▒░▒████▒░▒█░   ░▒█░       ▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒
░ ▒░   ░  ░░░ ▒░ ░ ▒ ░    ▒ ░       ▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
░  ░      ░ ░ ░  ░ ░      ░         ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
░      ░      ░    ░ ░    ░ ░       ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
       ░      ░  ░                  ░  ░    ░           ░       ░ 
''')
time.sleep(1)
def convert_csv_to_xlsx(csv_folder, xlsx_folder):
    if not os.path.exists(xlsx_folder):
        os.makedirs(xlsx_folder)
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            try:
                csv_file = os.path.join(csv_folder, filename)
                xlsx_file = os.path.join(xlsx_folder, filename.replace('.csv', '.xlsx'))
                df = pd.read_csv(csv_file, low_memory=False)
                df.to_excel(xlsx_file, index=False)
                os.remove(f'{csv_folder}\{filename}')
            except Exception as e:
                print(f"Error reading {filename}: {e}")

csv_folder = input(r'Enter the directory csv files: ')
xlsx_folder = input(r'Enter the directory for saving xlsx files (you can use the same path): ')
convert_csv_to_xlsx(csv_folder, xlsx_folder)