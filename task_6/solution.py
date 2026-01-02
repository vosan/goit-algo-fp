def greedy_algorithm(items, budget):
    """Select items by maximizing total calories without exceeding budget (greedy algorithm)."""
    budget = max(0, int(budget))
    pairs = []
    for name, data in items.items():
        c = int(data.get("cost", 0))
        cal = int(data.get("calories", 0))
        if c <= 0 or cal <= 0:
            continue
        pairs.append((name, c, cal, cal / c))
    pairs.sort(key=lambda x: x[3], reverse=True)

    chosen = []
    total_cal = 0
    remain = budget
    for name, cost, cal, _ in pairs:
        if cost <= remain:
            chosen.append(name)
            total_cal += cal
            remain -= cost
    return chosen, total_cal


def dynamic_programming(items, budget):
    """Select items by maximizing total calories without exceeding budget (dynamic programming)."""
    budget = max(0, int(budget))

    norm = []  # (name, cost, calories)
    for name, data in items.items():
        c = int(data.get("cost", 0))
        cal = int(data.get("calories", 0))
        if 0 < c <= budget and cal > 0:
            norm.append((name, c, cal))

    n = len(norm)
    if n == 0 or budget == 0:
        return [], 0

    # dp[i][w] = max calories using first i items and budget w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        _, cost, cal = norm[i - 1]
        for w in range(budget + 1):
            best = dp[i - 1][w]
            if cost <= w:
                take = dp[i - 1][w - cost] + cal
                if take > best:
                    best = take
            dp[i][w] = best

    # reconstruct selection
    w = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, cal = norm[i - 1]
            selected.append(name)
            w -= cost
    selected.reverse()
    return selected, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def _output(budget: int):
    g_sel, g_cal = greedy_algorithm(items, budget)
    d_sel, d_cal = dynamic_programming(items, budget)
    print("=" * 40)
    print(f"Budget: {budget}")
    print("Greedy:")
    print("\tselected:", g_sel)
    print("\ttotal calories:", g_cal)
    print("Dynamic programming (optimal):")
    print("\tselected:", d_sel)
    print("\ttotal calories:", d_cal)
    print("=" * 40)


if __name__ == "__main__":
    _output(60) # An example where Greedy algorithm is coincidentally optimal
    _output(70) # An example where Greedy algorithm fails while DP remains optimal
