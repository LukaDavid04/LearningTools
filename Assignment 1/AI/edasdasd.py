import random
import math

# Define the knapsack problem parameters
knapsack_capacity = 15  # Maximum weight the knapsack can hold
items = [
    {"name": "Item1", "weight": 1, "value": 1},
    {"name": "Item2", "weight": 1, "value": 2},
    {"name": "Item3", "weight": 2, "value": 2},
    {"name": "Item4", "weight": 4, "value": 4},
    {"name": "Item5", "weight": 12, "value": 10},
]

# Simulated Annealing parameters
initial_temperature = 1
cooling_rate = 0.95
iterations_per_temperature = 10

# Initialize the current solution (randomly)
current_solution = [random.randint(0, 1) for _ in items]


def objective_function(solution):
    total_value = sum(item["value"] * solution[i]
                      for i, item in enumerate(items))
    total_weight = sum(item["weight"] * solution[i]
                       for i, item in enumerate(items))
    return total_value if total_weight <= knapsack_capacity else 0


def neighbor(solution):
    # Generate a neighbor solution by flipping the inclusion of a random item
    neighbor_solution = solution.copy()
    random_item_index = random.randint(0, len(items) - 1)
    neighbor_solution[random_item_index] = 1 - \
        neighbor_solution[random_item_index]
    return neighbor_solution


def acceptance_probability(current_value, neighbor_value, temperature):
    if neighbor_value > current_value:
        return 1.0  # Accept the better solution
    return math.exp((neighbor_value - current_value) / temperature)


# Initialize variables
best_solution = current_solution
best_value = objective_function(current_solution)
current_temperature = initial_temperature

# Simulated Annealing main loop
while current_temperature > 0.01:
    for _ in range(iterations_per_temperature):
        neighbor_solution = neighbor(current_solution)
        neighbor_value = objective_function(neighbor_solution)

        # Calculate the acceptance probability
        probability = acceptance_probability(
            best_value, neighbor_value, current_temperature)

        # Decide whether to accept the neighbor solution
        if random.random() < probability:
            current_solution = neighbor_solution
            current_value = neighbor_value

            # Update the best solution if needed
            if current_value > best_value:
                best_solution = current_solution
                best_value = current_value

    # Cool down the temperature
    current_temperature *= cooling_rate

# Print the best solution and its value
print("Best Solution:", best_solution)
print("Best Value:", best_value)
