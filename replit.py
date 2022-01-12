# This software is licensed under the GPLv3 license. It can be found in docs/LICENSE.md
# Copyright 2022 Froggo





### Configuration
## [CONFIG] Debug
debug = False
update_pip = False

## [CONFIG] Program
program_d = "Replit-Pyfile"        # program directory from in /home/runner/
program_f = "test_script.py"       # program file from in /home/runner/[program_f]/
packages = ["pygame", "arcade"]    # all modules you need installed






### Autoupgrade & Run
import os, sys
out = os.popen("pip list").read().split("\n")

installed = False

def run():
  print("running")
  sys.path.append("/home/runner/"+program_d)
  print(os.popen("python3 /home/runner/"+program_d+"/"+program_f).read())
  sys.exit()

if update_pip:
  if debug:
    print("checking for pip update")
  update_pip_out = os.popen("pip install --upgrade pip").read()
  if debug:
    print(update_pip_out)

print("checking packages")
for item in out:
  if debug:
    print("tick: "+item)
  if item.startswith("arcade "):
    run()

print("installing packages")
install = os.popen("pip install "+" ".join(packages)).read()
if debug:
  print(install)
run()