import os
import datetime

now=datetime.datetime.now()
msg="{}commit".format(now.strftime('%Y{} %m{} %d{} %H{} %M{}'.format(*"년월일시분")))
# msg = "{}commit".format(now.atrftime('%Y-%m-%d %H:%M:'))

def gitcmd(cmd):
    os.system(cmd)

gitcmd('git add --all')
gitcmd(f'git commit -am "{msg}"')
gitcmd('git push')