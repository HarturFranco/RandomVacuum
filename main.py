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
our_vacuum_env = OurVacuumEnvironment((4,4))
lista_print = [["(Dirty)" if coluna["Dirty"] else "(Clean)" for coluna in linha] for linha in our_vacuum_env.cenario]

# Printa o estado inicial do ambiente
print("State of the Environment: {}.".format(tabulate(lista_print, tablefmt="grid")))

# Cria o agente randomico
random_agent = RandomVacuumAgent()

# Adiciona o agente ao ambiente e printa sua posição no grid
our_vacuum_env.add_thing(random_agent)
print("RandomVacuumAgent is located at {}.".format(random_agent.location))

# Rodando o ambiente
while True:
    
    sleep(2)
    os.system(clearCommand)

    our_vacuum_env.step()

    lista_print = [["(Dirty)" if coluna["Dirty"] else "(Clean)" for coluna in linha] for linha in our_vacuum_env.cenario]

    # Printa o estado atual do Ambiente
    
    lista_print[random_agent.location[0]][random_agent.location[1]]+= "\n(Agent)"

    print("State of the Environment:\n {:}.".format(tabulate(lista_print, tablefmt="grid")))
    
