

#Input=length,moral lessons and age group

#process=create a class story,with attributes of length,moral lessons and age group,create a methond 
#that checks on the oral stories according to the attributes and inheritance of the attributes 


#output=predict the oral stories according to length moral lessons and age groups.
class Story:
    def __init__(self, length, moral_lessons, age_group):
        self.length = length
        self.moral_lessons = moral_lessons
        self.age_group = age_group


class Storyteller:
    def __init__(self, name, specific_language):
        self.name = name
        self.specific_language = specific_language

    def tell_story(self, story):
        print(f"Storyteller {self.name} telling a story in {self.specific_language}:")
        print("The story")


class Youth:
    def __init__(self, name, specific_language):
        super().__init__(no_experience)
        self.name = name
        self.specific_language = specific_language


class Elderly(Youth):
    def __init__(self, old_language, experienced):
        super().__init__(experience)
        self.experience = experience


class Languages:
    def __init__(self, target_group):
        self.target_group = target_group

    def check_language(self):
        if self.target_group == "old":
            return "Language used is of great experience."
        else:
            return "Language used is youthful."

print(Elderly=67-89,Youth_age=18-24)




#**African Cuisine:** You're creating a recipe app specifically for African cuisine.
#The app needs to handle recipes from different African countries, each with its
#unique ingredients, preparation time, cooking method, and nutritional
#information. Consider creating a `Recipe` class, and think about how you might
#create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#`EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#methods.
class Recipe:
    def __init__(self, name, preparation_time, cooking_method, nutritional_information, ingredients):
        self.name = name
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_information = nutritional_information
        self.ingredients = ingredients

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Preparation Time: {self.preparation_time}")
        print(f"Cooking Method: {self.cooking_method}")
        print(f"Nutritional Information: {self.nutritional_information}")


class EthiopianRecipe(Recipe):
    def __init__(self, name, preparation_time, cooking_method, nutritional_information, ingredients, meat_required):
        super().__init__(name, preparation_time, cooking_method, nutritional_information, ingredients)
        self.meat_required = meat_required

    def display_recipe(self):
        super().display_recipe()
        print(f"Meat Required: {'Yes' if self.meat_required else 'No'}")


ethiopian_recipe = EthiopianRecipe(
    name="Ethiopian Spicy Chicken Stew",
    preparation_time="30 minutes",
    cooking_method="Simmering",
    nutritional_information="High in protein",
    ingredients=["Chicken", "Onions", "Tomatoes", "Spices"],
    meat_required=True
)

ethiopian_recipe.display_recipe()








#**Wildlife Preservation:** You're a wildlife conservationist working on a
#program to track different species in a national park. Each species has its own
#characteristics and behaviors, such as its diet, typical lifespan, migration
#patterns, etc. Some species might be predators, others prey. You'll need to

#create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
#these classes might relate to each other through inheritance.
class Species:
    def __init__(self, diet, lifespan):
        self.diet = diet
        self.lifespan = lifespan

class Predator(Species):
    def __init__(self, diet, lifespan, hunting_style):
        super().__init__(diet, lifespan)
        self.hunting_style = hunting_style

class Prey(Species):
    def __init__(self, diet, lifespan, migration_pattern):
        super().__init__(diet, lifespan)
        self.migration_pattern = migration_pattern






#**African Music Festival:** You're in charge of organizing a Pan-African music
#festival. Many artists from different countries, each with their own musical style
#and instruments, are scheduled to perform. You need to write a program to
#manage the festival lineup, schedule, and stage arrangements. Think about how
#you might model the `Artist`, `Performance`, and `Stage` classes, and consider
#how you might use inheritance if there are different types of performances or
#stages.
class Music:
    def __init__(self, line_up, schedule, stage_arrangements):
        self.line_up = line_up
        self.schedule = schedule
        self.stage_arrangements = stage_arrangements


class Performing:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def performance_details(self):
        if self.start_time > self.end_time:
            print("The artist has exceeded the time")
        else:
            print("The artist finished at the right time")


class Stage:
    def __init__(self, name, space):
        self.name = name
        self.space = space
        self.performances = []


class BigStage(Stage):
    def __init__(self, name, space):
        super().__init__(name, space)


class SmallStage(Stage):
    def __init__(self, name, space):
        super().__init__(name, space)






        










