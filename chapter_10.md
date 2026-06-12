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
  - file: notebooks/chapter_10.ipynb
---

# فصل ۱۰: تسلط بر scipy.stats در عمل

در فصل‌های ۶ تا ۹، متغیرهای تصادفی و توزیع‌های احتمال رایج را بررسی کردیم و شهودی ساختیم برای اینکه هر توزیع را چه زمانی و چرا به‌کار ببریم. از روش‌های پایهٔ `scipy.stats` مانند `.pmf()`، `.cdf()`، `.mean()` و `.var()` برای محاسبات استفاده کردیم. اما `scipy.stats` ابزار بسیار غنی‌تری برای کار با توزیع‌ها ارائه می‌دهد.

این فصل به‌عنوان **جمع‌بندی عملی** بخش ۳ عمل می‌کند و نحوهٔ تسلط بر API کامل `scipy.stats` را آموزش می‌دهد تا با هر توزیع احتمالی با اطمینان کار کنید. هدف ما بلندپروازانه اما دست‌یافتنی است:

> **پس از این فصل، [مستندات scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) تنها چیزی است که برای کار با هر توزیعی — چه آن‌هایی که در این کتاب پوشش داده‌ایم و چه ۸۰+ توزیع دیگر موجود در scipy — نیاز دارید.**

:::{admonition} اهداف یادگیری
:class: tip

تا پایان این فصل قادر خواهید بود:
- از رابط کامل `scipy.stats` برای هر توزیعی استفاده کنید
- پرسش‌های دنیای واقعی را به پرس‌وجوهای توزیعی تبدیل کنید
- کمیت‌ها را بیابید و صدک‌ها را تفسیر کنید
- توزیع‌ها را کنار هم مقایسه کنید
- درک خود را از طریق شبیه‌سازی اعتبارسنجی کنید
- مستقل در مستندات scipy.stats حرکت کنید
:::

```{code-cell} ipython3
:tags: [remove-output]

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

# Configure plots
plt.style.use('seaborn-v0_8-whitegrid')
```

## ۱. رابط یکپارچهٔ scipy.stats

یکی از بزرگ‌ترین نقاط قوت scipy.stats **API یکنواخت** آن است. چه با Bernoulli، پواسون، نرمال یا گاما کار کنید، روش‌ها به یک شکل عمل می‌کنند.

### الگو: توزیع‌های منجمد (Frozen)

رویکرد توصیه‌شده ساخت **شیء توزیع منجمد** با پارامترهای ثابت و سپس پرس‌وجو از آن است:

```{code-cell} ipython3
# Create frozen distribution objects
binomial_dist = stats.binom(n=20, p=0.3)     # Discrete
poisson_dist = stats.poisson(mu=4)            # Discrete
normal_dist = stats.norm(loc=100, scale=15)   # Continuous
exponential_dist = stats.expon(scale=2)       # Continuous

print("Created 4 frozen distributions")
print(f"Binomial(n=20, p=0.3), Poisson(μ=4), Normal(μ=100, σ=15), Exponential(scale=2)")
```

:::{admonition} چرا توزیع‌های «منجمد»؟
:class: note

اصطلاح «منجمد» یعنی پارامترها هنگام ساخت شیء ثابت می‌شوند. این کد را تمیزتر می‌کند:

```python
# Frozen (recommended - cleaner code)
dist = stats.poisson(mu=4)
dist.pmf(3)
dist.mean()

# Unfrozen (also works, but repetitive)
stats.poisson.pmf(3, mu=4)
stats.poisson.mean(mu=4)
```
:::

### مرجع کامل API

ابزار کامل موجود برای هر توزیع `scipy.stats`:

