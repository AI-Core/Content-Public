from atexit import register


@register
def hello():
    print('hello world')
