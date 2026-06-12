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
  - file: notebooks/chapter_18.ipynb
---

# فصل ۱۸: روش‌های Monte Carlo

+++

به فصل ۱۸ خوش آمدید! در این فصل به کلاسی قدرتمند از الگوریتم‌های محاسباتی می‌پردازیم که برای به‌دست آوردن نتایج عددی بر نمونه‌گیری تصادفی مکرر تکیه می‌کنند: **روش‌های Monte Carlo**. ایدهٔ زیربنایی به‌شکل قابل‌توجهی ساده و در عین حال عمیقاً مؤثر است: از تصادف برای حل مسائلی استفاده کنیم که در اصل ممکن است قطعی باشند، اما حل تحلیلی آن‌ها بسیار دشوار است.

+++

## ایدهٔ اصلی: استفاده از نمونه‌گیری تصادفی

+++

در هستهٔ خود، روش Monte Carlo از **قانون اعداد بزرگ (LLN)** بهره می‌برد. آموختیم که میانگین نتایج حاصل از تعداد زیادی آزمایش باید به مقدار مورد انتظار نزدیک باشد و با افزایش تعداد آزمایش‌ها به آن نزدیک‌تر می‌شود.

روش‌های Monte Carlo این اصل را برای برآورد کمیت‌هایی به‌کار می‌برند که محاسبهٔ مستقیم آن‌ها دشوار است. اگر بتوانیم کمیت مورد نظر را به‌صورت امید ریاضی یک متغیر تصادفی بیان کنیم، می‌توانیم آن را با این روش برآورد کنیم:
1.  شبیه‌سازی تعداد زیادی نمونهٔ تصادفی (تحقق) از متغیر تصادفی.
2.  محاسبهٔ میانگین نمونه‌ای این تحقق‌ها.

**چرا از آن‌ها استفاده کنیم؟**
* **پیچیدگی:** می‌توانند مسائلی با هندسهٔ پیچیده، بعد بالا یا وابستگی‌های پیچیده را حل کنند که در آن‌ها راه‌حل‌های تحلیلی عملی نیستند.
* **شبیه‌سازی:** امکان شبیه‌سازی سامانه‌های پیچیده (مانند صف‌ها، بازارهای مالی، فرایندهای فیزیکی) را برای درک رفتار آن‌ها و برآورد معیارهای کلیدی فراهم می‌کنند.
* **انعطاف‌پذیری:** می‌توان آن‌ها را برای طیف گسترده‌ای از مسائل در فیزیک، مهندسی، مالی، آمار و غیره تطبیق داد.

+++

**مثال: برآورد میانگین زمان انتظار در یک صف**

یک سامانهٔ صف پیچیده را تصور کنید (مثلاً مرکز تماس با نرخ‌های متغیر ورود تماس، سطوح مهارت متفاوت اپراتورها و قواعد مسیریابی پیچیده). محاسبهٔ دقیق میانگین زمان انتظار مشتری به‌صورت تحلیلی ممکن است غیرممکن باشد.

با Monte Carlo:
1.  **مدل:** توزیع‌های احتمالی برای ورود مشتریان (مثلاً فرایند پواسون) و زمان‌های سرویس (مثلاً توزیع نمایی) تعریف کنید.
2.  **شبیه‌سازی:** شبیه‌سازی مرکز تماس برای یک «روز» را بارها اجرا کنید (مثلاً ۱۰٬۰۰۰ بار). در هر اجرای شبیه‌سازی، زمان انتظار هر مشتری شبیه‌سازی‌شده را ردیابی کنید.
3.  **برآورد:** میانگین زمان انتظار در هر روز شبیه‌سازی‌شده را محاسبه کنید. سپس این میانگین‌های روزانه را در همهٔ ۱۰٬۰۰۰ شبیه‌سازی میانگین بگیرید. بر اساس LLN، این میانگین کلی برآورد خوبی از میانگین بلندمدت واقعی زمان انتظار خواهد بود.

+++

