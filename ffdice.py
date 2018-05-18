from random import choice
from collections import Counter


#Takes the results list and randonly appends choices from the colour list that has been passed to results 
    
def roll(result, colour, dice):
    
    if dice > 0:
        for i in range(dice):
            result.append(choice(colour))

    return result

#Counts the number of results of a given type.
def countResult(result, resultType):
    c = Counter(result)
    
    return c[resultType] 

#Uses count result function to count and combine different types of results into a new result dictionary
def combine(result): 
    combResult = {'success': countResult(result, 's') + countResult(result, 'ds')*2 + countResult(result, 'sb')}
    combResult['boon'] = countResult(result, 'b') + countResult(result, 'db')*2 + countResult(result, 'sb')
    combResult['triumph'] = countResult(result, 'tri')
    combResult['failure'] = countResult(result, 'f') + countResult(result, 'df')*2 + countResult(result, 'ft')
    combResult['threat'] = countResult(result, 't') + countResult(result, 'dt')*2 + countResult(result, 'ft')
    combResult['despair'] = countResult(result, 'des')
    
    return combResult 

#Adds success and failures and other result types and then subtracts their opposites
def add(result):
    addedResult = {'combSuccess': (result['success'] + result['triumph']) - (result['failure'] + result['despair'])}
    addedResult ['combBoon'] = result['boon'] - result['threat']
    addedResult ['triumph'] = result['triumph']
    addedResult ['despair'] = result['despair']

    return addedResult

#Gets the number of each die type from input
def dieNum():
    dice = {'yellow': 0, 'green': 0, 'blue': 0, 'red': 0, 'purple': 0, 'black': 0}
    for key in dice:
        print('How many' , key, 'dice?')
        dice[key] = int(input('> ')) 
        
    return dice
#Creates dictionaries for each die colour type, iterates through them to get dice number for each then combines and adds the results.
def rollIter(result, dice):

    # bl = blank, s = success, ds = double sucess, b = boon, sb = success and boon, db = success and boon and tri = triump
    # f = failure, df = double failure, t = threat, ft = failure threat, dt = double threat, des = despair
    yellow = ['bl', 's', 's', 'ds', 'ds', 'b', 'sb', 'sb', 'sb', 'db', 'db', 'tri']
    green = ['bl', 's', 's', 'ds', 'b', 'b', 'sb', 'db']
    blue = ['bl', 'bl', 's', 'sb', 'db', 'b']
    red = ['bl', 'f', 'f', 'df', 'df', 't', 't', 'ft', 'ft', 'dt', 'dt', 'des']
    purple = ['bl', 'f', 'df', 't', 't', 't', 'dt', 'ft']
    black = ['bl', 'bl', 'f', 'f', 't', 't']
    colourList = [yellow, green, blue, red, purple, black]
    i = 0
    for key in dice:
        result = roll(result, colourList[i], dice[key])
        i += 1
    result = add(combine(result))

    return result
