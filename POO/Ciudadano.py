class Ciudadano:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_genero(self):
        return self.__genero
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        self.__edad = edad
    def set_genero(self, genero):
        self.__genero = genero
class Actriz(Ciudadano):
    def __init__(self, nombre, edad, genero, pelicula_favorita, personaje_favorito):
        super().__init__(nombre, edad, genero)
        self.__pelicula_favorita = pelicula_favorita
        self.__personaje_favorito = personaje_favorito

    def get_pelicula_favorita(self):
        return self.__pelicula_favorita
    def get_personaje_favorito(self):
        return self.__personaje_favorito
    def set_pelicula_favorita(self, pelicula_favorita):
        self.__pelicula_favorita = pelicula_favorita
    def set_personaje_favorito(self, personaje_favorito):
        self.__personaje_favorito = personaje_favorito
    def accion(self):
        print(f"{self.get_nombre()} está actuando en una película")
class Azafata(Ciudadano):
    def __init__(self, nombre, edad, genero, aerolinea, idiomas):
        super().__init__(nombre, edad, genero)
        self.__aerolinea = aerolinea
        self.__idiomas = idiomas
    def get_aerolinea(self):
        return self.__aerolinea
    def get_idiomas(self):
        return self.__idiomas
    def set_aerolinea(self, aerolinea):
        self.__aerolinea = aerolinea
    def set_idiomas(self, idiomas):
        self.__idiomas = idiomas
    def accion(self):
        print(f"{self.get_nombre()} está atendiendo a los pasajeros en un vuelo de {self.get_aerolinea()}")
class Veterinaria(Ciudadano):
    def __init__(self, nombre, edad, genero, especialidad, experiencia):
        super().__init__(nombre, edad, genero)
        self.__especialidad = especialidad
        self.__experiencia = experiencia
    def get_especialidad(self):
        return self.__especialidad
    def get_experiencia(self):
        return self.__experiencia
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad
    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia
    def accion(self):
        print(f"{self.get_nombre()} está tratando a un animal de la especie {self.get_especialidad()}")
    def tratar_animal(self, animal):
        print(f"{self.get_nombre()} está tratando a un {animal} de la especie {self.get_especialidad()}")


def main():
    actriz1 = Actriz("Emma Stone", 33, "Femenino", "La La Land", "Mia")
    print(f'La actriz {actriz1.get_nombre()}'+f'tiene una edad de {actriz1.get_edad()}'+f'de genero {actriz1.get_genero()}'+\
          f'su pelicula favorita es {actriz1.get_pelicula_favorita()}'+f'y su personajes favorito es {actriz1.get_personaje_favorito()}\n')

    azafata1 = Azafata("Ana", 27, "Femenino", "Delta Airlines", ["Inglés", "Español", "Francés"])C
    print(f'La actriz {azafata1.get_nombre()}' + f'tiene una edad de {azafata1.get_edad()}' + f'de genero {azafata1.get_genero()}' + \
        f'trabaja en {azafata1.get_aerolinea()}' + f'y habla {azafata1.get_idiomas()}\n' + \
        f'y en este momento esta haciendo {azafata1.accion()}')

    vet1 = Veterinaria("María", 45, "Femenino", "Caninos", 20)
    print(f'La actriz {vet1.get_nombre()}' + f'tiene una edad de {vet1.get_edad()}' + f'de genero {vet1.get_genero()}' + \
        f'su especialidad es {vet1.get_especialidad()}' + f'y su experiencia es {vet1.get_experiencia()}\n' + \
        f'y en este momento esta haciendo {vet1.accion()}')

if __name__ == "__main__":
    main()

