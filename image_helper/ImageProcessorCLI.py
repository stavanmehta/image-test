#!/usr/local/bin/python

import click

from ImageProcessor import ImageProcessor


@click.group()
def main():
    """
    Simple CLI for Image processing
    """
    pass

@main.command()
@click.argument('file_path')
def capture_screen(file_path):
    imgp = ImageProcessor(file_path)
    screen = imgp.capture_screen()

    click.echo("Image '{0}' has been captured".format(screen))

if __name__ == "__main__":
    main()

