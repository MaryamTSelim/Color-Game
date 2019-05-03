import socket
import random
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 7510
    s.bind((host,port))
    s.listen(5)
    c,ad = s.accept()
    print('Connection Established with: '+ad[0])
    colors = ['purple','blue','green','yellow','orange','red']
    
    while True:
            textColor= colors [random.randint(0,len(colors)-1)]
            textWord= colors [random.randint(0,len(colors)-1)]
            while (textColor==textWord):
                textWord= colors [random.randint(0,len(colors)-1)]
            sentMessage = textWord[0]+textColor[0]
            c.send(sentMessage.encode('ascii'))
            recievedMessage = c.recv(2048).decode('ascii')
    s.close()
except socket.error as e :
    print(e)
except KeyboardInterrupt :
    print('chat ended')