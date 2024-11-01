#CREATE BY @meffking and @mishadsd
import pandas as pd
import os
import sys
def convert_csv_to_xlsx(csv_folder, xlsx_folder, remove):
    if not os.path.exists(xlsx_folder):
        os.makedirs(xlsx_folder)
    print('''

███    ███ ███████ ███████ ███████     ██   ██ ██ ███    ██  ██████  
████  ████ ██      ██      ██          ██  ██  ██ ████   ██ ██       
██ ████ ██ █████   █████   █████       █████   ██ ██ ██  ██ ██   ███ 
██  ██  ██ ██      ██      ██          ██  ██  ██ ██  ██ ██ ██    ██ 
██      ██ ███████ ██      ██          ██   ██ ██ ██   ████  ██████  
                                                                     
                                                                     

''')
    csv_f = os.path.join(csv_folder)
    for filename in os.listdir(csv_f):
        if filename.endswith('.csv'):
            try:
                csv_file = os.path.join(csv_folder, filename)
                xlsx_file = os.path.join(xlsx_folder, filename.replace('.csv', '.xlsx'))
                df = pd.read_csv(csv_file, low_memory=False)
                df.to_excel(xlsx_file, index=False)
                if remove == '--rm':
                    os.remove(f'{csv_folder}\{filename}')
            except Exception as e:
                print(f"Error reading {filename}: {e}")

csv_folder = sys.argv[1]
xlsx_folder = sys.argv[2]
try:
    remove = sys.argv[3]
except Exception:
    remove = 'f'
if xlsx_folder == '-': xlsx_folder=csv_folder
convert_csv_to_xlsx(csv_folder, xlsx_folder, remove)