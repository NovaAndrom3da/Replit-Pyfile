## What is Replit Pyfile?
Replit Pyfile is a project template/add-in for you to be able to run another python file using the run button. It automatically installs any modules you need to use in your program. This makes it easy for anyone who works on a project in replit and on a local computer.

## Why do I need it?
It can improve the flow between working on a local computer and replit. It was originally created to avoid renaming the main file in a project.

## How do I use it?
First, fork the project on [Replit](https://replit.com/@Froggo8311/Replit-Pyfile) or on [GitHub](https://github.com/Froggo8311/Replit-Pyfile).

1. Then, you can delete the `test_script.py` file.
2. Edit the configuration lines in the `replit.py` file.
   - `debug` - Enable (`True`) or disable (`False`) extra logging to the console.
   - `update_pip` - Enable or disable updating pip on run.
   - `program_d` - The directory of the file when in replit (such as `Replit-Pyfile`, in which `test_script.py` can be found).
   - `program_f` - The name of the file (such as `test_script.py`).
   - `packages` - The required modules (in python list form), such as `pygame` or `arcade`.

## How is it licensed?
It is licensed under [GPLv3](https://github.com/Froggo8311/Replit-Pyfile/blob/main/docs/LICENSE.md).

Copyright © 2022 Froggo
