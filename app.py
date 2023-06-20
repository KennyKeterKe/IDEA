from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

# imports necessary modules and classes from Flask and other libraries.

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

# An instance of the Flask class is created, representing the web application.
# The secret key and upload folder path are configured in the app's configuration.

# Create a form for uploading files
class UploadFileForm(FlaskForm):
    file = FileField("File")  # Field for file upload
    submit = SubmitField("Upload File")  # Submit button

    # The UploadFileForm class is defined as a subclass of FlaskForm. 
    # It represents a form for uploading files and contains a FileField for file selection and a SubmitField for form submission.

# Define the home route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()  # Instantiate the upload form

    # If the form is submitted and validated
    if form.validate_on_submit():
        file = form.file.data

        # Save the picture file
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               app.config['UPLOAD_FOLDER'], filename))

        return render_template('uploaded.html', picture=filename)

    return render_template('index.html', form=form)

# Two routes are defined for the home page, with support for both GET and POST requests. 
# The home function is associated with these routes, which renders the index.html template and instantiates the UploadFileForm.

# Route for certifying a picture
@app.route('/certify', methods=['POST'])
def certify_picture():
    picture = request.form.get('picture')
    return "Picture has been certified."

# Route for marking a picture as not certified
@app.route('/not_certify', methods=['POST'])
def not_certify_picture():
    picture = request.form.get('picture')
    return "Picture has been marked as not certified."

# There are two additional routes: /certify and /not_certify, both accepting POST requests. 
# These routes handle the certification and non-certification of a picture, respectively. 

if __name__ == '__main__':
    app.run(debug=True)

    # Finally, the app is run in debug mode when the script is executed directly.


