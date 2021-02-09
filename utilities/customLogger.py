import logging

class Logen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="E://pythonProject//Framefork1//automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s' ,datefmt='%m/%d/%Y %I:%M:%S %w')
        logger = logging.getLogger()
        logger.setLevel(logger.INFO)
        return logger