| روش | هدف | کاربرد | خروجی | مثال |
|--------|---------|----------|---------|---------|
| **احتمال‌ها** | | | | |
| `.pmf(k)` | P(X = k) | گسسته | احتمال | `poisson_dist.pmf(3)` |
| `.pdf(x)` | چگالی در x | پیوسته | چگالی | `normal_dist.pdf(110)` |
| `.cdf(x)` | P(X ≤ x) | هر دو | احتمال تجمعی | `binomial_dist.cdf(8)` |
| `.sf(x)` | P(X > x) = 1 - CDF | هر دو | احتمال بقا | `exponential_dist.sf(3)` |
| `.logpmf(k)` | log(P(X = k)) | گسسته | لگاریتم احتمال | `poisson_dist.logpmf(10)` |
| `.logpdf(x)` | log(چگالی) | پیوسته | لگاریتم چگالی | `normal_dist.logpdf(110)` |
| `.logcdf(x)` | log(P(X ≤ x)) | هر دو | لگاریتم تجمعی | `binomial_dist.logcdf(8)` |
| `.logsf(x)` | log(P(X > x)) | هر دو | لگاریتم بقا | `exponential_dist.logsf(3)` |
| **کمیت‌ها (وارون CDF)** | | | | |
| `.ppf(q)` | تابع نقطهٔ صدک | هر دو | مقدار در کمیت q | `normal_dist.ppf(0.95)` |
| `.isf(q)` | تابع بقای وارون | هر دو | مقداری که P(X>x)=q | `exponential_dist.isf(0.1)` |
| **ویژگی‌ها** | | | | |
| `.mean()` | E[X] | هر دو | میانگین | `poisson_dist.mean()` |
| `.median()` | صدک ۵۰ام | هر دو | میانه | `binomial_dist.median()` |
| `.var()` | Var(X) | هر دو | واریانس | `normal_dist.var()` |
| `.std()` | σ | هر دو | انحراف معیار | `binomial_dist.std()` |
| `.stats(moments)` | چند گشتاور | هر دو | تاپل | `poisson_dist.stats(moments='mvsk')` |
| **شبیه‌سازی** | | | | |
| `.rvs(size)` | نمونهٔ تصادفی | هر دو | آرایهٔ نمونه‌ها | `normal_dist.rvs(1000)` |
| **بازه‌ها** | | | | |
| `.interval(alpha)` | بازهٔ اطمینان | هر دو | (کران پایین، کران بالا) | `normal_dist.interval(0.95)` |

### مثال: کاوش پواسون(μ=4) با API کامل

```{code-cell} ipython3
dist = stats.poisson(mu=4)

print("="*60)
print("EXPLORING POISSON(μ=4) WITH THE FULL scipy.stats API")
print("="*60)

# Properties
print("\n1. PROPERTIES:")
print(f"   Mean:     {dist.mean():.4f}")
print(f"   Median:   {dist.median():.4f}")
print(f"   Variance: {dist.var():.4f}")
print(f"   Std Dev:  {dist.std():.4f}")

# Get all moments at once
m, v, s, k = dist.stats(moments='mvsk')
print(f"\n   Using .stats(moments='mvsk'):")
print(f"   Skewness (s): {s:.4f} (positive = right tail)")
print(f"   Kurtosis (k): {k:.4f} (positive = heavier tails)")

# Probabilities
print("\n2. PROBABILITIES:")
print(f"   P(X = 4):     {dist.pmf(4):.4f}")
print(f"   P(X ≤ 6):     {dist.cdf(6):.4f}")
print(f"   P(X > 6):     {dist.sf(6):.4f}")
print(f"   Check: cdf + sf = {dist.cdf(6) + dist.sf(6):.4f}")

# Quantiles
print("\n3. QUANTILES (Inverse CDF):")
print(f"   50th percentile (median): {dist.ppf(0.50):.0f}")
print(f"   75th percentile:          {dist.ppf(0.75):.0f}")
print(f"   90th percentile:          {dist.ppf(0.90):.0f}")
print(f"   95th percentile:          {dist.ppf(0.95):.0f}")

# Confidence intervals
lower, upper = dist.interval(0.90)
print("\n4. CONFIDENCE INTERVALS:")
print(f"   90% interval: [{lower:.0f}, {upper:.0f}]")
print(f"   Meaning: P({lower:.0f} ≤ X ≤ {upper:.0f}) ≈ 0.90")

# Simulation
samples = dist.rvs(size=10000, random_state=42)
print("\n5. SIMULATION:")
print(f"   Generated 10,000 samples")
print(f"   Sample mean: {samples.mean():.4f} vs theoretical {dist.mean():.4f}")
print("="*60)
```

