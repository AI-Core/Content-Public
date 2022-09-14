- fitting an sklearn machine learning model takes time and compute
- so once you've done the fitting, you want to be able to save it, so that you can load it in again later

- to do that you can use python's `joblib` libarary, which is installed when you install sklearn , but is not part of sklearn

`import joblib`

`joblib.dump(model, fp)`

`model = joblib.load(fp)`

- and if i didn't know how to do this, I'd just check the docs

_Show the docs_

- the docs also explain that you can use `pickle` alternatively to `joblib`
- but that `joblib` is optimised to save objects containing large numpy arrays

- to pickle to model, call `pickle.dumps` to serialise the model
- that is, encode it as a string
- then you can save this file, typically as a `.pickle` file

# when this won't work

- when you use either of these methods to load a model in somewhere else, you need to make sure you have the same dependencies installed
- and often, that means the exact same version
- so if you're going to load in a model somewhere else, make sure you export the exact names and versions of dependencies, and load them in before you try to unpickle something that need them

_Switch to conda env `joblib-only` and try to run `another_file.py`_

- but if you have all of those dependencies, then things should be fine

<!--
TODO move to lesson on deserialisation
# security
- you should also remember to be careful about deserialising data from untrusted sources, as when you do, they can execute code that might be malicious -->

# outro

- but that's
