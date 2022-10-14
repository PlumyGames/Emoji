from PIL import Image
from PIL.Image import Image as Img
import numpy as np
from numpy import ndarray

import utils

ImageArray2D = list[list[Img]]


# noinspection SpellCheckingInspection
class Canvas:
    """
    A canvas that holds a 2D-array of images.
    """

    def __init__(self, unit: tuple[int, int]):
        self.rows: ImageArray2D = []
        self.unit = unit
        self._rowi = 0

    def add(self, img: Img) -> bool:
        """
        add an image to current row
        :param img: the image to add, which match the unit
        :return: whether the image was added
        """
        if img.size == self.unit:
            row = self.get_cur_row()
            row.append(img)
            return True
        else:
            return False

    def get_cur_row(self) -> list[Img]:
        if len(self.rows) == 0:
            cur = []
            self.rows.append(cur)
            return cur
        else:
            return self.rows[self.rowi]

    def clean_empty(self):
        size = len(self.rows)
        if size > 0:
            last = self.rows[size - 1]
            if len(last) == 0:
                self.rows.pop()

    @property
    def rowi(self) -> int:
        return self._rowi

    def row(self):
        self._rowi += 1
        self.rows.append([])

    @property
    def max_colmun(self) -> int:
        cur = 0
        for row in self.rows:
            cur = max(cur, len(row))
        return cur

    @property
    def max_row(self) -> int:
        return len(self.rows)

    def view(self, is_horizontal: bool = True) -> ndarray:
        self.clean_empty()
        max_row = self.max_row
        max_colmun = self.max_colmun
        size = (max_row, max_colmun)
        res = np.full(shape=size, fill_value=None)
        for x in range(max_colmun):
            for y in range(max_row):
                e = utils.get_2d(self.rows, y, x, fallback=None)
                res[y, x] = e
        if is_horizontal:
            res = np.transpose(res)
        return res

    def output(self, *, is_horizontal: bool = True, mode="RGBA") -> Img:
        view = self.view(is_horizontal)
        row, column = view.shape
        ux, uy = self.unit
        size = (row * ux, column * uy)
        img = Image.new(mode, size)
        for x in range(row):
            for y in range(column):
                e: Img | None = view[x, y]
                if e is not None:
                    img.paste(e, box=(x * ux, y * uy))
        return img
