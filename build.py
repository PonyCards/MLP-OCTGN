import os
import shutil
import sys
from subprocess import check_call

def ignore(path, names):
  return shutil.ignore_patterns('.*', 'README.md', 'build.py', 'build')(path, names)

def build():
  selfDir = os.path.dirname(os.path.realpath(__file__))
  buildDir = os.path.join(selfDir, "build")
  print(selfDir)
  print(buildDir)
  try:
    shutil.rmtree(buildDir)
  except:
    pass
  shutil.copytree(selfDir, buildDir, ignore=ignore)
  check_call([shutil.which('o8build'), '-d', buildDir])

if __name__ == "__main__":
  build()