## برآورد احتمال‌ها و مقادیر مورد انتظار

+++

روش‌های Monte Carlo به‌ویژه برای برآورد احتمال‌ها و مقادیر مورد انتظاری که از فرایندهای پیچیده ناشی می‌شوند مفیدند.

+++

### برآورد احتمال‌ها

برای برآورد احتمال $P(A)$ یک واقعهٔ $A$ می‌توانیم:
1.  $N$ شبیه‌سازی مستقل از آزمایش تصادفی زیربنایی اجرا کنیم.
2.  تعداد دفعاتی که واقعهٔ $A$ در شبیه‌سازی‌ها رخ می‌دهد، $N_A$، را بشماریم.
3.  $P(A) \approx \frac{N_A}{N}$ را برآورد کنیم.

این در اصل محاسبهٔ بسامد تجربی واقعه است که بر اساس LLN با $N \to \infty$ به احتمال واقعی همگرا می‌شود.

+++

**مثال: برآورد احتمال برد در بازی Craps**

Craps بازی تاس با قواعد نسبتاً پیچیده برای برد است. می‌توانیم بازی را بارها شبیه‌سازی کنیم تا احتمال کلی برد «شوت‌کننده» را برآورد کنیم.

**(ساختار مفهومی کد)**
```python
def play_craps():
    # Roll dice, check rules (come-out roll: 7, 11 win; 2, 3, 12 lose)
    # If point established, continue rolling until point or 7
    # Return True if win, False if lose

N = 100000  # Number of simulations
wins = 0
for _ in range(N):
    if play_craps():
        wins += 1

estimated_prob_win = wins / N
print(f"Estimated P(Win) in Craps: {estimated_prob_win:.4f}")
```
(احتمال واقعی تقریباً ۲۴۴/۴۹۵ ≈ ۰٫۴۹۲۹ است)

+++

### برآورد مقادیر مورد انتظار

برای برآورد مقدار مورد انتظار $E[g(X)]$ تابع $g$ از متغیر تصادفی $X$:
1.  $N$ نمونهٔ تصادفی مستقل $X_1, X_2, ..., X_N$ از توزیع $X$ تولید کنید.
2.  $g(X_i)$ را برای هر نمونه محاسبه کنید.
3.  $E[g(X)] \approx \frac{1}{N} \sum_{i=1}^{N} g(X_i)$ را برآورد کنید.

این نیز بر LLN تکیه دارد؛ میانگین نمونه‌ای $g(X_i)$ به $E[g(X)]$ همگرا می‌شود. وقتی توزیع $X$ یا تابع $g$ محاسبهٔ تحلیلی امید را دشوار یا غیرممکن می‌کند، این روش بسیار قدرتمند است.

```{code-cell} ipython3
import numpy as np

# Example: Estimate E[e^X] where X ~ Normal(0, 1)
# Analytical answer: This is the MGF evaluated at t=1, which is e^(μt + σ^2*t^2/2) = e^(0*1 + 1^2*1^2/2) = e^(1/2) ≈ 1.6487

N = 100000  # Number of samples
mu = 0
sigma = 1

# 1. Generate samples from Normal(0, 1)
X_samples = np.random.normal(mu, sigma, N)

# 2. Apply the function g(x) = e^x
g_X_samples = np.exp(X_samples)

# 3. Calculate the sample mean
estimated_expectation = np.mean(g_X_samples)

print(f"Estimated E[e^X] where X ~ N(0, 1): {estimated_expectation:.4f}")
print(f"Analytical E[e^X]: {np.exp(0.5):.4f}")
```

## انتگرال‌گیری Monte Carlo

+++

روش‌های Monte Carlo راهی برای برآورد انتگرال‌های معین فراهم می‌کنند؛ به‌ویژه در ابعاد بالا که روش‌های عددی دیگر انتگرال‌گیری (مانند روش‌های چندجمله‌ای) از نظر محاسباتی پرهزینه می‌شوند («نفرین ابعاد»).

+++

