import pandas as pd 
from datetime import datetime

# import shared utility fpr saving dataframes to csv
#from utils.common_functions import save_to_csv


## Input/Loinc.csv
loinc = pd.read_csv(r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\input\Loinc.csv")

### Info to describe 
loinc.info()

### Strings 
loinc.STATUS.value_counts()

### print first row
loinc.iloc[0]

#### Checking potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

loinc_small['last_updated'] = '2025-09-03'

# loinc_small = loinc_small.rename(columns={})

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

file_output_path = r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\output\csv\loinc_small_noindex.csv"

loinc_small.to_csv(file_output_path, index=False)









