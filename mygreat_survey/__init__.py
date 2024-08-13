
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'mygreat_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    E = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    edad = models.IntegerField(label='escribe tu edad', max=120, min=0)
    eleccion = models.IntegerField(label='elige un numero del 1 al 20', max=20, min=1)
    deporte = models.IntegerField(choices=[[1, 'Formula 1'], [2, 'Tenis'], [3, 'Ajedrez']], label='¿Cual de estos deportes prefieres?')
    nombre = models.StringField(label='escribe tu nombre')
class Survey1(Page):
    form_model = 'player'
    form_fields = ['nombre', 'edad']
class Survey2(Page):
    form_model = 'player'
    form_fields = ['eleccion', 'deporte']
class Results(Page):
    form_model = 'player'
page_sequence = [Survey1, Survey2, Results]