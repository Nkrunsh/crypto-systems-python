import random
import string

class CaesarCode:

    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabet_len = len(self.alphabet)

    def generate_key(self, letter):
        index = self.alphabet.index(letter.lower())
        key_path = random.choice( range(self.alphabet_len))
        for _ in range(key_path):
            if index == 0:
                index = self.alphabet_len - 1
            else:
                index -= 1
        return self.alphabet[index] + str(key_path)
    
    def isStringNum(sefl, nun):
        for digit in nun:
            if digit not in string.digits:
                return False
        return True

    def get_char(self, key):
        key_char = key[0].lower()

        if key_char not in self.alphabet:
            raise ValueError("CharError")
        if self.isStringNum(key[1:]):
            key_path = int(key[1:])
        else:
            raise ValueError("NumError")

        index = self.alphabet.index(key_char)
        index = (key_path + index) % self.alphabet_len
        return self.alphabet[index]

    def encode(self, text):
        text = text.lower()
        msg_encode = ''
        for letter in text:
            if letter in self.alphabet:
                msg_encode += self.generate_key(letter)
            else:
                msg_encode += letter
        return msg_encode

    def decodeWord(self,word):
        star = 0
        end = 3
        msg = ''
        while 1:
            try:
                msg += self.get_char(word[star:end])
            except ValueError as e:
                try:
                    end -=1
                    msg += self.get_char(word[star:end])           
                except:
                    break
            star = end
            end += 3

            if end > len(word):
                end = len(word)

            if star == end:
                break
        return msg
    
    def decodeText(self, text):
        words = text.split(' ')
        decodeText =''
        for word in words:
            decodeText += self.decodeWord(word)
            decodeText += ' '
        return decodeText

    def manualDecode(self):
        msg = ''
        print("Ingresa las llaves para desencriptar:\n Para finalizar, ingresa #")
        while 1:
            key = input()

            if key[0] == '#':
                break

            try:
                msg += self.get_character(key)
            except:
                print("Llave incorrecta, vuelve a intentar")
        print(msg)
            

if __name__ == '__main__':
    code = CaesarCode()
    tex = code.encode('Hola Mundo')
    print(tex)
    detex = code.decodeText(tex)
    print(detex)
   