### روش ۱: برخورد یا عدم برخورد (برآورد مساحت)

این روش برای برآورد مساحت ناحیه‌ای $A$ درون ناحیهٔ بزرگ‌تری $B$ با مساحت شناخته‌شدهٔ $Area(B)$ شهودی است.
1.  $N$ نقطهٔ تصادفی یکنواخت در ناحیهٔ بزرگ‌تر $B$ تولید کنید.
2.  تعداد نقاطی که داخل ناحیهٔ $A$ می‌افتند، $N_{hit}$، را بشمارید.
3.  نسبت نقاط داخل $A$ نسبت مساحت‌ها را تقریب می‌زند: $\frac{N_{hit}}{N} \approx \frac{Area(A)}{Area(B)}$.
4.  $Area(A) \approx Area(B) \times \frac{N_{hit}}{N}$ را برآورد کنید.

مثال کلاسیک برآورد $\pi$ است.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# Estimate Pi using Monte Carlo integration

N = 10000  # Number of random points

# Generate N points (x, y) uniformly in the square [-1, 1] x [-1, 1]
# Area of square B = 2 * 2 = 4
x_coords = np.random.uniform(-1, 1, N)
y_coords = np.random.uniform(-1, 1, N)

# Check if points are inside the unit circle (x^2 + y^2 <= 1)
# Area of circle A = pi * r^2 = pi * 1^2 = pi
distances_sq = x_coords**2 + y_coords**2
is_inside_circle = distances_sq <= 1

# Count hits
N_hit = np.sum(is_inside_circle)

# Estimate Area(A) = Area(B) * (N_hit / N)
estimated_pi = 4.0 * N_hit / N

print(f"Estimated value of Pi: {estimated_pi:.5f}")

# --- Visualization (Optional) ---
plt.figure(figsize=(6, 6))
plt.scatter(x_coords[is_inside_circle], y_coords[is_inside_circle], color='blue', s=1, label='Inside Circle')
plt.scatter(x_coords[~is_inside_circle], y_coords[~is_inside_circle], color='red', s=1, label='Outside Circle')

# Draw the circle boundary
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), color='black', linestyle='--')

plt.title(f'Estimating Pi (N={N}, Estimate={estimated_pi:.4f})')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
```

### روش ۲: استفاده از مقادیر مورد انتظار

اغلب می‌خواهیم $I = \int_a^b g(x) dx$ را محاسبه کنیم. می‌توانیم این انتگرال را به‌صورت امید ریاضی بازنویسی کنیم. فرض کنید $X$ متغیر تصادفی یکنواخت روی $[a, b]$ باشد. تابع چگالی احتمال $X$ برابر است با $f(x) = \frac{1}{b-a}$ برای $x \in [a, b]$ و در غیر این صورت ۰.

آنگاه امید ریاضی $\frac{g(X)}{f(X)}$ برابر است با:
$$ E\left[\frac{g(X)}{f(X)}\right] = \int_a^b \frac{g(x)}{f(x)} f(x) dx = \int_a^b g(x) dx = I $$

از آنجا که $f(x) = \frac{1}{b-a}$ ثابت است، داریم $\frac{g(X)}{f(X)} = (b-a)g(X)$. پس:
$$ I = E[(b-a)g(X)] = (b-a) E[g(X)] $$

بنابراین می‌توانیم $I$ را با این روش برآورد کنیم:
1.  $N$ نمونه $X_1, ..., X_N$ از $Uniform(a, b)$ تولید کنید.
2.  $g(X_i)$ را برای هر نمونه محاسبه کنید.
3.  $I \approx (b-a) \times \frac{1}{N} \sum_{i=1}^{N} g(X_i)$ را برآورد کنید.

```{code-cell} ipython3
import numpy as np
from scipy import integrate

# Example: Estimate I = integral from 0 to 1 of exp(x^2) dx

def g(x):
    return np.exp(x**2)

a = 0.0
b = 1.0
N = 100000 # Number of samples

