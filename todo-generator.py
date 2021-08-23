# hi this is a random file because I'm bored
# let's randomly generate things to do
import random
from data_io import read_yaml, instantiate_yaml_documents

PRODUCT_NAME = 'NOT BORED Activity Generator (TM)'

# todo: turn this into txt file storage
# todo: use classes
# feeling active?
# class Activity
fun_outdoors = ['skateboarding',
                'watch a movie at Southbank',
                'window shop at the nearest Westfield',
                'blast music with the windows down on a mountain drive. Cootha, Tamborine or Mt Gravatt you choose!',
                'get donuts. Specifically Krispy Kremes',
                'impulse book that concert ticket you\'ve been thinking of going to', 'walk to the park',
                'walk aimlessly around the neighbourhood listening to music / a podcast',
                'bike ride to the city!', 'go to the gym', 'do 20 squats',
                'buy a paint-by-number kit from Kmart and set it up in the living room', 'do the laundry',
                'break out the goon and 2012 hits, time for another living room dance party!',
                'have a bath', 'give yourself a facial and mask', 'do a walk-in beauty treatment',
                'paint your nails, or book in to get them done now!',
                'text your friends - who\'s keen to hang out now / tonight?',
                'stretch', 'bother Lillian / Tiffany until they hang out with you :D',
                'catch a bus to the city for no reason. Wander around', 'spend an hour or 2 at a BCC library',
                'read an old fiction book you used to love',
                'skim a non-fiction book on the shelf',
                'crack open a project you\'ve been meaning to get to for a while', 'buy yourself some flowers :)',
                'drunk browse Facebook Marketplace for random things you don\'t need or want',
                ]

# class Food. meal, savoury, sweet, dessert, takeaway, price[]
food = ['make a DIY cheese platter', 'dessert', 'eggs on toast', '2 minute noodles',
        'pick a cafe within 10km and drive there. Get coffee and eat in. You won\'t regret it',
        'pastries', 'banh mi', 'DUMPLINGS', 'KFC (korean or kentucky-fried). Doesn\'t matter',
        'please eat some fruit. You need it', 'carrots and dip', 'at least 16 olives',
        'plan a bougee steak night let\'s goooo', 'bake that cake mix. (or get those ingredients rn)']

# for unsuccessful options
prompts = ['Let\'s try something else...', 'Hmmm let\'s see what other options we have.', 'Something else then!',
           'Ah okay, not that one.', 'Gotcha.']


def fun_decision_tree(choices=fun_outdoors):
    # Recursive func to go through all the options.
    opt = random.sample(choices, 1)  # to sample and rm from options
    opt = opt[0]  # rm from list format
    choices.remove(opt)
    # print(len(choices))

    print(f'What do you think about this option? {opt}')
    input_ = input('Type Y/N, or X to exit: ')
    input_clean = input_.strip()  # todo: add more robust input processing

    # exit condition
    if input_clean is 'Y':
        print(f"Nice! Hope you have fun :D See you back at the {PRODUCT_NAME} soon.")
        return 1
    # exit condition
    elif input_clean is 'X':
        print('Sorry to see you go :(')
        print(f"Hope to see you use the {PRODUCT_NAME} next time!")
        return 1
    # loop
    elif input_clean is 'N':
        print(random.choice(prompts))  # sample with replacement
        fun_decision_tree()
    # handle everything else
    else:
        # one condition is that list is empty
        if not len(choices):
            print('Apologies, we\'re out of options :(')
            print('Good luck finding something to do!')
            print('Hope to see you again soon.')
            return 1
        # else more likely, bad input for that field.
        # todo: add better handling
        else:
            print('y')
            fun_decision_tree()
            # print("Sorry that wasn't a valid option! Try again?")


def food_decision_tree():
    return 0


def indecisive_decision_tree():
    return 0


meal_prep_ideas = []
binge_recovery_counter = []
not_happy = []


if __name__ == '__main__':
    # prep - read into memory
    output = read_yaml()
    print(output) if output is str else instantiate_yaml_documents(output)
    # prompt
    # Todo: wrap this logic inside a loop, until exited.
    print(f"Hi, welcome to the {PRODUCT_NAME}!")
    print("What are we filling the void with today?")
    value = input("Enter (1) fun, (2) food or (3) i really don't care: ")
    print(value)
    # entr whic
    if int(value) == 1:
        print('Alright, let\'s get started!')
        fun_decision_tree()
    elif int(value) == 2:
        print('Alright, let\'s get started!')
        food_decision_tree()
    elif int(value) == 3:
        print('Alright, let\'s get started!')
        indecisive_decision_tree()
    else:
        print("Sorry that wasn't a valid option! Try again?")

    '''
    decision tree: 
    if fun:
        solo, or with other people?
        with others or  alone?
        
    if food:
        got a budget? 
        
    ++ recommendation engine. Loop while UNSATISFIED
    
    
    '''
