import os 
import yaml
from src.ai_or_human_text.logging import logger
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml,"r")as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file loaded sucessfully from {path_to_yaml}")
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e 
    
    return ConfigBox(content)


@ensure_annotations
def create_dir(file_path=list,verbose=True):
    for path in file_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"{path} created sucessfully")

@ensure_annotations
def get_size(file):
    size_in_kb=round(os.path.getsize(file)/1024)
    return f"file size:{size_in_kb} kb"