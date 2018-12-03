import  os
from PIL import Image, ImageGrab


class ImageProcessor(object):

    def __init__(self, path):
        self.path = path

    def capture_screen(self):
        img = ImageGrab.grab()
        file_name = "screenshot.png"
        FILE_PATH = os.path.join(self.path, file_name)
        img.save(FILE_PATH)
        return file_name


    def open_image(self, image_name):
        image_location = "{path}{file_name}".format(path=self.path, file_name=image_name)
        self.image = Image.open(image_location)

    def create_thumbnail(self, size):
        self.image.thumbnail(size)

    def save_image(self, outfile, image_format):
        self.image.save("{0}{1}".format(self.path, outfile), image_format)

    def get_image_format(self):
        return self.image.format

    def get_image_mode(self):
        return self.image.mode

    def get_image_size(self):
        return self.image.size

    def crop_image(self, sub_rectangle_box):
        self.image.crop(sub_rectangle_box)


if __name__ == '__main__':
    path = "../resources/images/"
    imgp = ImageProcessor(path)
    screen = imgp.capture_screen()
    imgp.open_image(screen)
    imgp.image.show()
