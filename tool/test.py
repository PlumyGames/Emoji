import ntpath

from canvas import *

pic_header = "E:/Emoji/emoji"

pics = [
    "daze",
    "sad",
    "laugh",
    "smile"
]


def pic(name: str):
    return ntpath.join(pic_header, f"{name}.png")


def test():
    for i, name in enumerate(pics):
        pics[i] = pic(name)
    cv = Canvas(unit=(57, 57))
    for i, p in enumerate(pics):
        with Image.open(p) as img:
            img.load()
            if i == 3:
                cv.row()
            cv.add(img)
    cv.output().show()


if __name__ == '__main__':
    test()
