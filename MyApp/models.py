from MyApp import app, database


class Contato(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    contatos = database.relationship('Cc', backref='cc', lazy=True)

    def to_dict(self):
        data = {'id': self.id, 'nome': self.nome, 'contatos': []}

        for c in self.contatos:
            data['contatos'].append(c.to_dict())

        return data
    
    def return_contatos(self):
        return [cont.to_dict() for cont in self.contatos]

    

class Cc(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tipo = database.Column(database.String, nullable=False)
    contato = database.Column(database.String, nullable=False)
    id_contato = database.Column(database.Integer, database.ForeignKey('contato.id'), nullable=False)

    def to_dict(self):
        data = {'id': self.id, 'tipo': self.tipo, 'contato': self.contato}

        return data



with app.app_context():
    database.create_all()