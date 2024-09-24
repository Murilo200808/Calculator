def calculadora():
  menu = input('''\t
   ______________________________________________
  /Digite a operação matemática que deseja fazer:|
  /1. Adição                                     |
  /2. Subtração                                  |
  /3. Multiplicação                              |
  /4. Divisão                                    |
  /5. Porcentagem                                |
  /6. Potencia                                   |
  /7. Maior ou Menor                             |
  ///////////////////////////////////////////////

  Digite: ''')

  number_1 = int(input('\ncoloque o primeiro número: \n'))
  number_2 = int(input('coloque o segundo número: \n'))

#soma
  if menu == "1":
      print('\n{} + {} = '.format(number_1, number_2))
      print(number_1 + number_2)
#subtração
  elif menu == "2":
      print('\n{} - {} = '.format(number_1, number_2))
      print(number_1 - number_2)
#multiplicação
  elif menu == "3":
      print('\n{} * {} = '.format(number_1, number_2))
      print(number_1 * number_2)
#divisão
  elif menu == "4":
      print('\n{} / {} = '.format(number_1, number_2))
      print(number_1 / number_2)
#porcentagem
  elif menu == "5":
   print('\n{} % {} = '.format(number_1, number_2))
   print(number_1 % number_2)
#potencia
  elif menu == "6":
   print('\n{} ** {} = '.format(number_1, number_2))
   print(number_1 ** number_2)
#maior ou menor
  elif menu == "7":
   if number_1 > number_2:
     print('\n{} > {} = '.format(number_1, number_2))
     print(number_1 > number_2)
   elif number_1 < number_2:
    print('\n{} < {} = '.format(number_1, number_2))
    print(number_1 < number_2)
#operador errado
  else:
    print('''
     ____________________________________
    /Você não digitou um operador válido.|
    /////////////////////////////////////
    ''')
    calculadora()

#Função para voltar ao inicio
def denovo():

  calc_dnovo = input('\nVocê quer calcular de novo? \n')

  if calc_dnovo.upper() == 'Y':
      calculadora()

  elif calc_dnovo.upper() == 'N':
   print('\nAté breve.')
   exit()
