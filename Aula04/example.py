#Exercícios de Funções em Python
#Função Simples




# DEFINIR SE UM NUMERO É PAR OU IMPAR

# Entrada
#numero = int(input("Digite um numero:"))
#resultado = ""

# PROCESSAMENTO
#if numero % 2 == 0:
#    resultado = "O numero é par"
#else:
#    resultado = "O numero é impar"

# SAÍDA (EXIBIÇÃO)
#print(resultado)

#======================================================================

#Logíca de Função


#def parOuImpar(numero):
#    resultado = ""  

#    if numero % 2 == 0:
#        resultado = "O numero é par"
#    else:
#        resultado = "O numero é impar"

        
#    return resultado 

#print(parOuImpar(10))

#==============================
#segundo exemplo

#def saudacao(nome):
#    return f"Ola , seja bem vindo {nome}"

#print(saudacao("Tião do Bar"))# sempre chamar de braços abertos

#========================================

#PARAMETRO PADRÃO

#def saudacao(nome="Tião do Bar"):# Paramêtro Padrão
#    return f"Ola , seja bem vindo {nome}"

#print(saudacao("Ze da carroça"))# sempre chamar de braços abertos
    
#===================================================

#Doc de função
#def somar(numero1,numero2):
#    """
#    numero1 -> numero inteiro 
#    numero2 -> numero inteiro 
#    
#    return -> essa função retorna o resultado da soma entre estes dois numeros

#    """
#    soma = numero1 + numero2 
#    return soma 

#print(somar(5,6))
#===========================================================

#def soma_pares():
#    resultado = 0
#    for i in range(11):
#        if i % 2 == 0:
#            resultado += i
#   print(resultado)
#soma_pares()
# 2+4+6+8+10