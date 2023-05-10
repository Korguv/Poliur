import random
import string


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Alphanum Random string of length", length, "is:", rand_string)


generate_alphanum_random_string(8)