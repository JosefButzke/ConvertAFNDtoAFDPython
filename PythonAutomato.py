import pandas as pd
import numpy as np

class Automato:
    def __init__(self, estados = [], estadoInicial = [], estadosFinais = [], transicoes = [], alfabeto = []):
        self.estados = estados
        self.estadoInicial = estadoInicial
        self.estadosFinais = estadosFinais
        self.transicoes = transicoes
        self.alfabeto = alfabeto

def carregaDados(automato):
    base = pd.read_csv('base.txt', header = None)
    base = base[0]
    automato.estados = base[0]
    automato.estadoInicial = base[1]
    automato.estadosFinais = base[2]

    for linha in base[3:]:
        automato.transicoes.append([linha[0:2], linha[3:4], linha[5:7]])

    letrasDoArquivo = []
    for i in automato.transicoes:
        letrasDoArquivo.append(i[1])

    automato.alfabeto = sorted(set(letrasDoArquivo))

def montarTabelaAFDInicial(automato):
    tabela = pd.DataFrame(columns= automato.alfabeto, index= [automato.estadoInicial])

    for letra in automato.alfabeto:
        destino = ''
        for transicao in automato.transicoes:
            if(letra == transicao[1] and transicao[0] == automato.estadoInicial):
                destino = destino + transicao[2]
                tabela.ix[automato.estadoInicial,letra] = destino
            else:
                tabela.ix[automato.estadoInicial,letra] = destino
                destino = destino + ''
    return tabela

def buscaTransicoes(estado, automato):
    transicoes = []
    for letra in automato.alfabeto:
        destino = ''
        for transicao in automato.transicoes:
            for est in range(0,len(estado),2):
                if(letra == transicao[1] and transicao[0] == estado[est:est+2]):
                    if(transicao[2] not in destino):
                        destino = destino + transicao[2]
                else:
                    destino = destino + ''
        transicoes.append(destino)
    return transicoes

def construcaoNovasLinhas(tabelaInicial, automato, linhaAtual):
    final = False
    if(linhaAtual > len(tabelaInicial.index) - 1):
        final = True
        return [tabelaInicial, final]
    for i in automato.alfabeto:
        if(tabelaInicial._ix[linhaAtual, i] not in tabelaInicial.index):
            transicoes = buscaTransicoes(tabelaInicial._ix[linhaAtual, i], automato)
            tabelaInicial.loc[tabelaInicial._ix[linhaAtual, i]] = transicoes
    return [tabelaInicial, final]

def main():
    automato = Automato()
    carregaDados(automato)
    tabelaInicial = montarTabelaAFDInicial(automato)
    inicio = 0
    #print(tabelaInicial)
    retorno = construcaoNovasLinhas(tabelaInicial, automato, inicio)
    #print(retorno[0])
    while(retorno[1] == False):
        inicio += 1
        retorno = construcaoNovasLinhas(retorno[0], automato, inicio)
        #print(retorno[0])

    print(retorno[0])



if __name__ == "__main__":
    main()
