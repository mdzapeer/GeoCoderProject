#import flask 
from flask import Flask, render_template, request, send_file
from flask_uploads import UploadSet, configure_uploads, UploadNotAllowed
from backgeocoder import geocoder

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
            filename=fileuploaded.save(file) #save file as per saved config parameters above
            coded=geocoder(filename)
            coded.to_csv("coded\yourCSV.csv")
        except UploadNotAllowed:
            return render_template("index.html", message="Please upload a valid .csv file")                        
        return render_template("index.html", message="Upload successful", data=coded.to_html(), btn="download.html")
    else:
        return render_template("index.html", message="No file selected")  

@app.route ("/template_down")
def template_down():
    return send_file("samples\sample template.csv", as_attachment=True)

@app.route("/download")
def download():
    return send_file("coded\yourCSV.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    app.run()

