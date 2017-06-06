#Rewite functions in 'storymaker.py'
def name():
    name_ = input('What is your first name?  ')
    print('Nice name!')
    input()

    return name_
def gender():
    ''' (NoneType) -> list of str and int'''

    while True:
        z = input('Are you a boy(1) or a girl(2)?')
        if z[0] == '1' or z[0] == 'b' or z[0] == 'B':
            a = 'boy'
            b = 'he'
            c = 1
            break
        if z[0] == '2' or z[0] == 'g' or z[0] == 'G':
            a = 'girl'
            b = 'she'
            c = 2
            break

    input()
    L = [a, b, c]
    return L

def mob_type(name):
    ''' (str) -> str'''

    while True:
        print('Okay ' + name + ', would you rather battle a fiery dragon, a hill giant, a poisonous snake, or a mountain troll?')
        enemy = input()
        enemy = enemy.lower()
        if enemy[0] == 'h' or enemy[0] == 'h':
            print('Have you ever seen one? No, of course you haven\'t.')
            enemy_ = 'hill giant'
            break
        if enemy[0] == 'd' or enemy[0] == 'f':
            print('Yeah, their fire is WAY too powerful.')
            enemy_ = 'fiery dragon'
            break
        if enemy[0] == 'p' or enemy[0] == 's':
            print('BEWARE their fangs!')
            enemy_ = 'poisonous snake'
            break
        if enemy[0] == 'm' or enemy[0] == 't':
            print('They smell REALLY bad, you know.')
            enemy_ = 'mountain troll'
            break
        else:
            print('Please enter one of the GIVEN choices.')
            input()

    input()
    return enemy_
def age_find():
    ''' (NoneType) -> ?'''

def story_1():
    ''' (NoneType) -> ?'''

def treasure_type():
    ''' (NoneType) -> ?'''

