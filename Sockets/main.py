import socket
try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, True)
    s.settimeout(5)
    s.connect(('ericc.ninja',80))
except:
    print('Error!')
else:
    print("Connection successful")
    sent = s.send('GET / HTTP/1.1\r\nHost: ericc.ninja\r\n\r\n'.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print(data)
    s.shutdown(socket.SHUT_RDWR)
    s.close()
