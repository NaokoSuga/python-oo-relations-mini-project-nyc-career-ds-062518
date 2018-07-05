from invite import Invite
from guest import Guest
from review import Review
from course import Course

class DinnerParty:

    _all = []

    def __init__(self, dinner_party):
        self._dinner_party=dinner_party
        DinnerParty._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def invites(self):
        return [invite for invite in Invite.all() if invite.dinner_party == self]

    def guests(self):
        return [invite.guest for invite in Invite.all() if invite.dinner_party == self]

    def number_of_attendees(self):
        attendee_list = [invite.guest for invite in Invite.all() if invite.accepted == True]
        return len(attendee_list)

    def courses(self):
        return [course for course in Course.all() if course.dinner_party == self]

    def recipes(self):
        return [course.recipe for course in Course.all() if course.dinner_party == self]

    def recipe_count(self):
        recipe_list = [course.recipe for course in Course.all() if course.dinner_party == self]
        return len(recipe_list)

    def reviews(self):
        recipe_list = [course.recipe for course in Course.all() if course.dinner_party == self]
        for recipe in recipe_list:
            return [review for review in Review.all() if review.recipe in recipe_list]

    def highest_rated_recipe(self): # highest average
        rating_list = [review.rating for review in Review.all()]
        highest = max(rating_list)
        return [review.recipe for review in Review.all() if review.rating == highest][0]
