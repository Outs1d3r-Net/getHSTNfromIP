#!/usr/bin/python3
# -*- coding: utf-8 -*-


# ADICIONANDO BIBLIOTECAS.
import socket    # BIBLIOTECA DE SOCKET PARA CONEXÃO COM IP.
import sys       # BIBLIOTECA DE SISTEMA PARA INTERAÇÃO COM SISTEMA OPERACIONAL.


if len(sys.argv) != 2:
    print("\n---*======== Get Hostname by IPAddress v1.0 ========*---\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n\nUsage: \n\n", sys.argv[0], "WordlistWithIpAddress.txt\n")
    sys.exit(1)


with open(sys.argv[1], 'r') as listIP:    # LISTANDO IPs DENTRO DA WORDLIST PASSADA PELO PRIMEIRO PARAMETRO.
    for IP in listIP:
        try:
            hostname = socket.gethostbyaddr(IP.strip())    # RESOLVENDO HOSTNAME PELO ENDEREÇO IP.
            print('IP;'+" ".join(hostname[2])+';Hostname;'+hostname[0])    # SAIDA EM FORMATO PARA ADICIONAR EM PLANILHA

        except (RuntimeError, TypeError, NameError, socket.herror, OSError):    # TRATAMENTO DE ERROS
            pass
