from copy import deepcopy
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

    def estaVazia(self):
        return len(self.__fila) == 0

class Concorrencia:
    def __init__(self):
        self.__fila_processos = Fila()
        self.__indice_add = 0
    
    def add(self, x):
        for _ in range(x):
            comando, *parametro = input().split(maxsplit=1)
            self.__fila_processos.enfileira((comando, parametro,self.__indice_add))
        self.__indice_add += 1

    def process(self):
        processo_atual = self.__fila_processos.desenfileira()
        match processo_atual[0]:
            case "merge":
                self.__merge(processo_atual[1][0])
            case "crypto":
                self.__crypto(processo_atual[1][0])
            case "deYodafy":
                self.__deYodafy(processo_atual[1][0])
    
    def halt(self):
        processos = 0
        comandos = 0
        ultimoProcesso = -1
        while not self.__fila_processos.estaVazia():
            processo = self.__fila_processos.desenfileira()
            if not processo[2] == ultimoProcesso:
                processos += 1
                ultimoProcesso = processo[2]
            comandos += 1
        print(f"{processos} processo(s) e {comandos} comando(s) órfão(s).")
    
    def __crypto(self, string):
        lista = []
        cont = 0
        cont_antigo = 0
        for operacao in string:
            if operacao == "+":
                for i in range(cont + 1, cont_antigo, -1):
                    lista.append(i)
                cont += 1
                cont_antigo = cont
            else:
                cont += 1
        if string[-1] == "-":
            for i in range(cont + 1, cont_antigo, -1):
                lista.append(i)
        else:
            lista.append(cont + 1)
        print("".join(str(item) for item in lista))

    def __merge(self, string):
        string = string.replace(", ", ",")
        string = string.replace("[", "")
        string = string.replace("]", "")
        lista = string.split()
        lista = [list(map(int, item.split(","))) for item in lista]
        lista_final = []
        troca = True
        while troca:
            troca = False
            while lista:
                for item, intervalo in enumerate(lista_final):
                    if (intervalo[1] >= lista[0][0] and intervalo[0] <= lista[0][0]) or (intervalo[0] <= lista[0][1] and intervalo[0] >= lista[0][0]):
                        lista_final[item] = [min(lista[0][0], intervalo[0]), max(lista[0][1], intervalo[1])]
                        lista.pop(0)
                        troca = True
                        break
                else:
                    lista_final.append(lista.pop(0))
            lista = deepcopy(lista_final)
            lista_final.clear()
        lista.sort(key = lambda x : x[0])
        print(*lista)
    
    def __deYodafy(self, string):
        ponto = string[-1]
        lista = string[:-1].split()
        lista.reverse()
        print(" ". join(lista), ponto, sep = "")

concorrencia = Concorrencia()
comando = [""]
while not comando[0] == "halt":
    comando = input().split(maxsplit=1)
    match comando[0]:
        case "add":
            concorrencia.add(int(comando[1]))
        case "process":
            concorrencia.process()
        case "halt":
            concorrencia.halt()