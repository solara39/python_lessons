import numpy

solar_constant = 1.361 * 10 ** 3 # 太陽定数 (J / m**2 * s)

ratio_of_solar_radiation = 0.8 #　日照時間

total_time = 365.25 * 24 * 3600 # 

daily_time = 24 * 3600

# 永久影のない地点での年間総エネルギー量 (J/m^2)
annual_solar_energy = solar_constant * total_time * ratio_of_solar_radiation

daily_solar_energy = solar_constant * ratio_of_solar_radiation * daily_time

#print("daily", daily_solar_energy, "(J/m**2)")
#print("solar", annual_solar_energy, "(J/m**2)")

radius1 = 0.1
radius2 = 0.3
radius3 = 0.5
radius4 = 1
area_of_mirror = numpy.pi * radius3 ** 2
#print("area", area_of_mirror)

reflectance = 0.9
focal_point_efficiency = 0.95

# 鏡の運動によって

daily_real_energy = daily_solar_energy * area_of_mirror * reflectance * focal_point_efficiency

annual_real_energy = daily_real_energy * 365.25

#print("daily_real", daily_real_energy, "(J/m**2)")
#print("annual_real", annual_real_energy, "(J/m**2)")

rise_temperature = 80
calorie = 4.2

total_calorie = calorie * rise_temperature

daily_gas_volume = daily_real_energy / total_calorie
annual_gas_volume = annual_real_energy / total_calorie

#print("daily_gas", daily_gas_volume, "(g)")
#print("annual_gas", annual_gas_volume, "(g)")

energy = solar_constant * area_of_mirror * reflectance * focal_point_efficiency

#print("energy", energy, "(J/s)")
#print("gas_volume_pers", energy / total_calorie, "(g/s)")


heat_capa = 200 # (J / K * kg)
volume = numpy.pi * (0.01 / 2) ** 2 * 0.03 # (m ^ 3)
density = 1100 # (kg / m ^ 3)
temperature = 50 # (K)

energy = heat_capa * volume * density * temperature
print("energy", energy, "(J)")