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
        
        

        
L =  ListaEnlazada()
L.añadir_final(2)
L.añadir_final(4)
L.añadir_final(12)
L.añadir_final(8)
L.añadir_final(3)
L.mostrar()
print('Size',len(L))


i = L.buscar(8)
print('Resultado',i)
i = L.buscar(20)
print('Resultado',i)

# L.añadir_inicio(15)
# L.mostrar()
# print('Size',len(L))

# L.eliminar_inicio()
# L.mostrar()
# print('Size',len(L))

L.eliminar_final()
L.mostrar()
print('Size',len(L))