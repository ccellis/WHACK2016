from flask import render_template, flash, redirect
from app import app, db, models
from .forms import ReviewForm


@app.route('/')
@app.route('/index')
def index():
    reviews = models.Review.query.all()[::-1]
    return render_template('index.html',
                            reviews=reviews)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Review="%s", Rating=%s' %
              (form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data,location="TESTPLACE")
        db.session.add(r)
        db.session.commit()
        return redirect('/reviews')
    return render_template('reviews.html',
                           form=form)