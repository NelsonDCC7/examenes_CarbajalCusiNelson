from datetime import date
from datetime import datetime
"""
 Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""
class Persona:

    def inicializar(self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad
        self.saldo = 2500
        self.nacionalidad ="Peruana"

    def mostrar(self):
        self.nombre=input("Ingrese su nombre :" )
        self.edad = int(input("Ingrese su edad :"))
        print("Nombre : ", self.nombre)
        print(" Edad :", self.edad)
    def cumpleanios(self):
        self.edad=self.edad +1
        print("La edad de la persona aumentada en 1 es : ", self.edad)

    def registro(self):
        regis = datetime.now()
        print("Fecha registrada: ", regis)




persona1 = Persona()


persona1.inicializar("",0)
persona1.mostrar()
persona1.cumpleanios()
persona1.registro()





