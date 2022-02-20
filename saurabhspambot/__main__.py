#saurabhspambot By @tera_baap_katil

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from saurabhspambot.utils import load_plugins
import logging
from telethon import events
from . import saurabh, saurabh2, saurabh3, saurabh4, saurabh5, saurabh6, saurabh7, saurabh8, saurabh9, saurabh10, saurabh11, saurabh12, saurabh13, saurabh14, saurabh15

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "saurabhspambot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Saurabh Spam Bot Successfully deployed -!")
print("Enjoy! Do visit @heartbrokenperson1")

if __name__ == "__main__":
    Riz.run_until_disconnected()
    
if __name__ == "__main__":
    Riz2.run_until_disconnected()

if __name__ == "__main__":
    Riz3.run_until_disconnected()
    
if __name__ == "__main__":
    Riz4.run_until_disconnected()

if __name__ == "__main__":
    Riz5.run_until_disconnected()
    
if __name__ == "__main__":
    Riz6.run_until_disconnected()
    
if __name__ == "__main__":
    Riz7.run_until_disconnected()

if __name__ == "__main__":
    Riz8.run_until_disconnected()
    
if __name__ == "__main__":
    Riz9.run_until_disconnected()

if __name__ == "__main__":
    Riz10.run_until_disconnected()   
    
if __name__ == "__main__":
    saurabh11.run_until_disconnected()
    
if __name__ == "__main__":
    saurabh12.run_until_disconnected()
    
if __name__ == "__main__":
    saurabh13.run_until_disconnected()
    
if __name__ == "__main__":
    saurabh14.run_until_disconnected()
    
if __name__ == "__main__":
    saurabh15.run_until_disconnected()
