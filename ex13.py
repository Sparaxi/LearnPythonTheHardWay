from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)

print("your first variable:", first)
print("your second variable:", second)
print("your third variable:", third)


print("How old are you ?", end = ' ')
age = input()

print(f"so you are {age} old?")

print('What have you learned sofar ?', end = ' ')
learned = input()

print(f'so what have you learned sofar {learned} That is so good of you ! well done !')
