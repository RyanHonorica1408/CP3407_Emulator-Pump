import enum
class States(enum.Enum):
    INSULIN_PUMP_STATE = 1
    RUN=2
    MANUAL =3
    SUGAR_LOW =4
    SUGAR_OK=5
    SUGAR_HIGH =6
    STARTUP = 7
    RESET = 8
    TEST = 9
