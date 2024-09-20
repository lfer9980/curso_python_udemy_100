import random
import string


print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# new_list: list = []

class PasswordGen: 
    letters: list = list(string.ascii_letters)
    numbers: list = list(string.digits)
    symbols: list = list(string.punctuation)
    total_data: list = [*letters, *numbers, *symbols]
    
    @classmethod
    def _random_(cls) -> str:
        return random.choice(cls.total_data)
    
    @classmethod
    def create_password(cls, len_pss: int) -> str:
        pss: list = [PasswordGen._random_() for _ in range(len_pss)]
        
        return ''.join(pss)
    
    def __call__(self, len_pss: int) -> str:
        return self.create_password(len_pss=len_pss)

	# @staticmethod
	# def select_random_item(base_list:list, len_new_list: int) -> list:     
	# 	len_base_list: int = len(base_list)
  
	# 	return [base_list[PasswordGen._random_number(len_base_list)] for _ in range(0, len_new_list)]

	# @staticmethod
	# def create_password(data: list) -> str:
	# 	random.shuffle(data)
	# 	return ''.join(data)
 	

if __name__ == "__main__":
    
    # final_list: str = [*letters_list, *symbols_list, *numbers_list]
    # # new_list:str = ''.join([*letters_list, *symbols_list, *numbers_list])
    
    # print(new_list)
    print(PasswordGen()(100))
    