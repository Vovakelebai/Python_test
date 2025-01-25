import random 

def createFileWihtRandomNumbers(filename, num_random_numbers, min_value, max_value):
    with open(filename,'w') as file:
        for _ in range(num_random_numbers):
            random_number = random.randint(min_value, max_value)
            file.write(f"{random_number}\n")  # Write each number on a new line
