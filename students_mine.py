import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header line

        for row in reader:
            key = row[key_column_index]
            value = row[1 - key_column_index]  # Assuming the other column is the value
            student_dict[key] = value

    return student_dict

def main():
    filename = "students.csv"
    key_column_index = 0  # Assuming I-Number is the first column

    student_dict = read_dictionary(filename, key_column_index)

   # Get an I-Number from the user
    i_number_input = input("Enter I-Number: ")

    # Remove dashes from the user input
    i_number = i_number_input.replace("-", "")

    # Validate the length of the I-Number
    if len(i_number) != 9:
        print("Invalid I-Number. It should have exactly 9 digits.")
        return

    # Use the I-Number to find the corresponding student name in the dictionary
    student_name = student_dict.get(i_number, None)

    # Print the result
    if student_name is not None:
        print("Student Name:", student_name)
    else:
        print("No such student")

if __name__ == "__main__":
    main()