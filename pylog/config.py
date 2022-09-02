# Created by Kernel.Huang.
# User: kernel@live.com
# Date: 2020/5/11
# Time: 16:28

import configparser
import os
from os.path import dirname, abspath


class Config(object):
    configFilepath = ''
    form = '%(asctime)s [%(process)d] [%(levelname)s] [%(module)s.%(funcName)s] [%(pathname)s:%(lineno)d] %(message)s'

    def __init__(self, directory='config', name='app'):
        filename = name + '.ini'
        project = dirname(abspath(__file__))
        self.set_path(project, directory, filename)
        self.config = configparser.ConfigParser()
        self.read()

    def set_path(self, project, directory, filename):
        configDirPath = os.path.join(project, directory)
        self.configFilepath = os.path.join(configDirPath, filename)

    def read(self):
        self.config.read(self.configFilepath)

    def get_dirname(self):
        return self.config.get('log', 'dir')

    def get_filename(self):
        return self.config.get('log', 'name')

    def get_level(self):
        return self.config.get('log', 'level')

    def get_format(self):
        return self.form

    def get_time_unit(self):
        return self.config.get('log', 'timeUnit')

    def get_file_number(self):
        return self.config.get('log', 'fileNumber')
