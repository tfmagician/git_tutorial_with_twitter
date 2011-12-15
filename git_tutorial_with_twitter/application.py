import os
import datasource

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/<screenname>/timeline')
def show_timeline(screenname):
    return render_template('timeline.html',tweets=datasource.timeline(screenname))#datasource.timeline(screenname)

@app.route('/<screenname>/favorites')
def show_favorites(screenname):
    return render_template('timeline.html',tweets=datasource.favorites(screenname))#datasource.mention(screenname)

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'DEVELOP':
        show_timeline('muro') 
        show_favorites('hoshi')
    else:
        app.run(debug=True,host='0.0.0.0',port=8080)
