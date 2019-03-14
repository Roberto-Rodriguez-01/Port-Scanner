import os, socket, urllib, smtplib, ftplib, tkinter, time

def mulit_thread():
    print("")
def Gui():
    print("")

def Start_scan():
    print("")

def Protocol():
    while(True):
        print("Tcp, Udp, or Both")
         

def Ip_address():
    while(True):
        print("Input Ip's by hand or by file")

def Ports():
    while(True):
        print("Input ports by hand or all of them")

def Web_server():
    while(True):
        print("Would you like to Fingerprint any port running a webserver")
        print("Would you like a status code returned")
        print("Would you like a title of the page found")
        print("Would you like Type and version of server found")

def Timeout():
    while(True):
        print("")

def Menu():
    while(True):
        Print("1. Set scan Protocol \n")
        Print("2. Set ip address/s \n")
        Print("3. Set Ports to scan \n")
        Print("4. Set web server scan options \n")
        print("5. Set Timeout value \n")
        Print("6. Start scan \n")
        Print("7. Exit \n")

        choice = input(": ")

        if(choice == 1):
            Protocol()

        elif(choice == 2):
            Ip_address()

        elif(choice == 3):
            Ports()

        elif(choice == 4):
            Web_server()

        elif(choice == 5):
            Timeout()

        elif(choice == 6):
            Start_scan()
    
        elif(choice == 7):
            SystemExit()

        else:
            continue

def Main():
    Menu()

main()