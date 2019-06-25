#!/usr/bin/python
import socket
def scanner(ip):
    #print("in scanner fucntion:"+ip)
    t=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #port=input("please enter the port nuber you want to scan")
    #print(type(port),type(ip))
    for i in range(1,65535):
            con=t.connect_ex(('192.168.1.225',i))
            if con==0:
                print("connected on tcp:"+str(i))
            t.close()
            t=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(22,24):
        con1=t.connect_ex(('192.168.1.225',i))
        if con1==0:
                print("connected on udp:"+str(i))
        else:
                print("not connnected on udp:"+str(i))
        t.close()
        t=socket.socket(socket.AF_INET, socket.SOCK_STREAM)'''

def main():
    #ip=raw_input("please enter the ip address:")
    #print("in main function:"+ip)
    scanner("127.0.0.1")
if __name__=="__main__":
    main()
