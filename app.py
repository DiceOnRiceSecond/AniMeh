from flask import Flask, render_template, request
from scraper import scrape_anime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    anime_list = []
    if request.method == "POST":
        query = request.form.get("query")
        anime_list = scrape_anime(query)
    return render_template("index.html", anime_list=anime_list)

# Only needed for local testing
# if __name__ == "__main__":
#     app.run()
git init
git add .
git commit -m "first deploy"
git branch -M main
git remote add origin https://github.com/DiceOnRiceSecond/AniMeh.git
git push -u origin main
