def open_file(text_file):
    with open (text_file, 'r') as f:
        words = f.readline().strip(' ').split(',')

    new_words = tuple(i.strip() for i in words)
    return new_words

def get_category():
    print('Choose the category you like:')
    print(
    '''
    1. Animals
    2. Brands
    3. Cars
    '''
    )
    try:
        num_of_category = int(input('Select 1, 2 or 3: '))
        if num_of_category == 1:
            print('Your choice is Animals', end='\n\n')
            return open_file('animals.txt')
        elif num_of_category == 2:
            print('Your choice is Brands', end='\n\n')
            return open_file('brands.txt')
        elif num_of_category == 3:
            print('Your choice is Cars', end='\n\n')
            return open_file('cars_brands.txt')
        else:
            print('Сhoose the suggested options')
            temp = input('If you don\'t want to play enter EXIT or CONTINUE if you want: ')
        if temp.lower() == 'exit':
            print('Bye, see you later!')
        elif temp.lower() == 'continue':
            return get_category()
        else:
            print('I don\'t know what do you want...')
    except ValueError:
        print('Choose the number!')
        return get_category()
