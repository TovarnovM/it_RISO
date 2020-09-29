from math import cos, pi

SOME_GLOB_VAR = 'I AM GLOBAL (in module)'

def some_foo(a,b):
    print(f'a = {a} fdgdfgdfgdgdfgfehrth')
    return a+2*b

class MyClass(object):
    def __init__(self):
        self.a = 123

if __name__ == '__main__':
    print(f'Да, да, вы вызвали {__file__} напрямую')
