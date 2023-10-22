import random

class PasswordGenerator:
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+="
    
    def __init__(self):
        
        self.pass_length = int(input("Enter the length of Password: "))
        self.no_of_passwords_to_be_generated = int(input("How many passwords you want to generate: "))
        
    def pass_generator(self):
        
        while True:
            
            for i in range(0, self.no_of_passwords_to_be_generated):
                password = ""
                
                for j in range(0, self.pass_length):
                    pass_char = random.choice(PasswordGenerator.characters)
                    password = password + pass_char
                
                print("The Generated Password is:", password)
            
            repeat = input("Do you want to generate more passwords?")
            
            if repeat == "No" or repeat == "no":
                break
        
        print("Thank You!")