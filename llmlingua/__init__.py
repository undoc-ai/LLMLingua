"""

Module: __init__

Overview:
This module initializes the `PromptCompressor` class, which provides functionalities for compressing prompts to increase efficiency when using large language models. Additionally, it specifies the `__version__` of the package along with the list of all module contents accessible using `__all__`.

Classes:
- `PromptCompressor`: A class that defines methods for prompt compression and related utilities.

Variables:
- `__version__`: A string indicating the version of the package.
- `__all__`: A list of strings representing the names of all publicly accessible objects provided by the module.


Note: Documentation automatically generated by https://undoc.ai
"""
# flake8: noqa
from .prompt_compressor import PromptCompressor
from .version import VERSION as __version__


__all__ = ["PromptCompressor"]