# 1. Generate samples from Uniform(a, b)
X_samples = np.random.uniform(a, b, N)

# 2. Calculate g(X_i)
g_X_samples = g(X_samples)

# 3. Estimate the integral
estimated_integral = (b - a) * np.mean(g_X_samples)

print(f"Monte Carlo estimate of integral: {estimated_integral:.5f}")

# Compare with SciPy's numerical integration (quad)
analytical_integral, error = integrate.quad(g, a, b)
print(f"SciPy quad estimate of integral: {analytical_integral:.5f} (error < {error:.1e})")
```

## تولید متغیرهای تصادفی

+++

روش‌های Monte Carlo به‌شدت به توانایی ما در تولید اعداد تصادفی مطابق توزیع‌های احتمالی مشخص وابسته‌اند. در حالی که کتابخانه‌هایی مانند `numpy.random` مولدهایی برای بسیاری از توزیع‌های رایج فراهم می‌کنند، گاهی باید متغیرهایی از توزیع‌های کم‌رایج‌تر یا سفارشی تولید کنیم.

دو روش رایج روش تبدیل معکوس و روش پذیرش-رد هستند.

+++

### روش تبدیل معکوس

این روش در صورتی قابل استفاده است که تابع توزیع تجمعی (CDF)، $F(x) = P(X \le x)$، شناخته شده و معکوس آن $F^{-1}(u)$ قابل محاسبه باشد.

**قضیه:** اگر $U$ متغیر تصادفی با توزیع $Uniform(0, 1)$ باشد، آنگاه متغیر تصادفی $X = F^{-1}(U)$ دارای CDF برابر $F(x)$ است.

**الگوریتم:**
1.  عدد تصادفی $u$ از $Uniform(0, 1)$ تولید کنید.
2.  $x = F^{-1}(u)$ را محاسبه کنید. این $x$ یک نمونهٔ تصادفی از توزیع با CDF برابر $F(x)$ است.

**مثال: تولید از توزیع نمایی ($\lambda$)**
CDF برابر است با $F(x) = 1 - e^{-\lambda x}$ برای $x \ge 0$. برای یافتن معکوس:
بگذارید $u = 1 - e^{-\lambda x}$.
$1 - u = e^{-\lambda x}$
$\ln(1 - u) = -\lambda x$
$x = -\frac{1}{\lambda} \ln(1 - u)$
پس $F^{-1}(u) = -\frac{1}{\lambda} \ln(1 - u)$.
(توجه: از آنجا که $U \sim Uniform(0, 1)$، آنگاه $1-U$ نیز $Uniform(0, 1)$ است. بنابراین اغلب می‌توان ساده‌سازی کرد و از $x = -\frac{1}{\lambda} \ln(u)$ استفاده کرد.)

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

def generate_exponential_inverse_transform(lambda_rate, size=1):
    """Generates samples from Exponential(lambda_rate) using Inverse Transform."""
    u = np.random.uniform(0, 1, size=size)
    x = - (1 / lambda_rate) * np.log(u) # Using the simplified form
    return x

lambda_val = 0.5 # Rate parameter
N_samples = 10000

generated_samples = generate_exponential_inverse_transform(lambda_val, size=N_samples)

# Compare with numpy's built-in generator
numpy_samples = np.random.exponential(scale=1/lambda_val, size=N_samples) # Note: numpy uses scale = 1/lambda

# Plot histograms to compare
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(generated_samples, bins=50, density=True, alpha=0.7, label='Inverse Transform')
plt.title(f'Exponential(lambda={lambda_val}) - Inverse Transform')
plt.xlabel('Value')
plt.ylabel('Density')

plt.subplot(1, 2, 2)
plt.hist(numpy_samples, bins=50, density=True, alpha=0.7, label='NumPy Built-in', color='orange')
plt.title(f'Exponential(lambda={lambda_val}) - NumPy')
plt.xlabel('Value')
plt.ylabel('Density')

# Add theoretical PDF
x_vals = np.linspace(0, np.max(generated_samples), 200)
pdf_vals = lambda_val * np.exp(-lambda_val * x_vals)
plt.subplot(1, 2, 1)
plt.plot(x_vals, pdf_vals, 'r--', label='Theoretical PDF')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(x_vals, pdf_vals, 'r--', label='Theoretical PDF')
plt.legend()

plt.tight_layout()
plt.show()
```

