from collections import deque
import time
cola=deque()

cola_reprocduciion=deque()

cola_reprocduciion.append("1 mochila azul")

cola_reprocduciion.append("2 libros tontos ")
cola_reprocduciion.append("3 toxica ")
#mostrar la canciones de en eswpera 

print("canciones en espera ")
for cancion in cola_reprocduciion:
    print("_",cancion)
    print("iniciando reproducion ")
#desencolar
while cola_reprocduciion:
    cancion_actual=cola_reprocduciion.popleft()
    print(f"sonando ahora :{cancion_actual}") 
    time.sleep (1) # simula la duracion  del tema 
    print(f"finalizado:{cancion_actual}")   
    #muestra cuantas canciones quedan en la cola 

    print(f"quedan{len(cola_reprocduciion)}canciones en la cola")
    print("la cala la reproducion en finalizado ") 