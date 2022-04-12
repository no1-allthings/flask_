import os
import datetime

now = datetime.datetime.now()
msg = "{}commit ".format(now.strftime('%Y-%m-%d %H시 '))

def gitcmd(cmd):
    os.system(cmd)

gitcmd('git add --all')
gitcmd('git commit -am "{}"'.format(msg))
gitcmd('git push')




