import os

restaurantes = [{'nome': 'Comida do Campus', 'categoria': 'Almoço', 'ativo': False},
                {'nome': 'Pastel', 'categoria': 'Pastelaria', 'ativo': False},
                {'nome': 'Pizzaria del Gatito', 'categoria': 'Pizzaria', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Macarrão', 'categoria': 'Massa', 'ativo': False},
                {'nome': 'Lasanha', 'categoria': 'Massa', 'ativo': False}
                ]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

#funções:
def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao menu principal'''
    input('Digite uma tecla para voltar ao menu principal\n')
    main()

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do retaurante')
    print('4. Sair\n')

def opcao_invalida():
    '''Essa função é responsável por exibir a mensagem de opção invalida'''
    print('Opção Invalida\n')
    input('Aperte uma tecla para voltar ao menu principal\n')
    main()
    voltar_ao_menu_principal()
        
def finalizar_app():
    '''Essa função é responsável por finalizar o app'''
    os.system('cls')
    print('Finalizando o app\n')

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


#cadastra um novo restaurante
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do resturante que deseja cadastrar:\n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}\n')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O resturante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    

#Lista os restaurantes
def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes'''
    exibir_subtitulo('Listando todos os restaurantes cadastrados')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Ativo'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'destivado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

#ativa um restaurante
def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o status de um restaurante'''
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status:\n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} coi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso\n'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado\n')
    voltar_ao_menu_principal()

#opções
def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        # print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except: 
        opcao_invalida()    

    # -Pode ser feito assim tambem:
    # opcao_escolhida = int(input('Escolha uma opção: '))
    # match opcao_escolhida:
    #     case 1:
    #         print('Adicionar restaurante')
    #     case 2:
    #         print('Listar restaurantes')
    #     case 3:
    #         print('Ativar restaurante')
    #     case 4:
    #         print('Finalizar app')
    #     case _:
    #         print('Opção inválida!')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