## ۲. درک کمیت‌ها و PPF

**تابع نقطهٔ صدک** (`.ppf()`) یکی از پرکاربردترین اما در ابتدا گیج‌کننده‌ترین روش‌هاست.

### PPF چیست؟

PPF **وارون CDF** است:

$$\text{ppf}(q) = \text{CDF}^{-1}(q) = \text{smallest } x \text{ where } P(X \le x) \ge q$$

**به زبان ساده:** «چه مقداری مرا در کمیت $q$-ام قرار می‌دهد؟»

```{code-cell} ipython3
# Example: Poisson(μ=5)
dist = stats.poisson(mu=5)

# Forward: value → probability
k_value = 7
prob = dist.cdf(k_value)
print(f"CDF: Given k={k_value}, probability P(X ≤ {k_value}) = {prob:.4f}")

# Inverse: probability → value
q = 0.867
k_inverse = dist.ppf(q)
print(f"PPF: Given probability q={q:.4f}, value k = {k_inverse:.0f}")
print(f"\nThey are inverses! CDF({k_value}) ≈ {prob:.4f}, PPF({prob:.4f}) = {k_value}")
```

:::{admonition} توزیع‌های گسسته و PPF
:class: warning

برای توزیع‌های گسسته، `.ppf(q)` **کوچک‌ترین عدد صحیح k** را برمی‌گرداند که CDF(k) ≥ q.

این می‌تواند «پرش» ایجاد کند:
```python
dist = stats.poisson(mu=4)
dist.ppf(0.60)  # Returns 4
dist.ppf(0.70)  # Also returns 4
dist.ppf(0.78)  # Also returns 4
dist.ppf(0.79)  # Returns 5 (jump!)
```

این رفتار درست است — ماهیت گسسته را منعکس می‌کند.
:::

### کاربردهای عملی PPF

**مورد ۱: تعیین آستانه**

```{code-cell} ipython3
# Customer service: calls per hour ~ Poisson(μ=15)
calls_dist = stats.poisson(mu=15)

threshold_90 = calls_dist.ppf(0.90)
threshold_95 = calls_dist.ppf(0.95)

print("Customer Calls per Hour ~ Poisson(μ=15)")
print(f"\nStaffing for 90% of hours: {threshold_90:.0f} calls")
print(f"  Verification: P(X ≤ {threshold_90:.0f}) = {calls_dist.cdf(threshold_90):.4f}")
print(f"\nStaffing for 95% of hours: {threshold_95:.0f} calls")
print(f"  Verification: P(X ≤ {threshold_95:.0f}) = {calls_dist.cdf(threshold_95):.4f}")
```

**مورد ۲: تحلیل ریسک**

```{code-cell} ipython3
# Defects per batch ~ Poisson(μ=2.5)
defect_dist = stats.poisson(mu=2.5)

worst_case_99 = defect_dist.ppf(0.99)
worst_case_999 = defect_dist.ppf(0.999)

print(f"Defects per Batch ~ Poisson(μ=2.5)")
print(f"\nRisk Analysis:")
print(f"  99th percentile (1 in 100):    {worst_case_99:.0f} defects")
print(f"  99.9th percentile (1 in 1000): {worst_case_999:.0f} defects")
print(f"\nPlan for {worst_case_99:.0f} defects to handle 99% of batches")
```

## ۳. مقایسهٔ توزیع‌ها

یکی از کاربردهای قدرتمند، مقایسهٔ کنار به کنار توزیع‌هاست.

### مثال: پواسون چه زمانی دوجمله‌ای را تقریب می‌زند؟

