#Escreva um programa que leia um valor em metros e escreva ele convertido em centímetros.

n1 = float(input('Digite a metragem a ser convertida: '))

km = n1/1000
hm = n1/100
dam = n1/10
cen = n1*100
mil = n1*1000

print(f'Você colocou o valor de {n1:.2f}m.\nConversão em centímetros: {cen:.0f}cm.\nConversão em milímetros: {mil:.0f}mm.'
      f'\nConversão em decametros: {dam:.2f}dam\nConversão em hectáres: {hm:.2f}hm\nConversão em quilômetros: {km:.2f}km')
