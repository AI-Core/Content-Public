- there's an even more flexible and easier to write version of JSON called YAML

_show simple YAML next to JSON_

- these files contain the same data

- YAML is easier to write than JSON because you don't need to include brackets, commas or quotes
- instead it's based on indentation
- but that can also make it harder to get right

- yaml files have a .yaml extension or sometimes just .yml without the "a"

- YAML is a funny name which stands for YAML ain't markup language
- which I assume someone thought was hilarious at the time, and now i have to try to explain that to people
- that's right, the Y in YAML stands for YAML
- which makes it a recursive acronym

- but the acronym isnt important
- what you need to know is that it's basically like JSON

- in fact, any valid JSON is also valid YAML
- that's because YAML is a superset of JSON
- it can do everything that JSON can do, but also gives you the flexibility to leave out brackets and other things

- there are a few things that I often see people get very confused with when writing YAML
- one of them is writing lists
- the key thing to remember is that in YAML, every list item starts with a dash

_type out equivalent YAML_

- by far the thing that people find most challenging with YAML is writing lists of dictionaries
- take a second to think about how you'd do that
- let me show you how people commonly get it wrong

_show every key in each dictionary as a list item and explain_

_show no list items and explain that this is just a dictionary with dup keys_

- again, just remember that each dash indicates a new list item

_show correct YAML_

<!-- OUTRO -->

- most people find YAML confusing to start with, but they learn to love it
- I love it, and I think you're gonna love it too once you get the practice in
