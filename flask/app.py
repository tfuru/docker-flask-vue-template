from flask import Flask, render_template

app = Flask(__name__, static_folder='/flask/vue-app/dist/static', template_folder='/flask/vue-app/dist')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)