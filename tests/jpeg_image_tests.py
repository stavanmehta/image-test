import pytest
import os, sys
from image_helper.ImageProcessor import ImageProcessor



@pytest.fixture(scope="module")
def image_processor():
    path = "resources/images/"
    return ImageProcessor(path)

def test_open_file(image_processor):
    image_processor.open_image("scout.jpg")
    assert image_processor.get_image_format() == "JPEG"
    assert image_processor.get_image_mode() == "RGB"
    assert image_processor.get_image_size() == (2400, 1350)

def test_open_non_image_file(image_processor):

    with pytest.raises(IOError) as excinfo:
        image_processor.open_image("scout.txt")
    assert 'cannot identify image file' in str(excinfo.value)


def test_convert_file_to_png(image_processor):
    file_name = "scout.jpg"
    infile = "{0}{1}".format(image_processor.path, file_name)
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    if infile != outfile:
        try:
            image_processor.open_image(file_name)
            image_processor.save_image(outfile, "png")
        except IOError:
            print("cannot convert", infile)


def test_screen_capture(image_processor):
    screen = image_processor.capture_screen()
    image_processor.open_image(screen)
    # image_processor.image.show()

def test_crop_image(image_processor):
    screen = image_processor.capture_screen()
    image_processor.open_image(screen)
    image_processor.create_thumbnail((20,20))
    thumbnail = "th_screenshot"
    image_processor.save_image(thumbnail, "PNG")
