def main():
        user_input = user_input = str(input('Enter food item (or "x" to exit): '))
        num_input = 0
        grocery_list = []


        while user_input != 'x':
                num_input = int(input(f'How many {user_input}? '))
                grocery_list.append([user_input,num_input])
                user_input = str(input('Enter food item (or "x" to exit): '))

        print(grocery_list)


main()