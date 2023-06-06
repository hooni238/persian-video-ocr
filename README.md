# persian-video-ocr
Persian video ocr is a python code that performs OCR on video frames. 

# OCR Video Frames with Tesseract

This code reads frames from a video file, performs OCR on each frame using Tesseract, and writes the output to a text file.

## Installation

To run this code, you will need to have the following libraries installed:

- cv2
- pytesseract

You can install these libraries using pip:
<pre>
'''
$ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config

$ pip install opencv-python pytesseract
'''
</pre>
Also, you need to install Persian Tesseract-OCR:
$ sudo apt-get install tesseract-ocr-fas


You can find more about TesserOCR from the [TesserOCR repository](https://pypi.org/project/tesserocr/). You can find other languages from [here](https://github.com/tesseract-ocr/tessdoc/blob/main/Data-Files.md).

## Usage

To use this code, run the following command:

$ python ocr_video_frames.py --input MyVideo_1.mp4 
The `--input` parameter specifies the path to the input video file.
The output.txt contain the extracted text.

## Contributing

If you find a bug or have a feature request, please [open an issue](https://github.com/hooni238/persian-video-ocr/issues).


