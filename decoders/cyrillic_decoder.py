class CyrillicDecoder:
    """Handles decoding of Cyrillic characters using Caesar cipher"""
    
    def __init__(self, shift=8):
        self.shift = shift
    
    def decode(self, text):
        """Decodes Cyrillic text with the specified shift"""
        result = ""
        for char in text:
            if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
                if char.lower() == 'ё':
                    base_ord = ord('е') + 1
                else:
                    base_ord = ord('а')
                    
                is_upper = char.isupper()
                char_lower = char.lower()
                
                if char_lower == 'ё':
                    pos = 6
                else:
                    pos = ord(char_lower) - ord('а')
                    
                new_pos = (pos - self.shift) % 33
                
                if new_pos == 6:
                    decoded = 'Ё' if is_upper else 'ё'
                else:
                    decoded = chr(new_pos + ord('а'))
                    if is_upper:
                        decoded = decoded.upper()
                        
                result += decoded
            else:
                result += char
        return result
    
    @property
    def key(self):
        """Returns the encryption key used"""
        return self.shift