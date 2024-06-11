from flask import Flask, render_template, request, send_from_directory, redirect, Blueprint
from flask_sitemap import Sitemap

from datetime import datetime
import json
import content
from utility_function import getcontext

# importing blueprients
from sudoku import sudoku
from instafonts import instafonts
from agecalculator import agecalculator

app = Flask(__name__)

app.register_blueprint(sudoku, url_prefix='/sudoku')
app.register_blueprint(instafonts, url_prefix='/instafonts')
app.register_blueprint(agecalculator, url_prefix='/agecalculator')

sitemap = Sitemap(app=app)
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
app.config['SITEMAP_URL_SCHEME'] = 'https'
app.config['SITEMAP_CHANGE_FREQ'] = 'weekly'
app.config['SITEMAP_PRIORITY'] = 0.5


@app.route('/')
def home():
    context = getcontext()
    context['developer'] = content.developer
    return render_template('index.html', context=context)

# common urls 
@app.route('/about')
def about():
    context = getcontext()
    context['content'] = content.about_us
    return render_template('otherpages.html', context=context)

@app.route('/privacy-policy')
def privacy_policy():
    context = getcontext()
    context['content'] = content.privacy_policy
    return render_template('otherpages.html', context=context)

@app.route('/disclaimer')
def disclaimer():
    context = getcontext()
    context['content'] = content.disclaimer
    return render_template('otherpages.html', context=context)

@app.route('/terms-and-conditions')
def terms_and_conditions():
    context = getcontext()
    context['content'] = content.terms_and_conditions
    return render_template('otherpages.html', context=context)

@app.route('/contactus')
def contactus():
    context = getcontext()
    context['content'] = content.contactus
    return render_template('otherpages.html', context=context)

@app.route('/sitemap.xml')
def sitemap_xml():
    return sitemap.sitemap()

# @app.route('/sitemap')
# def static_from_root():
#     return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run(debug = False)
