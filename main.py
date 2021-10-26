from busca import BuscaEndereco


cepTeste = 28911280  #teste cep

objCep = BuscaEndereco(cepTeste) # return Cep info in json

print(objCep.acessa_via_cep())

