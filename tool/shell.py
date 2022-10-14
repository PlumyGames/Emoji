import json
import ntpath

import gen
from gen import Config
from utils import read_fi


def start(config_path: str):
    parent, config_name = ntpath.split(config_path)
    name = config_name.removesuffix(".config.json")
    content = read_fi(config_path)
    config_map = json.loads(content)
    config = Config.by(parent, name, config_map)
    gen.start(config)
