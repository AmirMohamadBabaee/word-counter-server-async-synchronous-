#!usr/bin/env python3
# server.py

import socket
import counter
import sys
import logger

if __name__ == '__main__':
    log = logger.init_logger(file_name='server.log')

    with socket.socket(
            socket.AF_INET, # stand for IPv4 address family
            socket.SOCK_STREAM # stand for TCP protocol
        ) as s:
        try:
            s.bind(('', 1080))
            log.info('server is up...')
            s.listen(2)

            while True:
                connection, address = s.accept()

                with connection:
                    log.info(f"address of new client : {address}")

                    while True:
                        try:
                            data = connection.recv(8192)

                            if not data:
                                break

                            if data.decode('ascii') == 'close server':
                                log.info('Shuting down server from client...')
                                sys.exit(0)
                                
                            log.info(f'client {address} : ' + data.decode('ascii'))
                            wordsNum = counter.word_counter(data.decode('ascii'))
                            charNum = counter.character_counter(data.decode('ascii'))
                            output_data = f'words : {wordsNum}      characters : {charNum}'
                            log.info(output_data)
                            connection.sendall(output_data.encode())

                        except Exception as e:
                            log.exception(e)

                    log.info(f'client {address} now is down!')
        except KeyboardInterrupt as error:
            log.error(str(error) + '\r\nShutting down server...')

        except OSError as error:
            log.exception(str(error))
