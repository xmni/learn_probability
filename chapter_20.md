---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
downloads:
  - file: notebooks/chapter_20.ipynb
---

# فصل ۲۰: احتمال نمادین با SymPy

+++

به فصل ۲۰ خوش آمدید! در سراسر این کتاب از NumPy و SciPy برای محاسبات عددی استفاده کردیم — محاسبهٔ احتمال‌ها به‌صورت تقریب اعشاری، شبیه‌سازی فرایندهای تصادفی و رسم توزیع‌ها. این رویکرد عددی برای بیشتر کاربردهای واقعی قدرتمند و عملی است.

با این حال، راه دیگری برای کار با احتمال وجود دارد: **محاسبهٔ نمادین**. به‌جای دریافت `0.16666...` هنگام محاسبهٔ احتمال آمدن ۱ روی یک تاس منصفانه، می‌توانیم پاسخ دقیق `1/6` را به‌دست آوریم. به‌جای ارزیابی عددی انتگرال‌ها یا مشتق‌ها، می‌توانیم فرمول‌ها را جبری دستکاری کنیم.

این فصل **SymPy** (Symbolic Python)، کتابخانهٔ پایتون برای ریاضیات نمادین را معرفی می‌کند. SymPy به ما امکان می‌دهد:
- با کسرهای دقیق به‌جای تقریب‌های اعشاری کار کنیم
- فرمول‌های احتمال را با پارامترهای نمادین استخراج کنیم
- توزیع‌های احتمال را جبری دستکاری کنیم
- فرمول‌ها و اثبات‌های کتاب‌های درسی را تأیید کنیم
- محاسبات عددی را با ریاضیات خالص پیوند دهیم

+++

## اهداف یادگیری

* درک زمان استفاده از محاسبهٔ نمادین در مقابل عددی
* کار با احتمال‌های دقیق با استفاده از کسرهای SymPy
* استفاده از SymPy برای ترکیبیات نمادین (فاکتوریل‌ها، دوجمله‌ای‌ها)
* ایجاد و دستکاری متغیرهای تصادفی نمادین با `sympy.stats`
* محاسبهٔ احتمال‌ها، امیدها و واریانس‌ها به‌صورت نمادین
* استخراج فرمول‌های احتمال با پارامترهای نمادین
* تبدیل بین نمایش‌های نمادین و عددی

+++

## چرا محاسبهٔ نمادین؟

### رویکردهای عددی در مقابل نمادین

در سراسر این کتاب عمدتاً از **رویکرد عددی** استفاده کردیم:

```{code-cell} ipython3
import numpy as np
from scipy import stats

# Numerical: Probability of getting exactly 3 heads in 5 coin flips
prob_numerical = stats.binom.pmf(k=3, n=5, p=0.5)
print(f"Numerical result: {prob_numerical}")
print(f"As decimal: {prob_numerical:.10f}")
```

رویکرد عددی تقریب ممیزشناور به ما می‌دهد. برای بیشتر اهداف عملی این کافی است! اما اگر **پاسخ دقیق** بخواهیم چه؟

```{code-cell} ipython3
import sympy as sp
from sympy.stats import Binomial, P, E, variance

# Symbolic: Same problem with exact arithmetic
n, k = 5, 3
p_sym = sp.Rational(1, 2)  # Exact 1/2, not 0.5

# Calculate using combinatorics
prob_symbolic = sp.binomial(n, k) * p_sym**k * (1-p_sym)**(n-k)
print(f"Symbolic result: {prob_symbolic}")
print(f"Simplified: {sp.simplify(prob_symbolic)}")
print(f"As decimal: {float(prob_symbolic)}")
```

+++

### چه زمانی از هر رویکرد استفاده کنیم

**از رویکرد عددی (NumPy/SciPy) استفاده کنید وقتی:**
- با داده‌ها یا اندازه‌گیری‌های دنیای واقعی کار می‌کنید
- شبیه‌سازی با مجموعه‌داده‌های بزرگ اجرا می‌کنید
- سرعت حیاتی است
- تقریب‌های اعشاری کافی‌اند
- با توزیع‌های پیوسته‌ای کار می‌کنید که شکل بسته ندارند

