#Faça um programa que leia a altura e a largura de uma parede em metros calcule sua área e a quantidade de tinta necessária.
#para pintar a parede. Sabendo que para cara 2m^2 de parede se usa 1 litro de tinta.

al = float(input('Digite a altura em metros da sua parede: '))
lar = float(input('Digite a largura em mertos da sua parede: '))

area = al*lar
tin = area/2

print(f'A área da sua parede é: {area:.2f}m²\n')
print(f'A tinta necessária para pintar esta parede é: {tin:.2f} l.')
