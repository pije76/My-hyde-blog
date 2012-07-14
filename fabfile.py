from fabric.api import local


def gen():
  local("python ../hyde/hyde.py -g -d ../gen_simple")

def test():
  local("python ../hyde/hyde.py -w -d ../gen_simple")

def commithub(txt):
  local("git add .")
  local('git commit -m "%s"' % txt)
  local('git push origin master')
