import pandas as pd
def main():
    print("Cleaning data...")
    file_path = 
    df = pd.read_excel(file_path, sheet_name= 'TRANSACTIONS', usecols = "A:H")

 
    df. dropna(how = 'all', inplace = True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

    output_path = 
    df.to_csv(output_path, index= False)


if __name__ == "__main__":
    main()
    



