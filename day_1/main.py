
recipe_list = [
    "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.",
    "2. Knead the dough for 10 minutes.",
    "3. Add 3g of Salt.",
    "4. Leave to rise for 2 hours.",
    "5. Bake at 200 degrees C for 30 minutes.",
    ]

class Recipe():
    
    @staticmethod
    def print_recipe(list) -> list:
        for item in list:
            print(item)

if __name__ == "__main__":
    Recipe.print_recipe(recipe_list)
    
    print("hello" + " " + "angela")
    print("hello, " + input("What's your name? ") + "!")
    
    name = "Luis"
    
    print(len(name))