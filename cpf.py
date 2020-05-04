import pyperclip, random

def digitos_ver(numero):
    soma = 0
    mul = 0

    # Soma os dígitos de acordo com a equação do cpf
    for i in range(0, 9):
        soma += (int(numero[i])) * (10 - i)
        mul += (int(numero[i])) * (11 - i)

    # Define qual seria o primeiro dígito verificador
    if soma % 11 == 0 or soma % 11 == 1:
        prim_dig = 0
    else:
        prim_dig = (11 - (soma % 11))

    # Soma o primeiro dígito na equação do segundo digito
    mul += (prim_dig * 2)

    # Define qual seria o segundo dígito verificador
    if mul % 11 == 0 or mul % 11 == 1:
        seg_dig = 0
    else:
        seg_dig = (11 - (mul % 11))

    return (str(prim_dig) + str(seg_dig))


def verificar(numero):
    # Pega apenas os números
    num = ''.join(x for x in numero if x.isnumeric())

    # Se não tiver 11 digitos já invalida
    if len(num) != 11:
        return f'***{numero} não possui 11 dígitos***'

    # Invalida cpf caso todos os digitos forem iguais
    if num in invalidos:
        return f'***{numero} é apenas algorismos repetidos***'

    # Envia primeiros 9 digitos pra gerar quais seriam os digitos verificadores
    digitos = digitos_ver(num[:9])

    # Checa se os digitos gerados batem com os informados
    if (num[9] + num[10]) != digitos:
        return (f'***{num[0]}{num[1]}{num[2]}.{num[3]}{num[4]}{num[5]}.{num[6]}{num[7]}{num[8]}-{num[9]}{num[10]} NÃO é um cpf válido!***')

    # Se o cpf for válido retorna o cpf informado
    # já formatado dizendo de qual estado é a pessoa
    return (f'{num[0]}{num[1]}{num[2]}.{num[3]}{num[4]}{num[5]}.{num[6]}{num[7]}{num[8]}-{num[9]}{num[10]} é um CPF válido de alguem de {estados[num[8]]}!')


def verarquivo():
    print("""
    Verificador de CPFs por arquivo TXT
    Coloque os CPFs em um arquivo de texto, um por linha
    Depois, informe o nome do arquivo(sem o .txt)
    É necessário que o arquivo se localize no mesmo diretório que este programa
    Digite 0 para retornar ao menu
    """)
    while True:
        arquivo = input("Digite o nome do arquivo: ")
        lista = []
        erros = 0
        total = 0
        if arquivo == '0':
            break
        else:
            try:
                for line in open(f'{arquivo}.txt', 'r').readlines():
                    lista.append(line.strip())

                for i in lista:
                    k = verificar(i)
                    total += 1
                    if '***' in k:
                        erros += 1
                    print(k)
            except:
                print("Arquivo inválido")
        print(f"Verificação finalizada, dos {total} foram encontrados {erros} CPFs inválidos")


def gerar_cpf(a=0):
    # Define que digitos podem ser usados
    digits = '0123456789'
    # Gera 9 digitos
    num = ''.join(random.choice(digits) for x in range(9))
    # Gera os digitos verificadores do cpf
    ver = digitos_ver(num)
    # Une e formata o cpf completo
    cpf = f'{num[0]}{num[1]}{num[2]}.{num[3]}{num[4]}{num[5]}.{num[6]}{num[7]}{num[8]}-{ver[0]}{ver[1]}'
    if a == 0:  # resposta padrão para quando chamar essa função
        print('\n\n')
        print(cpf)
        pyperclip.copy(cpf)
        print(' Número copiado para o CTRL C, basta você agora colar ele\n Retornando ao menu...')
    elif a == 1:  # retorna CPF ao inves de copiar caso chamar com 1 no argumento
        return cpf


def criar_arq():
    length = input('\n Quantos CPFs você deseja criar: ')
    print(" O arquivo será criado no mesmo diretório deste programa")
    name = input(' Nome do arquivo: ')
    f = open(f'{name}.txt', 'w+')
    for i in range(int(length)):
        cpf = gerar_cpf(1)  # 1 para não printar/copiar pro ctrl c
        f.write(f'{cpf}\n')
    f.close()


def menu():
    print("\n Olá! Bem vindo!")
    print(" Opções: \n1- Verificar CPF\n2- Verificar CPFs de um arquivo TXT\n3- Gerar 1 CPF\n4- Gerar arquivo TXT com CPFs\nexit- Fechar programa\n\n\n")
    return input("Digite o número da opção desejada: ")


# Lista de estados e dígitos correspondentes
estados = {
    '0': 'Rio Grande do Sul',
    '1': 'Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul ou Tocantins',
    '2': 'Amazonas, Pará, Roraima, Amapá, Acre ou Rondônia',
    '3': 'Ceará, Maranhão ou Piauí',
    '4': 'Paraíba, Pernambuco, Alagoas ou Rio Grande do Norte',
    '5': 'Bahia ou Sergipe',
    '6': 'Minas Gerais',
    '7': 'Rio de Janeiro ou Espírito Santo',
    '8': 'São Paulo',
    '9': 'Paraná ou Santa Catarina'
}

# Lista de CPFS invalidos que retornariam falso positivo
invalidos = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
]

# Loop do menu
while True:
    opcao = menu()
    if opcao == '1':
        print("\n Verificador de CPF! Informe o número com ou sem pontos/traços\nou digite 0 para retornar ao menu")
        while True:
            numero = input()
            if numero == '0':
                break
            print(verificar(numero))
    elif opcao == '2':
        verarquivo()
    elif opcao == '3':
        gerar_cpf()
    elif opcao == '4':
        criar_arq()
    elif opcao == 'exit':
        quit()
    else:
        print('Comando não reconhecido, retornando ao menu')
