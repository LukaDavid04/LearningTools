import random
import math

weight = [46, 40, 42, 38, 10]
price = [12, 19, 19, 15, 8]
weight1 = [1, 1, 2, 4, 12]
price1 = [1, 2, 2, 4, 10]
capacity = 40
capacity1 = 15
best_solution_price = 0
best_solution = []
initial_temperature = 1
N = 10
cooling_rate = 0.95


def gen_random():
    random_selection = [0, 0, 0, 0, 0]
    for i in range(5):
        j = random.randint(0, 1)
        random_selection[i] = j
    return random_selection


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


def get_candidate(candidate):
    randint_location = random.randint(0, 4)
    if candidate[randint_location] == 0:
        candidate[randint_location] = 1
    else:
        candidate[randint_location] = 0
    return candidate


def get_change(x, x2):
    for i in range(5):
        if x[i] != x2[i]:
            return x[i]


def get_location(x, x2):
    print(x, x2)
    for i in range(5):
        if x[i] != x2[i]:
            return i


for z in range(N):
    while (initial_temperature > 0.01):
        initial_temperature *= cooling_rate
        x = gen_random()
        initial_price = get_price(x)
        if initial_temperature > random.random() and initial_price > 0:
            x2 = x
            randint_location = random.randint(0, 4)
            if x2[randint_location] == 0:
                x2[randint_location] = 1
            else:
                x2[randint_location] = 0
            randint_change = get_change(x, x2)
            price_of_bag = get_price(x2)
            if price_of_bag - initial_price > 0:
                best_solution_price = price_of_bag
                best_solution = x2
            else:
                r = random.random()
                if (get_change(x, x2) == 1):
                    objective_function = math.exp(
                        -price[get_location(x, x2)] / initial_temperature)
                else:
                    objective_function = math.exp(
                        price[get_location(x, x2)] / initial_temperature)
                if r < objective_function:
                    best_solution_price = get_price(x2)
                    best_solution = x2


print("best solution: " + str(best_solution))
print("best solution price: " + str(best_solution_price))
