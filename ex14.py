from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the script.")
print("I'd would like to ask you a few qeustions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. not sure where that is.
and you have a {computer} computer. Nice.
""")
