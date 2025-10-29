import datacleaner
import dataimporter
import sys 

def main():
    print('Initialising...') 
    print("Starting Data Cleaner...")

    success = datacleaner.main()

    if not success:
        print("Data Cleaner failed. Exiting program.")
        sys.exit()  

    print("Starting Data Importer...")
    try:
        dataimporter.main()
    except Exception as e:
        print(f"Data Importer failed: {e}")

if __name__ == "__main__": 
    main()
    input('Press Enter to exit...')