# 30 seconds on each data type

- Under the hood, all data is stored in bytes, in binary format
- but you should know about some of the key types of data that you can find

## Tabular data

- tabular data, is spreadsheet-like data which can be put into rows and columns
- it can be represented in many different formats, like CSV, JSON, YAML to name a few of the most common
- it's a form of structured data, because you always know the meaning of the information you can expect in each column

<!-- ## Tree-like data
- tabular data can't really be nested, so  -->

## Text data

- Text data is another abundant form of data
- most of the information available on the internet is text
- and again it can come in a variety of formats like txt files or PDFs
- it's a form of unstructured data, because you don't know the meaning of the information which any particular part of the text contains in advance

## Image data

- images can also be stored in many different formats, like jpeg or png
- structurally, most images are represented by a grid of numbers for each color channel that represents the intensity of that color in that location
- we call each of those grids, a channel, or a color channel in this case
- it's a form of unstructured data, because you don't know the meaning of the information which any particular pixel contains

## More complex data

- the idea behind how images are stored can easily be extended to how more complicated data is stored
- for example, imagine you have a satellite which is receiving the intensity of x-rays, UV rays, visible light, gamma rays and others
- the values for each of those would be stored in a different channel, which again would represent their intensity in different spatial locations
- so essentially you'd have something like image data, just with more channels

## Video data

- video data is much like image data, but there is another dimension, time, and you essentially have images for each frame in time
- it's another form of unstructured data

- videos are essentially images recorded over a timeline
- so much like images, you could easily extend video data to more complex data that has many more channels, just by storing those many channel datapoints over time

## Outro

- there are so many more data types which I haven't even mentioned
- but this should set you up to understand the most common of them
