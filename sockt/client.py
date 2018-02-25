import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.50.128', 8888)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    # Send data
    message = 'dlt'
    trace = ""
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    #file_len = int(sock.recv(2**16))
    #print file_len +1
    # confirm reception
    sock.send("ook")

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while True: #amount_received < file_len:
        data = sock.recv(80)
        if data == "":
            break
        amount_received += len(data)
        trace += str(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    log = open("trace.dlt", "wb")
    log.write(trace)
    log.close()
    print >>sys.stderr, 'closing socket'
    sock.close()
