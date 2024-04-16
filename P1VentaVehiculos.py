from abc import ABC, abstractmethod

#Fabrica abstracta
class FabricaVehiculo(ABC):
    @abstractmethod
    def crearAutomovil(self):
        pass
    @abstractmethod
    def crearScooter(self):
        pass
#Interfaz producto abstracto automovil
class Automovil(ABC):
    @abstractmethod
    def crear_automovil(self):
        pass
#Interfaz producto abstracto scooter
class Scooter(ABC):
    @abstractmethod
    def crear_scooter(self):
        pass
#Fabricas concretas
class FabricaVehiculoElectrecidad(FabricaVehiculo):
    def crearAutomovil(self):
        return AutomovilElectrecidad()
    def crearScooter(self):
        return ScooterElectrecidad()
class FabricaVehiculoGasolina(FabricaVehiculo):
    def crearAutomovil(self):
        return AutomovilGasolina()
    def crearScooter(self):
        return ScooterGasolina()
#Productos concretos
class ScooterElectrecidad(Scooter):
    def crear_scooter(self):
        return "Se ha creado un scooter eléctrico"
class ScooterGasolina(Scooter):
    def crear_scooter(self):
        return "Se ha creado un scooter a gasolina"
class AutomovilElectrecidad(Automovil):
    def crear_automovil(self):
        return "Se ha creado un automovil eléctrico"
class AutomovilGasolina(Automovil):
    def crear_automovil(self):
        return "Se ha creado un automovil a gasolina"

#Cliente
class Catalogo:
    def __init__(self, fabrica_vehiculo):
        self._fabrica_vehiculo_automovil = fabrica_vehiculo.crearAutomovil()
        self._fabrica_vehiculo_scooter = fabrica_vehiculo.crearScooter()
    def ordenar_automovil(self):
        return self._fabrica_vehiculo_automovil.crear_automovil()
    def ordenar_scooter(self):
        return self._fabrica_vehiculo_scooter.crear_scooter()

#Ordenando mi scooter a gasolina
scooter_gasolina = Catalogo(FabricaVehiculoGasolina())
print(scooter_gasolina.ordenar_scooter())

#Ordenando mi scooter electrico
scooter_electrico = Catalogo(FabricaVehiculoElectrecidad())
print(scooter_electrico.ordenar_scooter())

#Ordenando mi auto a gasolina
auto_gasolina = Catalogo(FabricaVehiculoGasolina())
print(auto_gasolina.ordenar_automovil())

#Ordenando mi auto electrico
auto_electrico = Catalogo(FabricaVehiculoElectrecidad())
print(auto_electrico.ordenar_automovil())