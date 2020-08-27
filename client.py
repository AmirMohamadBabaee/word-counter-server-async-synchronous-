#usr/bin/env python3
#client.py

import socket
import sys

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('127.0.0.1', 1080))

            while True:
                message = str(input('>>> ENTER your message here: '))

                if message == 'exit':
                    print('Shuting down client...')
                    break

                s.sendall(message.encode())
                data = s.recv(10240).decode('ascii')
                print('recieved : ', repr(data))

        except ConnectionRefusedError as error:
            print(error, '\r\nMaybe server is down or There is another problem.', file=sys.stderr)
            
        except KeyboardInterrupt as error:
            print(error, '\r\nShutting down client...' ,file=sys.stderr)