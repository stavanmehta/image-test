from PIL import Image

class ImageProcessor(object):

    def __int__(self, image_file):
        print "ImageProcessor constructor"
        self.image = None

    def open_image(self, image_name):
        self.image = Image.open(image_name)

    def create_thumbnail(self, size):
        self.image.thumbnail(size)

    def save_image(self, outfile, image_format):
        self.image.save(outfile, image_format)

    def get_image_format(self):
        return self.image.format

    def get_image_mode(self):
        return self.image.mode

    def get_image_size(self):
        return self.image.size

    def crop_image(self, sub_rectangle_box):
        self.image.crop(sub_rectangle_box)
