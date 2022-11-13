def areatrapezio(BaseMaior, Basemenor, Altura):
    print('_' * 30 )
    aretrap = ((BaseMaior + Basemenor)* Altura)/2
    print(f'A área do trapezio que tem como base maior {BaseMaior}, base menor {Basemenor} e Altura {Altura} é  {aretrap} metros quadrados.')
    print('_' * 30)

#Função principal
print('Imprimindo a área do trapézio')
print('_' * 30)
BM = float(input('Digite a Base Maior do trapézio :'))
Bm = float(input('Digite a base menor do trapézio:'))
H = float(input('Digite a Altura do trapézio:'))
areatrapezio(BM, Bm, H)