### روش پذیرش-رد

این روش وقتی مفید است که محاسبهٔ CDF معکوس دشوار باشد، اما بتوانیم تابع چگالی هدف $f(x)$ را به‌راحتی ارزیابی کنیم. همچنین به توزیع پیشنهادی $g(x)$ (که از آن *می‌توان* به‌راحتی نمونه گرفت) و ثابت $c$ نیاز دارد به‌طوری که $f(x) \le c \cdot g(x)$ برای همهٔ $x$ برقرار باشد.

**الگوریتم:**
1.  نمونهٔ کاندید $y$ از توزیع پیشنهادی $g(x)$ تولید کنید.
2.  عدد تصادفی $u$ از $Uniform(0, 1)$ تولید کنید.
3.  بررسی کنید آیا $u \le \frac{f(y)}{c \cdot g(y)}$.
    * اگر بله، $y$ را به‌عنوان نمونه از $f(x)$ **بپذیرید**.
    * اگر نه، $y$ را **رد** کنید و به گام ۱ بازگردید.

کارایی به انتخاب $g(x)$ و $c$ بستگی دارد. هرچه $c \cdot g(x)$ به $f(x)$ نزدیک‌تر باشد، احتمال پذیرش (که $1/c$ است) بالاتر است.

**مثال: نمونه‌گیری از توزیع نرمال کوتاه‌شده**
فرض کنید می‌خواهیم از $N(0, 1)$ نمونه بگیریم اما محدود به بازهٔ $[0, 2]$.
- تابع چگالی هدف $f(x)$ متناسب با PDF نرمال استاندارد در $[0, 2]$ و در غیر این صورت ۰ است.
- توزیع پیشنهادی $g(x)$ می‌تواند $Uniform(0, 2)$ باشد. PDF برابر است با $g(x) = 1/2$ برای $x \in [0, 2]$.
- به $c$ نیاز داریم به‌طوری که $f(x) \le c \cdot g(x)$. بیشینهٔ PDF نرمال استاندارد در $x=0$ است که برابر $1/\sqrt{2\pi}$ است. پس باید $(1/\sqrt{2\pi}) \le c \cdot (1/2)$. می‌توانیم $c = 2 / \sqrt{2\pi}$ را انتخاب کنیم.
- شرط پذیرش می‌شود $u \le \frac{f(y)}{c \cdot g(y)} = \frac{NormalPDF(y)}{ (2 / \sqrt{2\pi}) \cdot (1/2)} = \sqrt{2\pi} \cdot NormalPDF(y) = e^{-y^2/2}$.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_truncated_normal_accept_reject(mu, sigma, low, high, size=1):
    """Generates samples from N(mu, sigma) truncated to [low, high] using Accept-Reject."""
    samples = []
    # Use Uniform(low, high) as proposal distribution g(x)
    # PDF g(x) = 1 / (high - low)
    # Target PDF f(x) is proportional to norm.pdf(x, mu, sigma) in [low, high]
    # Find c such that norm.pdf(x) <= c * g(x)
    # Max of norm.pdf occurs at mu if mu is in [low, high], else at boundary
    x_mode = mu if low <= mu <= high else (low if mu < low else high)
    max_pdf = norm.pdf(x_mode, mu, sigma)
    c = max_pdf / (1 / (high - low))
    
    count_total = 0
    while len(samples) < size:
        count_total += 1
        # 1. Sample y from proposal g(x) = Uniform(low, high)
        y = np.random.uniform(low, high)
        
        # 2. Sample u from Uniform(0, 1)
        u = np.random.uniform(0, 1)
        
        # 3. Acceptance check: u <= f(y) / (c * g(y))
        target_pdf_val = norm.pdf(y, mu, sigma)
        proposal_pdf_val = 1 / (high - low)
        acceptance_ratio = target_pdf_val / (c * proposal_pdf_val)
        
        if u <= acceptance_ratio:
            samples.append(y)
            
    print(f"Acceptance Rate: {size / count_total:.3f} (Theoretical min: {1/c:.3f})")
    return np.array(samples)

