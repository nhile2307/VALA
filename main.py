import math
import time


def primeFactorsList(n):
    factor_list = []
    while n % 2 == 0:
        factor_list.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factor_list.append(i)
            n /= i
    if n > 2:
        factor_list.append(n)
    return factor_list


def check_data_base(number):
    file_obj = open("database.txt", "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    for i in range(len(lines)):
        if str(number) in lines[i]:
            return True
    file_obj.close()


def add_to_database(number, prime_factor_list ,executed_time):
    database_content = 'Prime Factors of number ' + str(number) + ' are ' + str(prime_factor_list)[1:-1] + '\n' +\
    "It took " + "{:.15f}".format(executed_time) + ' seconds to find those \n'
    file_obj = open('database.txt', 'a')
    file_obj.write(str(database_content))
    file_obj.close()


def print_from_database(number):
    file_obj = open("database.txt", "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    for i in range(len(lines)):
        if str(number) in lines[i]:
            print(lines[i] + '\n' + lines[i + 1])
    file_obj.close()


#===============================MAIN======================================


n = int(input('Give me the number: '))

# Check if given number in database or not
if check_data_base(n) is True:
    print_from_database(n)
    print('AVAILABLE')
else:
    # Define the time calculating prime factors
    start_execution = time.time()
    prime_factor_list = list(dict.fromkeys(primeFactorsList(n)))
    end_execution = time.time()
    executed_time = end_execution - start_execution

    # Printing results
    for i in prime_factor_list:
        print('Prime factor found: ' + str(i))
    print("It took " + "{:.15f}".format(executed_time) + ' seconds to find those')

    # Adding new result to database
    add_to_database(n, prime_factor_list, executed_time)
    print('ADDED')



