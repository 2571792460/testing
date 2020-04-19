import csv
def main():
    user_input = user_input = str(input('Enter food item (or "x" to exit): '))
    num_input = 0
    grocery_list = []


    while user_input != 'x':
        while type(num_input) != str:
            try:
                num_input = int(input(f'How many {user_input}? '))
            except ValueError:
                print('Quantity must be a number')
                break

            grocery_list.append([(user_input.casefold()).capitalize(),num_input])
            print(f'>{str(num_input) +" " + user_input} added to grocery list')
            user_input = str(input('Enter food item (or "x" to exit): '))
            if user_input == 'x':
                confirmation = input("Do you want to save your shopping list [Y|N]? ")
                if confirmation == 'Y' or confirmation == 'y':
                    file_name = input('Enter a name for your list: ')
                    with open(f'{file_name}.csv', 'w') as file_name:

                        writer = csv.writer(file_name)
                        for x in grocery_list:
                            writer.writerow(x)

                    print(f'Shopping list saved to {file_name}.csv')
                else:
                    break



main()

