- fastAPI is a popular python library that can be used for creating APIs
- with fastAPI, creating an API can be as simple as this

_Switch to screen capture_

- I've imported fastAPI, created an instance of the API, and then defined a handler function, which gets called when a GET request is made to the path specified in the decorator

_Hover over code_

- so how do you run this API so that it can recieve requests?

- well, to run it we need a web server that will listen for requests made to your computer, pass them to fastAPI, and then return a response

- the fastAPI docs recommend using uvicorn as your web server

- install it using pip

_`pip install uvicorn`_

- you can then use the uvicorn CLI which has been installed to run the API from the terminal

_Run the API by running `uvicorn example:api`_

- the command expects the name of the file and the name of the instance within the file separated by a colon as the first argument

- if I run this file from the terminal, it starts running the API locally

_stop the API, add a `--reload` flag, and run it again_

- the reload flag enables hot-reloading, where the behaviour of the API is reflected when you change the source files, without having to restart the API

- by default it listens for requests on port 8000

_Point to the port number in the endpoint shown in the terminal_

- you can alternatively run the API from within the python file
- just import uvicorn and call its `run` method

_Add uvicorn.run(api, port=8000, host='127.0.0.1') to the code within an if name == main block_

- and as you'd expect, if I make a get request to the root path, which I defined the method for, then I receive the response returned from the corresponding handler defined in my script

_Run request.py file to send request to the API and print the response_

_Hover over response received by request in console where printed_

- and as you can see there the request was logged by the API

_Hover over response in API terminal_

- fastAPI has many different decorators that can be used to define what happens to any of the different HTTP methods

_Change the decorator to a post request and then to a delete_

# TODO lesson on the HTTP methods

- and you can define many different handlers for different paths in the same way

_Create a get method for user, put method for user/basket, delete method for user/basket_

- you should note that you can't overwrite a handler method because fastAPI looks through the defined handlers in order and runs the first handler it sees which matches

- using this, you can create production ready APIs to respond to requests from any possible use case with FastAPI
