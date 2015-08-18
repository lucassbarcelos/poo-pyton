#__author__ = 'Lucas Barcelos'
print(2**63-1)
print(3/2)

c=1+1j
print(type(c))
print(c**3)

c='c'
s="Lucas"
x='''Lucas

Barcelos'''

print(x)
print(type(x))
print(type(s))
print(type(c))
print("ipsum lorum"*10)

def f():
    return 'string'


print(type(f))

a=f
print(type(a))
print(a())

def derivar(funcao, delta_x=0.00000001):
    def funcao_derivada(x):
        return (funcao(x+delta_x)-funcao(x))//delta_x
    return funcao_derivada
def reta(x):
    return x**2

reta_derivada=derivar(reta)

print(reta_derivada(1))
print(reta_derivada(2))
k
