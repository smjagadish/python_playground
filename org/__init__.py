from .wordprocessor import *
from .listprocessor import *


def combine():
    wordprocessor.display()
    listprocessor.display_list()


__all__ = ["wordprocessor", "listprocessor"]
