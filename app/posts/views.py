from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Post, User, Comment
from app.posts.forms import PostForm, CommentForm

posts = Blueprint('posts', __name__)


