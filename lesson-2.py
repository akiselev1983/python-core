"""
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
"""
def notebook():
    todo_list = []
    def inner(todo):
        todo_list.append(todo)
        return todo_list
    return inner


todo_list = notebook()
print(todo_list('hi'))
print(todo_list('hello'))
print(todo_list('world'))

"""
2) протипізувати перше завдання
"""
def notebook():
    todo_list = []
    def inner(todo:str)->list:
        todo_list.append(todo)
        return todo_list
    return inner

"""
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""
def expanded_form(n:str):
    sum=[]
    j = len(str(n))
    for i in str(n):
        j -= 1
        if i != '0':
            sum.append(i+'0'*j)
    print('+'.join(sum))

expanded_form(70304)



"""
4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
    та буде виводити це значення після виконання функцій
"""
def decor(func):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print('count: ', count)
        func(*args,**kwargs)
        print('--------------')
    return inner
@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')
func1()
func1()
func1()

func2()
func2()