from collections import namedtuple

from colorama import Fore, Back, Style


COLOURS = ['BLUE', 'CYAN', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']
STYLES = ['NORMAL', 'BRIGHT', 'DIM']

bit = namedtuple('Bit', ('symbol', 'colour', 'background', 'brightness'),
                 defaults=('', 'WHITE', 'WHITE', 'NORMAL'))
