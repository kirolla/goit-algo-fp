# Клас, що представляє одиничний предмет
class FoodItem:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    items.sort(key=lambda x: x.calories / x.cost, reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []
    for item in items:
        if total_cost + item.cost <= budget:
            total_cost += item.cost
            total_calories += item.calories
            selected_items.append(item.name)
    return selected_items, total_cost, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    K = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i - 1].cost <= w:
                K[i][w] = max(items[i - 1].calories + K[i - 1][w - items[i - 1].cost], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    res = K[n][budget]
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            selected_items.append(items[i - 1].name)
            res -= items[i - 1].calories
            w -= items[i - 1].cost

    return selected_items, budget - w, K[n][budget]

# Дані про страви
items_data = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Створення списку об'єктів FoodItem
items = [FoodItem(name, data["cost"], data["calories"]) for name, data in items_data.items()]

# Бюджет
budget = 100

# Виклик жадібного алгоритму
selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", selected_items_greedy)
print("Всього застрат:", total_cost_greedy)
print("Всього калорій:", total_calories_greedy)

# Виклик алгоритму динамічного програмування
selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nДинамічное програмування:")
print("Обрані страви:", selected_items_dp)
print("Всього застрат:", total_cost_dp)
print("Всього калорій:", total_calories_dp)