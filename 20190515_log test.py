import logging
from logging import handlers
import time


class MyLog(object):
    def __init__(self, name=None, when='m', interval=1, backupCount=0):
        self.logger = logging.getLogger(name or __name__)
        self.logger.setLevel(logging.DEBUG)

        # 建立格式
        format = '%(asctime)s-%(levelname)s: %(message)s'
        formatter = logging.Formatter(format)

        streamhandler = logging.StreamHandler()
        streamhandler.setFormatter(formatter)
        self.logger.addHandler(streamhandler)

        logfile = './' + (name or __name__) + ".log"
        filehandler = handlers.TimedRotatingFileHandler(
            filename=logfile,
            when=when,
            interval=interval,
            backupCount=backupCount)
        filehandler.suffix = "%Y%m%d-%H%M"
        filehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def log(self, level, msg):
        self.logger.log(level, msg)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def disable(self):
        logging.disable(50)


def main():
    test = MyLog(when="M", backupCount=5)

    while True:
        test.debug("1")
        test.info("2")
        test.warning("3")
        test.error("4")
        test.critical("5")
        time.sleep(1.)


if __name__ == "__main__":
    main()
