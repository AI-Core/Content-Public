<!-- MOTIVATION -->

- one of the key benefits of docker is that it reduces the chance of human error by defining everything in a dockerfile
- but what's the point in that when you still have to remember every flag and argument to a command like this

_Show long docker command_

- you could put all of that in a bash script
- but theres a standardised way to do it using docker compose

- docker compose is a command line tool that expects to find all of the configuration for how to run a container in a YAML file like this

_Show docker-compose.yml_

- all of the configuration that would typically be in command line flags and arguments is in this yaml file
- and I can run it with a single command `docker compose up`

_run docker compose up_

- it looks for a file called `docker-compose.yml` in the working directory and runs everything it specifies
- you can shut it down by running `docker compose down`

_run docker compose down_

- the terminal then displays the logs of the container running

- as with docker run, i can use the detach flag to run the system in the background

_run in detached mode_

_webcam_

- as always, I can never teach you everything, so it's important to understand how to teach yourself from the docs
- I'm gonna look up the docker compose reference to understand what's going on in this docker compose file

_show some of the keys and what they do_

- you can see here that the build key can be used instead of the image key to build an image from a dockerfile

_show the example [here](https://docs.docker.com/compose/)_

- as with docker run, the argument specifies what should be sent to the build context for docker to build the image
- and by default, docker looks for the dockerfile in that directory

- one thing to always remember is that if you change the source code in your image, then you need to rebuild the image
- you can build all the images in a docker compose file by running `docker compose build`

_webcam_

- that's nice, but the main point of docker compose is actually to run multi-container applications
- that's why it's called docker compose
- because composed together, several containers make up the whole application
- you might have a system that depends on a database which you're running in one container, and another application which collects data and puts it into the database

- that might look something like this

_Show docker compose file_

- I've added in another container definition
- in my case it's a very simple container which runs a python file...

_show dockerfile_

- ...which connects to the database

_show python file_

- but it could be a data collection system that i mentioned, for example

- and I've also specified that this container depends on the other one being set up first with the depends on key

<!-- NETWORKING -->

- importantly, the containers are created on the same network by default, so they can find each other and communicate

_run compose up_

- the name you give to each service, in my case "database" and "python" represent the IP address of each container within that network
- so in my python code, I've specified "database" as the host IP address
- and this translates to the ip address of the database container
- you can see this if i remove the depends on key so that the database isn't set up before python tries to connect to it, and so it throws an error and shows the IP address

- another really important thing about networking to notice is that localhost inside a container does not refer to the ip address of your host machine it refers to the ip address of the container
- so in this example, if i'd put localhost as the host for the database, this container would be trying to connect to itself, not to my host

- you can configure much more advanced networking situations with docker compose too, but I wont get into that here

<!-- LIMITATIONS -->

- note that a system deployed with docker compose is still going to be constrained by the limits of the host machine
- even though they act like isolated machines, the containers still have to share the underlying host resources, like memory and CPU

<!-- OTHER APPLICATIONS -->

- What are some of the other applications of docker compose?

- when developers are working on new features, they are of course going to have to work through bugs
- that's the nature of writing code
- so they definitely don't want to develop features on the production system
- so docker compose can be used to spin up an isolated local environment for development
- that is a version of the system which is only accessible on their machine, where they can introduce whatever bugs and test features they need to, without affecting users

- docker compose can also be used for testing your software
- typically, developers will spin up a local version of their system using docker compose so that they can run tests, which might depend on all of those resources, and then spin it down

<!-- OUTRO -->

- so now, you can start using docker compose to build multi-container applications

<!--
TODO lesson on typical prod, dev, staging envs
- well typically, a software team would have a production system, which is serving real users
- then they'll have a development system, which contains all the new features under development and is shared by the engineering team -->
