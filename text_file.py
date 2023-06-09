# Open the numbers.txt file for reading
with open('numbers.txt', 'r') as file:
    # Read the contents of the file into a list of integers
    numbers = [int(number) for number in file.read().split()]

# Create two new files, even.txt and odd.txt, for writing
with open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:
    # Loop through each number in the list
    for number in numbers:
        # Check if the number is even
        if number % 2 == 0:
            # Write the even number to the even.txt file
            even_file.write(str(number) + '\n')   
            print("\033[32m" + (str(number) + "\033[0m"))

        else:
            # Write the odd number to the odd.txt file
            odd_file.write(str(number) + '\n')
            print("\033[31m" + (str(number) + "\033[0m"))
           
