import os
import logging
from logging import handlers
import time


class Log(object):
    _instance = None

    # NOTE: 干預創建實例，達到實現單例模式的目的
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)  # NOTE: python2.7要寫成 ...(cls, *args, **kw)
        return cls._instance

    def __init__(self,
                 name=None,
                 path=".",
                 when='h',
                 interval=1,
                 backupCount=236):
        self.logger = logging.getLogger(name or __name__)
        self.logger.setLevel(logging.DEBUG)

        # 建立資料夾
        dir_path = os.path.abspath('.')
        self._path = os.path.join(dir_path, path)
        if not os.path.isdir(self._path):
            os.mkdir(self._path)

        # NOTE: 因為不判斷的話，logger會一直添加handler，導致handler過多，
        #       一瞬間輸出大量相同訊息，導致系統當機。
        if not self.logger.handlers:
            # 建立格式
            format = '%(asctime)s-%(levelname)s: %(message)s'
            formatter = logging.Formatter(format)

            streamhandler = logging.StreamHandler()
            streamhandler.setFormatter(formatter)
            self.logger.addHandler(streamhandler)

            logfile = self._path + "/" + (name or __name__) + ".log"
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
    while True:
        test = Log(when="m", backupCount=5)
        test.debug("1")
        test.info("2")
        test.warning("3")
        test.error("4")
        test.critical("5")
        time.sleep(1.)


if __name__ == "__main__":
    main()
