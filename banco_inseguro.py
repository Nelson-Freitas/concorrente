import threading
import random 
import time 

from typing import List 

class Conta: 
    def __init__(self, saldo = 0) -> None: 
        self.saldo = saldo 


def main(): 
    contas = criar_contas() 
    total = sum(conta.saldo for conta in contas) 
    print ('Iniciando transferências...') 

    tarefas = [
        threading.Thread(target= servicos, args=(contas, total))
    ] 

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas] 

    print("Transferência completa.") 
    valida_banco(contas, total) 

def servicos (contas, total): 
    for _ in range(1, 10_000): 
        c1, c2 = pega_duas_contas(contas)
