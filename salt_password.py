import random
import string


def get_new_salt_password(password: str, length_out_str: int = 10000) -> str:
    abc = ''
    abc += string.ascii_letters  # All letters a-z, A-Z
    abc += string.digits  # All digits 0-9
    abc += string.punctuation  # All punctuation
    abc = set(abc)
    abc.difference_update(set(password))
    out_str = []
    for _ in range(length_out_str):
        r = random.sample(list(abc), 1)
        out_str.extend(random.sample(list(abc), 1))

    position_symbol_word = random.sample(list(range(length_out_str)), len(password))
    position_symbol_word.sort()

    for i, symbol in enumerate(password):
        out_str[position_symbol_word[i]] = password[i]

    out_str = ''.join(out_str)
    print(out_str)
    return out_str


def get_password_from_salt_password(password_and_salt: str):
    symbols = set(password_and_salt)
    symbols = list(symbols)
    p = dict()
    for symbol in symbols:
        p[symbol] = password_and_salt.count(symbol)
        print(symbol, p[symbol])
    symbols = [k for k, v in p.items() if v < 200]
    print(symbols)
    out = [x for x in password_and_salt if x in symbols]
    out_str = ''.join(out)
    print(out_str)
    return out_str


if __name__ == '__main__':
    word = 'congratulation'
    word = 'you win!'
    word = 'I won to be free. congratulation !! you win!'

    salt_pass = get_new_salt_password(word, 100000)
    get_password_from_salt_password(salt_pass)
