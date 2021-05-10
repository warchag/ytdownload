from pytube import YouTube
from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":  
        nameurl = request.form['nameurl']  
        yt = YouTube(nameurl)
        datas = yt.streams.all()
        return render_template("index.html",data=datas)

if __name__ == "__main__":
    app.run(debug=True)


#yt = YouTube("https://www.youtube.com/watch?v=_nPAZjYQwT8")
#datas = yt.streams.all()
#for data in datas:
#    print(f"fps={data.fps} and  res ={data.resolution} and type={data.mime_type} link={data.url}")
   