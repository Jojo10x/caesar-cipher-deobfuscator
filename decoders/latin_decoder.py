class LatinDecoder:
    """Handles decoding of Latin characters using Caesar cipher"""
    
    def __init__(self, shift=15):
        self.shift = shift
    
    def decode(self, text):
        """Decodes Latin text with the specified shift"""
        result = ""
        for char in text:
            if char.isalpha():
                base = 'a' if char.islower() else 'A'
                decoded = chr((ord(char) - ord(base) - self.shift) % 26 + ord(base))
                result += decoded
            else:
                result += char
        return result
    
    @property
    def key(self):
        """Returns the encryption key used"""
        return self.shift