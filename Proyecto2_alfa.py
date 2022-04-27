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

def movimiento(T1,T2,m):
    T1.añadir_final(T2._final._elemento)
    T2.eliminar_final()
    p = T2._frente
    while p:
        if p._siguiente == None:
            T2._final = p
        p = p._siguiente
    print("\nmovimiento ", m)
    
    

def movimiento_x(T1,T2,m):
    T1.añadir_final(T2._final._elemento)
    T2.eliminar_inicio()
    p = T2._frente
    while p:
        if p._siguiente == None:
            T2._final = p
        p = p._siguiente
    print("\nmovimiento ", m)

def mostrar_todo():
    print("Lista A")
    A.mostrar()
    print("Lista B")
    B.mostrar()
    print("Lista C")
    C.mostrar()
    

def proceso():
    movimiento(C,A,1)
    mostrar_todo()
    movimiento(B,A,2)
    mostrar_todo()
    movimiento_x(B,C,3)
    mostrar_todo()
    movimiento(C,A,4)
    mostrar_todo()
    movimiento(A,B,5)
    mostrar_todo()
    movimiento_x(C,B,6)
    mostrar_todo()
    movimiento(C,A,7)
    mostrar_todo()
    movimiento_x(B,A,8)
    mostrar_todo()
    movimiento(A,C,9)
    mostrar_todo()
    movimiento(B,C,10)
    mostrar_todo()
    movimiento_x(B,A,11)
    mostrar_todo()
    movimiento_x(A,C,12)
    mostrar_todo()
    movimiento(C,B,13)
    mostrar_todo()
    movimiento_x(B,A,14)
    mostrar_todo()
    movimiento_x(B,C,15)
    mostrar_todo()
        
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


