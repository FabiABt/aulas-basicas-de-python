# A estrutura de um dicionário é delimitada por chaves, entre as quais ficam o conteúdo desse objeto.
# representam coleções de dados que contém na sua estrutura um conjunto de pares chave/valor, 
# # nos quais cada chave individual tem um valor associado
dados_nutris = {
    'Nome' : 'Fabiane',
    'Endereço' : 'Rua maricleide n 1234',
    'Telefone' : '1234567',
    'Estatura' : '1,67 cm',
    'Peso' : '60 kg'
}
print(dados_nutris)
dados_nutris['Idade'] = 32 #Para adicionar elementos num dicionário basta associar uma nova chave ao objeto e dar
# um valor a ser associado a ela
dados_nutris['Escolaridade'] = 'Pós graduação'
dados_nutris['Area de atuação'] = 'Hospitalar'
print(dados_nutris)
del dados_nutris[ 'Telefone'] #remover o item ‘Telefone’ do dicionário usaremos o 'del' que remove uma chave 
#e o valor associado a ela no dicionário.
print(dados_nutris)
fruta = "Melancia"
print(fruta[0:3])