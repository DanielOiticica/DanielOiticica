def alterar(custo, taxa_imposto):
    precrev = custo + (custo * (taxa_imposto/100))
    print(f'O valor final de revenda do produto é R${precrev:.2f}')



#Função Principal
cust = float(input('Insira o custo do produtor:'))
tx_impost = int(input('Insira a taxa de imposto cobrado em cima do produto em questão:'))
soma_imposto(cust, tx_impost)

alterar(cust, tx_impost)
