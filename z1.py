print('Программа для вывода списка факториалов от 1 до N')
n = int(input("Введите N: "))

def list_of_factorials(l):
    '''
    def factorial(n):
        sum = 1
        i = 2
        while i <= n:
            sum *= i
            i += 1
        return sum
    i = 1
    s = []
    while i <= l:
        s.append(factorial(i))
        i += 1
    return s
    '''
    i = 2
    s = [1]
    sum = 1
    while i <= l:
        sum *= i
        s.append(sum)
        i += 1
    return s
    
print(list_of_factorials(n))
