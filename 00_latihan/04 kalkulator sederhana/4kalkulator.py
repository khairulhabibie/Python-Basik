## kalkulator sederhana

print("kalkulator".center(25,"="))

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,x,:) = ")
angka_2 = float(input("masukkan angka 2 = "))

# percabangan
if operator == "+":
     hasil = angka_1 + angka_2
     print(f"hasilnya adalah {hasil}")
elif operator == "-":
     hasil = angka_1 - angka_2
     print(f"hasilnya adalah {hasil}")
elif operator == "*" or operator == "x":
     hasil = angka_1 * angka_2
     print(f"hasilnya adalah {hasil}")
elif operator == "/" or operator == ":":
     hasil = angka_1 / angka_2
     print(f"hasilnya adalah {hasil}")
else:
    print("operator yang anda masukkan salah")
print("akhir dari program, terima kasih")