```{code-cell} ipython3
# Compare Binomial and Poisson approximation
scenarios = [
    (20, 0.05, "Good"),
    (100, 0.03, "Excellent"),
    (20, 0.5, "Poor"),
]

print("="*70)
print("COMPARING BINOMIAL AND POISSON APPROXIMATION")
print("="*70)

for n, p, quality in scenarios:
    lam = n * p
    binom_dist = stats.binom(n=n, p=p)
    poisson_dist = stats.poisson(mu=lam)

    print(f"\nn={n}, p={p}, λ={lam} ({quality} approximation expected):")
    print(f"  Binomial mean={binom_dist.mean():.4f}, var={binom_dist.var():.4f}")
    print(f"  Poisson  mean={poisson_dist.mean():.4f}, var={poisson_dist.var():.4f}")

    # Compare probabilities at mode
    mode_k = int(lam)
    binom_prob = binom_dist.pmf(mode_k)
    poisson_prob = poisson_dist.pmf(mode_k)
    print(f"  P(X={mode_k}): Binomial={binom_prob:.6f}, Poisson={poisson_prob:.6f}")
    print(f"  Difference: {abs(binom_prob - poisson_prob):.6f}")
```

**قاعده تأیید شد:** پواسون دوجمله‌ای را خوب تقریب می‌زند وقتی n ≥ 20 و p ≤ 0.05.

## ۴. شبیه‌سازی و اعتبارسنجی

روش `.rvs()` نمونه تولید می‌کند تا اعتبارسنجی شود.

```{code-cell} ipython3
# Example: Binomial(n=50, p=0.3)
true_dist = stats.binom(n=50, p=0.3)
np.random.seed(42)
samples = true_dist.rvs(size=10000)

print("="*70)
print("SIMULATION VALIDATION: Binomial(n=50, p=0.3)")
print("="*70)

print("\nTHEORETICAL vs EMPIRICAL:")
print(f"  Mean:     {true_dist.mean():.4f} vs {samples.mean():.4f}")
print(f"  Variance: {true_dist.var():.4f} vs {samples.var():.4f}")
print(f"  Std Dev:  {true_dist.std():.4f} vs {samples.std():.4f}")

print("\nQUANTILE COMPARISON:")
for q in [0.25, 0.50, 0.75, 0.90]:
    theoretical = true_dist.ppf(q)
    empirical = np.percentile(samples, q*100)
    print(f"  {q:.2f}: {theoretical:5.1f} vs {empirical:5.1f}")

print("="*70)
```

با ۱۰٬۰۰۰ نمونه، مقادیر تجربی به‌خوبی با نظری مطابقت دارند!

## ۵. خواندن مستندات scipy.stats

:::{admonition} ساختار مستندات
:class: tip

صفحهٔ هر توزیع در scipy.stats ساختار یکسانی دارد:

1. **امضای تابع** — پارامترها را نشان می‌دهد
2. **بخش Parameters** — هر پارامتر را توصیف می‌کند
3. **Notes** — تعریف ریاضی و ویژگی‌ها
4. **Methods** — فهرست کامل روش‌های موجود
5. **Examples** — کد قابل کپی

**مثال:** [مستندات scipy.stats.poisson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html)
:::

### تمرین: یادگیری توزیع هندسی از مستندات

فقط با [مستندات scipy.stats.geom](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geom.html) پاسخ دهید:
1. چه پارامتری می‌گیرد؟
2. چه چیزی را مدل می‌کند؟
3. میانگین چقدر است؟
4. اگر p = 0.2 باشد، P(X = 5) چقدر است؟
5. صدک ۷۵ام چقدر است؟

```{code-cell} ipython3
# Solution using scipy.stats documentation
geom_dist = stats.geom(p=0.2)

print("="*70)
print("LEARNING GEOMETRIC DISTRIBUTION FROM SCIPY DOCS")
print("="*70)

print("\n1. Parameter: p = 0.2 (probability of success)")
print("2. Models: Number of trials until first success")
print(f"3. Mean (from docs: 1/p): {geom_dist.mean():.4f} = {1/0.2:.4f} ✓")
print(f"4. P(X = 5): {geom_dist.pmf(5):.6f}")

p75 = geom_dist.ppf(0.75)
print(f"5. 75th percentile: {p75:.0f} trials")

# Validate with simulation
samples = geom_dist.rvs(size=10000, random_state=42)
print(f"\nValidation (10,000 samples):")
print(f"  Empirical mean: {samples.mean():.4f} vs theory {geom_dist.mean():.4f}")
print("="*70)
```

