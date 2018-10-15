# This will make imports cleaner when importing all the sport scripts
# into the main
__all__ = []

global all_tools
all_tools = []

__all__.append('all_tools')

import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    if name == 'util':
        continue
    
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)

        if name.startswith('PDevTool_'):
            all_tools.append(module.__init_tool())