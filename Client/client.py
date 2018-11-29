import Pyro4
import os
from time import clock
import serpent

global frontLink

def conn():
    global frontLink
    frontLink = Pyro4.Proxy("PYRONAME:FrontEnd")
    print("Connected")

def upld():
    fileName = ""
    valid = False
    list = [f for f in os.listdir('.')]
    while not valid:
        fileName = input("Valid file name (inc. extension): ")
        for i in list:
            if fileName == i:
                valid = True
    reliable = ""
    while (reliable != "YES") and (reliable != "NO"):
        reliable = input("Reliability mode? (Yes/No) ")
        reliable = reliable.upper()
    file = open(fileName, 'rb')
    startTime = clock()
    response = frontLink.upload(fileName, file.read(), reliable)
    file.close()
    if response:
        time = clock() - startTime
        sizeTransferred = os.path.getsize(fileName)
        print("Transfer Complete")
        print("Time taken: " + str(time)[:8] + "s")
        print("size transfered: " + str(sizeTransferred) + " bytes")
    else:
        print("Transfer Failed")

def list():
    listNew = frontLink.list()
    print("Server Files: ")
    for i in listNew:
        print(i)
    print("")

def dwld():
    fileName = input("Valid file name (inc. extension): ")
    files = frontLink.list()
    if fileName not in files:
        print("File does not exist")
    else:
        file = frontLink.download(fileName)
        fileback = serpent.tobytes(file)
        f = open(fileName, 'wb')
        f.write(fileback)
        f.close()
        print("Downloaded: " + fileName)



def delf():
    fileName = input("Valid file name (inc. extension): ")
    files = frontLink.list()
    if fileName not in files:
        print("File does not exist")
    else:
        go = input("Confirm Delete: (Yes/NO) ")
        if go.upper() == "YES":
            frontLink.delete(fileName)
        else:
            print("Delete aborted")


def run():
    while True:
        print("Options: CONN, UPLD, DWLD, LIST, DELF, QUIT")
        message = input("prompt user for operation: ")
        if message.upper() == "CONN":
            print("CONNECTED")
        if message.upper() == "UPLD":
            print("UPLOAD")
            upld()
        if message.upper() == "LIST":
            print("LIST")
            list()
        if message.upper() == "DWLD":
            print("DOWNLOAD")
            dwld()
        if message.upper() == "DELF":
            print("DELETE FILE")
            delf()
        if message.upper() == "QUIT":
            print("Session Terminated")
            break

def start():
    print("Options: CONN, UPLD, DWLD, LIST, DELF, QUIT")
    message = input("prompt user for operation: ")
    while message.upper() != "CONN":
        print("Please Connect First")
        message = input("prompt user for operation: ")
    conn()
    run()

start()
