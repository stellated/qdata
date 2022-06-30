from trading_ig.rest import IGService
from trading_ig_config import config

print(config.acc_type)
print(config.username)

'''
import trading_ig
for a in sorted(dir(trading_ig)):
    if not a.startswith('_'):
        print(a, type(getattr(trading_ig, a)))

print('\n--rest--')
for a in sorted(dir(trading_ig.rest)):
    if not a.startswith('_'):
        print(a, type(getattr(trading_ig.rest, a)))

print('\n--utils--')
for a in sorted(dir(trading_ig.utils)):
    if not a.startswith('_'):
        print(a, type(getattr(trading_ig.utils, a)))
'''