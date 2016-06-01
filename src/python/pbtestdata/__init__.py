from .core import VERSION

def get_version():
    return ".".join([str(n) for n in VERSION])
