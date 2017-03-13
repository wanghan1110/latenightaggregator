import sendgrid
from flask import request, render_template, flash, current_app, jsonify
from application import app, logger, cache, agg, mongo
from application.decorators import threaded_async
# from application.models import *
from forms import *
from time import time
from aggregator import YTOptions
from collections import OrderedDict
import pymongo
import datetime

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@cache.cached(timeout=3600)
def index():
    channels=current_app.config['CHANNELIDS']
    vinfos=OrderedDict()
    for channel in channels:
        options=YTOptions(maxResults=10,
                          channelId=channel,
                          publishedAfter=agg.get_current_datestring()
        )
        vinfos.update(agg.retrive_youtube_updates(options))
    log_video_stats(vinfos)
    return render_template("index.html", vinfos=vinfos)

def log_video_stats(vinfos):
    for vid, vname in vinfos.iteritems():
        item = {"_id": vid,
                "video_name": vname,
                "date": datetime.datetime.today()}
        try:
            mongo.db.stats.insert_one(item)
        except pymongo.errors.DuplicateKeyError:
            pass
    
@threaded_async
def send_email(app, to, subject, body):
    with app.app_context():
        sg = sendgrid.SendGridClient("SG.pRFA8c9bRXXXXXXXXXXXXXXXXXXXXXXXXX")
        message = sendgrid.Mail()
        message.add_to(to)
        message.set_subject(subject)
        message.set_html(body)
        message.set_from('Template No-Reply <noreplay@flaskeasytemplate.com>')
        try:
            status, msg = sg.send(message)
            print("Status: " + str(status) + " Message: " + str(msg))
            if status == 200:
                return True
        except Exception, ex:
            print("------------ ERROR SENDING EMAIL ------------" + str(ex.message))
    return False


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    recaptcha = current_app.config['RECAPTCHA_SITE_KEY']
    email_sent = False

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        message = request.form['message']
        recaptcha_response = request.form['g-recaptcha-response']

        send_email(app, to=current_app.config['ADMIN_EMAIL'], subject="Contact Form Flask Shop",
                   body=email + " " + name + " " + message)

        email_sent = True

    return render_template("contact.html", RECAPTCHA_SITE_KEY=recaptcha, email_sent=email_sent)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
