# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#  à vista dinheiro/cheque: 10% de desconto
#  à vista no cartão: 5% de desconto
#  em até 2x no cartão: preço formal
#  3x ou mais no cartão: 20% de juros
print('='*10 + 'GuanaStore' + '='*10)
carrinho = float(input("Valor total das compras: R$"))
metodo = int(input("Selecione o metodo de pagamento:\n"
                   "[1] Á vista dinheiro/cheque\n"
                   "[2] Á vista no cartão\n"
                   "[3] Em 2x no cartão\n"
                   "[4] 3x ou mais no cartão\n"))
if metodo == 1:
    dinheirovista = carrinho - ((carrinho*10)/100)
    print(f"Você recebeu 10% de desconto.\nO valor total era R${carrinho} agora é R${dinheirovista}.")
elif metodo == 2:
    cartaovista = carrinho - ((carrinho*5)/100)
    print(f"Você recebeu 5% de desconto.\nO valor total era R${carrinho} agora é R${cartaovista}.")
elif metodo == 3:
    print(f"Nenhum desconto aplicado.\nValor total da compra é {carrinho}.\n2 parcelas de {carrinho/2}")
elif metodo == 4:
    cartaoparc = carrinho + ((carrinho*20)/100)
    parc = int(input("Digite a quantidade de parcelas:"))
    print(f"Juros de 20% aplicado.\nValor total da compra é R${cartaoparc}.\n{parc} parcelas de {cartaoparc/parc}")
else:
    print("ERRO!\nValor digitado inválido.")
