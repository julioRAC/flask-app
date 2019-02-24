from flask import Flask
from flask import render_template, request
from datetime import datetime
import os
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <html>
    <body>
      <form action = "http://localhost:5000/uploader" method = "POST" 
           enctype = "multipart/form-data">
           <input type = "file" name = "file" />
           <input type = "submit"/>
           </form>
         </body>
    </html>
    """

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      if os.path.isfile(f.filename):
         return 'file uploaded successfully'
      else:
          return 'file upload fail'    


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

