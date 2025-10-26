import pandas as pd
import mysql.connector
from mysql.connector import Error

def main():
    print("Importing data...")
    host = "localhost"
    user = "root"
    password = 
    database = 
    table = 
    csv_file = 

    try:
        
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if conn.is_connected():
            print("✅ Connected to MySQL database")
            
            
            df = pd.read_csv(csv_file)
            
        
            df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))
            df = df.where(pd.notnull(df), None)
            df.columns = [col.strip().replace(" ", "_").replace("-", "_") for col in df.columns]
            
            cursor = conn.cursor()
            
        
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table} (
                Date DATETIME,
                Description VARCHAR(255),
                Debit DECIMAL(10,2),
                Credit DECIMAL(10,2),
                Amount DECIMAL(10,2),
                Sub_category VARCHAR(100),
                Category VARCHAR(100),
                Transaction_Type VARCHAR(50)
            );
            """
            cursor.execute(create_table_query)
            print("🆕 Table checked/created")
            
        
            placeholders = ", ".join(["%s"] * len(df.columns))
            columns = ", ".join([f"`{col}`" for col in df.columns])
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            
            data = [tuple(row) for row in df.to_numpy()]
            cursor.executemany(sql, data)
            conn.commit()
            
            print(f"✅ Inserted {cursor.rowcount} rows into {table}")
            
    except Error as e:
        print("❌ Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("🔒 MySQL connection closed")

if __name__ == "__main__":
    main()

