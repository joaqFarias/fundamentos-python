import random
def randInt(min=0, max=100):
    if min < max:  
        num = round(random.random() * (max-min) + min)
    else:
        num = round(random.random() * (min-max) + max)
    return num

print(randInt()) 		# debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50)) 	# debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	# debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500
