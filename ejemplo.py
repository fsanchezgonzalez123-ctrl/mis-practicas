from collections import deque
cola=deque()




cola.append("cliente1 ")
cola.append("cliente2 ")
cola.append("cliente3 ")
atendido=cola.popleft()

print("atendidio",atendido)
print("cola resrtante",cola)