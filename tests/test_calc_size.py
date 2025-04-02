from src.resizer import calc_size
from PIL import Image


def fake_image(w: int, h: int):
    # create a simple in-memory image
    return Image.new("RGB", (w, h))


def test_keep_aspect_by_width():
    im = fake_image(4000, 2000)
    assert calc_size(im, width=1000, height=0) == (1000, 500)


def test_keep_aspect_by_height():
    im = fake_image(4000, 2000)
    assert calc_size(im, width=0, height=500) == (1000, 500)


def test_exact_size():
    im = fake_image(800, 600)
    assert calc_size(im, width=800, height=600) == (800, 600)

