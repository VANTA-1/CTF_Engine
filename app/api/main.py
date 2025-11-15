from flask_login import login_required
from flask import Blueprint, render_template, url_for, redirect, flash, request
from app.models.models import Challenge, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Welcome to the CTF Engine! <a href='/register'>Register</a> or <a href='/login'>Login</a>"

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main_bp.route('/challenges')
@login_required
def challenges():
    all_challenges = Challenge.query.all()
    return render_template('challenges.html', challenges=all_challenges)
