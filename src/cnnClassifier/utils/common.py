import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Loaded yaml file {path_to_yaml}')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file could not be read')
    except Exception as e:
        return e



def create_dirs(path_to_dirs: List[str], verbose: bool = True):
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'created directory {path}')


@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    with open(path_to_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f'saved json file {path_to_json}')


@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    with open(path_to_json) as json_file:
        content = ConfigBox(json.load(json_file))
    logger.info(f'loaded json file {path_to_json}')
    return content


@ensure_annotations
def save_bin(path_to_bin: Path, data: Any):
    with open(path_to_bin, 'w') as binary_file:
        joblib.dump(data, binary_file)

    logger.info(f'binary file saved at {path_to_bin}')


@ensure_annotations
def load_bin(path_to_bin: Path) -> Any:
    with open(path_to_bin, 'rb') as binary_file:
        data = joblib.load(binary_file)
    logger.info(f'loaded binary file {path_to_bin}')
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kbytes = round(os.path.getsize(path) / 1024)
    return f'~ {size_in_kbytes} KB'


def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encode_image_in_base64(cropped_image_path):
    with open(cropped_image_path, 'rb') as f:
        return base64.b64encode(f.read())
