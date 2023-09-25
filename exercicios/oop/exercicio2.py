class Contato:
    def __init__(self, id, nome='', telefone=''):
        self.id = id
        self.nome = nome
        self.telefone = telefone

class AgendaContato:
    def __init__(self, agenda_id, contato_id):
        self.ageda_id = agenda_id
        self.contato_id = contato_id

class Agenda:
    def __init__(self, id, nome, data_hora_ini, data_hora_fim):
        self.id = id
        self.nome = nome
        self.data_hora_ini = data_hora_ini
        self.data_hora_fim - data_hora_fim
