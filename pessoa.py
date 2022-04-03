import request


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

        self.dados_obtidos = False

    def obter_dados(self)
      resposta = request.get('url')

       if resposta.ok:
            self.dados_obtidos = True
            return 'coenectado'
        else:
            self.dados_obtidos = False
            return 'erro 404'
