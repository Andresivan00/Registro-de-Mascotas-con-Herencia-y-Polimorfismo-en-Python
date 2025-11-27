# Clase base para todas las mascotas
class Mascota:
    # Constructor de la clase Mascota
    def __init__(self, nombre: str, edad: int, color: str, raza: str, sonido):
        self._nombre = nombre
        self._edad = edad
        self._color = color
        self._raza = raza
       
        # Método abstracto: obliga a que las subclases implementen "sonido"
        def sonido(self):
            raise NotImplementedError("Subclase debe implementar sonido()")
        
        # Método especial para mostrar información de la mascota
        def __str__(self):
            pass

''' 
 ---------------------------
 Clase: Perro (hereda de Mascota)
 ---------------------------
'''                          
class Perro(Mascota):
    # Constructor de la clase Perro
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)  # Llama al constructor de Mascota
        self.peso = peso
        self.muerde = muerde

    # Implementación del sonido del perro
    def sonido():
        print("Los perros ladran")
   
    # Representación en texto de la mascota
    def __str__(self):
        return f"Perro: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Peso: {self.peso}kg, Muerde: {self.muerde}"
       
# Subclases de Perro
class PerroPequeno(Perro):
    # Personaliza la forma de mostrar un perro pequeño
    def __str__(self):
        return f"Perro Pequeño: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Peso: {self.peso}kg, Muerde: {self.muerde}"

class PerroMediano(Perro):
    # Representación de perro mediano
    def __str__(self, nombre: str, edad: int, color: str, peso, muerde):
        super().__init__(self, nombre, edad, color, raza="Mediana")
        return f"---"

class PerroGrande(Perro):
    # Representación de perro grande
    def __str__(self, nombre: str, edad: int, color: str, peso, muerde):
        super().__init__(self, nombre, edad, color, raza="Grande")
        return f"---"
                           
''' 
 ---------------------------
 Clase: Gato (hereda de Mascota)
 ---------------------------
''' 
class Gato(Mascota):
    # Constructor de la clase Gato
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)  # Llama al constructor de Mascota
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto
       
    # Implementación del sonido del gato
    def sonido():
        print("Los gatos maullan y ronronean")
   
    # Representación en texto de la mascota
    def __str__(self):
        return f"Gato: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Altura salto: {self.altura_salto}m, Longitud salto: {self.longitud_salto}m"
       
# Subclases de Gato
class GatoSinPelo(Gato):
    def __str__(self):
        return f"Gato sin pelo: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Altura salto: {self.altura_salto}m, Longitud salto: {self.longitud_salto}m"

class GatoPeloLargo(Gato):
    def __str__(self):
        return f"Gato de pelo largo: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Altura salto: {self.altura_salto}m, Longitud salto: {self.longitud_salto}m"

class GatoPeloCorto(Gato):
    def __str__(self):
        return f"Gato de pelo corto: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Altura salto: {self.altura_salto}m, Longitud salto: {self.longitud_salto}m"

'''
 ---------------------------
 Interacción con el usuario
 ---------------------------
'''
if __name__ == "__main__":
    # Pregunta al usuario qué mascota quiere registrar
    tipo = input("¿Quieres registrar un Perro o un Gato? ").lower()

    if tipo == "perro":
        # Solicita datos específicos del perro
        nombre = input("Nombre del perro: ")
        edad = int(input("Edad del perro: "))
        color = input("Color del perro: ")
        peso = float(input("Peso del perro (kg): "))
        muerde_input = input("¿El perro muerde? (s/n): ").lower()
        muerde = True if muerde_input == "s" else False

        # Clasificación automática por peso
        if peso < 10:
            mascota = PerroPequeno(nombre, edad, color, peso, muerde)
        elif 10 <= peso <= 25:
            mascota = PerroMediano(nombre, edad, color, peso, muerde)
        else:
            mascota = PerroGrande(nombre, edad, color, peso, muerde)

    elif tipo == "gato":
        # Solicita datos específicos del gato
        nombre = input("Nombre del gato: ")
        edad = int(input("Edad del gato: "))
        color = input("Color del gato: ")
        altura_salto = float(input("Altura de salto del gato (m): "))
        longitud_salto = float(input("Longitud de salto del gato (m): "))

        # Clasificación según el tipo de pelo
        pelo = input("¿El gato es sin pelo, de pelo largo o de pelo corto? ").lower()

        if pelo == "sin pelo":
            mascota = GatoSinPelo(nombre, edad, color, altura_salto, longitud_salto)
        elif pelo == "pelo largo":
            mascota = GatoPeloLargo(nombre, edad, color, altura_salto, longitud_salto)
        else:
            mascota = GatoPeloCorto(nombre, edad, color, altura_salto, longitud_salto)

    else:
        # Manejo de opción inválida
        print("Tipo de mascota no válido")
        mascota = None

    # Si la mascota se creó correctamente, se muestra
    if mascota:
        print("\n✅ Mascota registrada:")
        print(mascota)
