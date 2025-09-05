import pandas as pd
loinc = pd.read_csv('input\Loinc.csv')
loinc.info()
list_cols = ['LOINC_NUM' , 'DefinitionDescription']
subset = loinc[list_cols]








