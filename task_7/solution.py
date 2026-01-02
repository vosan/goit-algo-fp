import random
import sys


def simulate_two_dice(rolls):
    # counts[sum] stores how many times a particular sum (2..12) appeared
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(rolls):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1
    # convert counts to probabilities
    probs = {s: counts[s] / rolls for s in counts}
    return counts, probs


def analytical_probs():
    # Number of ways to get each sum with two dice
    ways = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    total = 36
    return {s: ways[s] / total for s in ways}


def main(argv):
    try:
        rolls = int(argv[1]) if len(argv) > 1 else 100_000
        if rolls <= 0:
            raise ValueError
    except ValueError:
        print("Usage: python task_7/solution.py [positive_number_of_rolls]")
        return

    counts, mc = simulate_two_dice(rolls)
    exact = analytical_probs()

    print(f"Monte Carlo simulation of two dice rolls: {rolls}")
    header = (
        "Sum",
        "Monte Carlo prob",
        "Analytical prob",
        "Absolute error",
        "Count",
    )
    print(f"{header[0]:>3}  {header[1]:>18}  {header[2]:>16}  {header[3]:>15}  {header[4]:>7}")
    for s in range(2, 13):
        p_mc = mc[s]
        p_ex = exact[s]
        err = abs(p_mc - p_ex)
        print(
            f"{s:>3}  {p_mc:18.4%}  {p_ex:16.4%}  {err:15.4%}  {counts[s]:7d}"
        )


if __name__ == "__main__":
    main(sys.argv)
