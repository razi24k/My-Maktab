def writer(address):
    def decorator(func):
        def inner(*args, **kwargs):
            file = open(address, "w")
            file.write(func(*args, **kwargs))
            file.close()
        return inner
    return decorator


@writer("address.txt")
def process():
    return "Hello World!"
