from flask import Flask
import sample

app = Flask(__name__)

@app.route('/')
def index():
    word_list = sample(histogram)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)