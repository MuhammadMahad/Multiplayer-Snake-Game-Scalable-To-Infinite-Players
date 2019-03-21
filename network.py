#class responsible for connecting to our server
import socket
import pickle
from Block import block

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.100.23"#"192.168.100.23"192.168.100.10
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        # print(self.id) #Should say connected


    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            data = pickle.loads(self.client.recv(4096))
            # data.playerBody = []
            # for block in data.blocks:
            #     data.playerBody.append(block(block["position"], block["dx"], block["dy"], block["blockColor"]))
            #     # data.blocks.append({
            #     #     "position": block.position,
            #     #     "dx": block.dx,
            #     #     "dy": block.dy,
            #     #     "blockColor": block.blockColor
            #     # })
            return data
        except:
            pass

    def send(self, data):
        try:
            # for i, block in enumerate(data.playerBody):
            #     data.blocks.append({
            #         "position": block.position,
            #         "dx": block.dx,
            #         "dy": block.dy,
            #         "blockColor": block.blockColor
            #     })
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

# n = Network()
# print(n.send("hello"))
# print(n.send("working"))
