
import csv


ID_NUMBER_INDEX = 0
NAME_INDEX = 1

def read_dictionary(filename, ID_NUMBER_INDEX):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
    filename: the name of the CSV file to read.
        key_column_index: the index of the column
        to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict={}

    with open(filename, "rt") as file:
        reader=csv.reader(file)
        next(reader)
        for line in reader:
            key=line[ID_NUMBER_INDEX]
            name=line[NAME_INDEX]
            student_dict[key]= name
    return student_dict

def main():
    filename= 'students.csv'
    ID_NUMBER_INDEX=0
    student_dict= read_dictionary(filename,ID_NUMBER_INDEX)
    user_input_id=input('Please entert an I-Number (xxxxxxxxx): ')
    if user_input_id in student_dict:
        print(student_dict[user_input_id])
    else:
        print('No such student')

if __name__ == '__main__':
    main()