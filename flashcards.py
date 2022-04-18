import random
import io
import argparse


def check(check_all, list_all):
    if check_all in list_all:
        return 'stop'
    else:
        return 'go'


def find_term(defin_find, dict_find):
    for k, v in dict_find.items():
        if v == defin_find:
            return k
    return 'not'


def add():
    print('The card:')
    key_add = str(input())
    print('The card:', file=fp, end='\n')
    print(key_add, file=fp, end='\n')
    while check(key_add, list_all) != 'go':
        print('The term "{}" already exists. Try again:'.format(key_add))
        print('The term "{}" already exists. Try again:'.format(key_add), file=fp, end='\n')
        key_add = input()
        print(key_add, file=fp, end='\n')
    list_cart.append(key_add)
    list_all.append(key_add)
    dict_fail[key_add] = 0
    print('The definition of the card:')
    defin_add = str(input())
    print('The definition of the card:', file=fp, end='\n')
    print(defin_add, file=fp, end='\n')
    while check(defin_add, list_all) != 'go':
        print('The definition "{}" already exists. Try again:'.format(defin_add))
        print('The definition "{}" already exists. Try again:'.format(defin_add), file=fp, end='\n')
        defin_add = input()
        print(defin_add, file=fp)
    list_all.append(defin_add)
    dict_cart[key_add] = defin_add
    print('The pair ("{}":"{}") has been added.'.format(key_add, defin_add))
    print('The pair ("{}":"{}") has been added.'.format(key_add, defin_add), file=fp, end='\n')
    return


def remove():
    print('Which card?')
    rem = str(input())
    print('Which card?', file=fp, end='\n')
    print(rem, file=fp, end='\n')
    if rem in dict_cart:
        dict_cart.pop(rem)
        list_cart.remove(rem)
        dict_fail.pop(rem)
        print('The card has been removed.')
        print('The card has been removed.', file=fp, end='\n')
        return
    else:
        print('''Can't remove "{}": there is no such card.'''.format(rem))
        print('''Can't remove "{}": there is no such card.'''.format(rem), file=fp, end='\n')
        return


def _import(imp):
    i = 0
    try:
        my_file = open(imp, 'r')
        while True:
            impo = my_file.readline().split()
            print(impo)
            if not impo:
                break
            key_imp = impo[0]
            if len(impo) == 2:
                dict_cart[key_imp] = impo[1]
            elif len(impo) == 3:
                dict_cart[key_imp] = impo[1]
                dict_fail[key_imp] = int(impo[2])
            else:
                dict_cart[key_imp] = ''
            list_cart.append(key_imp)
            i += 1
    except FileNotFoundError:
        print("File not found.")
        print("File not found.", file=fp, end='\n')
        return
    my_file.close()
    print('{} cards have been loaded.'.format(i))
    print('{} cards have been loaded.'.format(i), file=fp, end='\n')
    return


def _export(exp):
    my_exp_file = open(exp, 'w')
    i = 0
    for k in dict_cart.keys():
        string = str('')
        string += k + ' ' + dict_cart.get(k) + ' ' + str(dict_fail[k]) + '\n'
        my_exp_file.write(string)
        i += 1
    print('{} cards have been saved.'.format(i))
    print('{} cards have been saved.'.format(i), file=fp, end='\n')
    return


def ask():
    print('How many times to ask?')
    number = int(input())
    print('How many times to ask?', file=fp, end='\n')
    print(number, file=fp, end='\n')
    for j in range(number):
        i = random.randint(0, len(dict_cart) - 1)
        print('Print the definition of "', list_cart[i], '":', sep='')
        print('Print the definition of "', list_cart[i], '":', sep='', end='\n', file=fp)
        answer = input()
        print(answer, file=fp)
        if answer == dict_cart.get(list_cart[i]):
            print('Correct!')
            print('Correct!', end='\n', file=fp)
        elif find_term(answer, dict_cart) != 'not':
            dict_fail[list_cart[i]] += 1
            print('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                dict_cart.get(list_cart[i]), find_term(answer, dict_cart)))
            print('Wrong. The right answer is "{}", but your definition is correct for "{}".'.format(
                dict_cart.get(list_cart[i]), find_term(answer, dict_cart)), file=fp, end='\n')
        else:
            dict_fail[list_cart[i]] += 1
            print('Wrong. The right answer is "', dict_cart.get(list_cart[i]), '".', sep='')
            print('Wrong. The right answer is "', dict_cart.get(list_cart[i]), '".', sep='', file=fp, end='\n')
    return


def log():
    print('File name:')
    name = str(input())
    print('File name:', file=fp, end='\n')
    print(name, file=fp, end='\n')
    fp.getvalue()
    with open(name, 'w') as log:
        log.write(fp.getvalue())
    print('The log has been saved.', end='\n')
    print('The log has been saved.', file=fp, end='\n')
    return


def hardest():
    x = 0
    k = ''
    for key in dict_fail.keys():
        if dict_fail[key] > x:
            x = dict_fail[key]
            k = '"{}"'.format(key)
        elif dict_fail[key] == x:
            k += ', "{}"'.format(key)
    if x == 0:
        print('There are no cards with errors.')
        print('There are no cards with errors.', file=fp, end='\n')
        return
    print('The hardest card is {}. You have {} errors answering it'.format(k, x))
    print('The hardest card is {}. You have {} errors answering it'.format(k, x), file=fp, end='\n')
    return


def reset():
    for k in dict_fail.keys():
        dict_fail[k] = 0
    print('Card statistics have been reset.')
    print('Card statistics have been reset.', file=fp, end='\n')
    return


def _exit():
    print('Bye bye!')
    print('Bye bye!', file=fp, end='\n')
    fp.close()
    return


dict_cart = {}
dict_fail = {}
list_cart = []
list_all = []
parser = argparse.ArgumentParser()
parser.add_argument('--import_from', default=None)
parser.add_argument('--export_to', default=None)
fp = io.StringIO()
args = parser.parse_args()

if args.import_from is not None:
    _import(args.import_from)

while True:
    print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
    act = str(input())
    print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):",
          file=fp, end='\n')
    print(act, file=fp, end='\n')
    if act == 'add':
        add()
    elif act == 'remove':
        remove()
    elif act == 'import':
        print('File name:')
        imp = str(input())
        print('File name:', file=fp, end='\n')
        print(imp, file=fp, end='\n')
        _import(imp)
    elif act == 'export':
        print('File name:')
        exp = str(input())
        print('File name:', file=fp, end='\n')
        print(str, file=fp, end='\n')
        _export(exp)
    elif act == 'ask':
        ask()
    elif act == 'log':
        log()
    elif act == 'hardest card':
        hardest()
    elif act == 'reset stats':
        reset()
    elif act == 'exit':
        if args.export_to is not None:
            _export(args.export_to)
        _exit()
        break
