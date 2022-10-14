import ntpath
import os.path
from typing import Any
from canvas import *
import random


class Config:
    default = {
        "images": [],
        "isHorizontal": True,
        "name": "gen",
        "folder": ".",
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
        self.isHorizontal: bool = True
        self.name: str = "gen"
        self.folder: str = "."
        self.canvas: tuple[int, int] = (1, 1)
        self.unit: tuple[int, int] = (32, 32)

    @property
    def output_path(self) -> str:
        return ntpath.join(self.folder, f"{self.name}.g.png")

    @staticmethod
    def by(folder: str, name: str, content: dict[str, Any]) -> "Config":
        r = Config()
        r.name = name
        r.folder = folder
        r.images = content["images"]
        for i, img in r.images:
            if not os.path.isabs(img):
                r.images[i] = ntpath.join(folder, img)
        r.size = (int(content["width"]), int(content["height"]))
        r.isHorizontal = content["isHorizontal"]
        return r


def load_all(path: list[str]) -> list[Img]:
    res = []
    for p in path:
        with Image.open(p) as img:
            img.load()
            res.append(img)
    return res


def start(config: Config):
    cv = Canvas(config.unit)
    imgs = load_all(config.images)
    width, height = config.canvas
    for x in range(width):
        for y in range(height):
            cv.add(random.choice(imgs))
        cv.row()
    composed = cv.output()
    composed.save(config.output_path)
