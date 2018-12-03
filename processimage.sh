#!/bin/bash

python image_helper/ImageProcessorCLI.py --help

echo "What Image processing operation you want?"
read command

case "$command" in

    capture_screen)
         echo "Enter file path"
         read file_path
         python image_helper/ImageProcessorCLI.py $command $file_path
         ;;
    *)
        python image_helper/ImageProcessorCLI.py --help
        ;;
esac