from flask import Flask, render_template, url_for
from lockfile import LockFile

app = Flask(__name__)


@app.route("/")
def visitcount():
    lock = LockFile("visitors.txt")
    with lock:
        with open("visitors.txt", "r+") as f:
            fileContent = f.read()

            if fileContent == "":
                count = 1
            else:
                count = int(fileContent) + 1

            f.seek(0)
            f.write(str(count))
            f.truncate()
            return render_template("index.html", viewcount=str(count))


if __name__ == "__main__":
    app.run(debug=True)
