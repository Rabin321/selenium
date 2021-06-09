import logging

logging.basicConfig(filename="F://Projectselenium//Mylog//lasttesting.log",
                    format='%(asctime)s: %(levelname)s:%(message)s', # print time
                    datefmt='%m/%d/%Y %I:%M:%S %p', # date format
                    level=logging.DEBUG) #  level=logging.DEBUG ==> this will print debug and info too.

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")




