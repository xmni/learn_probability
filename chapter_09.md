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
  - file: notebooks/chapter_09.ipynb
---

# فصل ۹: توزیع‌های پیوسته رایج

## مقدمه

در فصل قبل، مفاهیم بنیادین متغیرهای تصادفی پیوسته را بررسی کردیم، از جمله توابع چگالی احتمال (PDF)، توابع توزیع تجمعی (CDF)، امید ریاضی و واریانس. اگرچه این مفاهیم برای *هر* متغیر تصادفی پیوسته‌ای صدق می‌کنند، بسیاری از پدیده‌های دنیای واقعی الگوهای مشخصی را دنبال می‌کنند. در طول زمان، ریاضی‌دانان و آمارشناسان چند «خانواده» توزیع پیوسته را که در عمل مکرراً ظاهر می‌شوند شناسایی و مشخصه‌بندی کرده‌اند.

این فصل برخی از رایج‌ترین و پرکاربردترین توزیع‌های پیوسته را معرفی می‌کند: یکنوا، نمایی، نرمال (Gaussian)، گاما و بتا. برای هر کدام:

1.  PDF و CDF آن را تعریف می‌کنیم.
2.  پارامترهای کلیدی و تفسیر آن‌ها را بحث می‌کنیم.
3.  امید ریاضی و واریانس آن را محاسبه می‌کنیم.
4.  کاربردهای معمول و ویژگی‌های مشخصه‌بند آن را برجسته می‌کنیم.
5.  نحوهٔ کار با آن در پایتون، عمدتاً با ماژول `scipy.stats` را نشان می‌دهیم.

درک این توزیع‌ها ابزار قدرتمندی برای مدل‌سازی پدیده‌های پیوسته — از زمان‌های ورود و عمر مفید تا خطاهای اندازه‌گیری و نسبت‌ها — فراهم می‌کند. همچنین به‌اختصار به روابط بین برخی از این توزیع‌ها می‌پردازیم.

