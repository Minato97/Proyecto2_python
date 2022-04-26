from asyncio.windows_events import NULL


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
        while p:
            print(p._elemento,end=' --> ')#end, argumento que permite agregar texto al final de una cadena
            p = p._siguiente
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
    
def movimiento1():
    C.añadir_final(A._final._elemento)
    C._size += 1
    A.eliminar_final()
    A._size -= 1
    A._final = A._final
    print("\nmovimiento 1")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()
    
def movimiento2():
    B.añadir_final(A._final._elemento)
    B._size += 1
    A.eliminar_final()
    A._size -= 1
    A._final = A._final
    print("\nmovimiento 2")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()

def movimiento3():
    B.añadir_final(C._final._elemento)
    B._size += 1
    C.eliminar_final()
    C._size -= 1
    C._final = C._final
    print("\nmovimiento 3")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()

def movimiento4():
    C.añadir_final(A._final._elemento)
    C._size += 1
    A.eliminar_final()
    A._size -= 1
    A._final = A._final
    print("\nmovimiento 4")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()

def movimiento5():
    A.añadir_final(B._final._elemento)
    A._size += 1
    B.eliminar_final()
    B._size -= 1
    B._final = B._final
    print("\nmovimiento 5")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()

def movimiento6():
    C.añadir_final(B._final._elemento)
    C._size += 1
    B.eliminar_final()
    B._size -= 1
    B._final = B._final
    print("\nmovimiento 6")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()
    
def movimiento7():
    C.añadir_final(A._final._elemento)
    C._size += 1
    A.eliminar_final()
    A._size -= 1
    A._final = A._final
    print("\nmovimiento 7")
    print("\nLista A")
    A.mostrar()
    print("\nLista B")
    B.mostrar()
    print("\nLista C")
    C.mostrar()

def proceso():
    movimiento1()
    movimiento2()
    movimiento3()
    movimiento4()
    movimiento5()
    movimiento6()
    movimiento7()
        
A =  ListaEnlazada()
B =  ListaEnlazada()
C =  ListaEnlazada()
A.añadir_final(4)
A.añadir_final(3)
A.añadir_final(2)
A.añadir_final(1)

A.mostrar()
print('Size',len(A))

proceso()
C.mostrar()

