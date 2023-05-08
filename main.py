import os
import pandas as pd
file_path = "C:/Users/User/Desktop/alt_text_issues.xlsx" #file path of the chosen filke
file_name = os.path.basename(file_path)
print(file_name)
excel_file = pd.ExcelFile(file_path)

# iterate through each sheet in the file
for sheet_name in excel_file.sheet_names:
    # read sheet into DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # get number of rows in sheet
    num_rows = df.shape[0]

    # print sheet name and number of rows
    print(f"{sheet_name}: {num_rows} rows")
