import random

def Numeros_aleatorios():
      lista=[0]*10

      for i in range(10):
            lista[i] = random.randrange(10, 27)


      return lista


print(Numeros_aleatorios() )

l=Numeros_aleatorios()
l2=l.sort()



def eliminar_duplicados(l2 : list):


    for i in range(11):
        if l2[i-1] == l2[i ]:
            del l2[i-1]
        else:
            i += 1
    return print(l2)










