
from pathlib import Path
import pandas as pd

file_path = Path(r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\input\sct2_Description_Full-en_US1000124_20250301.txt")

df = pd.read_csv(
    file_path, sep='\t', header=0, encoding='utf-8' ,nrows=100000
    #separator='\t',
    #has_header=True,
    #quote_char=None,
    #encoding='utf8-lossy',
    #truncate_ragged_lines=True,
   # dtypes={
        #'id': pl.Utf8,
        #'effectiveTime': pl.Utf8,
       # 'active': pl.Int32,
        #'moduleId': pl.Utf8,
        #'conceptId': pl.Utf8,
       # 'languageCode': pl.Utf8,
        #'typeId': pl.Utf8,
        #'term': pl.Utf8,
        #'caseSignificanceId': pl.Utf8
   # }
)

output_dir = Path(r"C:\Users\siddi\Desktop\MEDICAL-CODEX-PIPELINE\output\snomed")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'sct2_Description_Full.csv'

df.to_csv(output_path)

print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head()
#print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")


#print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
#print(f"Language codes: {df['languageCode'].unique().to_list()}")
