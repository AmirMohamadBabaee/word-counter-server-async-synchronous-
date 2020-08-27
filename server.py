#!usr/bin/env python3
# server.py

import socket
import counter
import sys

if __name__ == '__main__':
    with socket.socket(
            socket.AF_INET, # stand for IPv4 address family
            socket.SOCK_STREAM # stand for TCP protocol
        ) as s:
        s.bind(('', 1080))
        print("server is up!")
        try:
            s.listen(2)

            while True:
                connection, address = s.accept()

                with connection:
                    print(f"address of new client : {address}")

                    while True:
                        try:
                            data = connection.recv(1024)

                            if not data:
                                break

                            if data.decode('ascii') == 'close server':
                                print('\r\nShuting down server...')
                                sys.exit(0)
                                
                            print(f'client {address} : ', data.decode('ascii'))
                            wordsNum = counter.word_counter(data.decode('ascii'))
                            charNum = counter.character_counter(data.decode('ascii'))
                            output_data = f'words : {wordsNum}      characters : {charNum}'
                            print(output_data)
                            connection.sendall(output_data.encode())

                        except Exception as e:
                            print(e, file=sys.stderr)

                    print(f'client {address} now is down!')
        except KeyboardInterrupt as error:
            print(error, '\r\nShutting down server...', file=sys.stderr)
