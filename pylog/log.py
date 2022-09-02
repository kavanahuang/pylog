import logging
import os
from logging import handlers
from os.path import dirname, abspath
from pylog.config import Config


class Log(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    dirname = ""
    filename = ""
    filepath = ""
    logPath = ""
    project = ""
    logs = None
    form = None
    console = None
    cfg = Config()

    def __init__(self,
                 level=cfg.get_level(),
                 when=cfg.get_time_unit(),
                 back_count=cfg.get_file_number(),
                 formatter=cfg.get_format()):

        self.init_config()
        self.init_dir()
        self.init_file()

        self.logs = logging.getLogger(self.filepath)
        self.init_format(formatter)
        self.init_level(level)
        self.init_console()
        self.handler_log(when, back_count)

    def init_config(self):
        self.dirname = self.cfg.get_dirname()
        self.filename = self.cfg.get_filename()
        self.project = dirname(abspath(__file__))

    def init_dir(self):
        self.logPath = os.path.join(self.project, self.dirname)
        os.makedirs(self.logPath, exist_ok=True)

    def init_file(self):
        self.filepath = os.path.join(self.logPath, self.filename)

    def init_format(self, formatter):
        self.form = logging.Formatter(formatter)

    def init_level(self, level):
        self.logs.setLevel(self.level_relations.get(level))

    def init_console(self):
        self.console = logging.StreamHandler()
        self.console.setFormatter(self.form)

    def handler_log(self, when, back_count):
        files = handlers.TimedRotatingFileHandler(filename=self.filepath, when=when, backupCount=back_count,
                                                  encoding='utf-8')
        files.setFormatter(self.form)               # Write to file the log formatter.
        self.logs.addHandler(self.console)        # Add console handler object to logger.
        self.logs.addHandler(files)               # Add files handler object to logger.
