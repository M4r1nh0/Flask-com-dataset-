from flask import Flask, render_template, request, Blueprint
app = Flask(__name__)

bp_requisicao = Blueprint('requisicao', __name__)
@bp_requisicao.route('/tipoget')
def ir_get():
    return render_template('get.html')

@bp_requisicao.route('/tipopost')
def ir_post():
    return render_template('post.html')

@bp_requisicao.route('/receber/', methods=['GET','POST'])
def receber():
    if request.method == "POST":
        return u'Estou no tipo POST! <br> nome={} <br> idade={}'.format(request.form["Nome"],request.form["Idade"])
    elif request.method == "GET":
        return u'Estou no tipo GET! <br> nome={} <br> idade={}'.format(request.args.get("Nome"),request.args.get("Idade"))
