import itertools
weight = [1, 1, 2, 4, 12]
price = [1, 2, 2, 4, 10]
weight_price = []
capacity = 15
best_solution_price = 0
best_solution = []
i = 0

for j in range(5):
    weight_price.append((weight[j], price[j]))

print(weight_price)

for x in range(6):
    for subset in itertools.combinations(weight_price, x):
        price_of_bag = 0
        weight_of_bag = 0
        print(i, subset)
        if i != 0:
            for p in subset:
                price_of_bag += p[1]
                weight_of_bag += p[0]
            print("price: " + str(price_of_bag) +
                  ", " + "weight: " + str(weight_of_bag))
            if weight_of_bag <= capacity and price_of_bag > best_solution_price:
                print("best solution for now: " + str(subset))
                best_solution_price = price_of_bag
                best_solution = subset
        i += 1

best_solution_list = [0, 0, 0, 0, 0]
for i in range(len(best_solution)):
    for j in range(len(weight_price)):
        if best_solution[i] == weight_price[j]:
            best_solution_list[j] = 1

print("best solution list: " + str(best_solution_list))

print("best solution: " + str(best_solution))
print("best solution price: " + str(best_solution_price))
