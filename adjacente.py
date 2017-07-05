#verifica se número é adjacente e imprime os digitos adjacentes se for adjacente senão imprime não é adjacente
def main():

  numero = input("informe um numero: ")
  #pega tamanho numero para usar no laço  
  tamanho = len(numero)
  #num para usar nas divisões
  num = int(numero)
  numero = int(numero)
  #se for True, imprime dentro do laço os digitos adjacentes
  adjacente = False
  #controla o laço pelo tamanho do número, se tamanho 1 não executa
  
  while(tamanho != 1):
  
    #855 % 10 = 5
    #pega digito da direita
    direita = num % 10
    #855 % 100 = 55 e 55 // 10 = 5
    #pega digito da esquerda
    esquerda = (num % 100) // 10
    #855 // 10 = 85
    #remove ultimo numero
    num = num // 10
    
    if(direita == esquerda):
      adjacente = True
      print("numero adjacente entre", direita, "e", esquerda)
      
    tamanho = tamanho - 1
    
  if(adjacente == False):
    print("numero", numero, "não é adjacente")

main()
