import socket
import time

# Put in a website in HOST '  '
# EX HOST = 'data.pr4e.org'
HOST = '  '
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
#put the link of the image available in the website as provided in the word HOST
# EX  mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1\r\n\r\n')
mysock.sendall(b' HTTP/1\r\n\r\n')
count = 0
picture = b""

while True :
# recieving the data from the socket
    data = mysock.recv(5120)
# if data has finished, stop
    if len(data) < 1: break
# you can remove the '#', the code is to cause the data to pause at certain time, this aids if the data retrieving is large
    #time.sleep(0.25)
# ge the length & the count of the data
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close



# Skip past the header and save the picture data

# to use this remove the 'hashtag'
#picture = picture[pos+4:]
#fhand = open("stuff.jpg", "wb")
#fhand.write(picture)
#fhand.close()
