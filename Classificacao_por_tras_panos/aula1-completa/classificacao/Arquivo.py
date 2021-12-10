import csv

def carregar_acessos():
    dados = []
    marcacoes = []

    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    for acessou_home, acessou_como_funciona, \
        acessou_contato, comprou in leitor:

        dados.append([(acessou_home), 
                      (acessou_como_funciona), 
                      (acessou_contato)])
        marcacoes.append((comprou))

    return dados, marcacoes
        

def carregar_busca():
    dados = []
    marcacoes = []

    arquivo = open('busca.csv', 'r')
    leitor = csv.reader(arquivo)
    for home,busca, \
    logado,comprou in leitor:

        dados.append([(home), 
                      (busca), 
                      (logado)])
        marcacoes.append((comprou))

    return dados, marcacoes