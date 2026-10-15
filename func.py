def hello(username, age, country = "Россия"):
    print(f"hello {username}, age {age}, country{country}")

hello("John", 4, "Thailand")




def print_numbers(*numbs):
    for n in numbs:
        print(n)

print_numbers(1, 2, 3, 4, 5)


def print_numbers(*numbs):
    s = 0
    for n in numbs:
        s += n
        print(s)

print_numbers(1, 2, 3, 4, 5)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(
    a="hello"
    b="world"
    c="Tomsk"
)

name = 'John'
age = 28
work = 'teacher'

people = (
    'name': 'John',
    'age': 28,
    'work': 'teacher'
)
print(people)

person_data = {
    'person':{
        'name': 'Илатий'
        'last_name': 'Streich',
        'middle_name': 'Азарий',
    },
    'company':{
        'post': 'менеджер',
        'company_name': 'ОАО ДудинкаТрейдРус'
    },
}

print(
    person_data['person']['name']
)

if 'address' in person_data:
    print(person_data['address'])
else:
    print('no address')

print(
    person_data.get('person1')
)

person_data['education'] = {
    'school': 'high',
    'course': 4,
    }
print(person_data)

#получение ключей
print(person_data.keys())
print('-'*20)
#получение значений
print(person_data.values())

#замена значений
person_data['person']['last_name'] = 'Adbaham'

print(person_data)

print('-'*30)

#удаление по ключу
del person_data['address']
print(person_data)


a = 5**2
b = 25**0.5
print(a)
