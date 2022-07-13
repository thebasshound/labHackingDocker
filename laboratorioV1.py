#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def menu():
    while True:
        os.system('clear')
        print ("        _nnnn_")
        print ("        dGGGGMMb     ,----------------------------------------.")
        print ("       @p~qp~~qMb    | Laboratorio de hacking Docker bAssh0ND |")
        print ("       M|@||@) M|   _;........................................'")
        print ("       @,----.JM| -'")
        print ("      JS^\__/  qKL")
        print ("     dZP        qKRb")
        print ("    dZP          qKKb")
        print ("   fZP            SMMb")
        print ("   HZM            MMMM")
        print ("   FqM            MMMM")
        print (" __| M.        |\dSqML")
        print (" |    `.       | `' \Zq")
        print ("_)      \.___.,|     .'")
        print ("\____   )MMMMMM|   .'")
        print ("     `-'       `--' ")
        print ("\n\tMENU PRINCIPAL")
        print ("1 - Instalación del ambiente")
        print ("2 - Laboratorios")
        print ("9 - SALIR")
        opcionMenu = input("Elija una opción(1-2) >> ")
        if opcionMenu=="1":
            menuInstall()
            break
        elif opcionMenu=="2":
            menuLab()
            break
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuInstall():
    while True:
        os.system('clear')
        print ("                     ,---------------------------------------.")
        print ("                     | Laboratorio dockerizado de Pentesting |")
        print ("                     ;.......................................'")
        print ("\n\tInstalación")
        print ("1 - Instalación de Docker")
        print ("2 - Configuración de Red(172.28.5.0/24 br0)")
        print ("9 - Regresar")
        opcionMenuI = input("Elija una opción(1-2) >> ")
        if opcionMenuI=="1":
            print ("+++++++sudo apt update+++++++")
            os.system('sudo apt update')
            print ("+++++++sudo apt install docker.io+++++++")
            os.system('sudo apt install docker.io')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuI=="2":
            print ("sudo docker network create --driver=bridge --subnet=172.28.0.0/16  --ip-range=172.28.5.0/24  --gateway=172.28.5.254  br0")
            os.system('sudo docker network create --driver=bridge --subnet=172.28.0.0/16 --ip-range=172.28.5.0/24  --gateway=172.28.5.254 br0')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuI=="9":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    menu()
def menuLab():
    while True:
        os.system('clear')
        print ("                     ,---------------------------------------.")
        print ("                     | Laboratorio dockerizado de Pentesting |")
        print ("                     ;.......................................'")
        print ("\n\tLaboratorio")
        print ("1 - Iniciar Docker")
        print ("2 - Descargar imagen")
        print ("3 - Listar imagenes")
        print ("4 - Listar contenedores")
        print ("5 - Iniciar contenedor")
        print ("6 - Detener contenedor")
        print ("9 - Regresar")
        opcionMenuL = input("Elija una opción(1-2) >> ")
        if opcionMenuL=="1":
            print ("+++++++systemctl start docker+++++++")
            os.system('sudo systemctl start docker')
            print ("+++++++systemctl enable docker+++++++")
            os.system('sudo systemctl enable docker')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuL=="2":
            break
        elif opcionMenuL=="3":
            print ("+++++++sudo docker images+++++++")
            os.system('sudo docker images')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuL=="4":
            print ("+++++++sudo docker container ls -a+++++++")
            os.system('sudo docker container ls -a')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuL=="5":
            print ("+++++++sudo docker run --rm -p 3000:3000 bkimminich/juice-shop++++++")
            os.system('sudo docker run --rm -p 3000:3000 bkimminich/juice-shop')
            input("Terminado...\npulsa una tecla para continuar")
        elif opcionMenuL=="9":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    menu()

menu()