#application 1
def alternating(string):
    new_string = " "
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)


alternating("I am Gamze. And I am learning machine learning.")

#application 2

students = ["Harry", "Johnny", "Mark", "Donny"]

for student in students:
    print(student)

odd_index_list = []
even_index_list = []

for index, student in enumerate(students):
    if index % 2 == 0:
        even_index_list.append(student)
    else:
        odd_index_list.append(student)

    print(index, student)

print("Even index list:", even_index_list)
print("Odd index list:", odd_index_list)

#application 3

#divide_students fonksiyonunu yaz
#çift indexte yer alan öğrencileri bir listeye al
#tek indexte yer alan öğrencileri bir listeye al
#fakat bu iki liste tek bir liste olarak return olsun

students = ["Harry", "Johnny", "Mark", "Donny"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)


#Application 4 (app1 ile aynı amaç)

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("I am Gamze. And I am learning machine learning.")

#LIST COMPREHENSIONS

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

print(null_list)


#tüm bu işlemleri list comprehension ile nasıl yaparız

#[salary *2 for salary in salaries]
#[salary *2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary *2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

#Application 5

#students_no listesindeki ogrencilerin kücük harfle yazılmasını, digerlerinin ise büyük harflerler yazılmasını istiyoruz
#eğer il tek basına else olmadan varsa for başa yazılır

students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]

#in yerine not in kullanıp aynı şeyi yapabiliriz

[student.upper() if student not in students_no else student.lower() for student in students]

#DICT COMPREHENSIONS

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4
              }

dictionary.keys()
dictionary.values()
dictionary.items()

#keylere dokunmadan herbir valuenin karesini almak istiyoruz

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v**2 for (k, v) in dictionary.items()}

#Application 6

#Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek isteniyor
#keyler orijinal olacak, values değişecek

#klasik yontem

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

#dict comprehension ile

{n: n ** 2 for n in numbers if n % 2 == 0}