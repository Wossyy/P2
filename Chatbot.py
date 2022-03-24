"""

Hi, this program lets you convert Eur to any currency for any given year between 1999-now!

Enjoy!
- Alberto

"""

# http://data.fixer.io/api/2013-03-16?access_key=a8f66ac517f5118e099fb345731ab418&symbols=USD,AUD,CAD,PLN,MXN&format=1\

# https://www.geeksforgeeks.org/get-current-date-using-python/
# https://pypi.org/project/colorama/

# Imports
from datetime import date
from colorama import Fore
import requests
import json
import time


def welcome_animation():
    # Welcome Animation also sets everything green by using Fore.GREEN
    print(Fore.GREEN + """__       __  ________  __         ______    ______   __       __  ________
     """, end='')
    time.sleep(.3)
    print("""/  |  _  /  |/        |/  |       /      \  /      \ /  \     /  |/        |
    """, end='')
    time.sleep(.3)
    print("""$$ | / \ $$ |$$$$$$$$/ $$ |      /$$$$$$  |/$$$$$$  |$$  \   /$$ |$$$$$$$$/
    """, end='')
    time.sleep(.3)
    print("""$$ |/$  \$$ |$$ |__    $$ |      $$ |  $$/ $$ |  $$ |$$$  \ /$$$ |$$ |__
    """, end='')
    time.sleep(.3)
    print("""# $$ /$$$  $$ |$$    |   $$ |      $$ |      $$ |  $$ |$$$$  /$$$$ |$$    |
    """, end='')
    time.sleep(.3)
    print("""$$ $$/$$ $$ |$$$$$/    $$ |      $$ |   __ $$ |  $$ |$$ $$ $$/$$ |$$$$$/
    """, end='')
    time.sleep(.3)
    print("""$$$$/  $$$$ |$$ |_____ $$ |_____ $$ \__/  |$$ \__$$ |$$ |$$$/ $$ |$$ |_____
    """, end='')
    time.sleep(.3)
    print("""$$$/    $$$ |$$       |$$       |$$    $$/ $$    $$/ $$ | $/  $$ |$$       |
    """, end='')
    time.sleep(.3)
    print("""$$/      $$/ $$$$$$$$/ $$$$$$$$/  $$$$$$/   $$$$$$/  $$/      $$/ $$$$$$$$/
    """, end='')
    time.sleep(1)


welcome_animation()


def calc_one(base_euro, rate_dict, today):
    # Asks the user if they want to do calculations
    print('The ' + user_date + ' currency conversions for (' + str(today) + ') are:')
    for i in rate_dict:
        print('1 ' + base_euro + ' is equal to ' + str(rate_dict[i]) + ' ' + str(i))
    while True:
        calc_yn = input('Do you want to do some calculations with these results? Please enter y/n: ')
        if calc_yn.lower() == 'y' or calc_yn.lower() == 'yes':
            # Forces the user to enter the number, Source:
            # https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python
            while True:
                try:
                    num_currency = int(input('Ok! How many ' + base_euro + ' do you want to convert? Please enter '
                                                                           'a number: '))
                    break
                except ValueError:
                    print("\nPlease enter a number \n")
            print('Ok! What do you want to convert to? These are your options in case you forgot:')
            for i in rate_dict:
                print(str(i) + ' ', end='')
            # Asks the user which one they choose and prints out the results.
            while True:
                currency_convert = input('\nSo which one do you choose? ')
                if currency_convert in rate_dict:
                    print('\nOk! Here are your results:')
                    x = float(num_currency)
                    y = float(rate_dict[currency_convert])
                    converted = round(x * y, 10)
                    print('The value of ' + str(num_currency) + ' ' + base_euro + ' (for ' + str(today) + ')' +
                          ' is equal to ' + str(converted) + ' ' + str(currency_convert))
                    break
                else:
                    print('\nPlease enter a one of the choices')
            break
        elif calc_yn.lower() == 'n' or calc_yn.lower() == 'no':
            print('Ok! ending the program')
            exit()
        else:
            print('\nPlease enter y/n\n')
    return

# Calc_two is pretty similar to calc_one with just a few changes


def calc_two(base_euro, rate_dict, user_date):
    print('The ' + user_date + ' currency conversions for (' + user_date + ') are:')
    for i in rate_dict:
        print('1 ' + base_euro + ' is equal to ' + str(rate_dict[i]) + ' ' + str(i))
        # Asks the user if they want to do calculations
        while True:
            calc_yn = input('Do you want to do some calculations with these results? Please enter y/n: ')
            if calc_yn.lower() == 'y' or calc_yn.lower() == 'yes':
                while True:
                    # Forces the user to enter the number, Source:
                    # https://stackoverflow.com/questions/23326099/how-can-i-limit-the-user-input-to-only-integers-in-python
                    try:
                        num_currency = int(
                            input('Ok! How many ' + base_euro + ' do you want to convert? Please enter '
                                                                'a number: '))
                        break
                    except ValueError:
                        print("\nPlease enter a number \n")
                print('Ok! What do you want to convert to? These are your options in case you forgot:')
                for i in rate_dict:
                    print(str(i) + ' ', end='')
                # Asks the user which one they choose and prints out the results.
                while True:
                    currency_convert = input('\nSo which one do you choose? ')
                    if currency_convert in rate_dict:
                        print('\nOk! Here are your results:')
                        x = float(num_currency)
                        y = float(rate_dict[currency_convert])
                        converted = round(x * y, 10)
                        print('The value of ' + str(num_currency) + ' ' + base_euro + ' (for ' + str(
                            user_date) + ')' +
                              ' is equal to ' + str(converted) + ' ' + str(currency_convert))
                        break
                    else:
                        print('\nPlease enter a one of the choices')
                break
            elif calc_yn.lower() == 'n' or calc_yn.lower() == 'no':
                print('Ok! ending the program')
                exit()
            else:
                print('\nPlease enter y/n\n')
        break


# Greeting
print('\nThis program  basically lets you  see the conversion factors for euros from 1999 to right now!')
today = date.today()

# Asks the user what currency conversions they want to see
while True:
    user_date = input('What date do you want to see the currency conversion factors for? Please enter '
                      'the full date (YYYY-MM-DD) or enter latest to see the latest conversion factors: ')
    if user_date == 'latest':
        # Gets data
        data = requests.get(
            'http://data.fixer.io/api/' + 'latest' + '?access_key=1a08040b9823c19305d7650e109fc96b&symbols=USD,AUD,'
                                                     'CAD,PLN,MXN&format=1')
        data_dict = json.loads(data.text)
        rate_dict = data_dict['rates']
        base_euro = data_dict['base']
        # calculates
        calc_one(base_euro, rate_dict, today)
    elif '/' in user_date or '-' in user_date:
        # Gets data
        data = requests.get(
            'http://data.fixer.io/api/' + user_date + '?access_key=1a08040b9823c19305d7650e109fc96b&symbols=USD,AUD,'
                                                      'CAD,PLN,MXN&format=1')
        data_dict = json.loads(data.text)
        rate_dict = data_dict['rates']
        base_euro = data_dict['base']
        if data_dict['success']:
            # calculates
            calc_two(base_euro, rate_dict, user_date)
        else:
            print('\n Uh oh, that is not a supported date, please enter another date!\n')
    else:
        print('\nPlease enter \'latest\' or a valid date separated by / or - : \n')
