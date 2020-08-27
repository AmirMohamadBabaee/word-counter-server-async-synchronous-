import logging


def init_logger(file_name:str, **options) -> logging.Logger:
    """This function init a logger object that has console and 
    file handler. This function can use in any modules."""

    # initialize logger object
    log = logging.getLogger(__name__)

    # declare logger handler
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(file_name)

    # set level for handlers
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    # declare handler formatter
    console_format = logging.Formatter(str(options.get('console_fmt')) if options.get('console_fmt') else '%(levelname)s : %(message)s')
    file_format = logging.Formatter(str(options.get('file_fmt')) if options.get('file_fmt') else '%(asctime)s : %(name)s : %(levelname)s # %(message)s')
    
    # set formater for handlers
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # set handlers for logger object
    log.addHandler(console_handler)
    log.addHandler(file_handler)

    # set DEBUG mode level for logger object
    log.setLevel(logging.DEBUG)

    log.info('initialize logger object')

    return log