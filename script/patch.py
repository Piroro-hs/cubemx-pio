import os

Import('env')

env.PioPlatform().frameworks['stm32cubemx'] = {'script': os.path.join(os.getcwd(), 'script/stm32cubemx.py')}
