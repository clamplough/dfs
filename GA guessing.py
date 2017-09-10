import random
import string
import time

def start_pop( pop_size, goal ):
    pop = dict()
    for i in range(pop_size):
        text = ''
        for j in range(len(goal)):
            text += random.choice(letters)
        pop[text] = 0
    return pop

def calc_fitness( pop, goal ):
    limits = set()
    scores = list()
    temp_pop = dict()
    for word in pop:
        score = 0
        for i in range(len(word)):
            if word[i] == goal[i]:
                score += 1
        pop[word] = score

        #new calculation
        if score not in temp_pop:
            temp_pop[score] = list()
        temp_pop[score].append(word)
       
        #limit calc
        limits.add(score)
        scores.append(score)
    #probably need to calculate this differently once a score of 3 is met (perhaps by ranking it all)
    pop = temp_pop
    return pop, limits

def selection_criteria( limits ):
    scores = sorted(limits)
    probs = [0]
    S = max( 1, sum(scores) ) #catches error where sum == 0 
    M = max(scores)
    U = (2 + M)/M #sum of P's
    for i in range(len(scores)):
        L = sorted(scores)[i]
        P = (1+L)/S
        probs.append( P/U + probs[-1] )
    return probs[1:]
    
def new_generation( goal, pop, pop_size, letters, probs ):
    new_pop = list()
    for i in range(pop_size):
        pA, pB = get_parents( pop, probs )
        count = len(pA)
        child = ''
        for L in range(count):
            #mutation
            if random.random() < 0.05:
                child += random.choice(letters)
            #parent A
            elif random.random() < 0.5:
                child += pA[L]
            #parent B
            else:
                child += pB[L]
        new_pop.append(child)
    return new_pop
    
def reset_generation( pop ):
    new_pop = dict()
    for item in pop:
        new_pop[ item ] = 0
    return new_pop
    
def get_parents( pop, probs ):
    parents = list()
    for i in range(2):
        val = random.random()
        for score in range(len(probs)):
            if val > probs[score]:
                continue
            else:
                break
            
        #correct for error where dictionary is missing score entry
        try:
            handle = pop[score]
        except:
            try:
                handle = pop[ max(0, score - 1) ]
            except:
                max_score_key = sorted( pop.keys() )[-1]
                handle = pop[ max_score_key ]
              
        parent = random.choice( handle )
        parents.append( parent )
    return parents[0], parents[1]

def guess( pop, goal ):
    string = ''
    for i in range(len(goal)):
        letters = dict()
        for word in pop:
            if word[i] not in letters.keys():
                letters[ word[i] ] = 0
            letters[ word[i] ] += 1
        char = '-'
        count = 0
        for L in letters:
            if letters[L] > count:
                count = letters[L]
                char = L
        string += char
    return string
        
#global vars
goal = 'random text'
letters = string.ascii_letters[:26] + ' '
pop_size = 200
gen_limit = 30

gen = 0
converge = False
pop = start_pop( pop_size, goal )
while gen < gen_limit and not converge:
    gen += 1
    pop, limits = calc_fitness( pop, goal )
    probs = selection_criteria( limits )
    pop = new_generation( goal, pop, pop_size, letters, probs )
    if goal in pop:
        converge = True
        i = pop.index(goal)
        print('Found it at generation:', gen)
        print('\"{:s}\"'.format(pop[i]))
    pop = reset_generation( pop )
    
if not converge:
    print('Did Not Converge!\nBest Guess:', guess(pop, goal) )