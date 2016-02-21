from flask import render_template, flash, redirect
from app import app, db, models
from .forms import ReviewForm
from config import HALLS


@app.route('/')
@app.route('/index')
def index():
    reviews = models.Review.query.all()[::-1]
    return render_template('index.html',
                            reviews=reviews,
                            halls=HALLS)


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
                           form=form,
                           halls=HALLS)

@app.route('/hall/<name>', methods=['GET', 'POST'])
def hall(name):
    if name not in HALLS:
      return redirect('/index')
    form = ReviewForm()
    if form.validate_on_submit():
        #flash('Review="%s", Rating=%s' %
              #(form.review.data, str(form.rating.data)))
        r = models.Review(review=form.review.data,score=form.rating.data,location=name)
        db.session.add(r)
        db.session.commit()
        return redirect('/hall/'+name)
    reviews = models.Review.query.all()[::-1]
    reviews = filter(lambda review: review.location == name,reviews)
    return render_template('reviews.html',
                           form=form,
                           reviews = reviews,
                           location = name,
                           halls = HALLS)

"""@app.route('/tower', methods=['GET', 'POST'])
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
    return render_template('reviews.html',
                           form=form,
                           reviews = reviews,
                           location="Tower")"""