import datacleaner
import dataimporter


def main():
    print("Starting Data Cleaner...")
    datacleaner.main()  

    print("Starting Data Importer...")
    dataimporter.main()  

if __name__ == "__main__":
    main()

