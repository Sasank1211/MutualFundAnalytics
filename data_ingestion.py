import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:

    if file.endswith(".csv"):

        print("=" * 50)
        print("Dataset:", file)

        file_path = os.path.join(folder_path, file)

        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\n")