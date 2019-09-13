from flask import Flask
from flask import render_template, request
from datetime import datetime
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp/'


@app.route('/')
def homepage():
    return """
    <html>
    <body>
      <form action = "/uploader" method = "POST" 
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
      mypath = os.getcwd()+'/tmp/'
      if not os.path.isdir(mypath):
           os.mkdir(mypath)
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
      if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], f.filename)):
         return 'file uploaded successfully'
      else:
          return 'file upload fail'    


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

