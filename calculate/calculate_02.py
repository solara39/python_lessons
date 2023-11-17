import numpy

heat_capa = 200 # (J / K * kg)
volume = numpy.pi * (0.01 / 2) ** 2 * 0.03 # (m ^ 3)
density = 1100 # (kg / m ^ 3)
temperature = 50 # (K)

energy = heat_capa * volume * density * temperature
print("energy", energy, "(J)")