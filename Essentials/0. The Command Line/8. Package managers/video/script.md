- package managers are tools used to install code written by other people
- that's because the bundles of code in those 3rd party softwares are known as packages, and these package managers manage how and where they are installed
- you can use these package managers from the command line to do things like install other commands to run in the terminal or libraries that can be used within other programming languages
- to install terminal commands or other programs you use a system package manager
- to install extensions for a particular language, like python, you would use a python package manager
- if you're on ubuntu or in git bash in windows, then your system package manager will probably be a software called apt

_Type apt in the terminal_

- if you're on mac, it will be a software called brew

_Type brew in the terminal_

- for example on mac i can run `brew install tree`
- that's because i want to use my system package manager brew
- and i want to use its subcommand install to tell it to install something
- and the thing i want to install is a software called "tree"

_Run brew install tree_

- now my machine recognises the command that was installed
- notice that the name of the install is not always the name of the command which it makes available
- notice that one install may give you access to more than one command, or it might do somethign else and not give you access to any

- package managers can also be used to do other things like uninstall packages

_Run `brew` alone to show the different commands and highlight the usage_

- just to be clear about terminology
- installing something means making those files ready to run, which is different to downloading something
- this brew install command does the combination of downloading the files from somewhere like the internet or off a USB, and then also installs them so that commands can be recognised by your terminal, or applications can be found on your machine

<!-- SUMMARY -->

- so that's what a system package manager is and how it can be used
