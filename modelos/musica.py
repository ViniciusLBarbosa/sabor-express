class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica_1 = Musica('Animals', 'Maroon 5', '4 minutos')
musica_2 = Musica('IDFC', 'BlackBear', '5 minutos')


Musica.listar_musicas()