import os
import cv2
from flask import Flask, redirect, jsonify, request, url_for, render_template, flash

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "/Users/sai/Desktop/everything/Programming/mosaic/images/"
app.config["IMAGE_RESULTS"] = "/Users/sai/Desktop/everything/Programming/mosaic/results/"
img_path = "/static/images/"
res_path = "/static/results/"


@app.route("/")
def home():
    return render_template("upload_image.html")


# Route to upload image
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    mosaic_data = [0]
    image = request.files["image"]
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
    full_filename = img_path + image.filename
    img = cv2.imread('/Users/sai/Desktop/everything/Programming/mosaic/results/' + str(image.filename))
    mosaic = {'file_name': image.filename, 'file_name_1': full_filename,'img_height': img.shape[1]/1.2}
    mosaic_data[0] = mosaic
    return render_template("upload_image.html", mosaic_data=mosaic_data)


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_RESULTS"], filename)

@app.route('/full-screen', methods=['GET', 'POST'])
def download_image():
    mosaic_data=[0]
    mosaic = {'file_name': res_path + request.form.get("download")}
    mosaic_data[0] = mosaic
    return render_template("display_img.html", mosaic_data=mosaic_data)


@app.route('/go-back', methods=['GET', 'POST'])
def go_back():
    return render_template("upload_image.html")



if __name__ == "__main__":
    app.run()
