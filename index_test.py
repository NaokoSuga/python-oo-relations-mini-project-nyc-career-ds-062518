import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from review import Review
from invite import Invite
from dinnerparty import DinnerParty
from recipe import Recipe
from guest import Guest
from course import Course

class TestHasManyThroughMiniProj(unittest.TestCase):

    global guest_1
    guest_1 = Guest("Dwight Schrute")
    global guest_2
    guest_2 = Guest("Michael Scott")
    global guest_3
    guest_3 = Guest("Pam Beasley")
    global dinner_party_1
    dinner_party_1 = DinnerParty("Office Christmas Party")
    global dinner_party_2
    dinner_party_2 = DinnerParty("Your parent's friend's")
    global dinner_party_3
    dinner_party_3 = DinnerParty("Friend's House Warming")
    global invite_1
    invite_1 = Invite(dinner_party_1, guest_1)
    global invite_2
    invite_2 = Invite(dinner_party_1, guest_2)
    global invite_3
    invite_3 = Invite(dinner_party_1, guest_3)
    global invite_4
    invite_4 = Invite(dinner_party_2, guest_1)
    global invite_5
    invite_5 = Invite(dinner_party_3, guest_1)
    global recipe_1
    recipe_1 = Recipe("Disaster")
    global recipe_2
    recipe_2 = Recipe("Punch")
    global recipe_3
    recipe_3 = Recipe("Cookies")
    global recipe_4
    recipe_4 = Recipe("Punch")
    global recipe_5
    recipe_5 = Recipe("Cookies")
    global recipe_6
    recipe_6 = Recipe("Punch")
    global course_1
    course_1 = Course(dinner_party_1, recipe_1)
    global course_2
    course_2 = Course(dinner_party_1, recipe_2)
    global course_3
    course_3 = Course(dinner_party_1, recipe_3)
    global course_4
    course_4 = Course(dinner_party_1, recipe_4)
    global course_5
    course_5 = Course(dinner_party_2, recipe_5)
    global course_6
    course_6 = Course(dinner_party_2, recipe_6)
    global course_7
    course_7 = Course(dinner_party_2, recipe_2)
    global review_1
    review_1 = Review(guest_1, recipe_1, 3, "the Disaster wasn't as bad as I would've liked")
    global review_2
    review_2 = Review(guest_2, recipe_1, 5, "It was total chaos, exceeded expectations")
    global review_3
    review_3 = Review(guest_3, recipe_1, 4, "Just disastrous, nothing more")
    global review_4
    review_4 = Review(guest_1, recipe_2, 2, "way too much pineapple juice!")
    global review_5
    review_5 = Review(guest_2, recipe_2, 2, "not enough pineapple juice!")
    global review_6
    review_6 = Review(guest_3, recipe_2, 3, "right amount of pineapple juice, but wasn't anything to write home about")
    global review_7
    review_7 = Review(guest_1, recipe_3, 2, "I don't like cookies, that's all.")
    global review_8
    review_8 = Review(guest_2, recipe_1, 4, "Pretty disastrous, nothing more")
    global review_9
    review_9 = Review(guest_3, recipe_1, 4, "Meh, I've seen more bedlam")
    global review_10
    review_10 = Review(guest_1, recipe_4, 1, "It was more of a slap in the face")

    def test_guest_class_methods(self):
        self.assertItemsEqual(Guest.all(), [guest_1, guest_2, guest_3])
        self.assertEqual(Guest.most_popular(), guest_1)
        self.assertEqual(Guest.most_active_critic(), guest_1)

    def test_guest_instance_methods(self):
        self.assertEqual(guest_1.rsvp(invite_1, True), True)
        self.assertEqual(guest_1.number_of_invites(), 3)
        self.assertEqual(len(guest_1.review_recipe(recipe_1, 3, "The disaster just wasn't disastrous enough!")), 6)
        Review._all.pop()
        self.assertEqual(guest_1.favorite_recipe(), recipe_1)

    def test_invite_class_methods(self):
        self.assertItemsEqual(Invite._all, [invite_1, invite_2, invite_3, invite_4, invite_5])
        self.assertItemsEqual(Invite.all(), [invite_1, invite_2, invite_3, invite_4, invite_5])

    def test_invite_instance_methods(self):
        self.assertEqual(guest_1.rsvp(invite_1, True), True)
        self.assertEqual(invite_1.accepted, True)
        self.assertEqual(invite_1.dinner_party, dinner_party_1)

    def test_dinner_party_class_methods(self):
        self.assertItemsEqual(DinnerParty.all(), [dinner_party_1, dinner_party_2, dinner_party_3])

    def test_dinner_party_instance_methods(self):
        self.assertItemsEqual(dinner_party_1.reviews(), [review_1, review_2, review_3, review_4, review_5, review_6, review_7, review_8, review_9, review_10])
        self.assertItemsEqual(dinner_party_1.recipes(), [recipe_1, recipe_2, recipe_3, recipe_4])
        self.assertEqual(dinner_party_1.recipe_count(), 4)
        self.assertEqual(dinner_party_1.highest_rated_recipe(), recipe_1)
        invite_1.accepted = True
        invite_2.accepted = True
        invite_3.accepted = True
        self.assertEqual(dinner_party_1.number_of_attendees(), 3)

    def test_review_class_methods(self):
        self.assertItemsEqual(Review._all, [review_1, review_2, review_3, review_4, review_5, review_6, review_7, review_8, review_9, review_10])
        self.assertItemsEqual(Review.all(), [review_1, review_2, review_3, review_4, review_5, review_6, review_7, review_8, review_9, review_10])

    def test_review_instance_methods(self):
        self.assertEqual(review_1.rating, 3)
        self.assertEqual(review_1.reviewer, guest_1)
        self.assertEqual(review_1.recipe, recipe_1)
        self.assertEqual(review_1.comment, "the Disaster wasn't as bad as I would've liked")

    def test_recipe_class_methods(self):
        self.assertItemsEqual(Recipe.all(), [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5, recipe_6])
        self.assertItemsEqual(Recipe.top_three(), [recipe_1, recipe_2, recipe_3])
        self.assertItemsEqual(Recipe.bottom_three(), [recipe_4, recipe_2, recipe_3])

    def test_recipe_instance_methods(self):
        self.assertItemsEqual(recipe_1.top_five_reviews(), [review_1, review_2, review_8, review_3, review_9])
