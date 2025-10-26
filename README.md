# MySQL-Importer
A simple utility for cleaning and importing financial data from an Excel .xlsm spreadsheet into a MySQL database. This tool automates the process of extracting data from a formatted workbook, preprocessing it with pandas, and uploading it to a structured SQL table.

## Features
- Reads data from a specific Excel sheet (TRANSACTIONS)
- Cleans and formats dates and missing values
- Creates MySQL table if it doesn't exist
- Bulk inserts data into MySQL

## Requirements
- Python 3.7+
- MySQL Server
  
## Python packages
- pandas
- mysql-connector-python
- openpyxl or xlrd (for reading Excel files)
