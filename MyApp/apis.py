from flask import request, jsonify
from MyApp import app, database
from MyApp.models import Contato, Cc
import json


@app.route('/lista', methods=['GET'])
def lista():
    data = Contato.query.all()

    lista_contatos = [{"id": cont.id, "nome": cont.nome, "contatos": len(cont.contatos)} for cont in data]
    
    return jsonify(lista_contatos), 200


@app.route('/contato/<int:id>', methods=['GET'])
def contatos(id):
    data = Contato.query.filter_by(id=id).first()
    
    return jsonify(data.return_contatos()), 200



@app.route('/add', methods=['PUT'])
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

        return jsonify(contato.todict()), 200
    except Exception as err:
        print(err)
        return  jsonify({'mensagem': 'ERRO'}), 400
    
    
@app.route('/del_contato/<id>', methods=['DELETE'])
def remover_contato(id):
    try:
        contato = Contato.query.filter_by(id=id).first()
        for cc in contato.contatos:
            database.session.delete(cc)

        #database.session.delete(contato)
        database.session.commit()

        return jsonify({'status': 200, 'mensagem': 'Contato Removido'})
    
    except:
        return jsonify({'status': 400, 'mensagem': 'Falha na Operacao'})
    

@app.route('/del_cc/<int:id>', methods=['DELETE'])
def remover_cc(id):
    try:
        contato = Cc.query.filter_by(id=id).first()
        print()
        id_contato = contato.id_contato
        database.session.delete(contato)
        database.session.commit()

        return jsonify({'status': 200, 'mensagem': 'Contato Removido', 'id_contato': id_contato})
    except:
        return jsonify({'status': 400, 'mensagem': 'Falha na Operacao'})


@app.route('/atualizar/<id>', methods=['POST'])
def atualizar(id):
    try:
        data = request.get_json()

        contato = Cc.query.filter_by(id=id).first()
        contato.tipo = data['tipo']
        contato.contato = data['contato']
        
        database.session.commit()

        return jsonify(contato.to_dict())
    except:
        return jsonify({'status': 400, 'mensagem': 'Falha na Operacao'})
