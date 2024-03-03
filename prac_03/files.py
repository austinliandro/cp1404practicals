"""1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file. """
FILENAME = "name.txt"
user_name = input("Please enter your name: ")
with open(FILENAME, 'w') as out_file:
    print(user_name, file=out_file)

"""2. Write code that opens "name.txt" and reads the name (as above) then prints,
Your name is Bob"""

with open(FILENAME) as in_file:
    name = in_file.read().strip()
    print(f"Your name is {name}")

"""3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on 
separate lines in the file and save it """

with open('numbers.txt') as in_file:
    numbers = in_file.read().split()
    total_numbers = int(numbers[0]) + int(numbers[1])
#     add the first two numbers together
    print(total_numbers)

"""4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number 
of numbers. """
total = 0
with open('numbers.txt') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
