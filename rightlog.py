import logging


logging.basicConfig(filename="F://Projectselenium//Mylog//rightlasttesting.log",
                    format='%(asctime)s: %(levelname)s:%(message)s', # print time
                    datefmt='%m/%d/%Y %I:%M:%S %p', # date format
                    level=logging.DEBUG) #  level=logging.DEBUG ==> this will print debug and info too.

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")




