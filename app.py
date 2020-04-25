from flask import Flask,render_template, url_for, request , redirect
import os
from flask_bootstrap import Bootstrap
import inference
app = Flask(__name__)
Bootstrap(app)
"""
Routes
"""
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = inference.get_prediction(image_path)
            print('class name =', class_name)
    return render_template('index.html')
if __name__ == '__main__' :
    app.run(debug = True)
