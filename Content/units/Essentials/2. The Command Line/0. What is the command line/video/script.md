- Today, computers are very easy to use.
- they display everything with intuitive colors, icons, and layouts
- but under the hood, what's happening?
- what's happening when you move your mouse, open a browser, change your background, or move some files around?
- of course, your interactions are causing some code to run
- that code then updates the display
- and that code is really just a bunch of files
  - some of those files run when your computer turns on
    - they might do something like display your applications along the bottom of the screen
    - or display the login screen
  - some of them run when you take particular actions like rename files
- that's how everything on the computer works
  - you interact with something using the visual display, and some code runs
- we call that visual display the _graphical user interface_ or _GUI_ sometimes pronounced goo-ey
- the graphical user interface is just a layer on top of the code which is running that makes things look pretty
- we don't have to interact with our computer through the pretty GUI though
  - we can also run the code directly
- and we do that using the _command line interface_, or _CLI_
- the command line interface is a way to talk directly control the computer, without having to use the graphical user interface
- why would you want to do this?

  - graphical user interfaces are much more prone to human error compared to exact lines of text
  - in systems that need to run automatically, there isn't going to be a human
  - some popular applications widely used in industry, like git or airflow, don't have graphical user interfaces
    - in the case of other software, like docker or mlflow, the graphical user interfaces don't give you access to the complete functionality

- we call it the command line, because it provides a line where you can write text to send commands to the machine
- it is also known as the terminal, or the shell

## GUI vs CLI

- Everything that you can do using the graphical user interface, can also be done by running commands in the command line
- whether that is:
- Looking at your current folder
- Showing folder contents
- or Moving around folders
