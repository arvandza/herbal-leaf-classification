import os
import tensorflow as tf
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
=======
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
>>>>>>> 962d838 (update)
import skimage
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

<<<<<<< HEAD
# Load model
cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "herbal_leaf_models_vgg16.h5")


=======
app.config['UPLOAD_FOLDER'] = './static/uploads/'

# Load model
cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "herbal_leaf_models_vgg16.h5")

>>>>>>> 962d838 (update)
# Preprocess an image
def classify(model,image):
    class_names = ['Belimbing Wuluh', 'Jambu Biji', 'Jeruk Nipis', 'Kemangi', 'Lidah Buaya', 'Nangka', 'Pandan', 'Pepaya', 'Seledri', 'Sirih']
    new_image = plt.imread(image)
    resize_img = skimage.transform.resize(new_image, (224,224,3))
    pred = model.predict(np.array([resize_img]))
    list_index = [0,1,2,3,4,5,6,7,8,9]
    x = pred
    labels = []
    classified = []
    for i in range(10):
        for j in range(10):
            if x[0][list_index[i]] > x[0][list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    
    for i in range(2):
        label = class_names[list_index[i]]
        labels.append(label)
        classified_prob = round(pred[0][list_index[i]] * 100,2)
        classified.append(classified_prob)
    return labels, classified

<<<<<<< HEAD

=======
>>>>>>> 962d838 (update)
# home page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dataset")
def dataset():
    return render_template("dataset.html")

@app.route("/about")
def about():
    return render_template("about.html")

<<<<<<< HEAD
@app.route("/classify", methods=["POST", "GET"])
def upload_file():

    if request.method == "GET":
        return render_template("home.html")
    else:
=======
@app.route("/classify", methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
>>>>>>> 962d838 (update)
        try:
            file = request.files["image"]
            upload_image_path = os.path.join(dir_path,'static','uploads', secure_filename(file.filename))
            print(upload_image_path)
            file.save(upload_image_path)
        except FileNotFoundError:
            return render_template("home.html")    
<<<<<<< HEAD
        label,prob = classify(cnn_model, upload_image_path)
        
=======
        label,prob = classify(cnn_model, upload_image_path) 
    else:
        return render_template("home.html")
>>>>>>> 962d838 (update)
    return render_template(
        "class.html", image_file_name=file.filename, label=label, prob=prob
    )

@app.route("/classify/<filename>")
def send_file(filename):
<<<<<<< HEAD
    return send_from_directory(UPLOAD_FOLDER, filename)
=======
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
>>>>>>> 962d838 (update)

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
    app.debug = True
