- here, I've got a training loop set up
- and when I run it, my loss should be going down, in general
- but it's hard to tell that just by looking at the numbers
- and that makes it hard to debug
- i'd like to be able to see a graph showing the loss curve
- I could use any python graphing library like plotly for this, but there's something even better, something that's designed for monitoring machine learning experiments
- it's called tensorboard
- it was originally developed for use with tensorflow, another deep learning framework, but now you can use it in pytorch too

_Open tensorboard website homepage_

- it can be used to visualise all kind of things that you'd typically be interested in whilst training AI models, as you can see here

_Switch to webcam_

- the most common use case is visualising loss curves during model training

_Switch to code_

- to get started you need to import the "SummaryWriter" class from torch.utils.tensorboard

- then you can initialise this class
- it takes an optional parameter for a path to a folder where all of the logging data will be stored for this instance of the summary writer
- by default, each run is stored in a separate folder within a directory called runs, which will be created in the same location you run the code
- in VSCode, when you import tensorboard, you'll be prompted to start a tensorboard session, which will open the tensorboard dashboard in vscode

_Open browser window_

- if you were using another editor, then you could open up this window using the tensorboard command line tool, and visiting a particular local port on your browser
- to populate this dashboard with data, we need to add tracking to our code
- the instance of the summary writer has methods to do this which you can see prompted after the dot operator, or in the online documentation
- the simplest type of data you can add is scalar data
- that's just a number
- to do that you can use the add_scalar method
- it takes in three arguments
- the first is the tag for this data
- i'll tag it as the loss

_Set `'train'` as the first argument_

- the second is the value of the scalar, essentially the y axis value

_Set `loss.item()` as the second argument_

- the third is the global step, essentiall the x axis value

_Set `batch` as the third argument_

- for the x position, we could use the batch index
- but the problem with that is that the batch index resets every epoch
- a simple workaround is to initialise a batch index at the start of the training

_Set `batch_idx` as the third argument_

_batch_idx = 0 before training loop starts_

- and then increment it after every batch

_batch_idx += 1 at end of each iteration_

- then if we run this, you can see that visualised in tensorboard

_Run code_

_toggle smoothing param_

- and if we smooth it
- we should be able to see more clearly, that yes, it's going down!

- if we run this again, we should be able to see a new set of data

- and even just knowing these basics about tensorboard can be immensely helpful in running experiments and training models