mu_val = 0
sigma_val = 1
low_bound = 0
high_bound = 2
N_samples = 5000

generated_samples = generate_truncated_normal_accept_reject(mu_val, sigma_val, low_bound, high_bound, size=N_samples)

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(generated_samples, bins=50, density=True, alpha=0.7, label='Accept-Reject Samples')

# Overlay theoretical truncated normal PDF (scaled)
x_vals = np.linspace(low_bound, high_bound, 200)
pdf_vals = norm.pdf(x_vals, mu_val, sigma_val)
# Need to normalize the PDF over the interval [low_bound, high_bound]
normalization_factor, _ = integrate.quad(lambda x: norm.pdf(x, mu_val, sigma_val), low_bound, high_bound)
plt.plot(x_vals, pdf_vals / normalization_factor, 'r--', label='Theoretical PDF')

plt.title(f'Truncated Normal({mu_val}, {sigma_val}^2) on [{low_bound}, {high_bound}]')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
```

## مثال‌های عملی و تمرین‌ها

+++

### مثال ۱: مسئلهٔ سوزن بوفون

این مسئلهٔ کلاسیک از شبیه‌سازی Monte Carlo برای برآورد $\pi$ استفاده می‌کند. سوزن‌هایی به طول $L$ را روی کف با خطوط موازی به فاصلهٔ $D$ واحد ($L \le D$) بیندازید. احتمال عبور یک سوزن تصادفی از یکی از خطوط چقدر است؟

پاسخ تحلیلی $P(\text{cross}) = \frac{2L}{\pi D}$ است. می‌توانیم این احتمال را با شبیه‌سازی برآورد کنیم و سپس $\pi$ را به‌دست آوریم.

**تنظیم شبیه‌سازی:**
1.  موقعیت مرکز سوزن $(y)$ نسبت به نزدیک‌ترین خط پایین‌تر را در نظر بگیرید. $y$ یکنواخت روی $[0, D/2]$ توزیع شده است.
2.  زاویهٔ $(\theta)$ سوزن نسبت به خطوط موازی را در نظر بگیرید. $\theta$ یکنواخت روی $[0, \pi/2]$ توزیع شده است.
3.  سوزن از خطی عبور می‌کند اگر فاصلهٔ عمودی از مرکز آن تا نوک ($ (L/2) \sin \theta $) از فاصله تا نزدیک‌ترین خط ($y$) بیشتر باشد. یعنی عبور اگر $y \le (L/2) \sin \theta$.

**الگوریتم:**
1.  $L$ و $D$ را تنظیم کنید (مثلاً $L=1, D=2$).
2.  $N$ شبیه‌سازی اجرا کنید:
    a. $y \sim Uniform(0, D/2)$ تولید کنید.
    b. $\theta \sim Uniform(0, \pi/2)$ تولید کنید.
    c. بررسی کنید آیا $y \le (L/2) \sin \theta$. در صورت برقراری به‌عنوان «برخورد» بشمارید.
3.  $P(\text{cross}) \approx \frac{N_{hits}}{N}$ را برآورد کنید.
4.  $\pi \approx \frac{2L}{D \times P(\text{cross})}$ را برآورد کنید. (اگر $L=1, D=2$، آنگاه $\pi \approx \frac{1}{P(\text{cross})}$.)

```{code-cell} ipython3
import numpy as np
import math

