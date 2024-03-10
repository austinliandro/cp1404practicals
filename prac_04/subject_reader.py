"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    datas = get_data()
    print(datas)
    display_subject_details(datas)


def display_subject_details(datas):
    for data in datas:
        subject_code = data[0]
        teacher = data[1]
        number_of_student = data[2]
        print(f"{subject_code} is taught by {teacher} and has {number_of_student} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        datas.append(parts)
    input_file.close()
    return datas


main()
