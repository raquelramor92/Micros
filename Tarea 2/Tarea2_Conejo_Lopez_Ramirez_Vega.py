import random
import time
start_time = time.time()
#Defining variables 
A = [ ]
#Function: changing first 15 numbers for the number 30
def change_data(array):
	for i in range (15):
		A[i]=30
		print ('______________________Ejecucion de reescritura con 30: primera mitad del arreglo')
	print (A)
	return A
#Function: adding 33 units to each numbers in the second
#half of the array
def add_33(array):	
	for i in range (15):
		i += 15
		A[i]+=33
	print('______________________Ejecucion de reescritura con suma de 33 unidades')
	print (A)

if __name__ == "__main__":
	#Creating array, random numbers added
	for i in range (30):
		A.append(random.randint(1, 100))
	print('______________________Creando arreglo de numeros aleatorios')
	print (A)
	#Using both functions created in cascade mode
	add_33(change_data(A))
	print("______________________Por favor espere 2 segundos......")
	time.sleep(2)
	print ("---Tiempo de ejecucion")
	print("--- %s seconds ---" % (time.time() - start_time))
