
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

def print_grocery_list(grocery_list):
    for item in grocery_list:
        print (item)
        grocery_list.index(item)
    return grocery_list


print(print_grocery_list(grocery_list))



print_grocery_list(grocery_list)