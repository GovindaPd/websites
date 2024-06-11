from flask import render_template, request, redirect, Blueprint
import json
import content
from utility_function import getcontext
from sudoku_logic import check_num_can_be_fill, fill_sudoku, create_empty_sudoku, create_sudoku_puzle

sudoku = Blueprint('sudoku', __name__)
#simple_page = Blueprint('simple_page', __name__, template_folder='templates', static_folder='static')


@sudoku.route('/')
def home():
    context = getcontext()
    sdk = create_empty_sudoku()
    if (fill_sudoku(sdk, 0, 0)):
        #solution = sdk
        sdk_board = create_sudoku_puzle(sdk)
        context['msg'] = "SOLVE THIS SUDOKU ???"
        return render_template('sudoku.html', sdk_board=sdk_board, context=context)

    context['msg'] = "There is an error please try again."
    return render_template('sudoku.html', context=context)
    

@sudoku.route('/your-sudoku')
def your_sudoku():
    context = getcontext()
    context['msg'] = "Fill Your Sudoku Fields ^!^"
    sdk_board = [[0 for i in range(9)] for j in range(9)]
    return render_template('sudoku.html', sdk_board=sdk_board , context=context)


@sudoku.route('/solution', methods=['GET','POST'])
def solution():
    try:
        sdk = json.loads(request.args.get('sdk_box'))
        if (fill_sudoku(sdk, 0, 0)):
            return json.dumps({"sdk":sdk, "msg":"worked"})
        else:
            return json.dumps({"msg":"Numbers are filled in wrong orders >:"})
    except:
        return json.dumps({"msg": "Please send a valid Sudoku Puzle."})
