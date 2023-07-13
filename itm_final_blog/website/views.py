from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Post, User, Comment
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/feed', methods=['GET','POST'])
@login_required
def feed():
    posts = Post.query.all()
    if request.method == "POST":
        post = request.form.get('post')

        if not post:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(post=post, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.feed'))
    return render_template('feed.html', user=current_user, posts=posts)