ابتدا کتابخانه‌های لازم را وارد می‌کنیم.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import integrate # For potential numerical integration examples
```

```{code-cell} ipython3
# Configure plots for better readability
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
```

## ۱. توزیع یکنوا (Uniform)

توزیع یکنوا شاید ساده‌ترین توزیع پیوسته باشد. متغیری را توصیف می‌کند که پیامد آن در بازهٔ مشخص $[a, b]$ به‌طور مساوی محتمل است.

**تعریف:** متغیر تصادفی $X$ روی بازهٔ $[a, b]$ توزیع یکنوا دارد، با نماد $X \sim U(a, b)$، اگر PDF آن روی بازه ثابت و در جای دیگر صفر باشد.

**PDF (تابع چگالی احتمال):**
$$
f(x; a, b) = \begin{cases}
 \frac{1}{b-a} & \text{for } a \le x \le b \\
 0 & \text{otherwise}
\end{cases}
$$
مساحت کل زیر PDF باید ۱ باشد. اینجا مساحت سادهٔ مستطیلی با عرض $(b-a)$ و ارتفاع $\frac{1}{b-a}$ است.

**CDF (تابع توزیع تجمعی):**
$$
F(x; a, b) = P(X \le x) = \begin{cases}
 0 & \text{for } x < a \\
 \frac{x-a}{b-a} & \text{for } a \le x \le b \\
 1 & \text{for } x > b
\end{cases}
$$
CDF روی بازهٔ $[a, b]$ به‌صورت خطی از ۰ به ۱ افزایش می‌یابد.

**پارامترها:**
* $a$: کران پایین بازه.
* $b$: کران بالای بازه.

**امید ریاضی و واریانس:**
* $E[X] = \frac{a+b}{2}$ (نقطهٔ میانی بازه)
* $Var(X) = \frac{(b-a)^2}{12}$

**کاربردها:**
* مدل‌سازی مولدهای اعداد تصادفی.
* نمایش عدم‌قطعیت وقتی فقط محدودهٔ مقادیر ممکن مشخص است.
* موقعیت‌هایی که هر مقدار در بازه به‌طور مساوی محتمل است (مثلاً زمان ورود قطار در پنجرهٔ یک‌ساعته، با فرض احتمال مساوی برای هر دقیقه).

**مثال:** قطاری برای ساعت ۳ بعدازظهر برنامه‌ریزی شده، اما می‌تواند یکنوا و تصادفی بین ۲:۵۵ و ۳:۰۵ برسد. $X$ را زمان ورود بر حسب دقیقه پس از ۲:۵۵ در نظر بگیرید. آنگاه $X \sim U(0, 10)$.

**پیاده‌سازی پایتون (`scipy.stats.uniform`):**

`scipy.stats.uniform` از `loc` برای نقطهٔ شروع ($a$) و `scale` برای عرض ($b-a$) استفاده می‌کند.

```{code-cell} ipython3
# Define the parameters for the train example: a=0, b=10
a = 0
b = 10
loc = a
scale = b - a
```

```{code-cell} ipython3
# Create a uniform distribution object
uniform_dist = stats.uniform(loc=loc, scale=scale)
```

```{code-cell} ipython3
# Print key properties
print(f"Uniform Distribution U({a}, {b})")
print(f"Mean (Expected Value): {uniform_dist.mean():.2f} (Theoretical: {(a+b)/2:.2f})")
print(f"Variance: {uniform_dist.var():.2f} (Theoretical: {(b-a)**2/12:.2f})")
print(f"Standard Deviation: {uniform_dist.std():.2f}")
```

```{code-cell} ipython3
# Calculate probabilities using PDF and CDF
# P(X <= 3 minutes past 2:55) = P(arrival by 2:58 PM)
prob_le_3 = uniform_dist.cdf(3)
print(f"\nP(X <= 3) = {prob_le_3:.2f}")
```

```{code-cell} ipython3
# P(X > 7 minutes past 2:55) = P(arrival after 3:02 PM)
prob_gt_7 = 1 - uniform_dist.cdf(7) # Or uniform_dist.sf(7)
print(f"P(X > 7) = {prob_gt_7:.2f}")
```

```{code-cell} ipython3
# P(2 <= X <= 5) = F(5) - F(2)
prob_between_2_5 = uniform_dist.cdf(5) - uniform_dist.cdf(2)
print(f"P(2 <= X <= 5) = {prob_between_2_5:.2f}")
```

```{code-cell} ipython3
# Plotting the PDF and CDF
x = np.linspace(a - 2, b + 2, 500) # Range slightly outside [a, b]
pdf_values = uniform_dist.pdf(x)
cdf_values = uniform_dist.cdf(x)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].plot(x, pdf_values, 'r-', lw=2, label='Uniform PDF')
ax[0].set_title(f'Uniform({a},{b}) PDF')
ax[0].set_xlabel('x (Minutes past 2:55 PM)')
ax[0].set_ylabel('Density f(x)')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(x, cdf_values, 'b-', lw=2, label='Uniform CDF')
ax[1].set_title(f'Uniform({a},{b}) CDF')
ax[1].set_xlabel('x (Minutes past 2:55 PM)')
ax[1].set_ylabel('Cumulative Probability F(x)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
# Generate random samples
num_samples = 10000
samples = uniform_dist.rvs(size=num_samples)
```

```{code-cell} ipython3
# Plot histogram of samples vs theoretical PDF
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=20, density=True, alpha=0.6, color='g', label='Sample Histogram')
plt.plot(x, pdf_values, 'r-', lw=2, label='Theoretical PDF')
plt.title(f'Histogram of {num_samples} Uniform Samples vs PDF')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()
```

## ۲. توزیع نمایی (Exponential)

توزیع نمایی زمان تا وقوع یک رویداد در فرایند پواسون را توصیف می‌کند (فرایندی که رویدادها به‌طور پیوسته و مستقل با نرخ میانگین ثابت رخ می‌دهند).

**تعریف:** متغیر تصادفی $T$ با پارامتر نرخ $\lambda > 0$ توزیع نمایی دارد، با نماد $T \sim Exp(\lambda)$، اگر PDF آن زمان انتظار برای اولین رویداد را توصیف کند.

**PDF (تابع چگالی احتمال):**
$$
f(t; \lambda) = \begin{cases}
 \lambda e^{-\lambda t} & \text{for } t \ge 0 \\
 0 & \text{for } t < 0
\end{cases}
$$

**CDF (تابع توزیع تجمعی):**
$$
F(t; \lambda) = P(T \le t) = \begin{cases}
 1 - e^{-\lambda t} & \text{for } t \ge 0 \\
 0 & \text{for } t < 0
\end{cases}
$$
احتمال اینکه رویداد تا زمان $t$ *واقع نشده* باشد برابر $P(T > t) = 1 - F(t) = e^{-\lambda t}$ است. این اغلب تابع بقا نامیده می‌شود.

**پارامتر:**
* $\lambda$: پارامتر نرخ (میانگین تعداد رویدادها در واحد زمان).

**امید ریاضی و واریانس:**
* $E[T] = \frac{1}{\lambda}$ (میانگین زمان انتظار)
* $Var(T) = \frac{1}{\lambda^2}$

**خاصیت بی‌حافظه (Memoryless):**
ویژگی کلیدی توزیع نمایی *بی‌حافظه* بودن آن است. یعنی احتمال وقوع رویداد در بازهٔ زمانی بعدی، با فرض اینکه هنوز رخ نداده، به مدت انتظار گذشته وابسته نیست. به‌صورت رسمی:
$$ P(T > s+t \mid T > s) = P(T > t) $$
برای هر $s, t \ge 0$.

**کاربردها:**
* مدل‌سازی زمان تا ورود مشتری بعدی.
* مدل‌سازی عمر مفید قطعات الکترونیکی یا زمان واپاشی پرتوزا (با فرض نرخ خرابی ثابت).
* مدل‌سازی فاصلهٔ زمانی بین زلزله‌ها یا رویدادهای نادر دیگر.

**مثال:** عمر مفید نوعی قطعهٔ الکترونیکی توزیع نمایی دارد. به‌طور میانگین یک قطعه ۱۰۰۰ ساعت دوام می‌آورد. احتمال اینکه قطعه‌ای بیش از ۱۲۰۰ ساعت دوام بیاورد چقدر است؟

اینجا میانگین عمر $E[T] = 1000$ است. چون $E[T] = 1/\lambda$، پارامتر نرخ $\lambda = 1/1000$ خرابی در ساعت است.

**پیاده‌سازی پایتون (`scipy.stats.expon`):**

`scipy.stats.expon` از `scale` استفاده می‌کند که معادل $1/\lambda$ است. پارامتر اختیاری `loc` نیز دارد که شروع توزیع را جابه‌جا می‌کند (پیش‌فرض ۰ است).

```{code-cell} ipython3
# Define the parameters for the component lifetime example
mean_lifetime = 1000 # E[T] = 1/lambda
lambda_rate = 1 / mean_lifetime
scale_param = 1 / lambda_rate # scale = 1/lambda
```

```{code-cell} ipython3
# Create an exponential distribution object
exp_dist = stats.expon(scale=scale_param) # loc defaults to 0
```

```{code-cell} ipython3
# Print key properties
print(f"Exponential Distribution with rate lambda = {lambda_rate:.4f} (mean = {mean_lifetime})")
print(f"Mean (Expected Value): {exp_dist.mean():.2f} (Theoretical: {1/lambda_rate:.2f})")
print(f"Variance: {exp_dist.var():.2f} (Theoretical: {1/lambda_rate**2:.2f})")
print(f"Standard Deviation: {exp_dist.std():.2f}")
```

```{code-cell} ipython3
# Calculate probabilities
# P(T > 1200 hours)
prob_gt_1200 = exp_dist.sf(1200) # sf is the survival function (1 - CDF)
print(f"\nP(T > 1200) = {prob_gt_1200:.4f}")
```

```{code-cell} ipython3
# P(T <= 800 hours)
prob_le_800 = exp_dist.cdf(800)
print(f"P(T <= 800) = {prob_le_800:.4f}")
```

```{code-cell} ipython3
# P(500 <= T <= 1500) = F(1500) - F(500)
prob_between_500_1500 = exp_dist.cdf(1500) - exp_dist.cdf(500)
print(f"P(500 <= T <= 1500) = {prob_between_500_1500:.4f}")
```

```{code-cell} ipython3
# Demonstrate memoryless property: P(T > 1200 | T > 1000) == P(T > 200)?
# P(T > 1200 | T > 1000) = P(T > 1200 and T > 1000) / P(T > 1000)
#                        = P(T > 1200) / P(T > 1000)
prob_gt_1200_given_gt_1000 = exp_dist.sf(1200) / exp_dist.sf(1000)
prob_gt_200 = exp_dist.sf(200)
print(f"\nP(T > 1200 | T > 1000) = {prob_gt_1200_given_gt_1000:.4f}")
print(f"P(T > 200) = {prob_gt_200:.4f}")
print(f"Memoryless property holds: {np.isclose(prob_gt_1200_given_gt_1000, prob_gt_200)}")
```

```{code-cell} ipython3
# Plotting the PDF and CDF
t = np.linspace(0, 5 * mean_lifetime, 500) # Plot up to 5x the mean lifetime
pdf_values = exp_dist.pdf(t)
cdf_values = exp_dist.cdf(t)
```

```{code-cell} ipython3
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].plot(t, pdf_values, 'r-', lw=2, label='Exponential PDF')
ax[0].set_title(f'Exponential PDF ($\lambda={lambda_rate:.4f}$)')
ax[0].set_xlabel('t (Hours)')
ax[0].set_ylabel('Density f(t)')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(t, cdf_values, 'b-', lw=2, label='Exponential CDF')
ax[1].set_title(f'Exponential CDF ($\lambda={lambda_rate:.4f}$)')
ax[1].set_xlabel('t (Hours)')
ax[1].set_ylabel('Cumulative Probability F(t)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
# Generate random samples
num_samples = 10000
samples = exp_dist.rvs(size=num_samples)
```

```{code-cell} ipython3
# Plot histogram of samples vs theoretical PDF
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='Sample Histogram')
plt.plot(t, pdf_values, 'r-', lw=2, label='Theoretical PDF')
plt.title(f'Histogram of {num_samples} Exponential Samples vs PDF')
plt.xlabel('t (Hours)')
plt.ylabel('Density')
plt.xlim(0, 5 * mean_lifetime) # Adjust xlim for better view
plt.legend()
plt.show()
```

## ۳. توزیع نرمال (Gaussian)

توزیع نرمال که اغلب «منحنی زنگوله‌ای» نامیده می‌شود، شاید مهم‌ترین توزیع در احتمال و آمار باشد. به‌دلیل قضیهٔ حد مرکزی (که بعداً پوشش می‌دهیم) در بسیاری موقعیت‌ها به‌طور طبیعی پدیدار می‌آید و برای مدل‌سازی پدیده‌های فیزیکی، زیستی و اجتماعی متعدد به‌کار می‌رود.

**تعریف:** متغیر تصادفی $X$ با میانگین $\mu$ و واریانس $\sigma^2$ توزیع نرمال دارد، با نماد $X \sim N(\mu, \sigma^2)$، اگر PDF آن منحنی زنگوله‌ای مشخصه‌بند متمرکز در $\mu$ باشد.

**PDF (تابع چگالی احتمال):**
$$
f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{ - \frac{(x-\mu)^2}{2\sigma^2} }
$$
برای $-\infty < x < \infty$.

**CDF (تابع توزیع تجمعی):**
CDF یعنی $F(x) = P(X \le x)$ بیان بستهٔ ساده‌ای با توابع ابتدایی ندارد. معمولاً با روش‌های عددی یا جداول مربوط به توزیع نرمال استاندارد محاسبه می‌شود. CDF اغلب برای حالت استاندارد با $\Phi(z)$ نمایش داده می‌شود.

**پارامترها:**
* $\mu$: میانگین (یا امید ریاضی) که مرکز توزیع را تعیین می‌کند.
* $\sigma^2$: واریانس ($\sigma$ انحراف معیار است) که گسترش یا عرض توزیع را تعیین می‌کند.

**امید ریاضی و واریانس:**
* $E[X] = \mu$
* $Var(X) = \sigma^2$

**توزیع نرمال استاندارد:**
حالت ویژه **توزیع نرمال استاندارد** است، با نماد $Z \sim N(0, 1)$، که $\mu = 0$ و $\sigma^2 = 1$. هر متغیر نرمال $X \sim N(\mu, \sigma^2)$ را می‌توان با تبدیل زیر *استاندارد* کرد:
$$ Z = \frac{X - \mu}{\sigma} $$
این تبدیل برای محاسبات حیاتی است، زیرا احتمال‌های هر توزیع نرمالی را می‌توان با CDF توزیع نرمال استاندارد یافت. $P(X \le x) = P\left(\frac{X-\mu}{\sigma} \le \frac{x-\mu}{\sigma}\right) = P(Z \le z)$، که $z = (x-\mu)/\sigma$.

**قاعدهٔ تجربی (۶۸-۹۵-۹۹٫۷):** برای هر توزیع نرمال:
* تقریباً ۶۸٪ مقادیر در ۱ انحراف معیار از میانگین ($\mu \pm \sigma$) قرار دارند.
* تقریباً ۹۵٪ مقادیر در ۲ انحراف معیار از میانگین ($\mu \pm 2\sigma$) قرار دارند.
* تقریباً ۹۹٫۷٪ مقادیر در ۳ انحراف معیار از میانگین ($\mu \pm 3\sigma$) قرار دارند.

**کاربردها:**
* مدل‌سازی قد، وزن و سایر اندازه‌گیری‌های زیستی.
* مدل‌سازی خطاهای اندازه‌گیری در آزمایش‌ها.
* مدل‌سازی نمرات آزمون‌های استاندارد (مانند IQ یا SAT).
* مدل‌سازی مالی (مثلاً بازده سهام، اگرچه اغلب با محدودیت‌ها).
* تقریب توزیع‌های دیگر (مثلاً دوجمله‌ای، پواسون) در شرایط معین (به‌دلیل CLT).

**مثال:** فرض کنید نمرات IQ در جمعیتی به‌صورت نرمال با میانگین ($\mu$) ۱۰۰ و انحراف معیار ($\sigma$) ۱۵ توزیع شده‌اند. $X \sim N(100, 15^2)$.
1. احتمال اینکه فردی انتخاب‌شده به‌صورت تصادفی نمرهٔ IQ بین ۸۵ و ۱۱۵ داشته باشد چقدر است؟
2. احتمال اینکه نمرهٔ IQ بالاتر از ۱۳۰ باشد چقدر است؟
3. چه نمرهٔ IQ صدک ۹۵ام را مشخص می‌کند؟

**پیاده‌سازی پایتون (`scipy.stats.norm`):**

`scipy.stats.norm` از `loc` برای میانگین ($\mu$) و `scale` برای انحراف معیار ($\sigma$) استفاده می‌کند.

```{code-cell} ipython3
# Define the parameters for the IQ score example
mu = 100
sigma = 15
```

```{code-cell} ipython3
# Create a normal distribution object
norm_dist = stats.norm(loc=mu, scale=sigma)
```

```{code-cell} ipython3
# Print key properties
print(f"Normal Distribution N(mu={mu}, sigma^2={sigma**2})")
print(f"Mean (Expected Value): {norm_dist.mean():.2f} (Theoretical: {mu:.2f})")
print(f"Variance: {norm_dist.var():.2f} (Theoretical: {sigma**2:.2f})")
print(f"Standard Deviation: {norm_dist.std():.2f} (Theoretical: {sigma:.2f})")
```

```{code-cell} ipython3
# Calculate probabilities
# 1. P(85 <= X <= 115) = F(115) - F(85)
# Note: 85 is mu - sigma, 115 is mu + sigma. Should be approx 68%.
prob_between_85_115 = norm_dist.cdf(115) - norm_dist.cdf(85)
print(f"\nP(85 <= X <= 115) = {prob_between_85_115:.4f} (Matches empirical rule: ~68%)")
```

```{code-cell} ipython3
# 2. P(X > 130)
# Note: 130 is mu + 2*sigma. P(X > mu+2sigma) should be approx (1-0.95)/2 = 2.5%
prob_gt_130 = norm_dist.sf(130) # sf = 1 - cdf
print(f"P(X > 130) = {prob_gt_130:.4f} (Matches empirical rule: ~2.5%)")
```

```{code-cell} ipython3
# Check the 99.7% rule: P(mu - 3*sigma <= X <= mu + 3*sigma)
lower_3sd = mu - 3 * sigma
upper_3sd = mu + 3 * sigma
prob_within_3sd = norm_dist.cdf(upper_3sd) - norm_dist.cdf(lower_3sd)
print(f"P({lower_3sd:.1f} <= X <= {upper_3sd:.1f}) = {prob_within_3sd:.4f} (Matches empirical rule: ~99.7%)")
```

```{code-cell} ipython3
# 3. Find the IQ score at the 95th percentile (value x such that F(x) = 0.95)
# Use the Percent Point Function (PPF), which is the inverse of the CDF
iq_95th_percentile = norm_dist.ppf(0.95)
print(f"\n95th percentile IQ score: {iq_95th_percentile:.2f}")
# Verification: Calculate CDF at this value
print(f"CDF at {iq_95th_percentile:.2f}: {norm_dist.cdf(iq_95th_percentile):.2f}")
```

```{code-cell} ipython3
# Plotting the PDF and CDF
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500) # Range covering most of the probability mass
pdf_values = norm_dist.pdf(x)
cdf_values = norm_dist.cdf(x)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].plot(x, pdf_values, 'r-', lw=2, label='Normal PDF')
ax[0].set_title(f'Normal PDF ($\mu={mu}, \sigma={sigma}$)')
ax[0].set_xlabel('x (IQ Score)')
ax[0].set_ylabel('Density f(x)')
# Add lines for mean and std devs
ax[0].axvline(mu, color='k', linestyle='--', label=f'$\mu={mu}$')
ax[0].axvline(mu + sigma, color='gray', linestyle=':', label=f'$\mu+\sigma={mu+sigma}$')
ax[0].axvline(mu - sigma, color='gray', linestyle=':')
ax[0].axvline(mu + 2*sigma, color='lightgray', linestyle=':', label=f'$\mu+2\sigma={mu+2*sigma}$')
ax[0].axvline(mu - 2*sigma, color='lightgray', linestyle=':')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(x, cdf_values, 'b-', lw=2, label='Normal CDF')
ax[1].set_title(f'Normal CDF ($\mu={mu}, \sigma={sigma}$)')
ax[1].set_xlabel('x (IQ Score)')
ax[1].set_ylabel('Cumulative Probability F(x)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
# Generate random samples
num_samples = 10000
samples = norm_dist.rvs(size=num_samples)
```

```{code-cell} ipython3
# Plot histogram of samples vs theoretical PDF
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='Sample Histogram')
plt.plot(x, pdf_values, 'r-', lw=2, label='Theoretical PDF')
plt.title(f'Histogram of {num_samples} Normal Samples vs PDF')
plt.xlabel('x (IQ Score)')
plt.ylabel('Density')
plt.legend()
plt.show()
```

## ۴. توزیع گاما (Gamma)

توزیع گاما توزیعی انعطاف‌پذیر برای مقادیر نامنفی است. با توزیع نمایی و خی‌دو مرتبط است و به‌طور طبیعی زمان انتظار تا وقوع رویداد $k$-ام در فرایند پواسون پدید می‌آید.

**تعریف:** متغیر تصادفی $X$ با پارامتر شکل $k > 0$ و پارامتر نرخ $\lambda > 0$ (یا پارامتر مقیاس $\theta = 1/\lambda$) توزیع گاما دارد، با نماد $X \sim Gamma(k, \lambda)$ یا $X \sim Gamma(k, \theta)$، اگر PDF آن شامل تابع گاما $\Gamma(k)$ باشد.

تابع گاما به‌صورت $\Gamma(k) = \int_0^\infty x^{k-1} e^{-x} dx$ تعریف می‌شود. برای اعداد صحیح مثبت $k$، $\Gamma(k) = (k-1)!$.

**PDF (تابع چگالی احتمال):**
با شکل $k$ و نرخ $\lambda$:
$$
f(x; k, \lambda) = \frac{\lambda^k x^{k-1} e^{-\lambda x}}{\Gamma(k)} \quad \text{for } x \ge 0
$$
با شکل $k$ و مقیاس $\theta = 1/\lambda$:
$$
f(x; k, \theta) = \frac{1}{\Gamma(k)\theta^k} x^{k-1} e^{-x/\theta} \quad \text{for } x \ge 0
$$

**CDF (تابع توزیع تجمعی):**
CDF شامل تابع گامای ناقص پایین است و بیان بستهٔ ساده‌ای ندارد. معمولاً به‌صورت عددی محاسبه می‌شود.

**پارامترها:**
* $k$ (یا $\alpha$): پارامتر شکل. بر تیز بودن توزیع اثر می‌گذارد.
* $\lambda$ (یا $\beta$): پارامتر نرخ.
* $\theta = 1/\lambda$ (یا $\beta$): پارامتر مقیاس. توزیع را در افق کشیده یا فشرده می‌کند.
(توجه: پارامتردهی ممکن است متفاوت باشد! `scipy.stats.gamma` از شکل `a` و مقیاس `scale` یعنی $1/\lambda$ استفاده می‌کند).

**امید ریاضی و واریانس:**
* $E[X] = \frac{k}{\lambda} = k\theta$
* $Var(X) = \frac{k}{\lambda^2} = k\theta^2$

**رابطه با توزیع نمایی:**
* توزیع نمایی حالت ویژهٔ توزیع گاما با پارامتر شکل $k=1$ است. $Exp(\lambda) = Gamma(1, \lambda)$.
* مجموع $k$ متغیر مستقل $Exp(\lambda)$ توزیع $Gamma(k, \lambda)$ را دنبال می‌کند. این به ایدهٔ زمان انتظار برای رویداد $k$-ام مربوط است.

**کاربردها:**
* مدل‌سازی زمان انتظار تا وقوع چند رویداد (مثلاً زمان تا ورود مشتری پنجم).
* تحلیل قابلیت اطمینان و مدل‌سازی عمر مفید (انعطاف‌پذیرتر از نمایی).
* نظریهٔ صف.
* مدل‌سازی مقدار بارندگی یا خسارت بیمه.
* نقش در آمار بیزی (به‌عنوان توزیع مزدوج پیشین برای دقت توزیع نرمال).

**مثال:** مشتریان طبق فرایند پواسون با نرخ میانگین $\lambda = 2$ مشتری در دقیقه به فروشگاه می‌آیند. احتمال اینکه بین ۱ تا ۳ دقیقه برای ورود مشتری پنجم منتظر بمانیم چقدر است؟

زمان انتظار $T_5$ برای مشتری پنجم توزیع گاما با شکل $k=5$ و نرخ $\lambda=2$ دارد. پس $T_5 \sim Gamma(k=5, \lambda=2)$.

**پیاده‌سازی پایتون (`scipy.stats.gamma`):**

`scipy.stats.gamma` از `a` برای پارامتر شکل ($k$) و `scale` برای پارامتر مقیاس ($\theta = 1/\lambda$) استفاده می‌کند. پارامتر اختیاری `loc` نیز دارد (پیش‌فرض ۰).

```{code-cell} ipython3
# Define parameters for the customer arrival example
k_shape = 5 # Number of events (shape parameter a in scipy)
lambda_rate = 2 # Rate of arrivals per minute
theta_scale = 1 / lambda_rate # Scale parameter in scipy
```

```{code-cell} ipython3
# Create a Gamma distribution object
gamma_dist = stats.gamma(a=k_shape, scale=theta_scale) # loc defaults to 0
```

```{code-cell} ipython3
# Print key properties
print(f"Gamma Distribution Gamma(k={k_shape}, lambda={lambda_rate}) or Gamma(a={k_shape}, scale={theta_scale})")
print(f"Mean (Expected Value): {gamma_dist.mean():.2f} (Theoretical: {k_shape / lambda_rate:.2f})")
print(f"Variance: {gamma_dist.var():.2f} (Theoretical: {k_shape / lambda_rate**2:.2f})")
print(f"Standard Deviation: {gamma_dist.std():.2f}")
```

```{code-cell} ipython3
# Calculate probability: P(1 <= T_5 <= 3) = F(3) - F(1)
prob_between_1_3 = gamma_dist.cdf(3) - gamma_dist.cdf(1)
print(f"\nP(1 <= T_5 <= 3) = {prob_between_1_3:.4f}")
```

```{code-cell} ipython3
# Verify relationship with Exponential: Gamma(k=1, lambda=2) should match Exp(lambda=2)
gamma_k1 = stats.gamma(a=1, scale=1/lambda_rate)
exp_dist_check = stats.expon(scale=1/lambda_rate)
print(f"\nGamma(k=1) Mean: {gamma_k1.mean():.2f}, Exp Mean: {exp_dist_check.mean():.2f}")
print(f"Gamma(k=1) Var: {gamma_k1.var():.2f}, Exp Var: {exp_dist_check.var():.2f}")
test_x = 1.5
print(f"Gamma(k=1) PDF at {test_x}: {gamma_k1.pdf(test_x):.4f}, Exp PDF at {test_x}: {exp_dist_check.pdf(test_x):.4f}")
```

```{code-cell} ipython3
# Plotting the PDF and CDF for Gamma(5, 2)
x = np.linspace(0, gamma_dist.ppf(0.999), 500) # Plot up to 99.9th percentile
pdf_values = gamma_dist.pdf(x)
cdf_values = gamma_dist.cdf(x)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].plot(x, pdf_values, 'r-', lw=2, label=f'Gamma PDF (k={k_shape}, $\lambda$={lambda_rate})')
ax[0].set_title('Gamma PDF')
ax[0].set_xlabel('x (Waiting Time in Minutes)')
ax[0].set_ylabel('Density f(x)')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(x, cdf_values, 'b-', lw=2, label=f'Gamma CDF (k={k_shape}, $\lambda$={lambda_rate})')
ax[1].set_title('Gamma CDF')
ax[1].set_xlabel('x (Waiting Time in Minutes)')
ax[1].set_ylabel('Cumulative Probability F(x)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
# Plot different shapes of Gamma by varying k (keeping scale=1 for simplicity)
plt.figure(figsize=(10, 6))
shapes_to_plot = [1, 2, 5, 10]
x_gamma_shapes = np.linspace(0, 20, 500)
for k_val in shapes_to_plot:
    plt.plot(x_gamma_shapes, stats.gamma.pdf(x_gamma_shapes, a=k_val, scale=1),
             label=f'k={k_val} ($\lambda=1$)')
plt.title('Gamma PDF for different shape parameters k (scale=1)')
plt.xlabel('x')
plt.ylabel('Density f(x)')
plt.legend()
plt.ylim(bottom=0)
plt.show()
```

## ۵. توزیع بتا (Beta)

توزیع بتا روی بازهٔ $[0, 1]$ تعریف شده و برای مدل‌سازی احتمال‌ها، نسبت‌ها یا درصدها ایده‌آل است. شکل آن بسیار انعطاف‌پذیر است و با دو پارامتر شکل مثبت $\alpha$ و $\beta$ کنترل می‌شود.

**تعریف:** متغیر تصادفی $X$ با پارامترهای شکل $\alpha > 0$ و $\beta > 0$ توزیع بتا دارد، با نماد $X \sim Beta(\alpha, \beta)$، اگر PDF آن شامل تابع بتا $B(\alpha, \beta)$ باشد.

تابع بتا به‌صورت $B(\alpha, \beta) = \int_0^1 t^{\alpha-1} (1-t)^{\beta-1} dt = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ تعریف می‌شود.

**PDF (تابع چگالی احتمال):**
$$
f(x; \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1} = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha-1} (1-x)^{\beta-1}
$$
برای $0 \le x \le 1$.

**CDF (تابع توزیع تجمعی):**
CDF تابع بتا ناقص منظم‌شده $I_x(\alpha, \beta)$ است. بیان بستهٔ ساده‌ای ندارد اما به‌صورت عددی محاسبه می‌شود.

**پارامترها:**
* $\alpha$: پارامتر شکل اول.
* $\beta$: پارامتر شکل دوم.
شکل‌ها بسته به مقادیر $\alpha$ و $\beta$ بسیار متفاوت‌اند:
* $\alpha = 1, \beta = 1$: توزیع یکنوا روی $[0, 1]$.
* $\alpha > 1, \beta > 1$: تک‌مدی (زنگوله‌ای، اما ممکن است چوله باشد).
* $\alpha < 1, \beta < 1$: U-شکل (احتمال بیشتر نزدیک ۰ و ۱).
* $\alpha = 1, \beta > 1$: به‌طور یکنوا نزولی.
* $\alpha > 1, \beta = 1$: به‌طور یکنوا صعودی.
* $\alpha = \beta$: متقارن حول ۰٫۵.

**امید ریاضی و واریانس:**
* $E[X] = \frac{\alpha}{\alpha + \beta}$
* $Var(X) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}$

**کاربردها:**
* مدل‌سازی احتمال‌ها یا نسبت‌ها (مثلاً نرخ کلیک تبلیغ، درصد اقلام معیوب در دسته).
* نمایش عدم‌قطعیت دربارهٔ مقدار احتمال در استنتاج بیزی (اغلب به‌عنوان توزیع پیشین برای پارامتر دوجمله‌ای/Bernoulli).
* مدیریت پروژه (تحلیل PERT).
* آماره‌های ترتیبی.

**مثال:** فرض کنید نرخ کلیک (CTR) بنر تبلیغاتی وب‌سایت جدید را مدل می‌کنیم. بر اساس تجربهٔ قبلی با تبلیغات مشابه، CTR ($p$) را با توزیع بتا با $\alpha = 2$ و $\beta = 8$ مدل می‌کنیم. این CTR احتمالاً پایین را پیشنهاد می‌کند (چون $\beta > \alpha$)، متمرکز حول $E[p] = 2/(2+8) = 0.2$. احتمال اینکه CTR بین ۰٫۱ و ۰٫۳ باشد چقدر است؟

**پیاده‌سازی پایتون (`scipy.stats.beta`):**

`scipy.stats.beta` از `a` برای پارامتر شکل اول ($\alpha$) و `b` برای پارامتر شکل دوم ($\beta$) استفاده می‌کند. پارامترهای اختیاری `loc` و `scale` نیز دارد تا توزیع را از $[0, 1]$ به $[loc, loc+scale]$ تبدیل کند، اما پیش‌فرض بازهٔ استاندارد $[0, 1]$ است.

```{code-cell} ipython3
# Define parameters for the CTR example
alpha_param = 2 # Parameter a in scipy
beta_param = 8  # Parameter b in scipy
```

```{code-cell} ipython3
# Create a Beta distribution object
beta_dist = stats.beta(a=alpha_param, b=beta_param) # loc=0, scale=1 are defaults
```

```{code-cell} ipython3
# Print key properties
print(f"Beta Distribution Beta(alpha={alpha_param}, beta={beta_param})")
print(f"Mean (Expected Value): {beta_dist.mean():.2f} (Theoretical: {alpha_param / (alpha_param + beta_param):.2f})")
variance_theoretical = (alpha_param * beta_param) / ((alpha_param + beta_param)**2 * (alpha_param + beta_param + 1))
print(f"Variance: {beta_dist.var():.4f} (Theoretical: {variance_theoretical:.4f})")
print(f"Standard Deviation: {beta_dist.std():.4f}")
```

```{code-cell} ipython3
# Calculate probability: P(0.1 <= p <= 0.3) = F(0.3) - F(0.1)
prob_between_01_03 = beta_dist.cdf(0.3) - beta_dist.cdf(0.1)
print(f"\nP(0.1 <= CTR <= 0.3) = {prob_between_01_03:.4f}")
```

```{code-cell} ipython3
# Find the median (50th percentile) CTR
median_ctr = beta_dist.ppf(0.5)
print(f"Median (50th percentile) CTR: {median_ctr:.4f}")
```

```{code-cell} ipython3
# Plotting the PDF and CDF for Beta(2, 8)
x = np.linspace(0, 1, 500)
pdf_values = beta_dist.pdf(x)
cdf_values = beta_dist.cdf(x)
```

```{code-cell} ipython3
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].plot(x, pdf_values, 'r-', lw=2, label=f'Beta PDF (alpha={alpha_param}, beta={beta_param})') # Problem: missing backslash before alpha/beta
ax[0].set_title('Beta PDF')
ax[0].set_xlabel('x (Click-Through Rate)')
ax[0].set_ylabel('Density f(x)')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(x, cdf_values, 'b-', lw=2, label=f'Beta CDF (alpha={alpha_param}, beta={beta_param})') # Problem: missing backslash before alpha/beta
ax[1].set_title('Beta CDF')
ax[1].set_xlabel('x (Click-Through Rate)')
ax[1].set_ylabel('Cumulative Probability F(x)')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
# Plot different shapes of Beta
plt.figure(figsize=(12, 8))
params_to_plot = [(1, 1), (2, 2), (5, 5), (2, 8), (8, 2), (0.5, 0.5), (1, 5), (5, 1)]
x_beta_shapes = np.linspace(0.001, 0.999, 500) # Avoid exact 0 and 1 for shapes < 1
```

```{code-cell} ipython3
for a_val, b_val in params_to_plot:
    plt.plot(x_beta_shapes, stats.beta.pdf(x_beta_shapes, a=a_val, b=b_val),
             label=f'$\\alpha={a_val}, \\beta={b_val}$')

