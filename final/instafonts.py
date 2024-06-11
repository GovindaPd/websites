from flask import render_template, request, Blueprint
import content
from utility_function import getcontext

instafonts = Blueprint('instafonts', __name__)

@instafonts.route('/')
def home():
    context = getcontext()
    print(context)
    return render_template("instafonts.html", context=context)

