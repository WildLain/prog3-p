from functools import reduce
import sys
import re
for line in sys.stdin:
    print(''.join([chars[::-1] if chars.split() else chars for chars in re.split(r'(\s+)', line)]))
    # print(reduce(lambda x, y: x + y[::-1] + ' ', line.split(), ''))

    # eiD 17 adnaP-nereaB dnis, eniem hci ,   ZNAG_giztup!
    # Die 17 Panda-Baeren sind, meine ich ,   GANZ_putzig!