plt.title('Beta PDF for different shape parameters $\\alpha, \\beta$')
plt.xlabel('x')
plt.ylabel('Density f(x)')
plt.legend()
plt.ylim(0, 5) # Adjust ylim as needed, Beta PDF can be > 1
plt.grid(True)
plt.show()
```

## ۶. روابط بین توزیع‌ها

آگاهی از ارتباط بین این توزیع‌های رایج مفید است:

1.  **نمایی و گاما:** همان‌طور که گفته شد، توزیع نمایی حالت ویژهٔ توزیع گاما با پارامتر شکل $k=1$ است.
    * $Exp(\lambda) \equiv Gamma(k=1, \lambda)$
    * مجموع $k$ متغیر مستقل $Exp(\lambda)$ توزیع $Gamma(k, \lambda)$ را دنبال می‌کند.

2.  **یکنوا و بتا:** توزیع یکنوای استاندارد $U(0, 1)$ حالت ویژهٔ توزیع بتا با $\alpha = 1$ و $\beta = 1$ است.
    * $U(0, 1) \equiv Beta(\alpha=1, \beta=1)$

3.  **تقریب نرمال (از طریق قضیهٔ حد مرکزی):** اگرچه معادل مستقیم نیست، توزیع نرمال اغلب می‌تواند توزیع‌های دیگر را در شرایط معین تقریب بزند، به‌ویژه:
    * **تقریب دوجمله‌ای:** توزیع دوجمله‌ای($n, p$) را می‌توان با $N(np, np(1-p))$ تقریب زد وقتی $n$ بزرگ و $p$ نه خیلی نزدیک ۰ یا ۱ باشد (قواعد عملی مانند $np > 5$ و $n(1-p) > 5$ رایج است).
    * **تقریب پواسون:** توزیع پواسون($\lambda$) را می‌توان با $N(\lambda, \lambda)$ تقریب زد وقتی $\lambda$ بزرگ باشد (مثلاً $\lambda > 10$ یا $20$).
    * **تقریب گاما:** توزیع گاما($k, \lambda$) با افزایش پارامتر شکل $k$ متقارن‌تر و زنگوله‌ای‌تر می‌شود (به نرمال نزدیک می‌شود).
    (قضیهٔ حد مرکزی را در فصل ۱۵ به‌تفصیل بررسی می‌کنیم).

4.  **توزیع خی‌دو:** توزیع خی‌دو با $k$ درجهٔ آزادی، $\chi^2(k)$، حالت ویژهٔ توزیع گاما است: $\chi^2(k) \equiv Gamma(k/2, \text{rate}=1/2)$ یا $Gamma(\text{shape}=k/2, \text{scale}=2)$. در آزمون‌های آماری مکرراً ظاهر می‌شود.

درک این روابط به ساخت شهود کمک می‌کند و امکان بهره‌برداری از ویژگی‌های یک توزیع برای درک دیگری را می‌دهد.

+++

## ۷. کار با توزیع‌های پیوسته `scipy.stats`

ماژول `scipy.stats` رابط یکنواختی برای کار با این (و بسیاری توزیع‌های دیگر) فراهم می‌کند. برای شیء توزیع پیوسته `dist` ساخته‌شده از `stats.<distribution_name>()`:

* `dist.pdf(x)`: تابع چگالی احتمال در مقدار(های) `x`.
* `dist.cdf(x)`: تابع توزیع تجمعی تا مقدار(های) `x`، $P(X \le x)$.
* `dist.sf(x)`: تابع بقا، $1 - CDF(x)$، $P(X > x)$.
* `dist.ppf(q)`: تابع نقطهٔ صدک (وارون CDF، تابع کمیت). $x$ را می‌یابد به‌گونه‌ای که $P(X \le x) = q$.
* `dist.isf(q)`: تابع بقای وارون. $x$ را می‌یابد به‌گونه‌ای که $P(X > x) = q$.
* `dist.rvs(size=n)`: `n` نمونهٔ تصادفی (متغیر تصادفی) از توزیع تولید می‌کند.
* `dist.mean()`: میانگین نظری $E[X]$ را برمی‌گرداند.
* `dist.median()`: میانهٔ نظری (صدک ۵۰ام) را برمی‌گرداند.
* `dist.var()`: واریانس نظری $Var(X)$ را برمی‌گرداند.
* `dist.std()`: انحراف معیار نظری $\sqrt{Var(X)}$ را برمی‌گرداند.
* `dist.stats(moments='mvsk')`: میانگین ('m')، واریانس ('v')، چولگی ('s')، کشیدگی ('k') را برمی‌گرداند.

**پارامترهای کلیدی:**
* `loc`: عموماً پارامتر مکان (مثلاً $a$ در یکنوا، $\mu$ در نرمال). توزیع را جابه‌جا می‌کند.
* `scale`: عموماً پارامتر مقیاس (مثلاً $b-a$ در یکنوا، $1/\lambda$ در نمایی، $\sigma$ در نرمال، $\theta=1/\lambda$ در گاما). توزیع را می‌کشد/فشرده می‌کند.
* **پارامترهای شکل:** توزیع‌هایی مانند گاما (`a`) و بتا (`a`، `b`) پارامترهای شکل اضافی مخصوص خود دارند.

همیشه مستندات (`help(stats.<distribution_name>)`) را برای نام‌ها و تعاریف پارامترهای SciPy بررسی کنید، زیرا ممکن است کمی با نمادگذاری کتاب‌های درسی متفاوت باشند (به‌ویژه نرخ در برابر مقیاس).

```{code-cell} ipython3
# %%
# Example: Using PPF for Normal distribution
# Find the interval [x1, x2] centered around the mean that contains 95% of the probability
mu = 100
sigma = 15
norm_dist = stats.norm(loc=mu, scale=sigma)
```

```{code-cell} ipython3
# The central 95% leaves 2.5% in each tail
lower_bound = norm_dist.ppf(0.025)
upper_bound = norm_dist.ppf(0.975) # Or norm_dist.isf(0.025)
```

```{code-cell} ipython3
print(f"The central 95% interval for N({mu}, {sigma**2}) is [{lower_bound:.2f}, {upper_bound:.2f}]")
# Check: These values should be approximately mu +/- 1.96*sigma
print(f"Theoretical interval [mu - 1.96*sigma, mu + 1.96*sigma]: [{mu - 1.96*sigma:.2f}, {mu + 1.96*sigma:.2f}]")
```

## خلاصهٔ فصل

این فصل پنج توزیع احتمال پیوستهٔ بنیادین را معرفی کرد:

* **یکنوا $U(a, b)$:** احتمال مساوی روی بازهٔ ثابت $[a, b]$. با `stats.uniform(loc=a, scale=b-a)` مدل می‌شود.
* **نمایی $Exp(\lambda)$:** زمان انتظار برای یک رویداد در فرایند پواسون؛ خاصیت بی‌حافظه. با `stats.expon(scale=1/lambda)` مدل می‌شود.
* **نرمال $N(\mu, \sigma^2)$:** منحنی زنگوله‌ای فراوان‌گیر، محوری در آمار (CLT). با `stats.norm(loc=mu, scale=sigma)` مدل می‌شود.
* **گاما $Gamma(k, \lambda)$:** توزیع انعطاف‌پذیر برای مقادیر نامنفی؛ زمان انتظار برای $k$ رویداد. با `stats.gamma(a=k, scale=1/lambda)` مدل می‌شود.
* **بتا $Beta(\alpha, \beta)$:** روی $[0, 1]$ تعریف شده، ایده‌آل برای احتمال‌ها/نسبت‌ها؛ شکل بسیار انعطاف‌پذیر. با `stats.beta(a=alpha, b=beta)` مدل می‌شود.

PDF، CDF، پارامترها، گشتاورها (میانگین، واریانس) و کاربردهای معمول آن‌ها را بررسی کردیم. مهم‌تر از همه آموختیم چگونه با ماژول `scipy.stats` احتمال‌ها را محاسبه کنیم، صدک‌ها را بیابیم، نمونهٔ تصادفی تولید کنیم و این توزیع‌ها را در پایتون مصور کنیم. درک این توزیع‌های رایج پایه‌ای محکم برای مدل‌سازی انواع گسترده‌ای از پدیده‌های پیوسته در تحلیل داده و مدل‌سازی احتمالاتی فراهم می‌کند.

+++

## تمرین‌ها

1.  **زمان انتظار یکنوا:** اتوبوسی هر ۲۰ دقیقه از سر ساعت حرکت می‌کند (مثلاً ۶:۰۰، ۶:۲۰، ۶:۴۰...). در زمان تصادفی می‌رسید. فرض کنید زمان رسیدن شما نسبت به حرکت برنامه‌ریزی‌شدهٔ اتوبوس یکنوا روی بازهٔ ۲۰ دقیقه‌ای توزیع شده است.
    a. متغیر تصادفی و پارامترهای توزیع آن را تعریف کنید.
    b. احتمال اینکه کمتر از ۵ دقیقه برای اتوبوس بعدی منتظر بمانید چقدر است؟
    c. احتمال انتظار بین ۱۰ تا ۱۵ دقیقه چقدر است؟
    d. زمان انتظار مورد انتظار چقدر است؟ از `scipy.stats.uniform` استفاده کنید.

2.  **زمان خدمت نمایی:** زمان خدمت‌دهی صندوقدار بانک توزیع نمایی با میانگین ۳ دقیقه دارد.
    a. پارامتر نرخ $\lambda$ چقدر است؟
    b. احتمال اینکه خدمت مشتری بیش از ۵ دقیقه طول بکشد چقدر است؟
    c. احتمال اینکه خدمت کمتر از ۲ دقیقه طول بکشد چقدر است؟
    d. با فرض اینکه مشتری ۴ دقیقه خدمت گرفته، احتمال اینکه حداقل ۲ دقیقهٔ دیگر طول بکشد چقدر است؟ (راهنما: خاصیت بی‌حافظه). از `scipy.stats.expon` استفاده کنید.

3.  **قد نرمال:** فرض کنید قد مردان بالغ در کشوری خاص به‌صورت نرمال با میانگین ۱۷۵ سانتی‌متر و انحراف معیار ۷ سانتی‌متر توزیع شده است. $X \sim N(175, 7^2)$.
    a. چند درصد مردان قدبلندتر از ۱۸۵ سانتی‌متر هستند؟
    b. چند درصد مردان قدی بین ۱۷۰ تا ۱۸۰ سانتی‌متر دارند؟
    c. چه قدی صدک ۹۰ام را مشخص می‌کند؟
    d. ۵۰۰۰ نمونهٔ تصادفی از این توزیع تولید کنید و هیستوگرام رسم کنید. PDF نظری را روی آن قرار دهید. از `scipy.stats.norm` استفاده کنید.

4.  **زمان تعمیر گاما:** زمان تعمیر دستگاه (بر حسب ساعت) توزیع گاما با پارامتر شکل $k=3$ و پارامتر مقیاس $\theta=2$ (نرخ $\lambda=0.5$) دارد.
    a. زمان تعمیر مورد انتظار و انحراف معیار چقدر است؟
    b. احتمال اینکه تعمیر کمتر از ۵ ساعت طول بکشد چقدر است؟
    c. احتمال اینکه تعمیر بیش از ۱۰ ساعت طول بکشد چقدر است؟ از `scipy.stats.gamma` استفاده کنید.

5.  **نسبت بتا:** فرایند شیمیایی محصولی تولید می‌کند که نسبت ناخالصی $P$ آن با توزیع $Beta(2, 5)$ مدل می‌شود.
    a. نسبت ناخالصی مورد انتظار چقدر است؟
    b. احتمال اینکه نسبت ناخالصی کمتر از ۰٫۱ باشد چقدر است؟
    c. احتمال اینکه نسبت ناخالصی بیش از ۰٫۵ باشد چقدر است؟
    d. PDF این توزیع را رسم کنید. از `scipy.stats.beta` استفاده کنید.

+++

ساختار نمونهٔ پاسخ برای تمرین ۱ (دانشجویان این را تکمیل می‌کنند)

```{code-cell} ipython3
# تمرین ۱: زمان انتظار یکنواخت
wait_interval_max = 20
uniform_wait = stats.uniform(loc=0, scale=wait_interval_max)
```

```{code-cell} ipython3
# a. RV X = Waiting time (minutes), X ~ U(0, 20)
print("Ex 1: Uniform Wait Time")
print(f"a. X ~ U(0, {wait_interval_max})")
```

```{code-cell} ipython3
# b. P(X < 5)
prob_lt_5 = uniform_wait.cdf(5)
print(f"b. P(X < 5) = {prob_lt_5:.3f}")
```

```{code-cell} ipython3
# c. P(10 <= X <= 15)
prob_10_15 = uniform_wait.cdf(15) - uniform_wait.cdf(10)
print(f"c. P(10 <= X <= 15) = {prob_10_15:.3f}")
```

```{code-cell} ipython3
# d. E[X]
expected_wait = uniform_wait.mean()
print(f"d. E[X] = {expected_wait:.2f} minutes")
```

(دانشجویان به‌همین شکل کد تمرین‌های ۲ تا ۵ را اضافه می‌کنند)
