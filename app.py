# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
# import additional libraries below

app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # write the read and write function on image below 
    filedata=make_bw(file.read())
    with open(os.path.join('static/',filename),'wb') as f:
    	f.write(filedata)

        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


# Write the make_grayscale() function below
def make_bw(inimg):
	imgarray=np.fromstring(inimg,dtype='uint8')
	print('Image array: ',imgarray)
	simpleimg=cv2.imdecode(imgarray,cv2.IMREAD_UNCHANGED)
	bw=cv2.cvtColor(simpleimg,cv2.COLOR_RGB2GRAY)
	status,output=cv2.imencode('.png',bw)
	print('Satus: ',status)
	return output













# make_grayscale() function ends above

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


