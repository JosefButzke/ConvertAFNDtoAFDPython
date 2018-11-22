import pandas as pd

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
    automato.transicoes = base[3:]

    letrasDoArquivo = []
    for i in automato.transicoes:
        letrasDoArquivo.append(i[2])

    automato.alfabeto = set(letrasDoArquivo)

def MontaTabelaAFD():
    print("x")
    print(x)


def main():
    automato = Automato()
    carregaDados(automato)
    print(automato.estados)
    print(automato.estadoInicial)
    print(automato.estadosFinais)
    print(automato.transicoes)
    print(automato.alfabeto)

if __name__ == "__main__":
    main()