**از رویکرد نمادین (SymPy) استفاده کنید وقتی:**
- به پاسخ‌های دقیق نیاز دارید (کسرها، عبارات با π، e، √2)
- فرمول‌ها را با پارامترهای ناشناخته استخراج می‌کنید
- تدریس یا یادگیری می‌کنید (پاسخ‌های دقیق به درک کمک می‌کنند)
- اثبات‌های ریاضی را تأیید می‌کنید
- با مسائل گسستهٔ کوچک کار می‌کنید
- می‌خواهید عبارات جبری را دستکاری کنید

**بهترین روش:** با نمادین شروع کنید تا ریاضیات را بفهمید، سپس برای محاسبه از عددی استفاده کنید.

+++

## مبانی SymPy برای احتمال

### اعداد دقیق: Rational در مقابل Float

```{code-cell} ipython3
import sympy as sp

# The difference between symbolic and numerical
print("Floating point (numerical):")
print(f"  1/3 = {1/3}")
print(f"  1/3 + 1/3 + 1/3 = {1/3 + 1/3 + 1/3}")

print("\nRational (symbolic):")
one_third = sp.Rational(1, 3)
print(f"  1/3 = {one_third}")
print(f"  1/3 + 1/3 + 1/3 = {one_third + one_third + one_third}")
```

این حساب دقیق برای محاسبات احتمالی حیاتی است!

+++

### ترکیبیات نمادین

SymPy نسخه‌های نمادین توابع ترکیبیاتی که استفاده کرده‌ایم را فراهم می‌کند:

```{code-cell} ipython3
# Comparison with math and scipy.special
import math
from scipy.special import comb, perm

n, k = 10, 3

print("=== Factorials ===")
print(f"math.factorial(10) = {math.factorial(n)}")
print(f"sp.factorial(10) = {sp.factorial(n)}")

# Symbolic with variables
n_sym, k_sym = sp.symbols('n k', integer=True, positive=True)
print(f"\nSymbolic: n! = {sp.factorial(n_sym)}")

print("\n=== Permutations ===")
print(f"scipy perm(10, 3) = {perm(n, k, exact=True)}")
print(f"SymPy P(10, 3) = {sp.factorial(n) / sp.factorial(n-k)}")

print("\n=== Combinations ===")
print(f"scipy comb(10, 3) = {comb(n, k, exact=True)}")
print(f"SymPy C(10, 3) = {sp.binomial(n, k)}")

# With symbolic parameters
print(f"\nSymbolic: C(n, k) = {sp.binomial(n_sym, k_sym)}")
```

+++

### ساده‌سازی عبارات

یکی از قدرت‌های SymPy ساده‌سازی عبارات پیچیده است:

```{code-cell} ipython3
n, k = sp.symbols('n k', integer=True, positive=True)

# Probability of exactly k successes in n Bernoulli trials
p = sp.Symbol('p', real=True, positive=True)
q = 1 - p

# Binomial probability formula
binomial_pmf = sp.binomial(n, k) * p**k * q**(n-k)
print("Binomial PMF:")
print(f"  Original: {binomial_pmf}")
print(f"  Expanded: {sp.expand(binomial_pmf)}")

# Verify that probabilities sum to 1 (for small n)
n_val = 3
total_prob = sum(binomial_pmf.subs(n, n_val).subs(k, i) for i in range(n_val + 1))
print(f"\nSum of probabilities (n=3): {sp.simplify(total_prob)}")
```

+++

## متغیرهای تصادفی نمادین با sympy.stats

ماژول `sympy.stats` به ما امکان می‌دهد با متغیرهای تصادفی به‌صورت نمادین کار کنیم؛ مشابه نحوهٔ استفادهٔ عددی از `scipy.stats`.

### توزیع‌های گسسته

```{code-cell} ipython3
from sympy.stats import Die, Coin, Binomial, Poisson, Geometric
from sympy.stats import P, E, variance, density, sample

# Fair six-sided die
X = Die('X', 6)

print("=== Die Probabilities ===")
print(f"P(X = 3) = {P(X == 3)}")
print(f"P(X > 4) = {P(X > 4)}")
print(f"P(X is even) = {P(X % 2 == 0)}")  # Note: May not simplify automatically

print(f"\nE(X) = {E(X)}")
print(f"Var(X) = {variance(X)}")
```

