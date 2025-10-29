import pandas as pd
import os

def datacleaner(file_path, output_path):
    print('Cleaning data...')

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False 

    try:
        df = pd.read_csv(file_path)
        df.dropna(how='all',inplace=True)
    
        if 'Date' in df.columns:
            try:
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
            except Exception as e:
                print(f"Could not convert 'Date' column: {e}")
            
        else:
            print("No 'Date' column found — skipping date conversion.")

        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to: {output_path}")
        return True
    
    except Exception as e:
        print(f"An unexpected error has occured: {e}")
        return False

def main():
    file_path = input("Enter file path of CSV: ").strip()
    output_path = input("Enter path for output CSV file: ").strip()

    success = datacleaner(file_path, output_path)

    if not success:
        print("Data cleaning failed. Exiting program.")
        return success  

    print("Data cleaning completed successfully.")
    return success 

if __name__ == "__main__":
    main()
    



