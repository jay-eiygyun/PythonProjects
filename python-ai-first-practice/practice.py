string = "My name is Jay"
print (string)
my_long_string ="""
My name is Jay
and I love my gf <3
"""
print(my_long_string)
first_name = "Jay"
last_name = "Eyigun"
full_name = first_name + " " + last_name
print (full_name) 
long_dash = "-" * 10
print (full_name)
print (long_dash)
len (full_name)

is_true = True
age = 19;
is_18 = age <= 18

#Logical Operators
age = 22
has_license = True
drunk = False
can_drive = age >= 16 and has_license and not drunk
print (can_drive)

name = "jada"
string = f"Hi there, my name is {name}" 
name.lower()
name.upper()
sentence = "hi my name is ismet"
sentence.title()
--------------------------------

temperature = 32
if temperature > 30:
    print("It's very hot!!")
elif temperature > 25: 
    print("Its hot")
else:
    print("Its a nice weather")

-------------------------------
has_ticket = False
age = 18

if has_ticket:
    if age >= 18:
        print("Enjoy the movie")
    else:
        print("You are not eligable")
else:
    print("Please buy a ticket")
----------------------------------

for i in range(5):
    print(i)

--------------------------------

age = 25
has_license = False
my_list = ["Bob", 25, age, True, has_license]

my_list[0]
my_list [1]
my_list.remove ("Bob")
my_list.insert (0, "Bob")
print (my_list)

-------------------------------

person = {
    "name": "Jada",
    "age": 21,
    "city": "Toronto",
    "interest": "Real Estate",
    "has_dog": True
}
person["age"]
person["city"]
person["name"]
person["interest"]
person["has_dog"]
for key in ["age", "city", "has_dog", "interest", "city"]:
    print(person[key])
-------------------------------

empty_set = set()

numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

------------------------------
def greet():
    print ("Hello")
    print ("Shit")

greet()


def check_weather():
    temperature = 28
    if temperature > 25:
        print ("Its hot")
    else:
        print ("Its a good weather")
check_weather()

def greet(name):
    print(f"Hello, {name}")



def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("Jay", "Eiygyun")

-----------------------
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Toal: ${final_price}")
calculate_total(100, 0.08, 10)
calculate_total(250, 0.13, 4)

-------------------------
def add_print(a,b):
    print(a + b)
add_print(a=5, b=10)

def add_return(a,b):
    return a + b 

result = add_return(a=5, b=10)
result + 20
------------------------
def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers [0]
    last_number = numbers [-1]
    return first_number, last_number

first_number, last_number = simple_function()