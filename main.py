import enum


class Pilha:
    def __init__(self):
        self.__pilha = []
    
    def empilha(self, valor):
        self.__pilha.append(valor)
    
    def desempilha(self):
        return self.__pilha.pop()

    def estaVazio(self):
        return len(self.__pilha) == 0

class Fila:
    def __init__(self):
        self.__fila = []
    
    def enfileira(self, valor):
        self.__fila.append(valor)
    
    def desenfileira(self):
        return self.__fila.pop(0)

class Concorrencia:
    def __init__(self):
        self.__fila_processos = Fila()
    
    def add(self, x):
        for _ in range(x):
            comando, *parametro = input().split()
            self.__fila_processos.enfileira((comando, parametro))

    def process(self):
        processo_atual = self.__fila_processos.desenfileira()
        match processo_atual[0]:
            case "merge":
                pass
            case "crypto":
                self.__crypto(processo_atual[1][0])
            case "deYodafy":
                pass
    
    def __crypto(self, string):
        lista = []
        cont = 0
        cont_antigo = 0
        for operacao in string:
            if operacao == "+":
                for i in range(cont + 1, cont_antigo, -1):
                    lista.append(i)
                    print(lista)
                cont += 1
                cont_antigo = cont
            else:
                cont += 1
        if string[-1] == "-":
            for i in range(cont + 1, cont_antigo, -1):
                lista.append(i)
        else:
            lista.append(cont + 1)
        print(lista)

concorrencia = Concorrencia()
comando = ""
while not comando == "halt":
    comando = input().split()
    match comando[0]:
        case "add":
            concorrencia.add(int(comando[1]))
        case "process":
            concorrencia.process()