```{code-cell} ipython3
# Binomial distribution
n_trials = sp.Symbol('n', integer=True, positive=True)
p_success = sp.Symbol('p', real=True, positive=True)

# Create symbolic binomial random variable
X_binom = Binomial('X', 10, sp.Rational(1, 2))

print("=== Binomial(10, 1/2) ===")
print(f"P(X = 5) = {P(X_binom == 5)}")
print(f"P(X <= 3) = {P(X_binom <= 3)}")
print(f"E(X) = {E(X_binom)}")
print(f"Var(X) = {variance(X_binom)}")

# With symbolic parameters - expectations and variances
X_sym = Binomial('X', n_trials, p_success)
print(f"\n=== Binomial(n, p) - Symbolic ===")
print(f"E(X) = {E(X_sym)}")
print(f"Var(X) = {variance(X_sym)}")
```

```{code-cell} ipython3
# Geometric distribution
p_geo = sp.Rational(1, 6)  # Probability of rolling a 6
X_geo = Geometric('X', p_geo)

print("=== Geometric(1/6) - First success ===")
print(f"P(X = 1) = {P(X_geo == 1)}")  # Success on first trial
print(f"P(X = 6) = {P(X_geo == 6)}")  # Success on sixth trial
print(f"E(X) = {E(X_geo)}")
print(f"Var(X) = {variance(X_geo)}")
```

+++

### توزیع‌های پیوسته

```{code-cell} ipython3
from sympy.stats import Normal, Exponential, Uniform, ContinuousRV
from sympy import exp, pi, sqrt, oo

# Normal distribution with symbolic parameters
mu, sigma = sp.symbols('mu sigma', real=True)
sigma_pos = sp.Symbol('sigma', positive=True, real=True)

X_norm = Normal('X', mu, sigma_pos)

print("=== Normal(μ, σ) - Symbolic ===")
print(f"E(X) = {E(X_norm)}")
print(f"Var(X) = {variance(X_norm)}")

# With specific values
X_standard = Normal('Z', 0, 1)
print(f"\n=== Standard Normal(0, 1) ===")
print(f"E(Z) = {E(X_standard)}")
print(f"Var(Z) = {variance(X_standard)}")

# Probability calculations (may be slow for symbolic results)
X_concrete = Normal('X', 100, 15)
print(f"\n=== Normal(100, 15) ===")
print(f"P(X > 115) = {P(X_concrete > 115)}")  # Returns in terms of erf
```

```{code-cell} ipython3
# Exponential distribution
lambda_sym = sp.Symbol('lambda', positive=True)
rate = sp.Rational(1, 2)

X_exp = Exponential('X', rate)
print("=== Exponential(λ=1/2) ===")
print(f"E(X) = {E(X_exp)}")
print(f"Var(X) = {variance(X_exp)}")

# Symbolic rate parameter
X_exp_sym = Exponential('X', lambda_sym)
print(f"\n=== Exponential(λ) - Symbolic ===")
print(f"E(X) = {E(X_exp_sym)}")
print(f"Var(X) = {variance(X_exp_sym)}")
```

+++

## استخراج فرمول‌های احتمال

یکی از قدرتمندترین کاربردهای SymPy استخراج و تأیید فرمول‌های احتمال است.

### توابع تولید گشتاور

```{code-cell} ipython3
# Binomial MGF
n, p, t = sp.symbols('n p t', real=True)
n = sp.Symbol('n', integer=True, positive=True)
p = sp.Symbol('p', real=True, positive=True)

# MGF of Binomial: M(t) = (pe^t + q)^n where q = 1-p
q = 1 - p
mgf_binomial = (p * sp.exp(t) + q)**n

print("=== Binomial MGF ===")
print(f"M(t) = {mgf_binomial}")

# Expected value is the first derivative at t=0
mgf_derivative = sp.diff(mgf_binomial, t)
expected_value = mgf_derivative.subs(t, 0)
print(f"\nM'(t) = {mgf_derivative}")
print(f"E(X) = M'(0) = {sp.simplify(expected_value)}")

# Variance from second moment
mgf_second_derivative = sp.diff(mgf_binomial, t, 2)
second_moment = mgf_second_derivative.subs(t, 0)
variance_binomial = sp.simplify(second_moment - expected_value**2)
print(f"\nM''(0) = {sp.simplify(second_moment)}")
print(f"Var(X) = E(X²) - E(X)² = {variance_binomial}")
```

