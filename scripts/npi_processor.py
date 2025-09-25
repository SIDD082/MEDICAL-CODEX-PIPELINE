import polars as pl
import pandas as pd
import time

npi_file_path = r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\input\npidata_pfile_20050523-20250810.csv"

## just loading the first 1000 rows in order to minimize file size



start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(elapsed_time_pandas)



print(f"Successfully loaded {len(df_pandas)} records from NPI data")
print(f"Columns: {df_pandas.columns}")
print(f"\nDataset shape: {df_pandas.shape}")
print(f"\nFirst 5 rows:")
print(df_pandas.head())

#print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")


df_polars_small = df_pandas[[
    'NPI', 
    'Provider Last Name (Legal Name)'
]]

## add in a last_updated column

df_pandas["last_updated"] = '2025-09-03'


## rename colummns: code, description, last_updated
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})


## save to csv
output_path = r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\output\csv\npi_small_noindex.csv"
df_polars_small.to_csv(output_path)
#df_polars_small.write_parquet(r"MEDICAL-CODEX-PIPELINE/npi/output/npi_small.parquet")
