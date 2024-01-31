import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = []

    print(f'First Number list: {numbers}\n')

    append_random_numbers(numbers)
    print(f'Second Number list: {numbers}\n')
    user_quantity=int(input('How many numbers you want to add to the list: '))
    append_random_numbers(numbers,user_quantity)
    print(f'Third Number list: {numbers}')
    append_random_words(words)
    print(f'First word list: {words}')
    append_random_words(words,3)
    print(f'Second word list: {words}')
 
def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        newnumber = round(random.uniform(0,100),1)
        numbers_list.append(newnumber)

def append_random_words(word_list, quantity=1):
    choice_list = ['😊', 'love', 'smile', 'love', 'cloud', 'head', '😒']
    for i in range(quantity):
        new_word = random.choice(choice_list)
        word_list.append(new_word)

if __name__ == "__main__": main()