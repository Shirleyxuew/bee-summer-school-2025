import string

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
    payment_per_correct = models.CurrencyField()
    word = models.StringField()
    lookup_table = models.StringField()

    def setup_round(self):
        self.payment_per_correct = Currency(0.10)
        self.word = "AB"
        self.lookup_table = string.ascii_uppercase

    @property
    def lookup_dict(self):
        lookup = {}
        for letter in string.ascii_uppercase:
            lookup[letter] = self.lookup_table.index(letter)
        return lookup

    @property
    def correct_response(self):
        return [self.lookup_dict[letter] for letter in self.word]

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response_1 = models.IntegerField()
    response_2 = models.IntegerField()
    is_correct = models.BooleanField()

    @property
    def response(self):
        return [self.response_1, self.response_2]

    def check_response(self):
        self.is_correct == self.response == self.correct_response
        if self.is_correct:
            self.payoff = self.subsession.payment_per_correct


def creating_session(subsession):
    subsession.setup_round()
    #initialize at the beginning of the session

# PAGES
class Intro(Page):
    @staticmethod
    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    form_model = "player"
    form_fields = ["response_1", "response_2"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.check_response()


class Results(Page):
    @staticmethod
    def is_displayed(self):
        return self.round_number == C.NUM_ROUNDS


page_sequence = [Intro,
                 Decision,
                 Results]
