# Task 7 — Monte Carlo vs Analytical Probabilities (Two Dice)

This task compares **Monte Carlo–estimated probabilities** with **analytical (exact) probabilities** for the sum of two
fair six-sided dice.

The analytical distribution is known and fixed: each sum from 2 to 12 has a probability determined by the number of
possible dice combinations that produce it.  
The Monte Carlo approach estimates these probabilities empirically by simulating a large number of random dice rolls and
measuring how often each sum occurs.

## Methodology

- Two six-sided dice are rolled `N` times.
- The frequency of each possible sum (2–12) is recorded.
- Empirical probabilities are computed as `P(sum = k) ≈ count(k) / N`
- These empirical probabilities are compared against the exact analytical probabilities.
- Absolute errors are reported to quantify the difference.

## Results and Analysis

With **small numbers of rolls**, the Monte Carlo estimates fluctuate significantly due to randomness and insufficient
sampling. This leads to large deviations from the analytical probabilities:

```python task_7/solution.py 100```

Running this command multiple times produces noticeably different results each time, illustrating the high variance
inherent in low-sample simulations.

As the number of rolls increases, the empirical distribution stabilizes. The absolute errors decrease, and the Monte
Carlo probabilities converge toward the analytical values, demonstrating the Law of Large Numbers:

```python task_7/solution.py 1_000_000```

At high roll counts, the Monte Carlo simulation closely matches the analytical distribution, confirming that random
sampling can accurately approximate theoretical probabilities given sufficient trials.

## Conclusion

This task demonstrates that:

- Monte Carlo methods provide noisy estimates at low sample sizes.
- Increasing the number of simulations reduces variance and error.
- Given enough trials, empirical results converge to analytical probabilities.

This illustrates both the power and the limitations of Monte Carlo methods in probabilistic modeling.