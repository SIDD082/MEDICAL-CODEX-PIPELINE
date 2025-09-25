import polars as pl
from pathlib import Path
import pandas as pd

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

file_path = Path(r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\input\RXNATOMARCHIVE.RRF")

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pd.read_fwf(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

output_dir = Path(r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\output\csv\rxnorm")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

df.to_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
#print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")
