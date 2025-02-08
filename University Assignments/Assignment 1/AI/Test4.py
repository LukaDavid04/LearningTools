import random
import math

weight = [46, 40, 42, 38, 10]
price = [12, 19, 19, 15, 8]
capacity = 40
weight = [1, 1, 2, 4, 12]
price = [1, 2, 2, 4, 10]
capacity = 15
initial = [0, 0, 0, 0, 0]
best_solution_price = 0
best_solution = []
initial_temperature = 1
candidate_price = 0
N = 10
cooling_rate = 0.95
flag = 0


def get_price(random_selection):
    price_of_bag = 0
    weight_of_bag = 0
    for i in range(5):
        if random_selection[i] == 1:
            price_of_bag += price[i]
            weight_of_bag += weight[i]
    if weight_of_bag > capacity:
        return 0
    return price_of_bag


def gen_random():
    while (True):
        random_selection = [0, 0, 0, 0, 0]
        for i in range(5):
            j = random.randint(0, 1)
            random_selection[i] = j
        if get_price(random_selection) != 0:
            break
    return random_selection


def gen_candidate(candidate):
    while (True):
        randint_location = random.randint(0, 4)
        if candidate[randint_location] == 0:
            candidate[randint_location] = 1
        else:
            candidate[randint_location] = 0
        candidate_price = get_price(candidate)
        if candidate_price != 0:
            break
    return candidate


initial = gen_random()
initial_price = get_price(initial)
while (initial_temperature > 0.01):
    for x in range(N):
        candidate = gen_candidate(initial)
        candidate_price = get_price(candidate)
        if candidate_price - initial_price > 0:
            initial_price = candidate_price
            initial = candidate
        else:
            r = random.random()
            objective_function = math.exp(
                (((candidate_price - initial_price)))/initial_temperature)
            if r < objective_function:
                initial_price = candidate_price
                initial = candidate
        initial_temperature *= cooling_rate
    best_solution_price = initial_price
    best_solution = initial


print("best solution: " + str(best_solution))
print("best solution price: " + str(best_solution_price))
