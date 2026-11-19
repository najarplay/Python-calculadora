import math


class Conversiones:

    def grados_a_radianes(self, grados):
        return math.radians(grados)

    def radianes_a_grados(self, radianes):
        return math.degrees(radianes)

    def grados_a_gradianes(self, grados):
        return grados * (10 / 9)

    def gradianes_a_grados(self, gradianes):
        return gradianes * (9 / 10)

    def radianes_a_gradianes(self, radianes):
        return radianes * (200 / math.pi)

    def gradianes_a_radianes(self, gradianes):
        return gradianes * (math.pi / 200)
