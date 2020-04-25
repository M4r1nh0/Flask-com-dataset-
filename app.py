# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, redirect, url_for, Blueprint
from requisicao import bp_requisicao
import dataset


app = Flask(__name__)
app.secret_key = "Minha_chave_criptografada"
app.register_blueprint(bp_requisicao)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/Sessao/')
def ir_sessao():
    return render_template('sessao.html')

@app.route('/validacao/', methods=['POST'])
def validacao_sessao():
    if request.method == "POST":
        session['usuario'] = request.form['usuario']
        return redirect(url_for('restrito'))

    return redirect(url_for('ir_sessao'))

@app.route('/restrito/')
def restrito():
    if ( session['usuario'] ):
        return u"Estou na area de acesso restrito {}".format(session['usuario'])

    return redirect(url_for('ir_sessao'))

@app.route("/operacao/")
def operacao_banco():
	with dataset.connect("sqlite:///cursopython.db") as db:
		# Como inserir dados [CREATE]
		#db['aulas'].insert(dict(nome=u"Aula 1", tipo=u"python"))
		#db['aulas'].insert(dict(nome=u"Aula 2", tipo=u"Batata"))
		#db['aulas'].insert(dict(nome=u"Aula 3", tipo=u"Arroz"))
		#db['aulas'].insert(dict(nome=u"Aula 4", tipo=u"peru"))

		# Como ler dados [READ]
		#lista = db['aulas'].all()
		#lista = db['aulas'].find(_limit=2, order_by='nome', _offset=2)
		#lista = db['aulas'].find_one()
		#lista = db['aulas'].find_one(nome=u"Aula 1")

		# Como atualizar dados [UPDATE]
		#lista['tipo'] = u"Python ALTERADO"
		#db['aulas'].update(lista, ['id'])

		# Como excluir dados [DELETE]
		db['aulas'].delete(id=1)

	return u"Realizando operacoes CRUD"

@app.route("/banco/")
def listar_banco():
	with dataset.connect("sqlite:///cursopython.db") as db:
		lista = db['aulas'].all()

	html = "<ul>"
	for item in lista:
		html += "<li>{id} - {nome} - {tipo}</li>".format(id=item['id'],nome=item['nome'],tipo=item['tipo'])
	html += "</ul>"

	return u"Estou no banco !<Br>Lista: <br>{}".format(html)

#app.route('/informacao/')
#@app.route('/informacao/<nome>')
#@app.route('/informacao/<nome>/<idade>')
#def info(nome = None,idade = None):
 #   return u'nome:{}, idade:{}'.format(nome,idade)
