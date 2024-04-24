
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

def print_grocery_list(grocery_list):
    for i in range(len(grocery_list)):
        list = grocery_list.pop(0)
        print(list)

print_grocery_list(grocery_list)