+++

### قضیهٔ بیز به‌صورت نمادین

```{code-cell} ipython3
# Symbolic Bayes' Theorem
# P(A|B) = P(B|A) * P(A) / P(B)

P_A, P_B, P_B_given_A = sp.symbols('P(A) P(B) P(B|A)', real=True, positive=True)

# Prior, likelihood, and evidence
prior = P_A
likelihood = P_B_given_A
evidence = P_B

# Posterior
posterior = (likelihood * prior) / evidence

print("=== Bayes' Theorem ===")
print(f"P(A|B) = {posterior}")

# Concrete example: Medical test
# Disease prevalence = 1%
# Test sensitivity (true positive rate) = 95%
# Test specificity (true negative rate) = 90%
# What's P(Disease|Positive) ?

P_disease = sp.Rational(1, 100)
P_no_disease = 1 - P_disease
P_pos_given_disease = sp.Rational(95, 100)
P_pos_given_no_disease = sp.Rational(10, 100)  # False positive = 1 - specificity

# Total probability of testing positive
P_positive = P_pos_given_disease * P_disease + P_pos_given_no_disease * P_no_disease

# Posterior: P(Disease|Positive)
P_disease_given_pos = (P_pos_given_disease * P_disease) / P_positive

print(f"\n=== Medical Test Example ===")
print(f"P(Disease) = {P_disease}")
print(f"P(Positive|Disease) = {P_pos_given_disease}")
print(f"P(Positive|No Disease) = {P_pos_given_no_disease}")
print(f"P(Positive) = {P_positive} = {float(P_positive):.4f}")
print(f"P(Disease|Positive) = {P_disease_given_pos} = {float(P_disease_given_pos):.4f}")
```

+++

## تبدیل بین نمادین و عددی

```{code-cell} ipython3
# Symbolic computation
from sympy.stats import Binomial, P, E
import numpy as np
from scipy import stats

n, p_val = 20, sp.Rational(3, 10)
X_sym = Binomial('X', n, p_val)

# Symbolic probability
prob_sym = P(X_sym == 5)
print(f"Symbolic: P(X=5) = {prob_sym}")
print(f"Exact fraction: {prob_sym}")

# Convert to float
prob_float = float(prob_sym)
print(f"As float: {prob_float}")

# Compare with scipy
prob_scipy = stats.binom.pmf(5, n, float(p_val))
print(f"SciPy numerical: {prob_scipy}")
print(f"Difference: {abs(prob_float - prob_scipy)}")

# Expected value comparison
exp_sym = E(X_sym)
exp_scipy = stats.binom.mean(n, float(p_val))
print(f"\nSymbolic E(X) = {exp_sym} = {float(exp_sym)}")
print(f"SciPy E(X) = {exp_scipy}")
```

+++

## مثال‌های عملی

### مثال ۱: احتمال‌های دقیق پوکر

```{code-cell} ipython3
# Calculate exact probability of a full house in 5-card poker

# Total 5-card hands
total_hands = sp.binomial(52, 5)

# Full house: 3 of one rank, 2 of another
# Choose rank for triple: C(13, 1)
# Choose 3 suits from 4: C(4, 3)
# Choose rank for pair: C(12, 1)  # Can't be same as triple
# Choose 2 suits from 4: C(4, 2)

ways_full_house = sp.binomial(13, 1) * sp.binomial(4, 3) * sp.binomial(12, 1) * sp.binomial(4, 2)
prob_full_house = sp.Rational(ways_full_house, total_hands)

print(f"Total 5-card hands: {total_hands}")
print(f"Ways to get full house: {ways_full_house}")
print(f"Probability (exact): {prob_full_house}")
print(f"Probability (decimal): {float(prob_full_house):.6f}")
print(f"Odds: 1 in {float(1/prob_full_house):.2f}")
```

