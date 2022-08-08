# Docker Essentials

- there are 3 essentials that you need to know about to have a decent idea of how to use Docker
- understanding docker hub
- running containers
- defining images

- before I go further I want to be really clear about the difference between docker images and docker containers
- docker images are a collection of all of the software that a particular application needs in order to run
- they contain the operating system, the code environment, the dependencies
- everything
- docker containers are instances of that software actually running
- so from one image, I could make many containers which are all running the same software

- ok, so to get started, we need to install docker

_search "install docker" and step through the installation"_

## Dockerhub

- so the first of the essential things you need to know about is Dockerhub
- dockerhub is a online repository of docker images
- check out all of the publically available docker images available on [docker hub](https://hub.docker.com/search?image_filter=official&type=image)

_Open docker hub_

- on dockerhub you can find images which run almost all of the key software components you might find in your stack
- these images contain all of the dependencies required to create docker containers which run that software and will run in the same way on whatever machine you put them on

- as an example, I'll set up a postgres database

- [here](https://hub.docker.com/_/python) you can see the official postgres database image

_Search for postgres on docker hub_

- you can use it to run postgres... with NO setup, installation or any of the usual troubles

- I can use the docker command line interface to run the postgres container
- I'm gonna use a long and complicated looking command here, but I'll come back to it and break it down in just a minute

```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 --rm postgres
```

- now if i run `docker ps` i can see that postgres is running

_Run `docker ps`_

- i can prove it to you by connecting through pgadmin

_Connect to database through pgadmin_

- and what's important to notice here is that this same image would be able to run containers on a windows machine, a linux machine, a mac, or whatever else, as long as that machine is running docker
- the operating system is bundled inside the image

- now let me break down that command that I just ran
- `--name` names the container, as you can see in `docker ps`
- docker creates random names if you dont specify them
- `-e` specifies environment variables
- `-d` means that it will run in the background, and return me to the command line prompt
- `-p` allows you to specify a mapping between ports inside the docker container and those on your computer
- my docker container, which is essentially a virtual computer running within my own machine, that container has its own ports
- here i've mapped port 5432 on my local machine to port 5432 on the container, which is where postgres is listening to for connections

- `--rm` removes the container when it is stopped
- `postgres` is the name of the image you want to create a container from
- let's check out the documentation for `docker run` [here](https://docs.docker.com/engine/reference/run/) where we could find out the different flags available

_Search docker run_

## Making our own Docker image

_Switch to webcam_

- now let's take it all the way back to the fundamentals and create our own docker image

### The Dockerfile

- we define how to create our image in a Dockerfile

_Show the dockerfile contents_

- A Dockerfile contains a sequence of commands which we call instructions
- they define how to create the docker image step by step

- here we have a very simple dockerfile that illustrates how a few important instructions work

- every dockerfile starts with a FROM instruction
- it specifies the base image which the image will be built upon
- in our case, we're starting off from the python image which came from dockerhub
- it has python installed
- you can create images which build on top of others, stacking together layers
- so if you need to run something which depends on pytorch, you could build your container on top of the pytorch container

- the RUN instruction is for running terminal commands

_Highlight run instruction_

_Show docs_

- the WORKDIR command sets the current working directory within the image for following commands to use

- the COPY instruction copies files into the container, from where the image is being built
- here we're copying in the python file to the current directory

- finally, we specify an entrypoint
- the entrypoint is the shell command which is going to run when we run a container from this image
- it allows you to configure the docker container as an executable, that executes this command immediately when run
- your container could imemdiately start hosting a database, training a machine learning model, or serving an API, depending on what you put in the entrypoint

- in our case, the python file just runs a loop for 100 seconds

- you can find the details of all possible instructions in the dockerfile reference

_Open dockerfile docs_

### Build the image

- run `docker build -t <tag> . ` to build the image
- you can also tag it with a useful name and version with the -t flag

```
docker build -t myimage .
```

- the `.` represents the "build context"
- The build context is the set of files located at the specified PATH or URL.
- Those files are sent to the Docker daemon during the build so it can use them to build the image.
- that's somewhere else in the docker system files
- When we build the image in a given directory, everything is added recursively to the context
  - the image doesnt contain the context
  - this is just the set of files which can be reached during the build
- by default, docker looka for a dockerfile named `Dockerfile` with a capital D and no extension
- By default the docker build command will look for a Dockerfile at the root of the build context.

- you can specify files that you don't want to copy to the docker build context by putting them in the .dockerignore file, much like how you would use a .gitignore file

- run `docker images` to see local images

## Creating an instance of a docker image - a docker container

- now lets run a container based on the image we just created

```
docker run mycontainer
```

## See Docker containers

- run `docker ps`
- names are generated randomly

## Stop the Docker container

- we can stop the container by name

`docker stop <container_name> --time=0`

- its annoying to have to find the name
- so we can name our containers using the --name flag

`docker run --name mycontainer myimage`

- run `docker ps -a`

## Try to run it again

- now let's try and run it again

## The Docker VSCode extension

- you can start, stop, shell into containers and even run an instance of VScode inside one using the docker vscode extension, which is well worth checking out

<!-- TODO describe different shell and exec forms -->
<!-- TODO show examples other than postgres, highlighting that it's as simple as `docker run <CONTAINER NAME>` to run a container -->

<!-- ## Run the container interactively and with a terminal

- if we wanted to effectively shell into a docker container we can use the docker exec command to execute the instance of bash which is inside

```
docker exec
``` -->

<!-- ## Using VSCode in a local container
- install the docker extension
- here you should be able to see all of your images
- you can run them by right clicking
- you can attach a shell to any running container
- even better, you can attach VSCode to it -->

<!-- MOVE BELOW TO NEW LESSON -->
<!--

## Tips for creating images

### Know how the cache works and how to use it

### Chain commands together

### Small images

### Multi-stage builds -->
