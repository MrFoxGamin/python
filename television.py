class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, state: bool = False, mute: bool = False, given_volume: int = MIN_VOLUME, given_channel: int = MIN_CHANNEL):
        self.__status = state
        self.__muted = mute
        self.__volume = given_volume
        self.__channel = given_channel
