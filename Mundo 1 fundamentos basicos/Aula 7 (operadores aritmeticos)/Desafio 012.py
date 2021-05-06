#Faça um programa que leia o preço de um produto e mostre o seu valor com 5% de desconto

p1 = float(input('Digite o valor do produto: '))

desc = (p1*5)/100#calculando 5%
vd = p1-desc; #descontanto 5% do valor do produto

print(f'O valor do produto com desconto é: {vd:.2f}.')
