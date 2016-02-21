from flask import render_template, flash, redirect
from app import app, db, models
from .forms import ReviewForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Review="%s", Rating=%s' %
              (form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data)
        db.session.add(r)
        db.session.commit()
        return redirect('/reviews')
    reviews = models.Review.query.all()[::-1]
    print reviews
    return render_template('reviews.html',
                           form=form,
                           reviews = reviews)