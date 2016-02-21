import os
basedir = os.path.abspath(os.path.dirname(__file__))

HALLS = {'Bates':"http://media1.santabanta.com/full1/Fare/Snacks/snacks-20a.jpg",
        'Lulu':"http://www.ambwallpapers.com/wp-content/uploads/2015/12/veg-sandwich-hd-wallpaper-892073644-AMB.jpg",
        'Pomeroy':"https://wallpaperscraft.com/image/salad_plate_vegetables_tasty_89600_3840x2400.jpg",
        'Stone-D':"http://hdwallpapersfit.com/wp-content/uploads/2015/02/pizza-wallpapers.jpeg",
        'Tower':"http://www.emmaslittlekitchen.com/wp-content/uploads/2014/10/IMG_4697.jpg"}

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
