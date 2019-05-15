import logging
import getpass
from logging import handlers


class MyLog(object):
    def __init__(self, when='m', backupCount=0):
        # 獲取本地使用者
        user = getpass.getuser()

        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)

        # 建立格式
        format = '%(asctime)s-%(levelname)s-%(name)s: %(message)s'
        formatter = logging.Formatter(format)

        streamhandler = logging.StreamHandler()
        streamhandler.setFormatter(formatter)
        self.logger.addHandler(streamhandler)

        logfile = './' + user + ".log"
        filehandler = handlers.TimedRotatingFileHandler(filename=logfile, when=when,
                                                        interval=1, backupCount=backupCount)
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
    test = MyLog()
    test.debug("1")
    test.info("2")
    test.warning("3")
    test.error("4")
    test.critical("5")


if __name__ == "__main__":
    main()