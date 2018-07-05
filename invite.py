class Invite:

    _all = []

    def __init__(self,dinner_party,guest):
        self._guest = guest
        self._dinner_party = dinner_party
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def accepted(self):
        return self.accepted

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self,guest):
        self._guest = guest

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self,dinner_party):
        self._dinner_party = dinner_party

    pass
