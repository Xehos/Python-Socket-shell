import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1",9090));


minuladata = ""

# Print to the console
def sendsoc():
    global minuladata
    while(True):
        data = input()
        if data == "exit":
            break
        if (data == "") and (minuladata == ""):
            data = "b"
        clientSocket.send(data.encode())
        minuladata = data
        try: 
            dataFromServer = clientSocket.recv(1024)
            readsoc(dataFromServer)
        except:
            pass
    

def readsoc(dataFromServer):
    if dataFromServer != "":
        print(dataFromServer.decode())
        dataFromServer = ""
        sendsoc()
    else:
        sendsoc()
        
    
    
    
sendsoc()