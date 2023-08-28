from backend.geral.config import *

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # pontos do jogador
    tempo = db.Column(db.Text)

    def __str__(self):
        return f'Tempo: {self.tempo}'
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "tempo": self.tempo
        }