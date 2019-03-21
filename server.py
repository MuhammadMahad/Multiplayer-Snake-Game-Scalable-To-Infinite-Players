import socket
from _thread import *
import sys
import pickle
from Block import block
from Player import player

server = "192.168.100.23"#"192.168.100.23"192.168.100.10
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [player((10,10), (244, 238, 238)), player((11,11), (58, 55, 47))]

def displayScoreAndResetPlayer(p):

    Score = len(p.playerBody)
    # print('Score: ', len(p.playerBody))

    notificationBox('You Lost!', 'Your Score was ' + str(Score) + '. Play again?')
    p.resetPlayer((10, 10))




def threaded_client(conn, player):
    #conn.send(str.encode("Connected"))
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096)) #recieving data from connection in 2048 bits 2048*8 to increase size
            players[player] = data
            #reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                elif player == 0:
                    reply = players[1]
                elif player == 1 and players[player].lose == True:
                    reply = player((10,10), (244, 238, 238))
                    #reply = players[0]
                elif player == 0 and players[player].lose == True:
                    reply = player((11,11), (244, 238, 238))
                    #reply = players[1]




                print("Recieved: ", data.playerBody)
                print("Sending: ", reply.playerBody)



            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept() #accepts connection and stores the ip address of the connection
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1