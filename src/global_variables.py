import platform
import os

def init():
    global cleart, bar
    opsys = platform.system().lower()
    cleart, bar = ('clear','/') if opsys == 'linux' else ('cls','\\')
    relative_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(bar.join(relative_path.split(bar)[0:-1]))

if __name__ != '__main__':
    init()
