import pytest
import os, sys
from image_helper.ImageProcessor import ImageProcessor


def test_open_file():
    scout_jpg = ImageProcessor()
    scout_jpg.open_image("../resources/images/scout.jpg")
    assert scout_jpg.get_image_format() == "JPEG"
    assert scout_jpg.get_image_mode() == "RGB"
    assert scout_jpg.get_image_size() == (2400, 1350)

def test_open_non_image_file():
    scout_txt = ImageProcessor()
    with pytest.raises(IOError) as excinfo:
        scout_txt.open_image("../resources/images/scout.txt")
    assert 'cannot identify image file' in str(excinfo.value)


def test_convert_file_to_png():
    infile = "../resources/images/scout.jpg"
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    if infile != outfile:
        try:
            scout = ImageProcessor()
            scout.open_image(infile)
            scout.save_image(outfile, "png")
        except IOError:
            print("cannot convert", infile)
