# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
from random import randint

def rnd_list_posiive_negative(n, rnd_range = 10):
    rnd_list = []
    for i in range(n):
        rnd_list.append(randint(-rnd_range,rnd_range))
    return rnd_list;

N = 10
print(rnd_list_posiive_negative(N, N))
