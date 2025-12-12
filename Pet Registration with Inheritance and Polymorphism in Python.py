# Base class for all pets
class Pet:
    # Constructor of the Pet class
    def __init__(self, name: str, age: int, color: str, breed: str, sound):
        self._name = name
        self._age = age
        self._color = color
        self._breed = breed
       
        # Abstract method: forces subclasses to implement "sound"
        def sound(self):
            raise NotImplementedError("Subclass must implement sound()")
        
        # Special method to display pet information
        def __str__(self):
            pass

''' 
 ---------------------------
 Class: Dog (inherits from Pet)
 ---------------------------
'''                          
class Dog(Pet):
    # Constructor of the Dog class
    def __init__(self, name: str, age: int, color: str, weight: float, bites: bool):
        super().__init__(name, age, color)  # Calls the Pet constructor
        self.weight = weight
        self.bites = bites

    # Implementation of dog sound
    def sound():
        print("Dogs bark")
   
    # Text representation of the pet
    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Color: {self.color}, Weight: {self.weight}kg, Bites: {self.bites}"
       
# Dog subclasses
class SmallDog(Dog):
    # Customizes how to display a small dog
    def __str__(self):
        return f"Small Dog: {self.name}, Age: {self.age}, Color: {self.color}, Weight: {self.weight}kg, Bites: {self.bites}"

class MediumDog(Dog):
    # Representation of medium dog
    def __str__(self, name: str, age: int, color: str, weight, bites):
        super().__init__(self, name, age, color, breed="Medium")
        return f"---"

class LargeDog(Dog):
    # Representation of large dog
    def __str__(self, name: str, age: int, color: str, weight, bites):
        super().__init__(self, name, age, color, breed="Large")
        return f"---"
                           
''' 
 ---------------------------
 Class: Cat (inherits from Pet)
 ---------------------------
''' 
class Cat(Pet):
    # Constructor of the Cat class
    def __init__(self, name: str, age: int, color: str, jump_height: float, jump_length: float):
        super().__init__(name, age, color)  # Calls the Pet constructor
        self.jump_height = jump_height
        self.jump_length = jump_length
       
    # Implementation of cat sound
    def sound():
        print("Cats meow and purr")
   
    # Text representation of the pet
    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Color: {self.color}, Jump height: {self.jump_height}m, Jump length: {self.jump_length}m"
       
# Cat subclasses
class HairlessCat(Cat):
    def __str__(self):
        return f"Hairless Cat: {self.name}, Age: {self.age}, Color: {self.color}, Jump height: {self.jump_height}m, Jump length: {self.jump_length}m"

class LongHairCat(Cat):
    def __str__(self):
        return f"Long-haired Cat: {self.name}, Age: {self.age}, Color: {self.color}, Jump height: {self.jump_height}m, Jump length: {self.jump_length}m"

class ShortHairCat(Cat):
    def __str__(self):
        return f"Short-haired Cat: {self.name}, Age: {self.age}, Color: {self.color}, Jump height: {self.jump_height}m, Jump length: {self.jump_length}m"

'''
 ---------------------------
 User interaction
 ---------------------------
'''
if __name__ == "__main__":
    # Asks the user what pet they want to register
    pet_type = input("Do you want to register a Dog or a Cat? ").lower()

    if pet_type == "dog":
        # Requests specific dog data
        name = input("Dog's name: ")
        age = int(input("Dog's age: "))
        color = input("Dog's color: ")
        weight = float(input("Dog's weight (kg): "))
        bites_input = input("Does the dog bite? (y/n): ").lower()
        bites = True if bites_input == "y" else False

        # Automatic classification by weight
        if weight < 10:
            pet = SmallDog(name, age, color, weight, bites)
        elif 10 <= weight <= 25:
            pet = MediumDog(name, age, color, weight, bites)
        else:
            pet = LargeDog(name, age, color, weight, bites)

    elif pet_type == "cat":
        # Requests specific cat data
        name = input("Cat's name: ")
        age = int(input("Cat's age: "))
        color = input("Cat's color: ")
        jump_height = float(input("Cat's jump height (m): "))
        jump_length = float(input("Cat's jump length (m): "))

        # Classification by hair type
        hair_type = input("Is the cat hairless, long-haired, or short-haired? ").lower()

        if hair_type == "hairless":
            pet = HairlessCat(name, age, color, jump_height, jump_length)
        elif hair_type == "long-haired":
            pet = LongHairCat(name, age, color, jump_height, jump_length)
        else:
            pet = ShortHairCat(name, age, color, jump_height, jump_length)

    else:
        # Invalid option handling
        print("Invalid pet type")
        pet = None

    # If the pet was created successfully, display it
    if pet:
        print("\n✅ Pet registered:")
        print(pet)
