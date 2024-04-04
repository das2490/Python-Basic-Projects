import random

def Password_Generator():
    name = input("Enter your full name to create password : ").strip()
    nums = '1234567890'
    uni = '!@#$%\/'
    first = name[:name.index(' ')]
    last = name[name.index(' ')+1:]
    password = ''.join(random.sample(nums,3)) + first + random.choice(uni) + last
    print(f'Your password is : "{password}"')
