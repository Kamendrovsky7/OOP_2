from pprint import pprint

# первое задание, открытие и чтение фаила из исходного txt, создание кулинарной книги
def cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_cook = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_cook.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_cook
    return cook_book

# второе задание, реализация функции по расчёту ингрединетов на кол-во персон

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


# вывод книги рецептов
cook_book = cook_book()
pprint(cook_book)

# вывод расчета

print("Расчет ингредиентов на указанное количество персон:",'\n', get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

