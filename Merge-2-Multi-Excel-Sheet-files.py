#!/usr/bin/env python3

import sys
import pandas as pd

def merge_excel_files(file1, file2, output_file):
    # Load the Excel files
    xls1 = pd.ExcelFile(file1)
    xls2 = pd.ExcelFile(file2)
    
    # Create a new Excel writer for the output file using openpyxl engine
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Process all sheets from the first file
        for sheet in xls1.sheet_names:
            # Use the already loaded xls1 object to parse the sheet
            df = xls1.parse(sheet)
            df.to_excel(writer, sheet_name=sheet, index=False)
        
        # Process all sheets from the second file
        for sheet in xls2.sheet_names:
            df = xls2.parse(sheet)
            df.to_excel(writer, sheet_name=sheet, index=False)
    
    print(f"Merged Excel file has been created: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_excel_sheets.py <file1.xlsx> <file2.xlsx> <output.xlsx>")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    merge_excel_files(file1, file2, output_file)
