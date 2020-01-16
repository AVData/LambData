import string
import numpy as np


def increment(x):
    return(x + 1)


def string_punctuation(text):
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)
