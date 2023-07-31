from flask import request
from MyApp import app, database
from MyApp.models import Contato, Cc
import json


@app.route('/lista', methods=['GET','POST'])
def lista(nome=None):
    data = Contato.query.all()
    retorno = []
    for c in data:
        retorno.append(c.to_dict())
    return retorno


@app.route('/add', methods=['GET','POST'])
def add():

    '''formato de json
            {
            'id': 'id ou None',
            'nome': 'nome do contato',
            'contatos': [
                        {
                        'tipo': 'tipo',
                        'contato': 'contato'
                        },
                    ]
            }'''
    
    try:

        data = request.get_json()
        if data['id']:
            id = data['id']
        else:
            contat = Contato(nome=data['nome'])
            database.session.add(contat)
            database.session.commit()
            id = contat.id
        
        for c in data['contatos']:
            tip = c['tipo']
            contato = c['contato']

            cc = Cc(tipo=tip, contato=contato, id_contato=id)
            database.session.add(cc)
        
        database.session.commit()

        return json.dumps({'status': 200, 'mensagem': 'Contato Salvo'})
    except Exception as err:
        print(err)
        return  json.dumps({'status': 400, 'mensagem': 'ERRO na Solicitacao'})
    
    
@app.route('/remover_contato/<id>', methods=['GET', 'POST'])
def remover_contato(id):
    try:
        contato = Contato.query.filter_by(id=id).first()

        for cc in contato.contatos:
            database.session.delete(cc)

        database.session.delete(contato)
        database.session.commit()

        return json.dumps({'status': 200, 'mensagem': 'Contato Removido'})
    except:
        return json.dumps({'status': 400, 'mensagem': 'Falha na Operacao'})
    

@app.route('/remover_cc/<id>', methods=['GET', 'POST'])
def remover_cc(id):
    try:
        contato = Cc.query.filter_by(id=id).first()
        database.session.delete(contato)
        database.session.commit()

        return json.dumps({'status': 200, 'mensagem': 'Contato Removido'})
    except:
        return json.dumps({'status': 400, 'mensagem': 'Falha na Operacao'})


@app.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id):
    try:
        data = request.get_json()

        contato = Cc.query.filter_by(id=id).first()
        contato.tipo = data['tipo']
        contato.contato = data['contato']
        
        database.session.commit()

        return json.dumps(contato.to_dict())
    except:
        return json.dumps({'status': 400, 'mensagem': 'Falha na Operacao'})
