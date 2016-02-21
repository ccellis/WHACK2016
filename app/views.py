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
        #flash('Review="%s", Rating=%s' %
              #(form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data,location="TESTPLACE")
        db.session.add(r)
        db.session.commit()
        return redirect('/reviews')
    return render_template('reviews.html',
                           form=form)

@app.route('/bates', methods=['GET', 'POST'])
def bates():
    form = ReviewForm()
    if form.validate_on_submit():
        #flash('Review="%s", Rating=%s' %
              #(form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data,location="Bates")
        db.session.add(r)
        db.session.commit()
        return redirect('/bates')
    reviews = models.Review.query.all()[::-1]
    reviews = filter(lambda review: review.location == "Bates",reviews)
    return render_template('bates.html',
                           form=form,
                           reviews = reviews)

@app.route('/tower', methods=['GET', 'POST'])
def tower():
    form = ReviewForm()
    if form.validate_on_submit():
        #flash('Review="%s", Rating=%s' %
              #(form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data,location="Tower")
        db.session.add(r)
        db.session.commit()
        return redirect('/tower')
    reviews = models.Review.query.all()[::-1]
    reviews = filter(lambda review: review.location == "Tower",reviews)
    return render_template('tower.html',
                           form=form,
                           reviews = reviews)