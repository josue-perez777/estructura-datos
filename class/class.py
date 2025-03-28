class Vehiculo:
    marca: str
    combustible: int
    tipo_Vehiculo: str

    def __init__(self, marca: str, combustible: int, tipo_Vehiculo:str)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo_Vehiculo = tipo_Vehiculo

    def __str__(self)->str:
        return f"El tipo de vehiculo es: {self.tipo_Vehiculo}  La marca del vehiculo es: {self.marca}  y el nivel de combustible es de: {self.combustible}"

    def encender(self):
        if self.combustible < 10:
            print("ADVERTENCIA, ve a la gasolinera")
        else:
            print("Vehiculo encendido")
        
    def acelerar(self):
       if self.combustible > 0:
         self.combustible -= 5
       print(f"El vehículo ha acelerado. Nivel de combustible: {self.combustible} galones.") 
       if self.combustible < 10:
            print("ADVERTENCIA, debes de ir a la gasolinera")   
       if self.combustible == 0:
            print("Deten la marcha.")
            return  
class Moto(Vehiculo):
    pass
class Carro(Vehiculo):
    pass

vehiculo1 = Vehiculo('Toyota', 7, 'carro')
print(vehiculo1)
vehiculo1.encender()
vehiculo1.acelerar()

moto1 = Moto('Mercedes-Benz', 100, 'moto')
print(moto1)
moto1.encender()
moto1.acelerar()

carro1 = Carro('Ford', 30, 'carro')
print(carro1)
carro1.encender()
carro1.acelerar()