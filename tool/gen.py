from typing import Any
from canvas import *


class Config:
    default = {
        "images": [],
        "random": True,
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
        self.random: bool = True
        self.isHorizontal: bool = True
        self.name: str = "gen"
        self.folder: str = "."
        self.canvas: tuple[int, int] = (1, 1)
        self.unit: tuple[int, int] = (32, 32)

    @staticmethod
    def by(folder: str, filename: str, content: dict[str, Any]) -> "Config":
        r = Config()
        r.name = filename
        r.folder = folder
        r.images = content["images"]
        r.random = content["random"]
        r.size = (int(content["width"]), int(content["height"]))
        r.isHorizontal = content["isHorizontal"]
        return r


def gen(config: Config):
    Canvas()
