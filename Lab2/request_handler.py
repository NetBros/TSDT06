#!/usr/bin/env python3

import threading, socket, sys
from my_functions import *

class request_handler(threading.Thread):
    def __init__(self,conn,addr,BUFFER_SIZE):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.BUFFER_SIZE = BUFFER_SIZE

    def run(self):
        client_req = ''
        
        client_request = self.conn.recv(self.BUFFER_SIZE)
        client_req += str(client_request,"utf-8")

        # Finding host address from get request
        url_request = find_url(client_req)

        try:
            client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] Setting upp connection to ", url_request)
            client_socket.connect((url_request,80))
            client_socket.send(client_request)
            while 1:
                server_request = client_socket.recv(self.BUFFER_SIZE)
                if (len(server_request)>0):
                    #server_request += str(data_reply,"utf-8")
                    self.conn.send(server_request)
                else: break
            client_socket.close()
            self.conn.close()
        except socket.error as msg:
        	if client_socket:
        		client_socket.close()
        	if self.conn:
        		self.conn.close()
        	print("\n[*] Error could not open client socket")
        	sys.exit(2)