**همین الان یک توزیع را مستقل یاد گرفتید!**

## ۶. گردش‌کارهای عملی

### گردش‌کار ۱: تصمیم کنترل کیفیت

**سناریو:** کارخانه دسته‌های ۱۰۰ تایی تولید می‌کند. ۲٪ معیوب‌اند. اگر بیش از ۵ معیوب باشد دسته رد می‌شود. احتمال رد چقدر است؟

```{code-cell} ipython3
print("="*70)
print("QUALITY CONTROL WORKFLOW")
print("="*70)

# Step 1: Model selection
defect_dist = stats.binom(n=100, p=0.02)
print("\nModel: Binomial(n=100, p=0.02)")
print(f"Expected defectives: {defect_dist.mean():.2f}")

# Step 2: Answer question
prob_reject = defect_dist.sf(5)  # P(X > 5)
print(f"\nP(X > 5) = {prob_reject:.6f}")
print(f"→ {prob_reject*100:.3f}% of batches will be rejected")

# Step 3: Sensitivity analysis
print("\nWhat if threshold was 3?")
prob_reject_3 = defect_dist.sf(3)
print(f"  Rejection rate: {prob_reject_3*100:.3f}%")

print("="*70)
```

### گردش‌کار ۲: برنامه‌ریزی موجودی

**سناریو:** تقاضای روزانه ~ پواسون(μ=7). برای ۹۵٪ روزها کافی است. چقدر موجودی؟

```{code-cell} ipython3
demand_dist = stats.poisson(mu=7)

stock_95 = demand_dist.ppf(0.95)
stock_99 = demand_dist.ppf(0.99)

print("="*70)
print("INVENTORY PLANNING")
print("="*70)

print(f"\nDaily Demand ~ Poisson(μ=7)")
print(f"\nFor 95% service: Stock {stock_95:.0f} units")
print(f"  Verification: P(Demand ≤ {stock_95:.0f}) = {demand_dist.cdf(stock_95):.4f}")

print(f"\nFor 99% service: Stock {stock_99:.0f} units")
print(f"  Verification: P(Demand ≤ {stock_99:.0f}) = {demand_dist.cdf(stock_99):.4f}")

print("="*70)
```

## ۷. موضوعات پیشرفته (پیش‌نمایش)

### احتمال‌های لگاریتمی برای پایداری عددی

وقتی با احتمال‌های بسیار کوچک کار می‌کنید، از روش‌های لگاریتمی استفاده کنید:

```{code-cell} ipython3
rare_dist = stats.poisson(mu=2)
k_large = 20

# Regular probability (may underflow)
regular_prob = rare_dist.pmf(k_large)

# Log probability (numerically stable)
log_prob = rare_dist.logpmf(k_large)

print("="*60)
print("NUMERICAL STABILITY WITH LOG PROBABILITIES")
print("="*60)

print(f"\nP(X = {k_large}) for Poisson(μ=2):")
print(f"  Regular .pmf({k_large}):   {regular_prob}")
print(f"  Log .logpmf({k_large}): {log_prob:.4f}")
print(f"  Recover: exp(log_prob) = {np.exp(log_prob)}")

print("\nWhen to use log methods:")
print("  - Very small probabilities (< 1e-10)")
print("  - Products of many probabilities")
print("  - Maximum likelihood estimation")

print("="*60)
```

### برآورد پارامتر (پیش‌نمایش کوتاه)

```{code-cell} ipython3
# Observed data from unknown Poisson process
observed_data = np.array([3, 5, 4, 6, 3, 5, 4, 7, 2, 5, 4, 6, 5, 3, 4])

# For Poisson, MLE is simply the sample mean
mu_hat = observed_data.mean()

fitted_dist = stats.poisson(mu=mu_hat)

print("="*70)
print("PARAMETER ESTIMATION (PREVIEW)")
print("="*70)

print(f"\nObserved data: {observed_data}")
print(f"Estimated μ: {mu_hat:.4f}")
print(f"\nFitted distribution: Poisson(μ={mu_hat:.4f})")
print(f"  Mean: {fitted_dist.mean():.4f}")
print(f"  Variance: {fitted_dist.var():.4f}")

print("\nNote: Formal parameter estimation is covered in statistics courses.")
print("scipy.stats supports this through methods like .fit()")
print("="*70)
```

