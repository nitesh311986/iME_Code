import logging


import logging
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = '.\\Logs\\iME_Business_log' + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)



# class logGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger("iME Applicant")
#         fileHandler = logging.FileHandler('.\\Logs\\automationnew.log',mode="w")
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#         fileHandler.setFormatter(formatter)
#         logger.addHandler(fileHandler)
#         logger.setLevel(logging.INFO)
#         # logger = logging.getLogger("Test Name")
#         # logger.setLevel(logging.INFO)
#         return logger