from invite import Invite
from review import Review

class Guest:

    _all = []
    reviewer_dict = {}
    reviewer_average_rating_dict = {}
    review_count = {}

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def invites(self):
        return [invite for invite in Invite.all() if invite.guest == self]

    def reviews(self):
        return [review for review in Review.all() if review.guest == self]

    def number_of_invites(self):
        return len([invite for invite in Invite.all() if invite.guest == self])

    def rsvp(self, invite, rsvp_status):
        # for invite in Invite.all():
        #     if self == invite.guest:
        invite.accepted = rsvp_status
        return rsvp_status

    def review_recipe(self, recipe, rating, comment):
        Review(self, recipe, rating, comment)
        return [review for review in Review.all() if review.recipe == recipe]

    def favorite_recipe(self):
        recipe_list = {review.recipe:review.rating for review in Review.all() if review.reviewer == self}
        favorite = max(recipe_list.values())
        return [review for review, rating in recipe_list.items() if rating==favorite][0]

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_popular(cls):
        guest_list = [invite.guest for invite in Invite.all()]
        guest_dict = {guest:guest_list.count(guest) for guest in set(guest_list)}
        most_popular = max(guest_dict.values())
        return [key for key, value in guest_dict.items() if value == most_popular][0]

    @classmethod
    def toughest_critic(cls):
        for review in Review.all():
            if not review.reviewer in Guest.reviewer_dict.keys():
                Guest.reviewer_dict[review.reviewer] = [review.rating]
            else:
                Guest.reviewer_dict[review.reviewer].append(review.rating)
        for reviewer in Guest.reviewer_dict:
            Guest.reviewer_average_rating_dict[reviewer] = sum(Guest.reviewer_dict[reviewer])/len(Guest.reviewer_dict[reviewer])
        toughest = min(Guest.reviewer_average_rating_dict.values())
        return [reviewer for reviewer in Guest.reviewer_average_rating_dict if Guest.reviewer_average_rating_dict[reviewer] == toughest][0]


    @classmethod
    def most_active_critic(cls):
        for review in Review.all():
            if not review.reviewer in Guest.reviewer_dict.keys():
                Guest.reviewer_dict[review.reviewer] = [review.rating]
            else:
                Guest.reviewer_dict[review.reviewer].append(review.rating)
        for reviewer in Guest.reviewer_dict:
            Guest.review_count[reviewer] = len(Guest.reviewer_dict[reviewer])
            most_active = max(Guest.review_count.values())
        return [reviewer for reviewer in Guest.review_count if Guest.review_count[reviewer] == most_active][0]

    pass
