facts = {'rain', 'sprinkler'}

rules = [
    (['rain'], 'wet_grass'),
    (['sprinkler'], 'wet_grass'),
    (['wet_grass'], 'slippery_walkway'),
    (['slippery_walkway'], 'dangerous')
]

changed = True

while changed:

    changed = False

    for condition, result in rules:

        valid = True

        for item in condition:

            if item not in facts:
                valid = False

        if valid and result not in facts:

            facts.add(result)

            print("Derived :", result)

            changed = True

print("Final Facts :", facts)






facts = {'rain', 'sprinkler'}

rules = {
    'wet_grass': ['rain'],
    'slippery_walkway': ['wet_grass'],
    'dangerous': ['slippery_walkway']
}

goal = 'dangerous'

def backward(goal):

    if goal in facts:
        return True

    if goal not in rules:
        return False

    conditions = rules[goal]

    for item in conditions:

        if backward(item) == False:
            return False

    return True

if backward(goal):
    print("Goal Achieved")
else:
    print("Goal Not Achieved")