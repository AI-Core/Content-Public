# Motivation

- using pandas is all about manipulating data
- so let's take a look at how to do that

# dataframes

- the key datatype in pandas, which you are going to have to get very familiar with, is the pandas dataframe

_pd.DataFrame_

- it basically represents a table, with rows and columns
- pandas can take in a range of data formats and turn them into a dataframe
- for example, a dictionary, where the values are the columns
- or a list of records
- or a list of lists
- pandas can usually figure out the incoming format and correclty create the dataframe

_show dataframe_

# Common dataframe attributes and behaviours

- len of a dataframe shows you the number of records it contains

_print(len(df))_

- but if you iterate through a dataframe, it's going to iterate through the column names

_iterate through column names_

- if you want to get all of the columns, you can use .columns

_print df.columns_

- to get a visualisation of part of your dataframe, use head to see the first rows
- or tail to see the last rows

- if you index a dataframe, pandas expects a column name, not a row index
- and when you index out a column, yuo get a list of the values in it
- but its data types isnt a list - it's actually a pandas series
- a series is much like a dataframe, but 1d instead of 2d
- so in this case, indexing out a column of my dataframe which has 2 dimensions, rows and columns, gave me a 1d series

# index column

- if you want to index a particular row of a dataframe, you need to understand what an index column of a dataframe is
- every dataframe has an index column
- the index is a unique value for each row that can be used to reference them and select them
- by default, it's a range of as many integers as there are records in the dataframe
- but you can set it to any other column too

# Indexing overview

- if you want to select a particular row, you can index the loc method with the value for that row in its index column
- if you want to select out a particular part of a dataframe by position rather than by it's unique id, then you can index it's iloc attribute
- pandas actually has the ability to do all kinds of fancy indexing, like selecting ranges of data, or just particular rows or columns where a condition is met, or even more complicated stuff
- that's worth going into more detail at another time

# adding rows and cols

## adding new column

## adding new row

# dropping rows and cols

- axis=1

# inplace

- one important thing to understand is that many dataframe methods are not inplace, instead, they return a new dataframe which has the change applied

# Useful methods

<!-- ## df.info

- df.info shows you some key things like the datatype and count of how many values are non-null

## df.describe

- df.describe shows you some summary statistics of -->

## highlight other methods in the pop0-up documentation

- if you want to find out what any of these mean in more detail, then the best thing to do is to check the docs
- let me show you how I'd do that now with a method that you're gonna use all of the time...
- the read_csv method

# Read data

_open read_csv in docs_

- used to read CSV files straight into pandas

- and this returns you a dataframe
- there are loads of other methods you can use to connect to all kinds of data sources too, from json files to directly to databases

_show other from methods in documentation dropdown_

# save data

- you can save data using the dataframe's "to" methods
- to_csv saves it to a csv file by name
- and you can use any of the other methods to save to other formats too

# Outro

- that's a whirlwind tour of data frames and some of their useful methods
