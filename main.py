import pandas as pd
from data_handler import DataHandler

def main():
    """Main function to run the deobfuscation process"""
    try:
        handler = DataHandler()
        
        data = handler.load_sample_data()
        df = pd.DataFrame(data)
        
        df = handler.decode_data(df)
        
        output_file = handler.save_to_csv(df)
        
        print("\nПервые строки дешифрованных данных:")
        print(df.head())
        print(f"\nРезультат сохранен в файл: {output_file}")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
