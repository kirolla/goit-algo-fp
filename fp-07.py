import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    # Створення словника для зберігання кількості випадань кожної суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Проведення симуляцій
    for _ in range(num_trials):
        # Кидок двох кубиків
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        # Оновлення кількості випадань для відповідної суми
        sums_count[total] += 1

    # Обчислення ймовірностей для кожної суми
    probabilities = {i: count / num_trials * 100 for i, count in sums_count.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}%")

def plot_probabilities(probabilities, num_trials):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірності сум чисел на двох кубиках (Метод Монте-Карло), {num_trials} симуляцій)')
    plt.xticks(range(2, 13))
    plt.show()

def main():
    trials = [100, 1000, 10000, 100000]
    for num_trials in trials:
        probabilities = monte_carlo_simulation(num_trials)
        print(f"Результати для {num_trials} симуляцій:")
        print_probabilities(probabilities)
        plot_probabilities(probabilities, num_trials)

if __name__ == "__main__":
    main()

