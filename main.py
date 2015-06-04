# log ########################################################################
from os import path
from panda3d.core import MultiplexStream, Notify
import sys
from ya2.engine import Configuration, OptionMgr
from ya2.engine import Engine
from yorg import Yorg


if not path.exists('main.py'):  # is it the deployed version?
    sys.stdout = open('yorg_output.txt', 'w')
    sys.stderr = open('yorg_error.txt', 'w')
    nout = MultiplexStream()
    Notify.ptr().setOstreamPtr(nout, 0)
    nout.addFile('yorg_log.txt')


# main #######################################################################
if __name__ == '__main__' or path.exists('main.pyo'):
    Engine(
        Configuration(
            fps=True,
            win_title='Yorg',
            antialiasing=OptionMgr.get_options()['aa']),
        'yorg')
    Yorg().run()