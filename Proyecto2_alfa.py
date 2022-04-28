from asyncio.windows_events import NULL
import time
from tqdm import tqdm
class _Nodo:
    __slots__='_elemento', '_siguiente'

    def __init__(self, elemento,siguiente):
        self._elemento = elemento
        self._siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self._frente = None
        self._final = None
        self._size = 0

    def __len__(self):
        return self._size

    def esta_vacio(self):
        return self._size == 0 #retorna un booleano hace una comparacion de lo que dice en el return

    def añadir_final(self, e):
        nuevo = _Nodo(e, None)
        if self.esta_vacio():
            self._frente = nuevo
        else:
            self._final._siguiente = nuevo
        self._final = nuevo
        self._size += 1

    def mostrar(self):
        p = self._frente
        if self._frente == None:
            print("La lista esta vacia")
        while p:
            print(p._elemento,end=' --> ')#end, argumento que permite agregar texto al final de una cadena
            p = p._siguiente
            time.sleep(0.5)
        print("\n")

    def buscar(self,key):
        p = self._frente
        index = 0
        while p:
            if p._elemento == key:
                return index
            p = p._siguiente
            index += 1
        return -1

    def añadir_inicio(self,e):
        nuevo = _Nodo(e, None)
        if self.esta_vacio():
            self._frente = nuevo
            self._final = nuevo
        else:
            nuevo._siguiente = self._frente
            self._frente = nuevo
        self._size += 1

    def eliminar_inicio(self):
        i = self._frente
        self._frente=i._siguiente
        self._size -= 1

    def eliminar_final(self):
        p = self._frente
        while p:
            if p._siguiente == self._final:
                p._siguiente = None
            p = p._siguiente
        self._size -= 1

def movimiento(T1,T2,m):
    T1.añadir_final(T2._final._elemento)
    if T2._size == 1:
        T2.eliminar_inicio()
    else:
        T2.eliminar_final()
    p = T2._frente
    while p:
        if p._siguiente == None:
            T2._final = p
        p = p._siguiente
    print("-------------------------------------------------------------------------------------")
    print("\nMovimiento ", m)
    mostrar_todo()

def mostrar_todo():
    print("Lista A")
    A.mostrar()
    print("Lista B")
    B.mostrar()
    print("Lista C")
    C.mostrar()


def proceso():
    movimiento(C,A,1)
    movimiento(B,A,2)
    movimiento(B,C,3)
    movimiento(C,A,4)
    movimiento(A,B,5)
    movimiento(C,B,6)
    movimiento(C,A,7)
    movimiento(B,A,8)
    movimiento(B,C,9)
    movimiento(A,C,10)
    movimiento(A,B,11)
    movimiento(B,C,12)
    movimiento(C,A,13)
    movimiento(B,A,14)
    movimiento(B,C,15)
        
A =  ListaEnlazada()
B =  ListaEnlazada()
C =  ListaEnlazada()
A.añadir_final(4)
A.añadir_final(3)
A.añadir_final(2)
A.añadir_final(1)
print("\nCargando programa:")

for i in tqdm(range(200)):
    time.sleep(0.001)

print("\nEl presente programa resuelve la torre de hanoi con 4 discos y 3 torres usando pilas y listas enlazadas.\n")
time.sleep(1)
print("La torre A contiene todos los discos, los cuales son los siguientes:\n")
A.mostrar()
print('Size',len(A))

proceso()
print("\nEl ejercicio se completo en 15 movimientos los 4 discos fueron trasladados de la torre A a la torre B")

