from task1 import *
from task2 import sentence_generator
from task3 import diff
from task4 import timer
from task5 import pretty, character_generator

if __name__ == '__main__':
    # TASK 1:
    print('TASK 1')
    print(f'ADD: {my_add(1.232, 1.234, 22, 4)}')
    print(f'MUL: {my_mul(1, 2, 3, 4)}')
    print(f"MUL_ERROR: {my_mul('a', 'b', 'c')}")
    print(f'SUB: {my_sub(1, 2)}')
    print(f'SQRT: {my_sqrt(27, power=3)}')
    print(f'MOD: {my_mod(10, 2)}')
    # TASK 2:
    print('TASK 2')
    print(*sentence_generator(), sep='\n')
    # TASK 3:
    print('TASK 3')
    print(diff())
    # TASK 4:
    print('TASK 4')
    t = input('Введите время в формате: часы:минуты:секунды\n')
    timer(t)
    print('TASK 5')
    # TASK 5:
    pretty(character_generator())
