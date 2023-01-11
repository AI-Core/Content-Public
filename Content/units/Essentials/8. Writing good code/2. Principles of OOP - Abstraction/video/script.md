<!-- TODO ANIMATED DEFINITION -->

- simply put, abstraction is the process of exposing to the user only what they need, and moving the specific the implementation under the hood
- let me show you what I mean

_Switch to screen capture_

- an essential way that you can achieve abstraction is by defining functions
- they abstract away the detail of the implementation and provide an easy to use function name
- this code is a mess
- I'm going to abstract away the specific implementation of the different sections into functions

_Show putting code into function body_

- now look at how much more easy it is to understand

- we're now only showing the user what they need, and those details of the implementation are packed up in the function
- this makes your code easier to understand and to use

- we can always look into that function if we want to see the details, but at a glance, we just see what we need

- now when you scan over this file to look at the code that's actually being run, and you see this function name, you know exactly what it's doing

- I actually think that pythons indentation syntax makes it remarkably easy to get an overview
- in most cases, the level of detail quite literally represents the level of detail you are going into
- if I want to get a high level overview of the code, I can just look at what's defined at the top level

- another way that you can achieve abstraction is by implementing classes
- again, they abstract away the detail of any setup that might need to happen during the initialisation or other internal code

_Compare code before and after being put into a class_

_Switch to webcam_

- you should use abstraction lavishly
- but it's not necessary to abstract everything up into a single line of code
- the real art is finding the right level of abstraction that makes it easy to understand but also easy to use and to extend

<!-- TODO TYPEWRITE finding the right level of abstraction that makes it easy to understand but also easy to use and to extend -->

- in practice, you want to use layers of abstraction
- let's take a look at that

_Switch to screen capture_

- in this cell, we've combined many different types of processing into a single function
- but if they each consist of several lines, it's going to be hard to tell what part of the function relates to what part of the processing
- abstracting everything into this one function will make it harder to use and to debug
- there might also be cases where we want to apply the different parts of the processing independently, especially if you want to define automatic tests to test that each of them work as expected on their own
- because of that, it makes sense to firstly abstract the code relating to each part of the processing into its own function, then to abstract all of those together into a single function that performs every step

_Highlight the body of the first individual part of the processing, then highlight the body of the combined function_

- once we've done this, it makes it easy for anyone to look at the code and understand what it does by firstly looking at the outermost level of indentation
- once we see what's happening there, we can zoom in to those parts specifically
- then if we want we can go even deeper by following what's happening in there

_Highlight function body of first processing function called_

_Switch to webcam_

- with the right level of abstraction, your code can be a lot better
