

    # Adding and subtracting random numbers
    # 11/29/2022
    # CTI-110 P5HW2 - Math Quiz
    # William Mangas
    #

import random

def addProblem():
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(f' {a}')
    print(f'+{b}')
    print('Enter answer.')
    ans = int(input())
    while ans!=(a+b):
        if ans<(a+b):print('Sorry, guess is too low.')
        else: print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! your answer is correct...\n')

def subProblem():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    if a<b:a,b=b,a
    print(f' {a}')
    print(f'-{b}')
    print('Enter answer.')
    ans = int(input())
    while ans != (a - b):
        if ans < (a - b):
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! your answer is correct...\n')

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('-------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addProblem()
        elif choice == '2':
            subProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break


main()