#Persegi
sisi = float(input('Masukkan sisi persegi : '))

luas = sisi * sisi
keliling = sisi + sisi + sisi + sisi

print(f"Luas dari persegi dengan sisi {sisi} adalah {luas}")
print(f"Keliling dari persegi dengan sisi {sisi} adlah {keliling}")

#Persegi Panjang
p = float(input('Masukkan PANJANG persegi panjang : '))
l = float(input('Masukkan LEBAR persegi panjang : '))

luas = p * l
keliling = 2*(p+l)

print(f"Luas dari persegi panjang dengan PANJANG {p} dan LEBAR {l} adalah {luas}")
print(f"Luas dari persegi dengan PANJANG {p} dan LEBAR {l} adalah {keliling}")

#Trapesium 
a = float(input('Masukkan sisi A Trapesium : '))
b = float(input('Masukkan sisi B Trapesium : '))
c = float(input('Masukkan sisi C Trapesium: '))
d = float(input('Masukkan sisi D Trapesium: '))
h = float(input('Masukkan Tinggi Trapesium : '))

luas = 0.5 * (a+b) * h
keliling = a+b+c+d

print(f'Luas Trapesium adalah : {luas}')
print(f'Keliling Trapesium adalah : {keliling} ')

