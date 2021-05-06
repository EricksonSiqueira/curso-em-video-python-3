# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
media = ((n1+n2)/2)
print(f"Sua média é {media:.1f} .")
if 0 <= media < 5:
    print("Você foi REPROVADO!")
elif 5 <= media < 7:
    print("Você está de RECUPERAÇÃO!")
elif 7 <= media <= 10:
    print("Você está APROVADO. Parabéns!")
else:
    print("Média inválida.")
