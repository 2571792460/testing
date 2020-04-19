import csv

def file_reader():
    food_list = []
    f = open('food_items.csv', 'r')
    content = f.readlines()

    for x in content:
        new = x.split(",")
        food_list.append(new[1])

    food_list.pop(0)
    food_list.sort()
    f.close()
    return food_list

def main():
    food_list = file_reader()
    grocery_list = []
    user_input = user_input = str(input('Enter food item (or "x" to exit): '))
    num_input = ''
    while user_input != 'x':
            if user_input not in food_list:
                print(f'{user_input} is not available. Please try again...')
                user_input = str(input('Enter food item (or "x" to exit): '))
            else:
                num_input = int(input(f'How many {user_input}? '))
                grocery_list.append([user_input,num_input])
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