#usr/bin/env python3
#client.py

import socket
import sys
import logger

if __name__ == "__main__":
    log = logger.init_logger(file_name='client.log')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('127.0.0.1', 1080))
            log.info(f'connected to {s.getpeername()}')

            while True:
                message = str(input('>>> ENTER your message here: '))

                if message == 'exit':
                    log.info('Shuting down client...')
                    break

                s.sendall(message.encode())
                data = s.recv(8192).decode('ascii')
                log.info('recieved : ' + repr(data))

        except ConnectionRefusedError as error:
            log.exception(str(error) + '\r\nMaybe server is down or There is another problem.')
            # log.error(str(error) + '\r\nMaybe server is down or There is another problem.', exc_info=True)

        except BrokenPipeError as error:
            log.exception(str(error))
            
        except KeyboardInterrupt as error:
            log.error(str(error) + '\r\nShutting down client...')