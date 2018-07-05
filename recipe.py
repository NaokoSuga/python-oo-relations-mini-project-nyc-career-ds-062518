from review import Review
from course import Course

class Recipe:
    _all = []

    def __init__(self, recipe):
        self._recipe = recipe
        recipe_dict = {}
        recipe_average_rating_dict = {}
        Recipe._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    def top_five_reviews(self):
        return sorted(self.reviews(),key = lambda review:review.rating, reverse = True)[0:5]
        # rating_list = [review.rating for review in self.reviews()]
        # sorted_rating_list = sorted(rating_list)
        # top_five_rating = [rating[i] for i in range(0,4)]
        # return [review for review in self.reviews() if review.rating in top_five_rating]
    @classmethod
    def recipe_rating(cls):
        recipe_dict = {recipe:[review.rating for review in recipe.reviews()] for recipe in Recipe.all()}
        for recipe in list(recipe_dict.keys()):
            if recipe_dict[recipe] == []:
                del recipe_dict[recipe]
        recipe_rating_avg = {recipe: sum(rating_list)/len(rating_list) for recipe, rating_list in recipe_dict.items()}
        recipe_rating_sorted = sorted((recipe_rating_avg).items(), key = lambda t:t[1])
        return [recipe[0] for recipe in recipe_rating_sorted]

    @classmethod
    def top_three(cls):
        # for review in Review.all():
        #     if not review.recipe in Recipe.recipe_dict.keys():
        #         Recipe.recipe_dict[review.recipe] = [review.rating]
        #     else:
        #         Recipe.recipe_dict[review.recipe].append(review.rating)
        # for recipe in Recipe.recipe_dict:
        # self.recipe_rating()
        #     Recipe.recipe_average_rating_dict[recipe] = sum(Recipe.recipe_dict[recipe])/len(Recipe.recipe_dict[recipe])
        # sorted_dict = dict(sorted(Recipe.recipe_average_rating_dict[recipe].items(), key=lambda t: t[1], reverse = True))
        # top_three_list = []
        # for i in range(0,3):
        #     top_three_list.append(sorted_dict[list(sorted_dict.keys())[i]])
        return cls.recipe_rating()[-1:-4:-1]

    @classmethod
    def bottom_three(cls):
        # for review in Review.all():
        #     if not review.recipe in Recipe.recipe_dict.keys():
        #         Recipe.recipe_dict[review.recipe] = [review.rating]
        #     else:
        #         Recipe.recipe_dict[review.recipe].append(review.rating)
        # for recipe in Recipe.recipe_dict:
        #     Recipe.recipe_average_rating_dict[recipe] = sum(Recipe.recipe_dict[recipe])/len(Recipe.recipe_dict[recipe])
        # sorted_dict = dict(sorted(Recipe.recipe_average_rating_dict[recipe].items(), key=lambda t: t[1]))
        # top_three_list = []
        # for i in range(0,2):
        #     top_three_list.append(sorted_dict[list(sorted_dict.keys())[i]])
        return cls.recipe_rating()[0:3]
