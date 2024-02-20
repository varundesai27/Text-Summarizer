import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Read a yaml file and return a ConfigBox object

    Args: path_to_yaml(str): Path like input

    Raises: ValueError: if the file is empty

    Returns: ConfigBox
    """
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def cretae_directories(path_to_directories:list, verbose=True):
    """
    Create a list of directories

    Args: path_to_directories(list): list of directories to be created

    Returns: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path)->str:
    """
    Get the size of a file

    Args: path(str): Path like input

    Returns: str
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"