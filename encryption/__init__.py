from otree.api import *
from otree.models import player, subsession

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'encryption'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    payment_per_correct = models.CurrencyField
    word = models.StringField()

    def setup_round(self):
        self.payment_per_correct = Currency(0.10)
        self.word = "AB"


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

def creating_session(submission):
    subsession.setup_round()
    #initialize at the beginning of the session

# PAGES
class Intro(Page):
    @staticmethod
    def is_displayed(self):
        return player.round_number == 1


class Decision(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS


page_sequence = [Intro,
                 Decision,
                 Results]
