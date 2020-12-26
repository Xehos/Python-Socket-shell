
import socket
import os
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# Bind and listen

serverSocket.bind(("127.0.0.1",9090));

serverSocket.listen();
minuladata="   "
dataFromClient = ""
# Accept connections


def readsoc(dataFromClient):
    global clientConnected
    while(True):
        try:
            dataFromClient = clientConnected.recv(1024)
        except:
            print("Client disconnected!")
            clientconnect()
        if dataFromClient != "":
            sendsoc(dataFromClient)
        
        
def sendsoc(dataFromClient):
    global clientConnected
    #print("LOL")
    vstup = os.popen(dataFromClient.decode()).read()
    if vstup == "":
        vstup = "NO COMMAND"
    try:
        clientConnected.send(vstup.encode())
    except:
        print("Client disconnected!")
        clientconnect()
    dataFromClient = ""
    readsoc(dataFromClient)


def clientconnect():
    global clientConnected
    (clientConnected, clientAddress) = serverSocket.accept();
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    readsoc(dataFromClient)
    
while(True):
    clientconnect()
    


        