from pylog.log import Log


def test():
    log.debug('test')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
    log.debug('debug')


if __name__ == '__main__':
    log = Log().logs
    test()
