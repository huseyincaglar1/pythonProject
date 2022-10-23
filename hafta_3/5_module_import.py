import bizim_modul
from bizim_modul import topla
from bizim_modul import carp
import bizim_modul as degisken_cek

print(bizim_modul.topla(5, 10))
print(bizim_modul.e)
print(bizim_modul.carp(3, 2))

print(topla(5, 10))
print(carp(3, 2))

print(degisken_cek.q)
print(degisken_cek.w)

"""
Kendi yazdığımız bir modüle başka bir 
projede ihtiyaç hissettiğimizde o modülü 
yeni projeye aktarma işlemine import denir.
"""