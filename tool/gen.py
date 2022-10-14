import ntpath
import os.path
from typing import Any
from canvas import *
import random


class Config:
    default = {
        "images": [],
        "rotated": False,
        "name": "gen",
        "imgFolder": ".",
        "canvas": {
            "width": 1,
            "height": 1,
        },
        "unit": {
            "width": 32,
            "height": 32,
        }
    }

    def __init__(self):
        self.images: list[str] = []
        self.rotated: bool = False
        self.name: str = "gen"
        self.configFolder: str = "."
        self.imgFolder: str = "."
        self.canvas: tuple[int, int] = (1, 1)
        self.unit: tuple[int, int] = (32, 32)

    @property
    def output_path(self) -> str:
        return ntpath.join(self.configFolder, f"{self.name}.g.png")

    @staticmethod
    def by(folder: str, name: str, content: dict[str, Any]) -> "Config":
        r = Config()
        r.name = name
        r.configFolder = folder
        r.imgFolder = content["imgFolder"]
        r.images = content["images"]
        for i, img in enumerate(r.images):
            if not os.path.isabs(img):
                r.images[i] = ntpath.join(r.imgFolder, img)
        canvas = content["canvas"]
        r.canvas = (int(canvas["width"]), int(canvas["height"]))
        unit = content["unit"]
        r.unit = (int(unit["width"]), int(unit["height"]))
        r.rotated = content["rotated"]
        return r


def load_all(path: list[str]) -> list[Img]:
    res = []
    for p in path:
        with Image.open(p) as img:
            img.load()
            res.append(img)
    return res


def random_select(li, last):
    if len(li) == 0:
        return None
    elif len(li) == 1:
        return li[0]
    else:
        while True:
            choice = random.choice(li)
            if last is not choice:
                return choice


def start(config: Config):
    cv = Canvas(config.unit)
    imgs = load_all(config.images)
    width, height = config.canvas
    last_choice = None
    for x in range(width):
        for y in range(height):
            choice = random_select(imgs, last_choice)
            last_choice = choice
            cv.add(choice)
        cv.row()
    composed = cv.output(rotated=config.rotated)
    composed.save(config.output_path)
