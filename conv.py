#CREATE BY @meffking and @mishadsd
import pandas as pd
import os
import codecs
import argparse

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
        if filename.endswith('.csv') or filename.endswith('.txt'):
            try:
                codec = ['utf-8', 'utf-16', 'ANSI', 'Windows-1251', 'Windows-1252', 'ISO-8859-1']
                csv_file = os.path.join(csv_folder, filename)        
                for i in range(len(codec)):
                    if filename.endswith('.csv'):
                        xlsx_file = os.path.join(xlsx_folder, filename.replace('.csv', '.xlsx'))
                    else:
                        xlsx_file = os.path.join(xlsx_folder, filename.replace('.txt', '.xlsx'))
                    if not os.path.exists(xlsx_file):
                        with codecs.open(csv_file, 'r', codec[i], errors='ignore') as f:
                            df = pd.read_csv(f, low_memory=False, delimiter=';', skiprows=0, on_bad_lines='skip')
                            df.to_excel(xlsx_file, index=False)
                            f.close()
                            if remove == 'true':
                                os.remove(csv_file)
                            break
            except Exception as e:
                print(f"Error reading {filename}: {e}")
csv_folder = ''
parser = argparse.ArgumentParser(description='Csv To Xlsx')
parser.add_argument('csv_folder', type=str, help='Input folder with .csv')
parser.add_argument('xlsx_folder', type=str, default=csv_folder, help='Input output folder')
parser.add_argument('--rm', type=str, default='f', help='Specify to delete files (true/false)')
args = parser.parse_args()
convert_csv_to_xlsx(args.csv_folder, args.xlsx_folder, args.rm.lower())