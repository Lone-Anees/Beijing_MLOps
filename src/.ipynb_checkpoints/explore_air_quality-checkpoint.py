from pathlib import Path
import pandas as pd
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH= PROJECT_ROOT / "data" / "raw" / ("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
if not CSV_PATH.is_file():
    raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")
df=pd.read_csv(CSV_PATH)

print("DATASET LOADED")
print("Row and columns:", df.shape)
print("Column names:",df.columns.tolist())
print("First five rows:")
print(df.head())