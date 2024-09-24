import random
import string

class PasswordGen: 
    letters: list = list(string.ascii_letters)
    numbers: list = list(string.digits)
    symbols: list = list(string.punctuation)
    total_data: list = [*letters, *numbers, *symbols]
    
    @classmethod
    def _random_(self, data: list, n:int) -> str:
        return random.choices(data, k=n)
    
    @classmethod
    def create_password(self, len_letters: int, len_symbols: int, len_numbers: int, is_shuffle: bool) -> str:
        pss: list = []
        
        pss.extend(PasswordGen._random_(data=self.letters, n=len_letters))
        pss.extend(PasswordGen._random_(data=self.numbers, n=len_symbols))
        pss.extend(PasswordGen._random_(data=self.symbols, n=len_numbers))
        
        if (is_shuffle): random.shuffle(pss)
        
        return ''.join(pss)
    
    def __call__(self, len_letters: int, len_symbols: int, len_numbers: int, is_shuffle: int) -> str:
        
        is_shuffle: bool = True if is_shuffle is 1 else False
        
        return self.create_password(len_letters=len_letters,
                                    len_symbols=len_symbols,
                                    len_numbers=len_numbers,
                                    is_shuffle=is_shuffle)


if __name__ == "__main__":
    
    print("Welcome to the PyPassword Generator!")
    
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    shuffle = int(input(f"Do you like shuffle the password? 1 for true, 0 for false\n"))
    
    
    print(PasswordGen()(len_letters=nr_letters,
                        len_symbols=nr_symbols, 
                        len_numbers=nr_numbers,
                        is_shuffle=shuffle)
          )