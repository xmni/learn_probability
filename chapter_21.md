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
  - file: notebooks/chapter_21.ipynb
---

# فصل ۲۱: احتمال با SageMath

+++

به فصل ۲۱ خوش آمدید! در فصل پیشین SymPy را برای محاسبهٔ احتمال نمادین بررسی کردیم. اکنون **SageMath** (که اغلب فقط «Sage» نامیده می‌شود) را می‌شناسیم؛ سامانهٔ نرم‌افزاری ریاضی جامع و آزاد متن‌باز که قدرت بسیاری از کتابخانه‌های تخصصی از جمله NumPy، SciPy، SymPy، matplotlib و ده‌ها مورد دیگر را گرد هم می‌آورد.

SageMath بر پایهٔ پایتون ساخته شده اما با نحو ریاضی قدرتمند و قابلیت‌های گستردهٔ از پیش ساخته برای موارد زیر گسترش می‌یابد:
- محاسبات نمادین و عددی
- احتمال و آمار
- جبر خطی و حساب دیفرانسیل و انتگرال
- نظریهٔ اعداد و ترکیبیات
- نظریهٔ گراف و رمزنگاری
- و بسیار بیشتر

اگرچه می‌توان کل این کتاب را با SageMath نوشت، بر کتابخانه‌های استاندارد پایتون (NumPy، SciPy، SymPy) تمرکز کردیم چون در گردش‌کارهای علم داده و یادگیری ماشین رایج‌ترند. با این حال SageMath برای کار ریاضی مزایای منحصربه‌فردی دارد و شناخت آن ارزشمند است.

+++

## اهداف یادگیری

* درک SageMath و تفاوت آن با پایتون استاندارد
* راه‌اندازی و دسترسی به SageMath (محلی یا از طریق CoCalc)
* استفاده از SageMath برای ترکیبیات و محاسبات احتمال دقیق
* کار با توزیع‌های احتمال در SageMath
* بهره‌گیری از قابلیت‌های نمادین SageMath برای نظریهٔ احتمال
* مقایسهٔ SageMath با رویکردهای NumPy/SciPy/SymPy
* تصمیم‌گیری دربارهٔ زمان استفاده از SageMath در مقابل کتابخانه‌های استاندارد پایتون

+++

## SageMath چیست؟

### SageMath در مقابل پایتون + کتابخانه‌ها

**رویکرد پایتون استاندارد** (آنچه در این کتاب استفاده کردیم):
```python
import numpy as np
import scipy.stats as stats
import sympy as sp
import matplotlib.pyplot as plt
```

**رویکرد SageMath**:
- همهٔ کتابخانه‌های ریاضی اصلی از پیش یکپارچه‌اند
- نحو تقویت‌شده برای عملیات ریاضی
- پشتیبانی داخلی از حساب دقیق
- توابع ریاضی گسترده بدون نیاز به import
- محیط تعاملی (Sage REPL یا Jupyter)

**فلسفهٔ کلیدی**: SageMath می‌خواهد جایگزین آزاد و متن‌باز Mathematica، Maple و MATLAB باشد.

+++

## نصب و دسترسی

### گزینهٔ ۱: CoCalc (توصیه‌شده برای مبتدیان)

