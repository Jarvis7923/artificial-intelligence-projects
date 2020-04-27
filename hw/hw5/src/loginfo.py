"""
For colorful terminal log messages

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""
from enum import Enum

class log_type(Enum):
    error = 0
    system = 1
    info = 2

def show_loginfo(logtype, msg, end='\n'):
    RESET = '\033[0m'
    if logtype is log_type.error:
        expr1 = '\033[1;31m[ERROR]'+ RESET
        msg = ' \033[1m' + msg + RESET
    elif logtype is log_type.system:
        expr1 = '\033[1;35m[SYSTEM]'+ RESET
        msg = ' \033[4m' + msg + RESET
    elif logtype is log_type.info:
        expr1 = '\033[1;32m[INFO]'+ RESET
        msg = ' ' + msg + RESET

    print(expr1 + msg, end=end)
