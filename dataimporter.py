import pandas as pd
import mysql.connector
from mysql.connector import Error

def dataimporter(csv_path, host, user, password, database, table_name):
    print("Importing data into MySQL...")

    try:
        df = pd.read_csv(csv_path)

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print(f"Connected to MySQL database '{database}'")
            columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS `{table_name}` (
                {columns}
            );
            """
            cursor.execute(create_table_query)

            for _, row in df.iterrows():
                placeholders = ", ".join(["%s"] * len(row))
                insert_query = f"INSERT INTO `{table_name}` ({', '.join(df.columns)}) VALUES ({placeholders})"
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f"Successfully imported {len(df)} rows into '{table_name}'.")

    except Error as e:
        print(f" MySQL error: {e}")
        return False

    except Exception as e:
        print(f" An unexpected error occurred: {e}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 MySQL connection closed.")

    return True



def main():
    csv_path = input("Enter path of cleaned CSV file: ").strip()
    host = input("Enter MySQL host (e.g. localhost): ").strip()
    user = input("Enter MySQL username: ").strip()
    password = input("Enter MySQL password: ").strip()
    database = input("Enter MySQL database name: ").strip()
    table_name = input("Enter table name to import data into: ").strip()

    success = dataimporter(csv_path, host, user, password, database, table_name)

    if success:
        print("Data import completed successfully.")
    else:
        print("Data import failed.")


if __name__ == "__main__":
    main()