class Underscore:
    def map(self, iterable, callback):
        # tu código aqui
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        # tu código aqui
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                return iterable[i]

    def filter(self, iterable, callback):
        # tu código aqui
        i = 0
        while i < len(iterable):
            if callback(iterable[i]) == False:
                iterable.pop(i)
                i -= 1
            i += 1
        return iterable
    def reject(self, iterable, callback):
        # tu código
        i = 0
        while i < len(iterable):
            if callback(iterable[i]) == True:
                iterable.pop(i)
                i -= 1
            i += 1
        return iterable
# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore()    # sí, estamos configurando una instancia a una variable 
                    # que es un guión bajo
mapa = _.map([1,2,3], lambda x: x*2) # debe retornar [2,4,6]
encontrar = _.find([1,2,3,4,5,6], lambda x: x>4) # debe retornar el primer 
                                            # valor que es mayor que 4
filtrar = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [2,4,6]
sacar = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [1,3,5]
print(f"Resultado de map: {mapa}")
print(f"Resultado de find: {encontrar}")
print(f"Resultado de filter: {filtrar}")
print(f"Resultado de reject: {sacar}")