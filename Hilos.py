# un hilo es una unidad d eprocesamiento que se puede ejecutar y se puede crear con la libreria que paython nos ofrece(los usamos si queremos usar treas a la vez)
# los procesos(espacio de memoria propio) son deferente de hilos(espacio de memoria compartido)
# para crear mas hilos debe de haber un hilo principal

        #crear un hilo
import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        print("{} inicio".format(self.getName))
        time.sleep(1)
        print("{} terminado".format(self.getName()))

if __name__=="__main__":    
    for x in range(4):
    
        hilo=MiHilo(name="Thread-{}".format(x+1))
        hilo.start()
        time.sleep(.90)