**CoCalc** (https://cocalc.com) بستر آنلاین رایگی است که SageMath را در مرورگر شما فراهم می‌کند:
- بدون نیاز به نصب
- شامل Jupyter notebook با کرنل SageMath
- سطح رایگان موجود
- قابلیت‌های همکاری
- ایده‌آل برای یادگیری و آزمایش

### گزینهٔ ۲: نصب محلی

**نصب SageMath به‌صورت محلی**:

**در Ubuntu/Debian:**
```bash
sudo apt-get install sagemath
```

**در macOS (با Homebrew):**
```bash
brew install --cask sagemath
```

**در Windows:**
- از https://www.sagemath.org/ دانلود کنید
- از WSL (Windows Subsystem for Linux) + نصب لینوکس استفاده کنید
- یا از Docker استفاده کنید

**از طریق Conda (غیررسمی):**
```bash
conda install -c conda-forge sage
```

### گزینهٔ ۳: Docker

```bash
docker pull sagemath/sagemath
docker run -p 8888:8888 sagemath/sagemath:latest sage-jupyter
```

### گزینهٔ ۴: SageMathCell

برای محاسبات سریع یک‌باره: https://sagecell.sagemath.org/

+++

:::{admonition} نکته دربارهٔ این فصل
:class: warning

مثال‌های کد این فصل برای اجرا به **SageMath** نیاز دارند. در محیط استاندارد Python/Jupyter کار نمی‌کنند.

برای اجرای این مثال‌ها:
- از CoCalc (https://cocalc.com) با کرنل SageMath استفاده کنید
- SageMath را محلی نصب کنید و از Sage notebook استفاده کنید
- برای مثال‌های تکی از SageMathCell (https://sagecell.sagemath.org/) استفاده کنید

مثال‌ها برای نمایش قابلیت‌ها و نحو SageMath ارائه شده‌اند.
:::

+++

## مبانی SageMath برای احتمال

### حساب دقیق به‌صورت پیش‌فرض

برخلاف پایتون که `1/3` مقدار `0.333...` می‌دهد، SageMath به‌صورت پیش‌فرض حساب دقیق فراهم می‌کند:

```python
# In SageMath (this would give exact result)
sage: 1/3
1/3

sage: 1/3 + 1/3 + 1/3
1

sage: sqrt(2)
sqrt(2)

sage: sqrt(2).n()  # .n() for numerical approximation
1.41421356237310

sage: pi
pi

sage: pi.n(digits=50)
3.1415926535897932384626433832795028841971693993751
```

این حساب دقیق شبیه SymPy است اما در هستهٔ زبان تعبیه شده است.

+++

### ترکیبیات در SageMath

SageMath پشتیبانی داخلی گسترده‌ای از ترکیبیات دارد:

```python
# Factorials
sage: factorial(10)
3628800

sage: factorial(100)  # Handles large numbers easily
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# Binomial coefficients
sage: binomial(10, 3)
120

sage: binomial(52, 5)  # Poker hands
2598960

# Permutations
sage: factorial(8) / factorial(8-3)  # P(8,3)
336

# SageMath also has Permutations class for working with permutation objects
sage: Permutations(3).list()
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

sage: Permutations(3).cardinality()
6

# Combinations as mathematical objects
sage: Combinations(5, 2).list()
[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]

sage: Combinations(5, 2).cardinality()
10
```

+++

### متغیرها و عبارات نمادین

```python
# Declare symbolic variables
sage: var('n k p')
(n, k, p)

# Binomial probability formula
sage: prob = binomial(n, k) * p^k * (1-p)^(n-k)
sage: prob
(p - 1)^(-k + n)*p^k*binomial(n, k)

# Substitute values
sage: prob.subs(n=10, k=3, p=1/2)
15/128

# Simplify
sage: expr = (n * (n-1)) / n
sage: expr.simplify()
n - 1

# Expand
sage: expand((p + (1-p))^5)
1
```

+++

## توزیع‌های احتمال در SageMath

SageMath چند راه برای کار با توزیع‌های احتمال فراهم می‌کند.

### استفاده از SciPy از طریق SageMath

SageMath شامل SciPy است، بنابراین می‌توانید دقیقاً همان‌طور که در سراسر این کتاب استفاده کردیم از آن بهره ببرید:

```python
sage: import scipy.stats as stats
sage: stats.binom.pmf(3, 10, 0.5)
0.1171875
```

### احتمال نمادین با SageMath

```python
# Exact probability calculations
sage: var('n k p')
sage: binomial_prob = binomial(n,k) * p^k * (1-p)^(n-k)

# Calculate for specific values
sage: binomial_prob(n=5, k=2, p=1/2)
5/16

# Verify sum to 1
sage: n_val = 5
sage: sum(binomial_prob(n=n_val, k=k_val, p=1/2) for k_val in range(n_val+1))
1
```

### توزیع‌های گسسته

```python
# Creating a discrete probability distribution
sage: def coin_flip():
....:     return 'H' if random() < 0.5 else 'T'

sage: # Simulate flips
sage: [coin_flip() for _ in range(10)]
['T', 'H', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T']

# Using GeneralDiscreteDistribution
sage: outcomes = [1, 2, 3, 4, 5, 6]
sage: probabilities = [1/6] * 6
sage: die_dist = GeneralDiscreteDistribution(probabilities)

sage: # Sample from distribution
sage: [outcomes[die_dist.get_random_element()] for _ in range(10)]
[4, 1, 6, 2, 3, 5, 1, 6, 4, 2]
```

+++

## مثال‌های پیشرفتهٔ ترکیبیات

### مثال ۱: احتمال‌های دست پوکر

```python
sage: # Total 5-card poker hands
sage: total_hands = binomial(52, 5)
sage: total_hands
2598960

sage: # Royal flush: A,K,Q,J,10 of same suit
sage: royal_flush = 4  # One per suit
sage: prob_royal_flush = royal_flush / total_hands
sage: prob_royal_flush
1/649740

sage: # Full house: 3 of one rank, 2 of another
sage: full_house = binomial(13,1) * binomial(4,3) * binomial(12,1) * binomial(4,2)
sage: full_house
3744
sage: prob_full_house = full_house / total_hands
sage: prob_full_house
6/4165

sage: # Convert to decimal
sage: prob_full_house.n()
0.00144057623049925
```

+++

### مثال ۲: مسئلهٔ تولد

```python
sage: def birthday_probability(n):
....:     """Exact probability that at least 2 people share a birthday"""
....:     prob_all_different = 1
....:     for i in range(n):
....:         prob_all_different *= (365 - i) / 365
....:     return 1 - prob_all_different

sage: # Test various group sizes
sage: for n in [10, 20, 23, 30, 50]:
....:     print(f"n={n:2d}: {birthday_probability(n).n():.6f}")
n=10: 0.116948
n=20: 0.411438
n=23: 0.507297
n=30: 0.706316
n=50: 0.970374

sage: # Find minimum n where probability > 0.5
sage: n = 1
sage: while birthday_probability(n) < 1/2:
....:     n += 1
sage: print(f"Minimum group size for >50%: {n}")
Minimum group size for >50%: 23
```

+++

### مثال ۳: ضرایب چندجمله‌ای

```python
sage: # Multinomial coefficient: n! / (k1! * k2! * ... * km!)
sage: # Example: Arrangements of MISSISSIPPI (11 letters)
sage: # M:1, I:4, S:4, P:2

sage: n = 11
sage: multinomial([1, 4, 4, 2])
34650

sage: # Verify with factorial formula
sage: factorial(11) / (factorial(1) * factorial(4) * factorial(4) * factorial(2))
34650

sage: # Probability that a random arrangement spells MISSISSIPPI
sage: 1 / multinomial([1, 4, 4, 2])
1/34650
```

+++

## نظریهٔ احتمال نمادین

### استخراج فرمول‌های امید ریاضی

```python
sage: # Expected value of binomial distribution
sage: var('n p k')
sage: # E(X) = sum(k * P(X=k)) for k=0 to n

sage: # Using symbolic sum (this may be slow for symbolic n)
sage: # We can verify for small concrete values
sage: n_val = 5
sage: p_val = var('p')
sage: expected = sum(k * binomial(n_val, k) * p_val^k * (1-p_val)^(n_val-k)
....:                for k in range(n_val + 1))
sage: expected.simplify()
5*p

sage: # This confirms E(X) = np for Binomial(n,p)
```

+++

### توابع تولید گشتاور

```python
sage: # MGF of Binomial distribution: M(t) = (pe^t + (1-p))^n
sage: var('t n p')
sage: mgf = (p * exp(t) + (1-p))^n

sage: # First derivative at t=0 gives E(X)
sage: mgf_prime = diff(mgf, t)
sage: expected_value = mgf_prime.subs(t=0).simplify()
sage: expected_value
n*p

sage: # Second derivative for variance
sage: mgf_double_prime = diff(mgf, t, 2)
sage: second_moment = mgf_double_prime.subs(t=0).simplify()
sage: variance = (second_moment - expected_value^2).simplify()
sage: variance
n*p*(p - 1)
sage: # Which simplifies to n*p*(1-p)
```

+++

## انتگرال‌گیری عددی و احتمال

SageMath هم انتگرال‌گیری نمادین و هم عددی را پشتیبانی می‌کند:

```python
sage: # Numerical integration for continuous distributions
sage: var('x')

sage: # Standard normal PDF
sage: normal_pdf = 1/sqrt(2*pi) * exp(-x^2/2)

sage: # P(Z < 1) for standard normal
sage: prob = integral(normal_pdf, x, -oo, 1)
sage: prob.n()
0.841344746068543

sage: # P(0 < Z < 1)
sage: prob_range = integral(normal_pdf, x, 0, 1)
sage: prob_range.n()
0.341344746068543

sage: # Verify using scipy for comparison
sage: import scipy.stats as stats
sage: stats.norm.cdf(1)  # Should match first calculation
0.8413447460685429
```

+++

## رسم توزیع‌ها

SageMath قابلیت رسم داخلی دارد که شبیه matplotlib است اما با برخی بهبودها:

```python
sage: # Plot binomial PMF
sage: n, p = 10, 0.5
sage: points = [(k, binomial(n,k) * p^k * (1-p)^(n-k)) for k in range(n+1)]
sage: bar_chart(points, color='blue', width=0.5)

sage: # Plot normal PDF
sage: var('x')
sage: mu, sigma = 0, 1
sage: pdf = 1/(sigma*sqrt(2*pi)) * exp(-(x-mu)^2/(2*sigma^2))
sage: plot(pdf, (x, -4, 4), color='red', thickness=2,
....:      axes_labels=['x', 'PDF'], title='Standard Normal Distribution')

sage: # Multiple distributions on same plot
sage: p1 = plot(pdf, (x, -4, 4), color='blue', legend_label='N(0,1)')
sage: pdf2 = 1/(2*sqrt(2*pi)) * exp(-(x-1)^2/(2*4))  # N(1,2)
sage: p2 = plot(pdf2, (x, -4, 6), color='red', legend_label='N(1,2)')
sage: (p1 + p2).show()
```

+++

## شبیه‌سازی و Monte Carlo

```python
sage: # Monte Carlo estimation of π
sage: def estimate_pi(n):
....:     inside = 0
....:     for _ in range(n):
....:         x, y = random(), random()
....:         if x^2 + y^2 <= 1:
....:             inside += 1
....:     return 4 * inside / n

sage: estimate_pi(10000)
3.1416  # Will vary

sage: # Simulate dice rolls
sage: rolls = [randint(1,6) for _ in range(1000)]
sage: # Count frequencies
sage: {i: rolls.count(i)/1000 for i in range(1,7)}
{1: 0.163, 2: 0.171, 3: 0.166, 4: 0.168, 5: 0.162, 6: 0.170}  # Approximately uniform
```

+++

## مقایسه: SageMath در مقابل NumPy/SciPy/SymPy

### چه زمانی از SageMath استفاده کنیم

**✅ از SageMath استفاده کنید وقتی:**
- عمدتاً کار ریاضی/نظری انجام می‌دهید
- می‌خواهید همه‌چیز از پیش یکپارچه باشد (بدون جستجوی import)
- به محاسبهٔ نمادین قدرتمند نیاز دارید
- ریاضیات یا نظریهٔ احتمال تدریس می‌کنید
- محیط ریاضی تعاملی می‌خواهید
- روی تحقیق ریاضی خالص کار می‌کنید
- نحوی شبیه Mathematica را ترجیح می‌دهید

**❌ از SageMath استفاده نکنید وقتی:**
- سامانه‌های تولیدی علم داده/ML می‌سازید
- در محیط‌های استاندارد پایتون کار می‌کنید (استقرار، CI/CD)
- باید با پشتهٔ استاندارد دادهٔ پایتون یکپارچه شوید
- با دانشمندان داده‌ای که از NumPy/pandas/scikit-learn استفاده می‌کنند همکاری دارید
- کارایی حیاتی است (NumPy/SciPy اغلب سریع‌ترند)

### مقایسهٔ نحو

```python
# Exact probability: P(X=3) for Binomial(10, 0.5)

# NumPy/SciPy (numerical)
from scipy.stats import binom
prob = binom.pmf(3, 10, 0.5)  # 0.1171875

# SymPy (symbolic)
from sympy.stats import Binomial, P
from sympy import Rational
X = Binomial('X', 10, Rational(1,2))
prob = P(X == 3)  # 15/128

# SageMath (natural mathematical syntax)
binomial(10, 3) * (1/2)^10  # 15/128
```

+++

## مثال عملی: تحلیل کامل

بیایید یک مسئله را با تمام قابلیت‌های SageMath حل کنیم:

**مسئله**: یک سکهٔ منصفانه ۱۰۰ بار پرتاب می‌شود. احتمال آمدن بین ۴۵ تا ۵۵ شیر (شامل هر دو) چقدر است؟

```python
sage: # Method 1: Exact calculation
sage: n = 100
sage: p = 1/2
sage: prob_exact = sum(binomial(n,k) * p^n for k in range(45, 56))
sage: prob_exact.n()
0.728747317564360

sage: # Method 2: Using scipy for comparison
sage: import scipy.stats as stats
sage: prob_scipy = stats.binom.cdf(55, n, 0.5) - stats.binom.cdf(44, n, 0.5)
sage: prob_scipy
0.7287473175643597

sage: # Method 3: Normal approximation
sage: # Binomial(100, 0.5) ≈ Normal(50, 25)
sage: mu = n * p
sage: sigma = sqrt(n * p * (1-p))
sage: sigma.n()
5.00000000000000

sage: # Using continuity correction: P(44.5 < X < 55.5)
sage: from scipy.stats import norm
sage: prob_normal = norm.cdf(55.5, mu, sigma) - norm.cdf(44.5, mu, sigma)
sage: prob_normal
0.7287181077536644

sage: print(f"Exact: {prob_exact.n():.10f}")
sage: print(f"SciPy: {prob_scipy:.10f}")
sage: print(f"Normal approx: {prob_normal:.10f}")
```

+++

## ویژگی‌های منحصربه‌فرد SageMath برای احتمال

### ۱. نظریهٔ گراف داخلی (برای زنجیره‌های مارکوف)

```python
sage: # Create a transition matrix for a Markov chain
sage: P = matrix(QQ, [[1/2, 1/2, 0],
....:                  [1/4, 1/2, 1/4],
....:                  [0, 1/2, 1/2]])

sage: # Visualize as directed graph
sage: G = DiGraph(P, format='weighted_adjacency_matrix')
sage: G.plot(edge_labels=True)

sage: # Find stationary distribution
sage: # Solve π P = π
sage: eigenspaces = P.transpose().eigenspaces_right()
sage: # Extract eigenvector for eigenvalue 1
```

### ۲. ساده‌سازی خودکار

```python
sage: # SageMath often simplifies automatically
sage: var('n')
sage: expr = binomial(n, 0) + binomial(n, n)
sage: expr
2  # Automatically simplified!

sage: expr2 = factorial(n) / (factorial(n-1) * n)
sage: expr2.simplify()
1
```

### ۳. خروجی LaTeX

```python
sage: var('n k p')
sage: formula = binomial(n,k) * p^k * (1-p)^(n-k)
sage: latex(formula)
\left(p - 1\right)^{-k + n} p^{k} \binom{n}{k}

# This is great for generating formulas for papers and presentations!
```

+++

## یکپارچگی با Jupyter

SageMath با Jupyter notebook به‌خوبی کار می‌کند:

1. **CoCalc**: Jupyter داخلی با کرنل SageMath
2. **Jupyter محلی**: پس از نصب SageMath از `sage -n jupyter` استفاده کنید
3. **کرنل SageMath**: کرنل «SageMath» را در Jupyter انتخاب کنید

**مزایا**:
- ترکیب کد SageMath با توضیحات markdown
- خروجی به PDF، HTML
- اشتراک‌گذاری آسان notebookها
- استفاده از LaTeX برای نمادگذاری ریاضی

+++

## محدودیت‌ها و ملاحظات

### پیچیدگی نصب
- نصب سادهٔ `pip install sage` نیست
- حجم دانلود بیشتر از کتابخانه‌های جداگانه
- مشکلات نصب وابسته به پلتفرم

### سازگاری اکوسیستم
- یکپارچگی کمتری با ابزارهای مدرن ML/علم داده
- ترکیب SageMath و pandas/sklearn در تولید به‌راحتی ممکن نیست
- استقرار پیچیده است

### کارایی
- NumPy/SciPy برای عملیات عددی می‌توانند سریع‌تر باشند
- SageMath سربار چند سامانه را شامل می‌شود

### اندازهٔ جامعه
- جامعهٔ کوچک‌تر از NumPy/SciPy/pandas
- پاسخ‌های کمتر در Stack Overflow
- پذیرش صنعتی کمتر

+++

## خلاصه

**SageMath** سامانهٔ نرم‌افزاری ریاضی قدرتمند و جامعی است که بر پایهٔ پایتون ساخته شده و موارد زیر را ارائه می‌دهد:

**نقاط قوت:**
- ✅ محیط ریاضی همه‌در‌یک
- ✅ حساب دقیق به‌صورت پیش‌فرض
- ✅ قابلیت‌های نمادین گسترده
- ✅ پشتیبانی غنی از ترکیبیات و نظریهٔ اعداد
- ✅ عالی برای تدریس و تحقیق
- ✅ جایگزین آزاد و متن‌باز Mathematica/Maple

**مصالحه‌ها:**
- ❌ نصب پیچیده‌تر
- ❌ یکپارچگی کمتر با پشتهٔ صنعتی علم داده
- ❌ اکوسیستم کوچک‌تر از NumPy/SciPy
- ❌ می‌تواند برای کار صرفاً عددی کندتر باشد

**توصیه:**
- **برای مخاطبان این کتاب** (متخصصان علم داده/ML): با NumPy/SciPy/SymPy بمانید
- **برای دانشجویان/پژوهشگران ریاضی**: SageMath عالی است
- **برای تدریس نظریهٔ احتمال**: SageMath مزایای آموزشی بزرگی دارد
- **برای سامانه‌های تولیدی**: از پشتهٔ استاندارد پایتون استفاده کنید

**بهترین هر دو دنیا**: مفاهیم را با SageMath بیاموزید، کد تولیدی را با NumPy/SciPy پیاده‌سازی کنید!

+++

## تمرین‌ها

1. **نصب**: SageMath را با روش دلخواه خود (CoCalc، محلی یا Docker) راه‌اندازی کنید و صحت کار آن را تأیید کنید.

2. **احتمال‌های دقیق**: احتمال دقیق آمدن دقیقاً ۵ شیر در ۱۲ پرتاب سکه را محاسبه کنید. هم به‌صورت کسر و هم اعشاری بیان کنید.

3. **احتمال پوکر**: احتمال دقیق گرفتن «چهارتا از یک نوع» در پوکر ۵ کارتی را با ترکیبیات SageMath محاسبه کنید.

4. **واریانس نمادین**: فرمول واریانس توزیع هندسی را با محاسبهٔ نمادین در SageMath استخراج کنید.

5. **توسعهٔ مسئلهٔ تولد**: کمینهٔ تعداد افراد لازم برای شانس بیش از ۹۰٪ تولد مشترک را بیابید.

6. **زنجیرهٔ مارکوف**: ماتریس گذار سادهٔ ۳ حالته برای زنجیرهٔ مارکوف بسازید و توزیع ایستای آن را با قابلیت‌های جبر خطی SageMath بیابید.

7. **مقایسه**: همان مسئلهٔ احتمال دوجمله‌ای را با SciPy (عددی)، SymPy (نمادین) و SageMath حل کنید. نتایج و زمان اجرا را مقایسه کنید.

8. **Monte Carlo**: شبیه‌سازی Monte Carlo در SageMath پیاده‌سازی کنید تا احتمال بزرگ‌تر بودن مجموع دو تاس از ۸ را برآورد کند.

+++

## مطالعهٔ بیشتر

- **SageMath Official Website**: https://www.sagemath.org/
- **SageMath Documentation**: https://doc.sagemath.org/
- **SageMath Tutorial**: https://doc.sagemath.org/html/en/tutorial/
- **CoCalc**: https://cocalc.com/
- **SageMath for Combinatorics**: https://doc.sagemath.org/html/en/reference/combinat/
- **Computational Mathematics with SageMath** (book): Free online at http://sagebook.gforge.inria.fr/

+++

## نتیجه‌گیری

اکنون سفر احتمال در عمل با پایتون را به پایان رساندید! از مفاهیم پایهٔ احتمال تا روش‌های Monte Carlo، زنجیره‌های مارکوف و اکنون محاسبهٔ نمادین با SymPy و SageMath، مجموعهٔ ابزار جامعی برای حل مسائل احتمالی دارید.

**نکات کلیدی این کتاب:**
- **NumPy/SciPy**: ابزار اصلی شما برای احتمال و آمار عددی
- **matplotlib/seaborn**: مصورسازی توزیع‌ها و نتایج
- **SymPy** (فصل ۲۰): محاسبهٔ نمادین دقیق و استخراج فرمول
- **SageMath** (فصل ۲۱): سامانهٔ ریاضی جامع برای کار نظری

**گام‌های بعدی:**
- این ابزارها را در مسائل واقعی حوزهٔ خود به‌کار ببرید
- موضوعات پیشرفته‌ای مانند فرایندهای تصادفی، سری‌های زمانی یا Bayesian inference را کاوش کنید
- در کتابخانه‌های آزاد احتمال/آمار مشارکت کنید
- با تدریس به دیگران دانش خود را به‌اشتراک بگذارید!

از همراهی شما در این سفر عملی احتمال با پایتون سپاسگزاریم. باشد p-valueهایتان معنادار و فاصله‌های اطمینانتان باریک باشند! 🎲📊🐍
