import math
import random


def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%^&*"

pass_len = 16

alpha_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (alpha_len + num_len)

password = []

# alpha password
generate_pass(alpha_len, alpha, True)
# numeric password
generate_pass(num_len, num)
# special Character password
generate_pass(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert list to string
gen_password = ""
for i in password:
    gen_password += str(i)

print(gen_password)
