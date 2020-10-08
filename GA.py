import random
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!#%&/()=?@${[]}"

Target = "I love liujuying"
POPULATION_SIZE = 100


def mutated_genes():
    '''
    create random genes for mutation
    '''
    global GENES
    gene = random.choice(GENES)
    return gene

def create_gnome():
    global Target
    lenght = len(Target)
    gnome = ""
    for _ in xrange(lenght):
        gnome += mutated_genes()
    return gnome
def cal_fitness(wait):
    global Target
    fitness = 0
    lenght = len(Target)
    for i in xrange(lenght):
        if wait[i] != Target[i]:
            fitness += 1
    return fitness

def mate(a,b):
    length = len(a)
    child_gnome = ""
    for i in xrange(length):
        prob = random.random()
        if prob <0.45:
            child_gnome += a[i]
        elif prob <0.90:
            child_gnome += b[i]
        else:
            child_gnome += mutated_genes()
    return child_gnome


def sortPopulation(pop):
    length = len(pop)
    a =[]
    for i in xrange(length):
        astring = pop[i]
        astore = cal_fitness(astring)
        a.append(astore)
    for k in xrange(length-1):
        for j in xrange(length-k-1):
            if  a[j] > a[j+1]:
                mid = a[j]
                xmid = pop[j]
                a[j] = a[j+1]
                pop[j] = pop[j+1]
                a[j+1] = mid
                pop[j+1] = xmid
    return a


population = []
for _ in xrange(POPULATION_SIZE):
    gnome = create_gnome()
    population.append(gnome)

print population[0]

for i in xrange(80):
    sortPopulation(population)
    if cal_fitness(population[0]) == 0:
        print  population[0]
        break
    new_generation = []
    new_generation.extend(population[:10])
    for _ in xrange(90):
        parent1 = random.choice(population[:50])
        parent2 = random.choice(population[:50])
        child = mate(parent1,parent2)
        new_generation.append(child)
    population = new_generation
    if i == 79:
        print population[0]


