# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
co = {'li': '\033[m', 'vm': '\033[31m', 'vd': '\033[32m'}
valorCasa = float(input("Digite o valor da casa: "))
sal = float(input("Digite o seu salario: "))
tempo = int(input("Em quantos anos pretende pagar a casa? "))
prestmensal = (valorCasa/(tempo*12))
porcensal = (sal*30)/100
print(f"Para pagar esta casa em {tempo} anos o valor da prestação mensal será de R${prestmensal:.2f}")
if prestmensal > porcensal:
    print(f"Seu emprestimo foi{co['vm']} negado{co['li']}!")
else:
    print(f"Seu emprestimo foi {co['vd']}aprovado{co['li']}!")
