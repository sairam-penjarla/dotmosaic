# DotMosaic

DotMosaic is a Python project that converts images into mosaic dot images. It uses the `Pillow` library for image processing and `numpy` for numerical operations.

## Features

- Converts any image into a mosaic dot image.
- Allows customization of dot size.
- Allows customization of background color.

## Requirements

- Python 3.x
- Pillow
- numpy

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/sairam-penjarla/dotmosaic.git
    cd dotmosaic
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your input images in the `input` directory.

2. Run the `dot_mosaic.py` script with your desired parameters:

    ```python
    create_dot_mosaic('input/1.jpg', dot_size=10, background="black", output_path='output/1.png')
    create_dot_mosaic('input/2.jpg', dot_size=11, output_path='output/2.png')
    create_dot_mosaic('input/3.jpg', dot_size=12, output_path='output/3.png')
    create_dot_mosaic('input/4.jpg', dot_size=13, output_path='output/4.png')
    create_dot_mosaic('input/5.jpg', dot_size=14, output_path='output/5.png')
    ```

3. The output mosaic images will be saved in the `output` directory.