def estimate_pi_buffon(N=100000, L=1.0, D=2.0):
    """Estimates Pi using Buffon's Needle simulation."""
    if L > D:
        print("Warning: Method assumes L <= D")
        
    hits = 0
    for _ in range(N):
        # 1. Sample y from Uniform(0, D/2)
        y_center = np.random.uniform(0, D / 2.0)
        
        # 2. Sample theta from Uniform(0, pi/2)
        theta = np.random.uniform(0, math.pi / 2.0)
        
        # 3. Check for crossing
        vertical_dist_tip = (L / 2.0) * math.sin(theta)
        if y_center <= vertical_dist_tip:
            hits += 1
            
    # Estimate probability
    prob_cross = hits / N
    
    # Estimate Pi
    if prob_cross == 0: # Avoid division by zero if N is very small / unlucky
        return None, 0
        
    estimated_pi = (2 * L) / (D * prob_cross)
    return estimated_pi, prob_cross

# Run simulation
num_simulations = 500000
needle_length = 1.0
line_spacing = 2.0

pi_estimate, p_cross_estimate = estimate_pi_buffon(num_simulations, needle_length, line_spacing)

print(f"Buffon's Needle Simulation (N={num_simulations}, L={needle_length}, D={line_spacing})")
print(f"Estimated P(Cross): {p_cross_estimate:.5f}")
if pi_estimate is not None:
    print(f"Estimated Pi: {pi_estimate:.5f}")
    print(f"Absolute Error: {abs(pi_estimate - math.pi):.5f}")
```

### تمرین‌ها

1.  **احتمال پوکر:** شبیه‌سازی‌ای بنویسید که احتمال دریافت «فلاش» (پنج کارت از یک خال) از یک دستهٔ استاندارد ۵۲ کارتی را برآورد کند. برآورد خود را با احتمال تحلیلی شناخته‌شده مقایسه کنید.
2.  **انتگرال‌گیری Monte Carlo:** مقدار $\int_0^\pi \sin(x) dx$ را با روش مقدار مورد انتظار (روش ۲) برآورد کنید. پاسخ تحلیلی ۲ است. دقت با افزایش تعداد نمونه‌ها $N$ چگونه تغییر می‌کند؟
3.  **توزیع سفارشی:** از روش پذیرش-رد برای تولید نمونه از توزیعی که PDF آن متناسب با $f(x) = 1 + \sin(2\pi x)$ برای $x \in [0, 1]$ است استفاده کنید. $Uniform(0, 1)$ را به‌عنوان توزیع پیشنهادی به‌کار ببرید. هیستوگرام نمونه‌های خود را رسم کنید.

+++

## خلاصهٔ فصل

+++

روش‌های Monte Carlo مجموعه‌ای چندمنظوره و قدرتمند از تکنیک‌ها بر پایهٔ نمونه‌گیری تصادفی هستند.
* از **قانون اعداد بزرگ** برای تقریب کمیت‌های مورد نظر بهره می‌برند.
* به‌ویژه برای **برآورد احتمال‌ها و مقادیر مورد انتظار** در سناریوهای پیچیده‌ای که راه‌حل‌های تحلیلی دشوارند مؤثرند.
* **انتگرال‌گیری Monte Carlo** راهی برای برآورد انتگرال‌های معین فراهم می‌کند؛ به‌ویژه در ابعاد بالا یا برای انتگرال‌پذیرهای پیچیده ارزشمند است.
* تولید متغیرهای تصادفی از توزیع‌های مشخص حیاتی است. تکنیک‌هایی مانند **روش تبدیل معکوس** (وقتی CDF معکوس در دسترس است) و **روش پذیرش-رد** (وقتی PDF شناخته شده است) امکان نمونه‌گیری از توزیع‌های سفارشی را می‌دهند.
* دقت برآوردهای Monte Carlo معمولاً با افزایش تعداد شبیه‌سازی‌ها ($N$) بهبود می‌یابد و معمولاً با $1/\sqrt{N}$ مقیاس می‌شود.

این روش‌ها پایهٔ بسیاری از تکنیک‌های پیشرفتهٔ شبیه‌سازی در علوم، مهندسی و مالی هستند.
