print ("============Calculadora de tinta============")
lar = float(input('Digite qual a largura em metros: '))
alt = float(input('Digite qual a altura em metros: '))
preço = float(input("Digite o preço do galão de 18 litros: "))
areacober = float(input("Digite a área de cobertura da tinta: "))
area = lar*alt
cober = areacober/18
litro = area/cober
gasto = preço/18*litro
print('A área total é {:.2f} m²'.format(area))
print('Gasto {:.2f} litros de tinta'.format(litro))
print('Investimento de R$ {:.2f} '.format(gasto))
print("_"*70)
print("Programa Calculadora de Tinta         *** Bravo Tecnologic 2021***")



