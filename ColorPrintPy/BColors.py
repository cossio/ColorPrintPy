'''
ASCII color codes for printing colors in terminal
'''

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def colstr(dec, what):
    '''
    Colored string with decorator. Adds ENDC at the end.
    '''

    return dec + what + ENDC
