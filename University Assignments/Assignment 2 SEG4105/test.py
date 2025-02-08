def optimal_plan(low_stress_values, high_stress_values):
    n = len(low_stress_values)
    opt_values = [0] * (n + 1)
    choices = [""] * (n + 1)

    opt_values[1] = low_stress_values[0]
    opt_values[2] = max(low_stress_values[1], high_stress_values[1])

    for i in range(3, n + 1):
        option_low_stress = opt_values[i - 1] + low_stress_values[i - 1]
        option_high_stress = opt_values[i - 2] + high_stress_values[i - 1]
        option_none = opt_values[i - 1]

        print(i, option_low_stress, option_high_stress)
    
        if option_low_stress >= option_high_stress and option_low_stress >= option_none:
            opt_values[i] = option_low_stress
            choices[i] = "low-stress"
        elif option_high_stress >= option_low_stress and option_high_stress >= option_none:
            opt_values[i] = option_high_stress
            choices[i] = "high-stress"
        else:
            opt_values[i] = option_none
            choices[i] = "none"

    # Reconstruct the optimal plan
    plan = []
    i = n
    while i >= 1:
        print(choices[i])
        plan.append(choices[i])
        if choices[i] == "low-stress" or choices[i] == "none":
            i -= 1
        else:
            i -= 2

    plan.reverse()
    return opt_values[n], plan

# Example usage
low_stress_values = [10, 1, 10, 10]
high_stress_values = [5, 50, 5, 1]
max_value, optimal_plan = optimal_plan(low_stress_values, high_stress_values)
print("Maximum value:", max_value)
print("Optimal plan:", optimal_plan)