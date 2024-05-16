import threading
import time 
import random

NUM_FILOSOFOS = 5
tenedores = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

def filosofo(filosofo_id):
    filosofo_numero = filosofo_id + 1 #Ajustamos el número del filósofo para que vaya de 1 a 5.

    while True:
        #Filosofo pensando
        print(f"Filósofo {filosofo_numero} está pensando.")
        time.sleep(random.uniform(0,1))
        
        #Filósofo quiere comer
        print(f"Filósofo {filosofo_numero} quiere comer.")
        comer(filosofo_id)

def comer(filosofo_id):
    filosofo_numero = filosofo_id + 1 #Ajustamos el número del filósofo para que vaya de 1 a 5.
    
    #Se intenta tomar tenedores izquierdo y derecho.
    tenedores[filosofo_id].acquire()
    print(f"Filosofo {filosofo_numero} ha tomado el tenedor izquierdo.")
    
    tenedores[(filosofo_id + 1) % NUM_FILOSOFOS].acquire()
    print(f"Filosofo {filosofo_numero} ha tomado el tenedor derecho.")
    
    #Filósofo comiendo
    print(f"Filósofo {filosofo_numero} está comiendo.")
    time.sleep(random.uniform(0,1))
    
    #Se intenta liberar tenedores izquierdo y derecho.
    tenedores[filosofo_id].release()
    print(f"Filosofo {filosofo_numero} ha soltado el tenedor izquierdo.")
    
    tenedores[(filosofo_id + 1) % NUM_FILOSOFOS].release()
    print(f"Filosofo {filosofo_numero} ha soltado el tenedor derecho.")

if __name__ == "__main__":
    #Creamos hilos para cada filósofo
    filosofos = [threading.Thread(target = filosofo, args = (i,)) for i in range(NUM_FILOSOFOS)]
    
    #Inicializamos los hilos
    for filosofo_thread in filosofos:
        filosofo_thread.start()
    
    #Se espera a que todos los hilos terminen
    for filosofo_thread in filosofos:
        filosofo_thread.join()