- if you think about the kinds of products that you use every day, you'll come up with loads of examples of where you would need to be able to send data to the API, and to get data from it, often as a response

<!-- QUERY STRING PARAMETERS -->

- you can pass parameters to your API endpoints by specifying them as arguments in the handler

_Define category as an argument in the handler_

- by default, these will be expected as query string parameters
- that means you would expect to pass them as key value pairs in the request endpoint, like so

_Add the category=camera query string to the endpoint requested and send a request_

- we wouldn't be making use of fastAPI's key features like type hinting, type casting, or useful error messages if we didn't tell it what types to expect though
- so let me add the types in there

_Add type `: str` to argument_

- notice that i'm using pythons colon syntax to specify the type here, i'm not using an equal sign to define the default argument, and

- if I pass in a datatype other than what's specified, then fastAPI generates a useful error message like this

_Send float to request body_

<!-- PATH PARAMETERS -->

- but you can also specify them as path parameters, where the variable is actually part of the path, by including their name in braces within the path, like this

_Add a new handler for /products/{product_id} as a path parameter_

- again we should include the type
- if fastAPI finds a match between the name of a something between braces in the path, and an argument name of the handler, then it will assume that variable will be found in the path rather than as a query string parameter

_Switch to screen capture and define a new handler that gets a product of a specific id based on the id being specificed in the path_

- so I could implement an endpoint that gets me a specific product based on the product id which is part of the path which I make the request to

<!-- DEFAULT VALUES -->

- you can assign default values for any of these parameters in the usual way

_Add min_price query string parameter with default value 0 to the `get_products` method_

- remember that when you type function arguments in python it's best to leave a space on either side of the equal sign, but when you don't type your variables, it makes your code clearer without the spaces

<!-- OPTIONAL VALUES -->

- the recommended way to specify optional arguments is by setting their default to `None` and allowing their type to also be none

\_Add default value category=None to the get_products function and put the category filter inside an `if category` statement, otherwise, return `product_data`

- to specify that the type can be one of multiple options, import the union class from the typing library, then follow it with a list of the different possible types

- so in our case, the category can either be a string or `None`

<!-- REQUEST BODY PARAMETERS -->

- the other, more common way that you can pass data to an API endpoint is by passing it in as the request body
- in the request call, that might look like this

_create a dictionary of {"address": "1 Melgrove Lane", "preferred_name": "Harry"} and add it to the requests.post method call as the keyword body arg_

- FastAPI will look for that data in the request body if the type of an argument is specified as a class which inherits from the pydantic BaseModel class, like this

_define class which inherits from the basclass_

- and if you didn't know, this syntax is just the same as defining the attributes for any instance of this class in the initialiser

- if it's not sent with the request, then you'll get an error like this

_Remove data from request body_

- you can see the helpful error message provided by fastAPI

<!-- RESPONSES -->

- that's how you get data
