from flask import request, url_for, redirect
from MyApp import app, database
from MyApp.models import Contato, Cc
import json

from datetime import datetime

@app.route('/lista', methods=['GET','POST'])
def lista():
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

        return json.dumps({'status': 200, 'mensagem': 'contato salvo'})
    except Exception as err:
        print(err)
        return  json.dumps({'status': 400, 'mensagem': 'ERRO na solicitação'})