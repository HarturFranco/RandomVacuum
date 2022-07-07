# Im
from agents import *
from tabulate import tabulate
from time import sleep
import os

""" Verifica o SO em que o código esta sendo executado
 e seta o comando de limpar o terminal para cada SO"""
if os.name == 'nt':
    clearCommand = 'cls'
else:
    clearCommand = 'clear'

# Inicializa o ambiente customizado 
our_vacuum_env = OurVacuumEnvironment((2,3))

# Cria o agente randomico
random_agent = RandomVacuumAgent()

# Adiciona o agente ao ambiente e printa sua posição no grid
our_vacuum_env.add_thing(random_agent)

# Printa o estado inicial do ambiente
lista_print = [["(Dirty)" if coluna["Dirty"] else "(Clean)" for coluna in linha] for linha in our_vacuum_env.cenario]
lista_print[random_agent.location[0]][random_agent.location[1]]+= "\n(Agent)"
print("Estado inicial do cenário:\n{}.".format(tabulate(lista_print, tablefmt="grid")))

# Rodando o ambiente
while True:
    
    sleep(2)
    os.system(clearCommand)

    # Faz com que o agente realiza uma operação
    our_vacuum_env.step()

    # Preparativos para o print do estado atual do Ambiente
    lista_print = [["(Dirty)" if coluna["Dirty"] else "(Clean)" for coluna in linha] for linha in our_vacuum_env.cenario]
    lista_print[random_agent.location[0]][random_agent.location[1]]+= "\n(Agent)"
    
    # Printa o estado atual do Ambiente
    print("Ação realizada: {}".format(random_agent.last_action))
    print("Estado do cenário após a realização da ação:\n{}.".format(tabulate(lista_print, tablefmt="grid")))
    
