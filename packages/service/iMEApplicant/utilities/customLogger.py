import logging
import os
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        log_dir = os.path.join('.', 'Logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.LogFileName = os.path.join(log_dir, f'iME_Applicant_log_{curr_time}.txt')
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