+++

### مثال ۲: مسئلهٔ تولد — راه‌حل دقیق

```{code-cell} ipython3
# What's the probability that in a group of n people, at least 2 share a birthday?

def birthday_probability_exact(n):
    """Calculate exact probability using SymPy"""
    # P(at least 2 share) = 1 - P(all different)
    # P(all different) = 365/365 * 364/365 * 363/365 * ... * (365-n+1)/365

    prob_all_different = sp.Rational(1, 1)
    for i in range(n):
        prob_all_different *= sp.Rational(365 - i, 365)

    prob_at_least_two_share = 1 - prob_all_different
    return prob_at_least_two_share

# Test for different group sizes
for n in [10, 20, 23, 30, 50]:
    prob = birthday_probability_exact(n)
    print(f"n={n:2d}: P(at least 2 share) = {float(prob):.6f}")

# The famous n=23 case
prob_23 = birthday_probability_exact(23)
print(f"\nExact probability for n=23: {float(prob_23):.10f}")
print(f"Greater than 50%? {float(prob_23) > 0.5}")
```

+++

### مثال ۳: استخراج فرمول واریانس

```{code-cell} ipython3
# Prove that Var(X) = E(X²) - E(X)² symbolically

from sympy.stats import DiscreteRV, E, variance

# Create a simple discrete RV
x = sp.Symbol('x')
X = DiscreteRV(x, {1: sp.Rational(1,6),
                    2: sp.Rational(1,6),
                    3: sp.Rational(1,6),
                    4: sp.Rational(1,6),
                    5: sp.Rational(1,6),
                    6: sp.Rational(1,6)})

# Method 1: Using variance function
var_direct = variance(X)

# Method 2: E(X²) - E(X)²
E_X = E(X)
E_X_squared = E(X**2)
var_formula = E_X_squared - E_X**2

print(f"E(X) = {E_X}")
print(f"E(X²) = {E_X_squared}")
print(f"\nVar(X) using variance(): {var_direct}")
print(f"Var(X) using E(X²) - E(X)²: {sp.simplify(var_formula)}")
print(f"Are they equal? {sp.simplify(var_direct - var_formula) == 0}")
```

+++

## کار با توزیع‌های مشترک

```{code-cell} ipython3
from sympy.stats import Die, P, E

# Two independent dice
X = Die('X', 6)
Y = Die('Y', 6)

# Sum of two dice
S = X + Y

print("=== Sum of Two Dice ===")
print(f"P(S = 7) = {P(S == 7)}")
print(f"P(S = 12) = {P(S == 12)}")
print(f"P(S > 10) = {P(S > 10)}")

print(f"\nE(X) = {E(X)}")
print(f"E(Y) = {E(Y)}")
print(f"E(X + Y) = {E(S)}")
print(f"Verify: E(X) + E(Y) = {E(X) + E(Y)}")

# Conditional probability
print(f"\n=== Conditional Probabilities ===")
# P(X=6 | X+Y=10)
# Using sympy.stats conditional might be complex, so we'll use the definition
# P(X=6, X+Y=10) / P(X+Y=10)
```

+++

## محدودیت‌ها و ملاحظات کارایی

SymPy قدرتمند است، اما محدودیت‌هایی دارد:

```{code-cell} ipython3
import time

# SymPy can be slow for complex symbolic computations
print("=== Performance Comparison ===")

# Numerical computation (fast)
start = time.time()
result_numerical = stats.binom.pmf(50, 100, 0.5)
time_numerical = time.time() - start

# Symbolic computation (slower)
start = time.time()
X_sym = Binomial('X', 100, sp.Rational(1, 2))
result_symbolic = float(P(X_sym == 50))
time_symbolic = time.time() - start

print(f"Numerical (SciPy): {result_numerical:.10f} in {time_numerical:.6f}s")
print(f"Symbolic (SymPy):  {result_symbolic:.10f} in {time_symbolic:.6f}s")
print(f"Speedup: {time_symbolic/time_numerical:.1f}x slower")
```

