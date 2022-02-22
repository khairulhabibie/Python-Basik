## konversi suhu

print("PROGRAM KONVERSI SUHU TYPE 1 - celcius to all")
celcius = float(input('masukkan suhu dalam celcius : '))
print("suhu celcius adalah", celcius) 

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur) 

# fahreinheit
fahreinheit = ((9/5) * celcius) + 32
print("suhu dalam fahreinheit adalah", fahreinheit) 

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin) 

## TYPE 2
print("")
print("PROGRAM KONVERSI SUHU TYPE 2 - fahreinheit to kelvin")
fahreinheit = float(input('masukkan suhu dalam fahreinheit : '))
print("suhu fahreinheit adalah", fahreinheit)

# kelvin
kelvin = ((5/9) * (fahreinheit-32)) + 273
print("suhu dalam kelvin adalah", kelvin) 
 
## TYPE 3
print("")
print("PROGRAM KONVERSI SUHU TYPE 3 - kelvin to fahreinheit")
kelvin = float(input('masukkan suhu dalam kelvin : '))
print("suhu kelvin adalah", kelvin)

# fahreinheit
fahreinheit = ((9/5) * (kelvin - 273)) + 32 
print("suhu dalam kelvin adalah", fahreinheit) 