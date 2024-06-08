from PIL import Image, ImageDraw
import numpy as np


def create_dot_mosaic(image_path, dot_size=10, background="white", output_path='dot_mosaic.png'):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_width, img_height = img.size

    # Create a new image for the mosaic dot output
    mosaic_img = Image.new('RGB', (img_width, img_height), background)
    draw = ImageDraw.Draw(mosaic_img)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Loop through the image pixels with a step size of dot_size
    for y in range(0, img_height, dot_size):
        for x in range(0, img_width, dot_size):
            # Get the color of the current block
            block = img_array[y:y + dot_size, x:x + dot_size]
            avg_color = block.mean(axis=(0, 1)).astype(int)

            # Draw a circle with the average color of the block
            bbox = [x, y, x + dot_size, y + dot_size]
            draw.ellipse(bbox, fill=tuple(avg_color))

    # Save the output image
    mosaic_img.save(output_path)


create_dot_mosaic('input/1.jpg', dot_size=10, background="black", output_path='output/1.png')
create_dot_mosaic('input/2.jpg', dot_size=11, output_path='output/2.png')
create_dot_mosaic('input/3.jpg', dot_size=12, output_path='output/3.png')
create_dot_mosaic('input/4.jpg', dot_size=13, output_path='output/4.png')
create_dot_mosaic('input/5.jpg', dot_size=14, output_path='output/5.png')