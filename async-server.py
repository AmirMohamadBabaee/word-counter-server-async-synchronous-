# usr/bin/env python3
# async server.py
# 
# =============================================================
# 
# for more information about async socket program visit :
# 
#       https://docs.python.org/2/library/asyncore.html 
# 
# =============================================================

import asyncore
import socket
import logger
import counter


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        try:
            data = self.recv(8192)

            if data:
                log.info(f'client {self.socket.getpeername()} : ' + data.decode('ascii'))
                wordsNum = counter.word_counter(data.decode('ascii'))
                charNum = counter.character_counter(data.decode('ascii'))
                output_data = f'words : {wordsNum}      characters : {charNum}'
                log.info(f'client {self.socket.getpeername()} : ' + output_data)
                self.send(output_data.encode())

        except Exception as error:
            log.exception(str(error))


class WordCounterServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        log.info('server is up...')

    def handle_accept(self):
        pair = self.accept()

        if pair is not None:
            socket, address = pair
            log.info (f"address of new client : {address}")
            handler = EchoHandler(socket)
            

if __name__ == "__main__":
    log = logger.init_logger('async-server.log')

    try:
        server = WordCounterServer('localhost', 1080)
        asyncore.loop()
        
    except KeyboardInterrupt as error:
        log.error(str(error) + '\r\nShutting down server...')

    except OSError as error:
        log.exception(str(error))

    except Exception as error:
        log.exception(str(error))