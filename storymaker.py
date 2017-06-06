genders = ['boy', 'girl', 'he', 'she']
mobs = ['fiery dragon', 'dragon', 'tree giant', 'giant', 'poisonous snake', 'snake', 'mountain troll', 'troll']
Treasures = ['1', '2', '3', '4', '5', 'gems', 'precious metals', 'magical items', 'beutiful artifacts', 'gold', 'artifacts', 'magic items', 'metals']
def gender():
    while True:
        print('Are you a boy or a girl?')
        while True:
            gender = input()
            gender = gender.lower()
            if gender == genders[0]:
                gender_ = genders[2]
                gender_1 = str(gender_)
                break
            elif gender == genders[1]:
                gender_ = genders[3]
                gender_1 = str(gender_)
                break
        break
    return gender_1
def mob_type():
    while True:
        print('Okay ' + name + ', would you rather battle a fiery dragon, a tree giant, a poisonous snake, or a mountain troll?')
        enemy = input()
        enemy = enemy.lower()
        if enemy not in mobs:
            print('Enter one of the GIVEN choices, please. Also, make sure you spelled it correctly')
        elif enemy == mobs[0] or enemy == mobs[1]:
            print('Yeah, their fire is WAY too powerful.')
            enemy_ = 'fiery dragon'
            break
        elif enemy == mobs[2] or enemy == mobs[3]:
            print('Have you ever seen one? No, of course you haven\'t.')
            enemy_ = 'hill giant'
            break
        elif enemy == mobs[4] or enemy == mobs[5]:
            print('BEWARE their fangs!')
            enemy_ = 'poisonous snake'
            break
        else:
            enemy == mobs[6] or enemy == mobs[7]
            print('They smell REALLY bad, you know.')
            enemy_ = 'mountain troll'
            break
    return enemy_
def age_find():
    storyline = 0
    print('How old are you?')
    age = input()
    age = int(age)
    return age
def story_1(gender_, age):
    if age < 15.5:
        print('What do you want to be when you grow up, ' + name + '?')
        job = input()
        storyline = 1
    if age > 15.5:
        print('What is your job?')
        job = input()
        storyline = 2
    print('Okay ' + name + ''', you're doing well. Here is the story I have generated so far:''')
    if storyline == 1:
        print('One day, ' + name + ' was walking through the woods near ' + location + ', and while ' + gender_ + ' was thinking about what it would be like to be a ' + job + ', suddenly ' + gender_ + ' ...')
    if storyline == 2:
        print('One day, ' + name + ' was walking through the woods near ' + location + ', and while ' + gender_ + ' was thinking about being a ' + job + ', suddenly ' + gender_ + ' ...')
    return storyline, job
def treasure_type(enemy_):
    print('What kind of treasure does a ' + enemy_ + ' keep, ' + name + '?')
    print('''1. Gold
2. Gems
3. Precious Metals
4. Magical Items
5. Beutiful Artifacts''')
    while True:
        treasure = input()
        treasure = treasure.lower()
        if not treasure in Treasures:
            print('Please enter one of the given treasure choices, and make sure you spelled it correctly.')
        if treasure in Treasures:
            break

import time
print('Hello User! \nIn these questions, please answer all of them correctly.\nRemember - you CANNOT save your work(YET).')
time.sleep(2)

print('What is your first name?')
name = input()

print('Where do you live, ' + name + '?')
location = input()

gender_ = gender()

age = age_find()

storyline, job = story_1(gender_, age)
time.sleep(4)

print('''\nIt isn't finished yet, so I'll need you to answer some more questions.''')
time.sleep(2)

t_enemy = mob_type()
time.sleep(1)

print('What do you like to do outside, ' + name + '?')
activity = input()

print('What is your favorite snack food?')
snack = input()

print('Blech! I prefer electricity to ' + snack + '!')
time.sleep(1)

print('What is your least favorite type of weather, ' + name + '?')
weather = input()

print('What is your favorite type of weather?')
fav_weather = input()

print('So, this is what I\'ve generated now that you\'ve answered more questions:\n')
if storyline == 1:
    print('One day, ' + name + ' was walking through some woods near ' + location + ', and while ' + gender_ + ' was eating ' + snack + ', ' + gender_ + ' thoght about what it would be like to be a ' + job + ' . Suddenly, ' + gender_ + ' came out of the woods into a place that ' + gender_ + ' had never been before.')
if storyline == 2:
    print('One day, ' + name + ' was walking through some woods near ' + location + ', and while ' + gender_ + ' was eating ' + snack + ', ' + gender_ + ' thought about being a ' + job + ' . Suddenly, ' + gender_ + ' came out of the woods into a place that ' + gender_ + ' had never been before.')

print('Now, I still need more information.')

print('Where do you think a ' + t_enemy + ' would live, ' + name + '?')
setting = input()

print('On a scale of 1-10, how hard do you think it would be to get there?')
gt_setting = input()

treasure_type(t_enemy)