**نکات کلیدی:**
- SymPy از NumPy/SciPy کندتر است
- SymPy را برای پاسخ‌های دقیق و استخراج فرمول‌ها به‌کار ببرید، نه محاسبات در مقیاس بزرگ
- وقتی به سرعت نیاز دارید به عددی تبدیل کنید
- برخی عملیات نمادین ممکن است به‌طور خودکار ساده نشوند

+++

## خلاصه

در این فصل **محاسبهٔ احتمال نمادین** با SymPy را بررسی کردیم:

**مفاهیم کلیدی:**
- **حساب دقیق** با `sp.Rational` در مقابل تقریب ممیزشناور
- **ترکیبیات نمادین**: `sp.factorial`، `sp.binomial`
- **متغیرهای تصادفی نمادین** با `sympy.stats`
- **استخراج فرمول‌ها** با پارامترهای نمادین
- **تبدیل** بین نمایش‌های نمادین و عددی

**چه زمانی از SymPy استفاده کنیم:**
- نیاز به پاسخ‌های دقیق (کسرها، عبارات)
- استخراج فرمول‌ها با پارامترهای ناشناخته
- تأیید اثبات‌های ریاضی
- تدریس و یادگیری نظریهٔ احتمال
- مسائل احتمال گسستهٔ کوچک

**چه زمانی از NumPy/SciPy استفاده کنیم:**
- داده‌ها و اندازه‌گیری‌های دنیای واقعی
- شبیه‌سازی‌های در مقیاس بزرگ
- سرعت حیاتی است
- توزیع‌های پیوسته بدون شکل بسته

**بهترین روش:** از SymPy برای درک ریاضیات استفاده کنید، سپس از NumPy/SciPy برای محاسبهٔ عملی.

در فصل بعدی **SageMath** را بررسی می‌کنیم؛ سامانهٔ نرم‌افزاری جامع ریاضی که قدرت SymPy، NumPy و بسیاری ابزارهای دیگر را در یک محیط یکپارچه گرد هم می‌آورد.

+++

## تمرین‌ها

1. **پرتاب سکهٔ دقیق**: احتمال دقیق آمدن دقیقاً ۷ شیر در ۱۰ پرتاب سکهٔ منصفانه را با SymPy محاسبه کنید. با SciPy مقایسه کنید.

2. **واریانس نمادین**: متغیر تصادفی نمادینی با توزیع پواسون و پارامتر λ بسازید. $E(X)$ و $Var(X)$ را به‌صورت نمادین استخراج کنید.

3. **دست‌های پوکر**: احتمال دقیق گرفتن «استریت فلاش» (۵ کارت متوالی از یک خال) در پوکر ۵ کارتی را محاسبه کنید.

4. **احتمال شرطی**: با دو تاس نمادین $X$ و $Y$، مقدار دقیق $P(X = 4 | X + Y = 9)$ را محاسبه کنید.

5. **استخراج MGF**: تابع تولید گشتاور توزیع هندسی با پارامتر $p$ را استخراج کنید و با آن $E(X)$ و $Var(X)$ را بیابید.

6. **توسعهٔ مسئلهٔ تولد**: مسئلهٔ تولد را تغییر دهید تا کوچک‌ترین اندازهٔ گروهی را بیابید که در آن $P(\text{at least 2 shared birthdays}) > 0.9$.

7. **به‌روزرسانی Bayesian inference**: بیماری نادری ۰٫۱٪ جمعیت را مبتلا می‌کند. آزمون ۹۹٪ دقیق است (هم حساسیت و هم ویژگی). اگر مثبت شوید، احتمال دقیق ابتلا به بیماری چقدر است؟

8. **مجموع یکنواخت‌ها**: دو متغیر تصادفی گسستهٔ یکنواخت مستقل روی $\{1,2,3,4,5,6\}$ بسازید. تابع جرم احتمال دقیق مجموع آن‌ها را بیابید.

+++

## مطالعهٔ بیشتر

- **SymPy Documentation**: https://docs.sympy.org/
- **SymPy Stats Module**: https://docs.sympy.org/latest/modules/stats.html
- **SymPy Tutorial**: https://docs.sympy.org/latest/tutorial/index.html
- **Computer Algebra Systems in Education**: Various papers on using CAS for teaching probability and statistics
