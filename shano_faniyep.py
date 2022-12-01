import matplotlib.pyplot as plt
import math


# encoded by CodedDom

class  node :
    def __init__(self): # использую self для получения доступа к атрибутам и мктодат своего класса
        self.sym='' # храненте симлов 
        self.pro=0.0
        self.arr=[0]*20
        self.top=0
p=[node() for _ in range(20)]
 
# функция для поиска кода Шеннона
def shano_fano(l, h, p): 
    bundle1 = 0; bundle2 = 0; various1 = 0; various2 = 0 # Переменные
    if ((l + 1) == h or l == h or l > h) : #
        if (l == h or l > h):
            return
        p[h].top+=1
        p[h].arr[(p[h].top)] = 0
        p[l].top+=1
        p[l].arr[(p[l].top)] = 1
         
        return
    #
    else : 
        for i in range(l,h):
            bundle1 = bundle1 + p[i].pro
        bundle2 = bundle2 + p[h].pro
        various1 = bundle1 - bundle2
        if (various1 < 0):
            various1 = various1 * -1
        j = 2
        while (j != h - l + 1) :
            k = h - j
            bundle1 = bundle2 = 0
            for i in range(l, k+1):
                bundle1 = bundle1 + p[i].pro
            for i in range(h,k,-1):
                bundle2 = bundle2 + p[i].pro
            various2 = bundle1 - bundle2
            if (various2 < 0):
               various2 = various2 * -1
            if (various2 >= various1):
                break
            various1 = various2
            j+=1
         
        k+=1
        for i in range(l,k+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 1
             
        for i in range(k + 1,h+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 0
             
 
        # Вызов функции Шеннона
        shano_fano(l, k, p)
        shano_fano(k + 1, h, p)

# Функция для сортировки символов
# на основе их вероятности или частоты
def sortByProbability(n, p):
    temp=node()
    for j in range(1,n) :
        for i in range(n - 1) :
            if ((p[i].pro) > (p[i + 1].pro)) :
                temp.pro = p[i].pro
                temp.sym = p[i].sym
 
                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym
 
                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym

# функция для отображения кодов Шеннона
def display(n, p):
    print("\n\n\n\tСимволы\tВероятность\tCoded",end='')
    for i in range(n - 1,-1,-1):
        print("\n\t", p[i].sym, "\t\t", p[i].pro,"\t",end='')
        for j in range(p[i].top+1):
            print(p[i].arr[j],end='')
#Диограмма 
x = [0.11,0.05,0.09,0.10,0.12,0.03,0.02,0.08,0.15,0.07,0.14,0.04]
def plot_pie(x):
        plt.pie(x,autopct='%1.1f%%',  startangle=90,  shadow=True)
        plt.show()
#Значение     
if __name__ == '__main__':
    total = 0
    # Вводимое количество символов
    print("Введите кол-во символов\t: ",end='')
    n = 12
    print(n)
    i=0
    # Входной символ
    for i in range(int(n)):
        print("Введите символ:", i + 1," : ",end="")
        ch = chr(65 + i)
        print(ch)
        p[i].sym += ch

    #Вероятность ввода символов
    x = [0.11,0.05,0.09,0.10,0.12,0.03,0.02,0.08,0.15,0.07,0.14,0.04]
    for i in range(int(n)):
        print("\nВведите вероятность ", p[i].sym, ": ",end="")
        print()
        p[i].pro = x[i]
        total = total + p[i].pro
    sortByProbability(n, p)

    for i in range(n):
        p[i].top = -1
    shano_fano(0, n - 1, p)
    display(n, p)
    plot_pie(x)