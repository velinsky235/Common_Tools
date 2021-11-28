''' Utility functions
'''


import os


def formatsize(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def ensure_dir(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != os.errno.EEXIST:
            raise

