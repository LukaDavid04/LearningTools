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


def accept(candidate_price, initial_price):
    if candidate_price - initial_price >= 0:
        return True
    else:
        r = random.random()
        if r < random.random():
            return True
        else:
            return False


for x in range(N):
    while (initial_temperature > 0.01):
        initial = gen_random()
        initial_price = get_price(initial)
        while (initial_price == 0):
            initial = gen_random()
            initial_price = get_price(initial)
        if initial_temperature > random.random():
            while (candidate_price == 0):
                candidate = initial
                randint_location = random.randint(0, 4)
                if candidate[randint_location] == 0:
                    candidate[randint_location] = 1
                else:
                    candidate[randint_location] = 0
                candidate_price = get_price(candidate)
            if candidate_price - initial_price > 0:
                best_solution_price = candidate_price
                best_solution = candidate
            else:
                r = random.random()
                if r < math.exp((-(initial_temperature - cooling_rate))/initial_temperature):
                    best_solution_price = candidate_price
                    best_solution = candidate
        initial_temperature *= cooling_rate


print("best solution: " + str(best_solution))
print("best solution price: " + str(best_solution_price))

# if flag:
#     objective_function = math.exp(
#         -price[randint_location] / initial_temperature)
# else:
#     objective_function = math.exp(
#         price[randint_location] / initial_temperature)
