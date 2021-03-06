a = input('DIgite algo pra que nosso leitor possa ler; ')
n1 = a + 1
n2 = a - 1
print(f'Analisando seu o número {a}.\nVemos que o numero antecessor dele é {n2}.\nE seu número posterior é {n1}.')
print('O tipo primitivo do valor digitado é ', type(a))
print('O numero digitado é feito de espaços? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É um uma letra? ',a.isalpha())
print('É um caracter alfanurica? ',a.isalnum())
print('Muito bem')