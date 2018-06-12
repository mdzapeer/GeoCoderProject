#import flask 
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads
from werkzeug import secure_filename

#web app
app=Flask(__name__)
app.config['UPLOADED_FILECSV_DEST']="../uploaded"
#intiazlize flaskuploads class
fileuploaded=UploadSet('filecsv', ('csv',))
configure_uploads(app,(fileuploaded,))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    if request.method=='POST':
        file=request.files["file"]
        fileuploaded.save(file)
        return render_template("index.html")
    

# @app.route ("/temp_down")
# def template_down():
#     return render_template("index.html")

# @app.route("/download")
# def download():
#     return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()


