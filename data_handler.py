import pandas as pd
from datetime import datetime
from decoders.latin_decoder import LatinDecoder
from decoders.cyrillic_decoder import CyrillicDecoder

class DataHandler:
    """Handles data processing and file operations"""
    
    def __init__(self):
        self.latin_decoder = LatinDecoder()
        self.cyrillic_decoder = CyrillicDecoder()
    
    def load_sample_data(self):
        """Loads sample encrypted data"""
        return {
            'email': [
                'pmjmz.bzmujtig@nzqmamv.kwu',
                'giyh.lsxyl@pifeguh.vct',
                'enxbepbms.tkexgx@ykbxlxg.vhf'
            ],
            'address': [
                'ыу. Лпмшорхщтцкцл.6 тй.466',
                'Юдуебвудашэеюут жя.ч.34 юх.102',
                'вг. Сэёкэыатц.60 эф.107'
            ]
        }
    
    def decode_data(self, df):
        """Decodes the data and adds encryption keys"""
        df['encryption_key_email'] = self.latin_decoder.key
        df['encryption_key_address'] = self.cyrillic_decoder.key
        
        df['email_decoded'] = df['email'].apply(
            lambda x: self.latin_decoder.decode(x) if '@' in x 
            else self.cyrillic_decoder.decode(x)
        )
        df['address_decoded'] = df['address'].apply(self.cyrillic_decoder.decode)
        
        return df
    
    def save_to_csv(self, df, filename=None):
        """Saves the decoded data to a CSV file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'deobfuscated_data_{timestamp}.csv'
        
        df.to_csv(filename, index=False, encoding='utf-8')
        return filename
