import random

def generate_love_percentage(name1, name2):
    combined_name = (name1 + name2).lower()
    seed = sum(ord(char) for char in combined_name) % 100
    random.seed(seed)
    return random.randint(0, 100)

def display_love_message(love_percentage):
    if love_percentage > 75:
        return "Wow, you two are a great match!"
    elif love_percentage > 50:
        return "There's a strong connection between you two."
    elif love_percentage > 25:
        return "You might need to work on it a bit."
    else:
        return "It seems like it's a bit of a struggle."

def main():
    print("Welcome to the Love Calculator!")
    
    name1 = input("Enter Your Name: ")
    name2 = input("Enter Your Partner's Name: ")
    
    love_percentage = generate_love_percentage(name1, name2)
    message = display_love_message(love_percentage)
    
    print(f"\nLove Percentage between {name1} and {name2} is: {love_percentage}%")
    print(message)

if __name__ == "__main__":
    main()