## ۸. خلاصه و گام‌های بعدی

### آنچه آموختید

**مهارت‌های اصلی:**
- ✅ الگوی API یکپارچهٔ scipy.stats (برای همهٔ ۸۰+ توزیع)
- ✅ محاسبهٔ احتمال‌ها با `.pmf()`، `.pdf()`، `.cdf()`، `.sf()`
- ✅ یافتن کمیت‌ها و صدک‌ها با `.ppf()`
- ✅ پرس‌وجوی ویژگی‌ها با `.mean()`، `.median()`، `.var()`، `.std()`، `.stats()`
- ✅ تولید نمونه با `.rvs()` برای شبیه‌سازی
- ✅ مقایسهٔ بصری و عددی توزیع‌ها

**گردش‌کارهای عملی:**
- ✅ تبدیل مسائل واقعی به پرسش‌های توزیعی
- ✅ تعیین آستانه بر اساس سطح اطمینان
- ✅ تحلیل ریسک با کمیت‌ها
- ✅ حرکت مستقل در مستندات scipy.stats

### مستندات scipy.stats اکنون منبع شماست

اکنون می‌توانید:
1. هر توزیعی را از [فهرست scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) انتخاب کنید
2. صفحهٔ مستندات آن را بخوانید
3. پارامترها، روش‌ها و مثال‌ها را درک کنید
4. با اطمینان به مسائل خود اعمال کنید

:::{admonition} قدرت API یکپارچه
:class: important

رابط scipy.stats **در همهٔ توزیع‌ها یکسان** است. این الگو برای *هر* توزیعی کار می‌کند:

```python
dist = stats.DISTRIBUTION_NAME(params)

# Query properties
dist.mean(), dist.median(), dist.var(), dist.std()

# Calculate probabilities
dist.pmf(k) or dist.pdf(x)  # Point
dist.cdf(x)                  # Cumulative
dist.sf(x)                   # Survival

# Find quantiles
dist.ppf(q)                  # Inverse CDF
dist.interval(alpha)         # Confidence interval

# Generate samples
dist.rvs(size=n)             # Random variates
```

این الگو را بیاموزید → با *هر* توزیعی کار کنید!
:::

### تمرین‌های عملی

1. **مقایسهٔ توزیع‌ها:** دوجمله‌ای(n=20, p=0.3) را با نرمال(μ=6, σ=2.05) مقایسه کنید. تقریب نرمال چقدر نزدیک است؟

2. **تحلیل ریسک:** بازدیدکنندگان وب‌سایت ~ پواسون(μ=500). سرور ۶۵۰ را پوشش می‌دهد. احتمال از کار افتادن چقدر است؟ چه ظرفیتی برای ریسک کمتر از ۱٪ لازم است؟

3. **یادگیری توزیع جدید:** Negative Binomial را انتخاب کنید. مدل: «تا سه شش بیاید تاس بیندازیم. احتمال دقیقاً ۲۰ پرتاب چقدر است؟»

4. **شبیه‌سازی:** ۱۰۰۰ نمونه از نمایی(λ=0.5) تولید کنید. میانگین نمونه را با نظری مقایسه کنید. ۱۰٬۰۰۰ نمونه را هم امتحان کنید.

5. **کاوش مستندات:** مستندات `scipy.stats.describe()` را بیابید. برای تحلیل داده استفاده کنید و همهٔ آمارها را تفسیر کنید.

---

**اکنون با scipy.stats آشنا هستید!** مستندات مرجع جامع شما برای همهٔ کارهای احتمالی آینده است. در فصل بعد بررسی می‌کنیم چند متغیر تصادفی چگونه با هم تعامل می‌کنند (توزیع‌های مشترک، کوواریانس، همبستگی).
