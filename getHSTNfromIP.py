#!/usr/bin/python3
# -*- coding: utf-8 -*-

######################
##### BIBLIOTECAS ####
######################

import socket    # BIBLIOTECA DE SOCKET PARA CONEXÃO COM IP.
import sys       # BIBLIOTECA DE SISTEMA PARA INTERAÇÃO COM SISTEMA OPERACIONAL.

########################################################################################################################################

#################
#### FUNÇÕES ####
#################

def Usage():    # FUNÇÃO EXIBE INSTRUÇOES DE USO NA TELA.
    print('''\n---*======== Get Hostname by IPAddress v1.1 ========*---\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n
\nUsage: \n\npython3 ''', sys.argv[0], '''--single 127.0.1.1\nOr:\npython3''',sys.argv[0], '''--file WordlistWithIpAddress.txt
\n''')
    sys.exit(1)    # FIM.


def withHOST():    # FUNÇÃO PARA UTILIZAÇÃO COM APENAS UM IP.
    try:
        hostname = socket.gethostbyaddr(sys.argv[2].strip())    # RESOLVENDO HOSTNAME PELO ENDEREÇO IP. (https://docs.python.org/3/library/socket.html#socket.gethostbyaddr)
        print('IP: ', " ".join(hostname[2]), 'Hostname:',hostname[0])    # SAIDA EM FORMATO AMIGAVEL.

    except (RuntimeError, TypeError, NameError, socket.herror, OSError):    # TRATAMENTO DE ERROS.
        pass

    sys.exit(1)    # FIM.

def withFILE():    # FUNÇÃO PARA UTILIZAÇÃO COM UMA LISTA DE IPs.
    with open(sys.argv[2], 'r') as listIP:    # LISTANDO IPs DENTRO DA WORDLIST PASSADA PELO PRIMEIRO PARAMETRO.
        for IP in listIP:
            try:
                hostname = socket.gethostbyaddr(IP.strip())    # RESOLVENDO HOSTNAME PELO ENDEREÇO IP.
                print('IP;'+" ".join(hostname[2])+';Hostname;'+hostname[0])    # SAIDA EM FORMATO PARA ADICIONAR EM PLANILHA.

            except (RuntimeError, TypeError, NameError, socket.herror, OSError):    # TRATAMENTO DE ERROS.
                pass

    sys.exit(1)    # FIM.
########################################################################################################################################

##############
#### MAIN ####
##############

if len(sys.argv) != 3:    # VERIFICA A QUANTIDADE DE PARAMETROS PASSADO PARA O SCRIPT.
    Usage()

if sys.argv[1] == "--single":    # INICIA A FUNÇÃO DE DESCOBERTA DE HOSTNAME PARA UM HOST APENAS.
    withHOST()

elif sys.argv[1] == "--file":    # INICIA A FUNÇÃO DE DESCOBERTA DE HOSTNAME PARA UM LISTAS DE IPs.
    withFILE()

else:
    print("Opção invalida !")    # TRATA FLUXOS INVALIDOS.
    sys.exit(1)

########################################################################################################################################
