- there are just two ways that I think you should run python scripts
- the first way is from the terminal
- you do that by typing python followed by the path to your file
- if your file is in the currently open folder, then that's just going to be the name of your file
- otherwise it needs to be the relative or absolute path to that file

- another extremely useful way to run a python is by using these magic comments

_Type `#%%`_

- like all lines that start with a hashtag in a python file, these are not run by the interpreter
- they are ignored
- but in VSCode this particular expression of a hashtag followed by two percentage signs does something special
- it splits the python file up into different cells that can be run independently, and interactively, like a notebook file
- like in a notebook you can use the `SHIFT+ENTER` shortcut to run each cell
- this brings the benefits of a notebook file, like the fact that you can still see the values of a variable after a cell has run, and that you don't have to run the entire file to run the piece of code you're interested in
- but it has a major benefit over notebook files, which is that this file can be run as a regular python file from the terminal
- this means that you can develop this file as if it were a notebook, and then deploy it to the cloud where there's nobody to run cells, only terminals, and it will work in exactly the same way

<!-- HOW NOT TO RUN PYTHON FILES -->

- now I want to highlight some ways NOT to run a python file, which commonly lead to issues and confusion

- the first mistake is trying to run a py file by pressing shift enter like you would in a notebook cell
- this might seem to run something in the terminal, but it only runs the line that your cursor is currently on, not the whole file

- the second way NOT to run a python file is by hitting the play button in the top right
- when you do that, you can see that VSCode opens up a new terminal and runs a long command
- sometimes this works fine, but when it doesn't people get confused
- if you look at the command that's been run, it has two parts
- the first is an absolute filepath to the version of python being used to run the file
- the second is the absolute filepath to the file which you've tried to run
- this can cause problems becuase
- 1. it typically runs a different version of python than you want, which is in an environment that doesn't have all of the libraries you need installed
- 2. it sometimes tries to look for the file in the wrong place

- so stick to running the python file from the integrated terminal or by using the magic comments

- note that everything I've said here applies to python files, that is files ending in `.py`
- it doesn't apply to python notebooks which have the `.ipynb` extension
- there is only one way to run notebooks, and that's by running each of the cells using the play button or the shift+ENTER shortcut
