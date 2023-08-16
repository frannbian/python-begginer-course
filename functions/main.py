# Functions

def hello(name, age):
    if not name:
        return
    print(f"Hello! {name}, you have {age} years old")
    
hello("Franco", "asd")


#variables scopes
# if we declare the variable before the function we can use inside there
age = 8

def test():
    print(age)
    
print(age) #return 8
test() #return 8


#functions inside a function

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I AM GOING TO BUY MILK")

# Nonlocal variable

def count():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(count)
    increment()
    
count()