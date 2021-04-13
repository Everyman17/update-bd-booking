import pandas as pd
from utils import clean_data, update_df
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from datetime import date

#%% Configures date

today = date.today()

#%% Select files to import

Tk().withdraw()
path_new_data = askopenfilename(
    initialdir=r'C:\Users\d_alv\Confidencial Imobiliario\Canal de Equipa - SIR Alojamento Local\Parque_Final_Tratado',
    title='Selecione o ficheiro do parque final tratado',
    filetypes=[("Excel files", ".xlsx .xls")]
)

path_db = askopenfilename(
    initialdir=r'C:\Users\d_alv\OneDrive - Confidencial Imobiliario\Parque_AL',
    title='Selecione o ficheiro da BD Booking',
    filetypes=[("Excel files", ".xlsx .xls")]
)

#%% Import data

db = pd.read_excel(
    path_db,
    engine='openpyxl'
)

new_data = pd.read_excel(
    path_new_data,
    engine='openpyxl',
    sheet_name='Final'
)

#%% Filter for needed columns, removes NaN and drops duplicates from id_unico column

new_data_clean = clean_data(new_data, list(db.columns))

#%% Concatenates new data on top of old data and removes duplicates from id_unico column

db_book_updated = update_df(new_data_clean, db)

#%% Write to excel updated Booking db

path_write = askdirectory(
    initialdir=r'C:\Users\d_alv\OneDrive - Confidencial Imobiliario\Parque_AL',
    title='Seleciona a pasta da BD'
)

db_book_updated.to_excel(
    excel_writer=path_write + f'\\{today.year}\\BD_Booking_{today}.xlsx',
    sheet_name='BD_Book',
    index=False,
    engine='openpyxl',
)
