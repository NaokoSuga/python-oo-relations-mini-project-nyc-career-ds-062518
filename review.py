class Review:

    _all = []

    def __init__(self, reviewer,recipe, rating, comment):
        self._rating = rating
        self._recipe = recipe
        self._reviewer = reviewer
        self._comment = comment
        Review._all.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):
        self._rating = rating

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self,recipe):
        self._recipe = recipe

    @property
    def reviewer(self):
        return self._reviewer

    @reviewer.setter
    def reviewer(self,reviewer):
        self._reviewer = reviewer

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = comment

    @classmethod
    def all(cls):
        return cls._all

    pass
