#import flask 
from flask import Flask, render_template, request, send_file
from flask_uploads import UploadSet, configure_uploads, UploadNotAllowed
import backgeocoder

#web app object
app=Flask(__name__)
#config for app object for uploadset, UPLOADED_XXXX_DEST uses fileuploaded object defined name below
app.config['UPLOADED_FILECSV_DEST']="uploaded"
#define uploadset object 'fileuploaded' and name as 'filecsv' and only accepting .csv extension files
fileuploaded=UploadSet('filecsv', ('csv',))
#apply configure_uploads method on flask app object and fileuploaded object to save the changes
configure_uploads(app,(fileuploaded,))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    if request.method=='POST':
        file=request.files["file"] #get the file from HTML page
        try:
            fileuploaded.save(file) #save file as per saved config parameters above
        except UploadNotAllowed:
            return render_template("index.html", message="Please upload a valid .csv file")
        filename=file            
        return render_template("index.html", message="Upload successful")

@app.route ("/template_down")
def template_down():
    return send_file("samples\sample template.csv", as_attachment=True)

# @app.route("/download")
# def download():
#     return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()


