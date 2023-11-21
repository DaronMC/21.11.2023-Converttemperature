def convert_temperature(Temperature, What_to_Convert):
    if What_to_Convert == "CelToFah":
        return (Temperature*1.8)+32
    elif What_to_Convert == "FahToCel":
        return(Temperature-32)*(5/9)
print(convert_temperature(23, "CelToFah"))
print(convert_temperature(73.4, "FahToCel"))

