from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/about')
def index():
    # используем хтмл файл, то есть к главным страницам соединяем файл index.html
    return render_template('index.html')

@app.route('/audio')
def about_page():
    return render_template('audio-page.html')

if __name__ == '__main__':
    app.run(debug = False)