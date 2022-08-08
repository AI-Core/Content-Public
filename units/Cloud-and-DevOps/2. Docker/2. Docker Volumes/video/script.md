<!-- MOTIVATION -->

- when a Docker container finishes doing its job, it exits
- and with that, all of the data inside that container disappears

- If a docker container fails for some reason, such as the host machine running out of memory and crashing, then you will lose all of your data

- Docker containers are supposed to be stateless

totally isolated, but often you have containers which

- because of this, it sometimes makes sense to store data outside of the container itself

- in another case, you would want data to be shared across containers
- for example, if you have a container that runs a database, you could scale it up horizontally by adding more containers, which all connect to the same storage

- in cases like this, you could use Docker volumes

<!-- WHAT ARE VOLUMES? -->

- Docker volumes are persistent storage shared between the host machine and the docker containers
- they allow you to attach external storage to a container, and potentially to share the same storage across many containers
- the data in a docker volume persists outside of the container lifecycle
- so if, for example, you had a data collection system which ran in a container once per week, you could create a docker volume to store the files it saves, and they would still be there the next week, even though the container is stopping and starting and any data inside is lost

- Docker volumes are created by docker, either using the command line, or when you specify a new one to attach to a container
- a Docker volume is a lot like any other folder on your machine
- in fact, you can find the contents of a volume in your filesystem if you really look for it
- but their contents are intended to only be manipulated by Docker processes
- so they aren't stored in the most accessible place

- as is inevitably the case, I can't teach you everything, so it's important you know how to use the docs
- let's practice using them to look up how to work with docker volumes

_search create docker volume_

<!-- CREATE VOLUME -->

- you can see that to create a docker volume, you simply run `docker volume create` followed by the name of your volume

_create volume with `docker volume create myvolume`_

- and then the docs show that I can attach a volume to a container when I run it like this
- the argument to the `-v` flag, for volume, is a mapping between the volume name

_highlight volume name in docs_

- and the path inside the container which this will be mapped to

_highlight path in docs_

- we can also look up the main docker volumes ref to see all the details

- it shows a bunch of stuff
- including that you can attach a volume to a container when you run it using the `--volume` or `--mount` flag as well as the `-v` flag, which all do roughly the same thing

<!-- LIST VOLUMES -->

- we can list our volumes with `docker volume list`

<!-- INSPECT A VOLUME -->

- you can see the details of a volume by running docker inspect

\_run `docker volume inspect myvolume`

<!-- DELETE A VOLUME -->

- looking at the docs, we can see how to delete a volume once we're done with it

_look up "delete docker volume" and show docs_

_run `docker volume delete myvolume`_

<!-- BIND MOUNTS -->

- although its not recommended to mount filepaths which are not docker volumes to a container, you can do it
- we call that a bind mount
- and it's done in exactly the same way
- just specify an absolute filepath rather than a volume name

- because the filepath needs to be absolute, a handy trick here is to use the `PWD` environment variable

_run `echo $PWD`_

- ...which evaluates to my current directory...

- ...in the absolute filepath

_type out `docker run -v $PWD/my_bind_mound_path:path_in_container`_

- a common mistake is trying to use a relative path
- unless the argument is an absolute path docker assumes that you're referring to the name of a volume
- and if that doesn't exist, then it creates the a volume with that name

- so if I run this...

_run `docker run -v my_bind_mound_path:path_in_container`_

- ...then that container isn't actually mapping the directory next to me to the location inside
- instead, it's created a blank volume with that name

_list volumes and highlight_

- a good use case of a bind mount is when you want to make changes to a file which a container uses, and see the effect, without having to stop and start the container over and over between each change
- whenever the container looks for the file, it looks for it in the mounted location, and uses whatever is there

<!-- BIND MOUNT VS VOLUMES -->

- so why would you use a docker volume over a bind mount?

- bind mounts are dependent on the host OS. If you run the same command on another machine, it might not have that same filesystem location to mount to
- this would mean that the docker container is not totally independent and self-contained
- and as such, it would not be portable

- volumes also have other advantages and features over bind mounts
- they can be pre-populated by a container as they are created
- they can easily be encrypted
- they can easily be stored on a cloud storage service like S3
- and they are also more performant
- aside from that, they work in nearly the exact same way
