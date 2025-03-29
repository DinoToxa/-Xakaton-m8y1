import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
