import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep Inválido")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        return requests.get(url).json()



