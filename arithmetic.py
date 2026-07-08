class Arithmetic:
    def encode(self, api: str):
        res = ""

        for char in api:
            res += f"{((ord(char) << (9 - ord(char).bit_length())) & 0xFF) | (1 << ((ord(char) & -ord(char)).bit_length() - 1)):08b} "
        return res
    
    def decode(self, encodedstr: str):
        res = ""

        chars = encodedstr.split()
        for byte in chars:
            res += chr((int(("1" + byte[:byte.rfind('1', 0, byte.rfind('1')) + 1]), 2) << ((int(byte, 2) & -int(byte, 2)).bit_length() - 1)) & 0xFF)
        return res


AEngine = Arithmetic()