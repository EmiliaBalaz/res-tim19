import select, socket


        
class AMSService:
    def __init__(self, servicePort):
        self.servicePort = servicePort
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(0)

        self.server.bind(('localhost',self.servicePort))
        self.server.listen(10)
        self.inputs = [self.server]

    def Listen(self):
        print("--SERVER CEKA NOVE KONEKCIJE!--")
        while self.inputs:
            readable, _, _ = select.select(self.inputs, [],[])
            for s in readable:
                if s is self.server:
                    connection, client_address = s.accept()
                    connection.setblocking(0)
                    self.inputs.append(connection)
                else:
                    data = s.recv(1024)
                    if data:
                        print(data)
                    else:
                        self.inputs.remove(s)
                        s.close()

            

