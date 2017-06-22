import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from logging import DEBUG
from forms import BookmarkForm
# from models import Bookmark # cause circular import
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\x87\xd7\x14j\xee\x87\xbcS\x80\x98\xbc\x966q\xea\xd4\x03\x94s-\x96\x8d\x06\xbe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# bookmarks = []

# def store_bookmark(url, description):
#     bookmarks.append(dict(
#         url = url,
#         description = description,
#         user = "Aloysius Yoko",
#         date = datetime.utcnow()
#     ))

# def new_bookmarks(num):
#     return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route("/")
@app.route("/index")
def index():
    # import models
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))

@app.route('/add', methods=['GET','POST'])
def add():
    # import models
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        # store_bookmark(url, description)
        flash("stored url: '{}'".format(description))
        # app.logger.debug('stored url: ' + url)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)