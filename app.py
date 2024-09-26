from flask import Flask, render_template

app = Flask(__name__)

# Data from the problem
items = [
    {'weight': 3, 'value': 6, 'max_qty': 3},
    {'weight': 4, 'value': 8, 'max_qty': 2},
    {'weight': 5, 'value': 10, 'max_qty': 2},
    {'weight': 6, 'value': 12, 'max_qty': 1},
    {'weight': 7, 'value': 14, 'max_qty': 2},
    {'weight': 2, 'value': 4, 'max_qty': 4},
    {'weight': 1, 'value': 3, 'max_qty': 5},
    {'weight': 9, 'value': 16, 'max_qty': 1},
]

max_capacity = 20  # Maximum capacity of the knapsack

# Recursive function for backtracking (store all valid solutions)
def knapsack_backtracking(i, current_weight, current_value, selected_items, valid_solutions):
    if i == len(items):
        if current_weight <= max_capacity:
            valid_solutions.append((selected_items.copy(), current_value))
        return

    item = items[i]

    for qty in range(item['max_qty'] + 1):
        new_weight = current_weight + item['weight'] * qty
        new_value = current_value + item['value'] * qty

        if new_weight <= max_capacity:
            selected_items[i] = qty
            knapsack_backtracking(i + 1, new_weight, new_value, selected_items, valid_solutions)
        else:
            break

    selected_items[i] = 0  # Backtrack and reset

# Main function to start backtracking
def find_all_valid_combinations():
    valid_solutions = []
    selected_items = [0] * len(items)

    knapsack_backtracking(0, 0, 0, selected_items, valid_solutions)

    return valid_solutions

@app.route('/')
def index():
    valid_solutions = find_all_valid_combinations()

    # Output best solution
    max_solution = max(valid_solutions, key=lambda x: x[1]) if valid_solutions else ([], 0)
    
    return render_template('index.html', valid_solutions=valid_solutions, max_solution=max_solution)

if __name__ == '__main__':
    app.run(debug=True)
