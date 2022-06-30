from trading_ig.rest import IGService
from trading_ig_config import config

for a in dir(config):
    print(a, type(getattr(config, a)), getattr(config, a))

ig_service = IGService(config.username, config.password, config.api_key)
print(ig_service)
ig = ig_service.create_session()
print(ig)

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