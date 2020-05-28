from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from predict_api import make_prediction, decode_prediction, load_ml_model
from lesion_dict import get_lesion_info
import os

# Setup Variables
wk_dir = os.path.dirname(__name__)
UPLOAD_FOLDER = os.path.join(wk_dir, 'uploads/')
ALLOWED_EXTENSIONS = {'png', 'tiff', 'jpg'}
file_list = []

# Define Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Model
model = load_ml_model(wk_dir)


# Function to check if filename is acceptable
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():

    # Set Default Upload Image
    placeholder_image = os.path.join(app.config['UPLOAD_FOLDER'], 'upload.png')
    lesion_description = ['Upload an image to get description', 'https://www.healthline.com/symptom/skin-lesion']

    # If Post Request
    if request.method == 'POST':
        file = request.files["image"]

        # If File has no filename
        if file.filename == '':
            return render_template('index.html', message='File has no name, select file with name.', full_filename=placeholder_image, lesion_description=lesion_description)

        # If File has filename and is of accepted type
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('static', app.config['UPLOAD_FOLDER'], filename))
            image_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_source = os.path.join('static', app.config['UPLOAD_FOLDER'], filename)

            # Append to file_list
            file_list.append(image_location)

            # Make Prediction
            pred = make_prediction(image_source, model=model, main_dir=wk_dir, model_loaded=True)

            # Decode Prediction
            decoded = decode_prediction(pred)

            # Get Lesion Description
            lesion_description = get_lesion_info(decoded[0])

            # Return Result
            return render_template('index.html', message=decoded, full_filename=image_location, lesion_description=lesion_description)

    else:
        # Return Default
        return render_template('index.html', message=['Upload an image.', 'NO UPLOAD'], full_filename=placeholder_image, lesion_description=lesion_description)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
