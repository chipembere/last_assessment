import random

activities = ['shopping', 'air travel', 'work', 'taxi', 'walking', 'pets', 'childcare', 'eating out', 'lunchtime', 'dinnertime', 'snacking', 'swimming', 'dancing', 'dating', 'exercising', 'cooking', 'growing up', 'booking a holiday', 'decorating a house', 'relaxing', 'chilling out']
people = ['mums', 'dads', 'children', 'brothers', 'sisters', 'families', 'married couples', 'teachers', 'unemployed people', 'wealthy people', 'politicians', 'aliens', 'farmers', 'city workers', 'teenagers', 'models', 'coach potatoes', 'pirates', 'waiters', 'air stewards', 'pilots', 'celebrities', 'average joes']

def getRandomIdea():
    i = random.randint(0, len(activities)-1)
    j = random.randint(0, len(people)-1)

    return activities[i].capitalize(), people[j].capitalize()
