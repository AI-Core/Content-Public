# Docker

## What is Docker?

- Docker is a tool that allows us to package our software applications with all the necessary dependencies in a self-contained environment called a docker image
- We can then create instances of these images which run that code
- we call those images docker containers
- they are called containers because, like shipping containers, regardless of what's inside, they are standardised and will work anywhere

<!-- USEFUL FOR PORTABILITY -->

- this portability is one of docker's key features
- Docker images define what code runs in which software environment when you create a container
- the software environment includes everything the container needs to run
- from the application code, to its dependencies, to the virtual operating system that runs on top of whatever OS is actually installed on the host machine
- what that means, is that docker containers will run in the same way on any operating system
- no need to tailor your software to the OS

<!-- USEFUL FOR REPRODUCABILITY -->

- because everything required for a container to start running whatever software it contains is defined in the image, containers can be set up programmatically
- that means there's no need for someone to configure them manually and no room for human error to be introduced
-

<!-- USEFUL FOR SCALABILITY -->

- Standardized development environment across many workstations
- Consistent deployment of applications
  - no human errors
- Full reproducibility (e.g. for research)

- because everything is defined in code, and the image contains everything required for the software to run, containerised applications are very easy to scale simply by adding more containers

- as a result many of the worlds largest software systems are containerised
- and they work at scale simply by adding more instances to do more of the same compute in parallel
- you might have hundreds of instances running the same image, with the workload balanced between them
- that application might be an API, or a data processing system, or a machine learning platform used within a company

- these days, docker is used pretty much everywhere
- and it's an absolute essential tool for any software engineer to be familiar with
