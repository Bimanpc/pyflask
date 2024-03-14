from flask import Flask, request, Blueprint, render_template;
app = Flask(__name__);
DEBUG=False;
#Registramos una nueva url
media_pt=Blueprint("media", __name__, static_folder="./media", static_url_path="/media");
app.register_blueprint(media_pt);

media_pt=Blueprint("static", __name__, static_folder="./static", static_url_path="/static");
app.register_blueprint(media_pt);

@app.route("/")
def index():
    return render_template("index.html");
@app.route("/ok")
def is_of():
    return "is okk";
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=DEBUG)
