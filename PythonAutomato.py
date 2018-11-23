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

    for linha in base[3:]:
        automato.transicoes.append([linha[0:2], linha[3:4], linha[5:7]])

    letrasDoArquivo = []
    for i in automato.transicoes:
        letrasDoArquivo.append(i[1])

    automato.alfabeto = sorted(set(letrasDoArquivo))

def montarTabelaAFDInicial(automato):
    tabelaAFD = pd.DataFrame(columns= automato.alfabeto, index= [automato.estadoInicial])

    for letra in automato.alfabeto:
        destino = ''
        for transicao in automato.transicoes:
            if(letra == transicao[1] and transicao[0] == automato.estadoInicial):
                destino = destino + transicao[2]
                tabelaAFD.ix[automato.estadoInicial,letra] = destino
            else:
                destino = ''



    print(tabelaAFD)

def main():
    automato = Automato()
    carregaDados(automato)
    montarTabelaAFDInicial(automato)

if __name__ == "__main__":
    main()
