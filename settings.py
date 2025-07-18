from os import environ

SESSION_CONFIGS = [
    dict(
        name="splash_demo",
        app_sequence=[
            "splash"
        ],
        num_demo_participants=3,
    ),
    dict(
        name="quiz_demo",
        app_sequence=[
            "quiz"
        ],
        num_demo_participants=3,
    ),
dict(
        name="contest_demo",
        app_sequence=[
            "contest"
        ],
        num_demo_participants=2,
    ),
dict(
        name="contest_share",
        app_sequence=[
            "contest"
        ],
        num_demo_participants=2,
        contest_csf="share",
        contest_endowment=9,
    ),
dict(
        name="contest_allpay",
        app_sequence=[
            "contest"
        ],
        num_demo_participants=2,
        contest_csf="allpay",

    ),
dict(
        name="contest_lottery",
        app_sequence=[
            "contest"
        ],
        num_demo_participants=2,
        contest_csf="lottery",
        contest_group_randomly=True,
    ),
dict(
        name="encryption",
        app_sequence=[
            "encryption"
        ],
        num_demo_participants=2,
    ),
dict(
        name="summary",
        app_sequence=[
            "summary"
        ],
        num_demo_participants=2,
    ),
dict(
        name="Full_experiment",
        app_sequence=[
            "contest",
            "encryption",
            "summary"
        ],
        num_demo_participants=2,
        contest_csf="share",
        contest_endowment=9,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "GBP"
USE_POINTS = False

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = "8668690891855"
