from ourpackages import barcelos
import os

os.system('cls')
print("(1) Kevin Joseph V. Barcelos")
print("(2) Marc D. Veslino")
print("(3) Kirby G. Consultado")
print("(4) Gener A. Andaya")
print("(5) Edriane O. Piadozo")
user_choice = int(input("Enter your choice: "))

match(user_choice):
    case 1:
        barcelos.kevin()
    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
    