import random

def inputting():
    f=open("input_characters.txt").read().split("\n")
    if f[-1] == "": f.pop()

    return [i for i in f]


def purely_random_passwords(maximal_lenght, minimal_lenght, fill_with_random_chars, minimal_each, amount_of_passwords):
    file = inputting()

    minimal_total=0
    for i in minimal_each: minimal_total+=i
    if minimal_total>maximal_lenght: return "max lenght is lower than required elements"

    for i in range(amount_of_passwords):
        password=''
        for allchars in range(3):
            for idx in range(minimal_each[allchars]):
                password += random.choice(file[allchars])

        if len(password) < maximal_lenght:
            to_gen = random.randint(0, maximal_lenght-minimal_lenght) + sum(minimal_each)

            for i in range(to_gen):
                if fill_with_random_chars: char = random.choice(file[random.randint(0,3)])
                else: char = random.choice(file[3][:26])

                password += char


        print(''.join(random.sample(password,len(password))))


#minimal_each --> [CAPITAL LETTERS, numb3rs, str@nge symb()ls]
#fill_with_random_chars --> if False, extra characters in password will be more letter focused
#                       --> if True, extra characters in password will be equally distributed
print(purely_random_passwords(maximal_lenght=20, minimal_lenght=7, fill_with_random_chars=False, minimal_each=[2, 3, 2], amount_of_passwords=300))
