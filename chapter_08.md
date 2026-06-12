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
  - file: notebooks/chapter_08.ipynb
---

# فصل ۸: متغیرهای تصادفی پیوسته

+++

## تعریف و تفاوت با متغیرهای گسسته

در فصل‌های قبل بر *متغیرهای تصادفی گسسته* تمرکز کردیم؛ یعنی متغیرهایی که تعداد محدود یا شمارا بی‌نهایت مقدار متمایز می‌گیرند. به تعداد شیر در ۱۰ پرتاب سکه (۰، ۱، ...، ۱۰)، تعداد ایمیل‌های دریافتی در یک ساعت (۰، ۱، ۲، ...) یا پیامد پرتاب تاس ({۱، ۲، ۳، ۴، ۵، ۶}) فکر کنید.

اکنون توجه خود را به *متغیرهای تصادفی پیوسته* معطوف می‌کنیم. این متغیرها می‌توانند هر مقداری در یک بازه یا محدوده معین بگیرند. نمونه‌ها عبارت‌اند از:

* قد دقیق یک فرد بالغ انتخاب‌شده به‌صورت تصادفی (مثلاً ۱٫۷۵۳۲... متر).
* زمان تا واپاشی یک ذرهٔ پرتوزا (مثلاً ۳٫۱۴۱۵... ثانیه).
* دمای یک اتاق (مثلاً ۲۱٫۵... درجهٔ سانتی‌گراد).
* غلظت دقیق یک مادهٔ شیمیایی در محلول.

تفاوت اساسی در ماهیت فضای نمونه نهفته است. برای متغیرهای گسسته می‌توان پیامدهای ممکن را فهرست کرد. برای متغیرهای پیوسته، بین هر دو مقدار داده‌شده تعداد نامتناهی (غیرقابل‌شمارش) مقدار ممکن وجود دارد.

**مثال:** اندازه‌گیری قد دقیق یک فرد متغیری پیوسته به‌دست می‌دهد، زیرا قد از نظر نظری می‌تواند هر مقداری در یک بازه بگیرد (مثلاً ۱٫۵ متر، ۱٫۵۱ متر، ۱٫۵۱۱ متر، ...). در مقابل، شمارش تعداد افراد قدبلندتر از ۱٫۸ متر در نمونه‌ای ۱۰۰ نفره متغیری گسسته می‌دهد (۰، ۱، ۲، ...، ۱۰۰).

این تفاوت بنیادین یعنی دیگر نمی‌توانیم دربارهٔ احتمال برابر بودن متغیر با یک *مقدار مشخص* صحبت کنیم، مانند $P(\text{Height} = 1.80000... \text{ meters})$. چون تعداد ارتفاع‌های ممکن بی‌نهایت است، احتمال برخورد به هر مقدار دقیق واحد تقریباً صفر است. در عوض، برای متغیرهای پیوسته دربارهٔ احتمال افتادن متغیر *در یک بازهٔ مشخص* صحبت می‌کنیم، مانند $P(1.7\text{m} < \text{Height} \le 1.8\text{m})$.

برای توصیف توزیع احتمال متغیرهای تصادفی پیوسته، دو تابع کلیدی معرفی می‌کنیم: تابع چگالی احتمال (PDF) و تابع توزیع تجمعی (CDF).

+++

## تابع چگالی احتمال (PDF)

برای متغیر تصادفی پیوسته $X$، **تابع چگالی احتمال (PDF)** که با $f_X(x)$ نمایش داده می‌شود، *احتمال نسبی* (چگالی) گرفتن مقدار معین را توصیف می‌کند. برخلاف PMF برای متغیرهای گسسته، مقدار PDF یعنی $f_X(x)$ *خودِ احتمال نیست*. در عوض، *مساحت زیر منحنی PDF* روی یک بازه با احتمال افتادن متغیر در آن بازه مطابقت دارد.

ویژگی‌های کلیدی PDF یعنی $f_X(x)$:
1.  نامنفی بودن: $f_X(x) \ge 0$ برای همهٔ $x$.
2.  مساحت کل برابر ۱: $\int_{-\infty}^{\infty} f_X(x) dx = 1$. (مجموع احتمال روی کل محدودهٔ مقادیر ممکن برابر ۱ است).
3.  احتمال به‌صورت مساحت: احتمال افتادن $X$ در بازهٔ $[a, b]$ با انتگرال PDF روی آن بازه داده می‌شود:

    $$P(a \le X \le b) = \int_a^b f_X(x) dx$$

**نکتهٔ مهم:** برای هر متغیر تصادفی پیوسته $X$ و هر مقدار مشخص $c$، داریم $P(X=c) = \int_c^c f_X(x) dx = 0$. از این رو $P(a \le X \le b) = P(a < X \le b) = P(a \le X < b) = P(a < X < b)$. برای متغیرهای پیوسته، شامل یا مستثنی کردن نقاط انتهایی بازه احتمال را تغییر نمی‌دهد.

**مثال:** توزیع نمرات IQ در جمعیت بزرگ را تصور کنید که اغلب با توزیع نرمال (منحنی «زنگوله‌ای») مدل می‌شود. PDF در حوالی میانگین IQ (مثلاً ۱۰۰) بیشینه است و به‌سوی نمرات بسیار بالا یا بسیار پایین تنزل می‌یابد. مقدار PDF در $x=110$ چگالی توزیع در آن نقطه را می‌گوید، اما احتمال $P(\text{IQ}=110)$ برابر ۰ است. با این حال می‌توانیم احتمال $P(100 \le \text{IQ} \le 110)$ را با یافتن مساحت زیر منحنی زنگوله‌ای بین ۱۰۰ و ۱۱۰ محاسبه کنیم.

در پایتون، کتابخانه‌هایی مانند `scipy.stats` اشیایی برای انواع توزیع‌های پیوسته فراهم می‌کنند که امکان ارزیابی PDF آن‌ها با روش `.pdf()` را می‌دهد.

+++

## تابع توزیع تجمعی (CDF)

**تابع توزیع تجمعی (CDF)** که با $F_X(x)$ نمایش داده می‌شود، احتمال این را می‌دهد که متغیر تصادفی $X$ مقداری کمتر یا مساوی $x$ بگیرد.

$$F_X(x) = P(X \le x)$$

برای متغیر تصادفی پیوسته با PDF $f_X(t)$، CDF با انتگرال‌گیری PDF از منفی بینهایت تا $x$ به‌دست می‌آید:

$$F_X(x) = \int_{-\infty}^{x} f_X(t) dt$$

ویژگی‌های کلیدی CDF یعنی $F_X(x)$:
1.  $F_X(x)$ تابعی نزول‌ناپذیر از $x$ است.
2.  $\lim_{x \to -\infty} F_X(x) = 0$. (احتمال کمتر یا مساوی بودن با عددی بسیار کوچک برابر ۰ است).
3.  $\lim_{x \to \infty} F_X(x) = 1$. (احتمال کمتر یا مساوی بودن با عددی بسیار بزرگ برابر ۱ است).
4.  احتمال افتادن $X$ در بازهٔ $(a, b]$ با CDF محاسبه می‌شود:

    $$P(a < X \le b) = F_X(b) - F_X(a)$$
5.  PDF با مشتق‌گیری CDF (در جاهایی که مشتق وجود دارد) به‌دست می‌آید: $f_X(x) = \frac{d}{dx} F_X(x)$.

**مثال:** برای توزیع IQ، مقدار CDF یعنی $F_X(110)$ احتمال این را می‌دهد که فردی انتخاب‌شده به‌صورت تصادفی نمرهٔ IQ کمتر یا مساوی ۱۱۰ داشته باشد. این با مجموع مساحت زیر منحنی PDF در سمت چپ $x=110$ مطابقت دارد.

اشیای `scipy.stats` همچنین روش `.cdf()` را برای ارزیابی CDF فراهم می‌کنند.

+++

## امید ریاضی و واریانس

مشابه متغیرهای تصادفی گسسته، می‌توانیم برای متغیرهای پیوسته معیارهای گرایش به مرکز و پراکندگی را با انتگرال‌گیری به‌جای جمع تعریف کنیم.

**امید ریاضی (میانگین):**
امید ریاضی یا میانگین متغیر تصادفی پیوسته $X$ که با $E[X]$ یا $\mu$ نمایش داده می‌شود، میانگین مقداری است که در تکرارهای زیاد آزمایش انتظار مشاهدهٔ آن را داریم. با انتگرال حاصل‌ضرب هر مقدار ممکن $x$ و چگالی متناظر $f_X(x)$ روی کل محدوده محاسبه می‌شود:

$$E[X] = \mu = \int_{-\infty}^{\infty} x f_X(x) dx$$

آن را مانند مرکز جرم توزیع در نظر بگیرید.

**واریانس و انحراف معیار:**
واریانس گسترش یا پراکندگی توزیع حول میانگین را اندازه می‌گیرد. امید ریاضی مربع انحراف از میانگین است:

$$Var(X) = \sigma^2 = E[(X - \mu)^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f_X(x) dx$$

اغلب فرمول محاسباتی جایگزین زیر راحت‌تر است:

$$Var(X) = E[X^2] - (E[X])^2$$

که در آن $E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) dx$ گشتاور دوم حول مبدأ است.

**انحراف معیار** یعنی $\sigma = \sqrt{Var(X)}$، معیاری از پراکندگی در واحدهای اصلی متغیر تصادفی است.

**مثال:** برای توزیع IQ (که اغلب به‌صورت نرمال با میانگین ۱۰۰ و انحراف معیار ۱۵ مدل می‌شود)، $E[\text{IQ}] = 100$ و $Var(\text{IQ}) = 15^2 = 225$. انحراف معیار $\sigma = 15$ انحراف معمول نمرات IQ از میانگین ۱۰۰ را نشان می‌دهد.

توزیع‌های `scipy.stats` اغلب روش‌هایی مانند `.mean()`، `.var()` و `.std()` برای محاسبهٔ مستقیم این مقادیر دارند، یا `.expect()` برای امیدهای عمومی‌تر.

+++

## صدک‌ها و کمیت‌ها

صدک‌ها و کمیت‌ها به درک نقاط مشخص توزیع نسبت به احتمال تجمعی کمک می‌کنند.

**صدک $p$-ام** (که $0 < p < 1$) مقدار $x_p$ است به‌گونه‌ای که احتمال کمتر یا مساوی بودن متغیر تصادفی با $x_p$ برابر $p$ باشد. از نظر CDF:

$$F_X(x_p) = P(X \le x_p) = p$$

**تابع کمیت** که اغلب با $Q(p)$ نمایش داده می‌شود، وارون CDF است: $Q(p) = F_X^{-1}(p) = x_p$. مقداری را می‌دهد که زیر آن نسبت $p$ از توزیع قرار دارد.

* کمیت ۰٫۵ (یا صدک ۵۰ام) **میانه** است.
* کمیت ۰٫۲۵ (صدک ۲۵ام) چارک اول (Q1) است.
* کمیت ۰٫۷۵ (صدک ۷۵ام) چارک سوم (Q3) است.

**مثال:** یافتن نمرهٔ IQ که صدک ۹۵ام را مشخص می‌کند یعنی یافتن $x_{0.95}$ به‌گونه‌ای که $P(\text{IQ} \le x_{0.95}) = 0.95$. برای توزیع نرمال با میانگین ۱۰۰ و انحراف معیار ۱۵، این مقدار تقریباً ۱۲۴٫۷ است؛ یعنی ۹۵٪ جمعیت نمرهٔ IQ برابر ۱۲۴٫۷ یا کمتر دارند.

`scipy.stats` روش `.ppf()` (تابع نقطهٔ صدک) را فراهم می‌کند که وارون CDF (تابع کمیت) است.

+++

## توابع یک متغیر تصادفی پیوسته

اغلب به متغیر تصادفی جدید $Y$ علاقه‌مندیم که تابعی از متغیر تصادفی پیوستهٔ موجود $X$ باشد؛ یعنی $Y = g(X)$. چگونه PDF یا CDF $Y$ را بیابیم؟

**روش ۱: استفاده از CDF**
1.  CDF $Y$ را بیابید: $F_Y(y) = P(Y \le y) = P(g(X) \le y)$.
2.  رویداد $\{g(X) \le y\}$ را بر حسب $X$ بیان کنید. ممکن است لازم باشد نامعادله را برای $X$ حل کنید. اگر $g(x)$ یکنوا صعودی نباشد (یعنی بالا و پایین برود) دقت کنید.
3.  $P(\text{event in terms of } X)$ را با CDF متغیر $X$ یعنی $F_X(x)$ محاسبه کنید.
4.  $F_Y(y)$ حاصل را نسبت به $y$ مشتق بگیرید تا PDF $Y$ به‌دست آید: $f_Y(y) = \frac{d}{dy} F_Y(y)$.

**روش ۲: فرمول تغییر متغیر (برای توابع یکنوا)**
اگر $y = g(x)$ تابعی یکنوای صعودی یا نزولی و مشتق‌پذیر روی محدودهٔ $X$ باشد، تابع وارون $x = g^{-1}(y)$ دارد. PDF $Y$ به‌صورت زیر است:

$$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{dx}{dy} \right|$$

که $\frac{dx}{dy}$ مشتق تابع وارون $x = g^{-1}(y)$ نسبت به $y$ است. مقدار مطلق تضمین می‌کند PDF نامنفی بماند.

**مثال:** فرض کنید دمای $T$ بر حسب سلسیوس متغیری تصادفی است، شاید یکنوا بین ۱۵°C و ۲۵°C توزیع شده باشد. می‌خواهیم توزیع دما بر حسب فارنهایت یعنی $F = 1.8T + 32$ را بیابیم.
اینجا $g(T) = 1.8T + 32$ که به‌طور یکنوا صعودی است.
تابع وارون $T = g^{-1}(F) = (F - 32) / 1.8$ است.
مشتق $\frac{dT}{dF} = 1 / 1.8$ است.
اگر PDF $T$ برابر $f_T(t) = \frac{1}{25-15} = 0.1$ برای $15 \le t \le 25$ (و در غیر این صورت ۰) باشد، آنگاه PDF $F$ برابر است با:

$$f_F(f) = f_T\left(\frac{f - 32}{1.8}\right) \left| \frac{1}{1.8} \right|$$

باید محدودهٔ $F$ را بیابیم. وقتی $T=15$، $F = 1.8(15) + 32 = 59$. وقتی $T=25$، $F = 1.8(25) + 32 = 77$.
پس برای $59 \le f \le 77$:

$$f_F(f) = (0.1) \times \left| \frac{1}{1.8} \right| = \frac{0.1}{1.8} = \frac{1}{18}$$

بنابراین $F$ یکنوا بین ۵۹°F و ۷۷°F توزیع شده است.

محاسبهٔ امید ریاضی تابع $Y=g(X)$ اغلب بدون یافتن توزیع کامل $Y$ و با **قانون آماردان ناخودآگاه (LOTUS)** مستقیم‌تر انجام می‌شود:

$$E[Y] = E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$$

+++

## کار عملی: کار با متغیرهای پیوسته در پایتون

بیایید این مفاهیم را با کتابخانه‌های پایتون عملی کنیم. قدها را با فرض توزیع نرمال شبیه‌سازی می‌کنیم و هیستوگرام را با PDF نظری مقایسه می‌کنیم؛ همچنین محاسبات را با `scipy.stats` و `scipy.integrate` انجام می‌دهیم.

```{code-cell} ipython3
# Essential imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import integrate

# Configure plots for better visualization
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline
%config InlineBackend.figure_format = 'retina' # Make plots sharper
plt.rcParams['figure.figsize'] = (10, 6)
```

### ۱. تعریف PDF و CDF با `scipy.stats`

`scipy.stats` اشیای مناسبی برای بسیاری از توزیع‌های پیوسته استاندارد فراهم می‌کند (در فصل ۹ به‌تفصیل بررسی می‌کنیم). دوباره توزیع نرمال را مثال می‌زنیم. فرض کنید قد مردان بالغ (بر حسب سانتی‌متر) به‌صورت نرمال با میانگین ($\mu$) ۱۷۷ سانتی‌متر و انحراف معیار ($\sigma$) ۷ سانتی‌متر توزیع شده باشد.

```{code-cell} ipython3
# Define the normal distribution for heights
mu_height = 177
sigma_height = 7
# Create a frozen distribution object
height_dist = stats.norm(loc=mu_height, scale=sigma_height) # loc=mean, scale=std dev

# Define a range of height values for plotting
# Go out +/- 4 standard deviations to cover most of the probability mass
x_height = np.linspace(height_dist.ppf(0.0001), height_dist.ppf(0.9999), 500)

# Calculate PDF and CDF values for the range
pdf_values = height_dist.pdf(x_height)
cdf_values = height_dist.cdf(x_height)

# Plot PDF
plt.figure()
plt.plot(x_height, pdf_values, label=f'Normal PDF (mu={mu_height}, sigma={sigma_height})')
plt.fill_between(x_height, pdf_values, alpha=0.2)
plt.title('Probability Density Function (PDF) of Adult Male Height')
plt.xlabel('Height (cm)')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

# Plot CDF
plt.figure()
plt.plot(x_height, cdf_values, label=f'Normal CDF (mu={mu_height}, sigma={sigma_height})')
plt.title('Cumulative Distribution Function (CDF) of Adult Male Height')
plt.xlabel('Height (cm)')
plt.ylabel('Cumulative Probability P(Height <= x)')
# Add lines for key percentiles
plt.axhline(0.5, color='grey', linestyle='--', label='Median (50th percentile)')
plt.axvline(height_dist.ppf(0.5), color='grey', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
```

### ۲. محاسبهٔ احتمال‌ها با PDF و CDF

می‌خواهیم احتمال افتادن قد در بازهٔ مشخصی را محاسبه کنیم، مثلاً P(170 cm < Height ≤ 185 cm).

**روش ۱: استفاده از CDF**
$P(170 < X \le 185) = F_X(185) - F_X(170)$

```{code-cell} ipython3
# Calculate probability using CDF method
prob_cdf = height_dist.cdf(185) - height_dist.cdf(170)
print(f"P(170 < Height <= 185) using CDF: {prob_cdf:.4f}")

# Visualize this area on the PDF
plt.figure()
plt.plot(x_height, pdf_values, label='Normal PDF')
# Create filter for the range of interest
range_filter = (x_height > 170) & (x_height <= 185)
plt.fill_between(x_height[range_filter], pdf_values[range_filter], alpha=0.4, label='P(170 < Height <= 185)')
plt.title('Area under PDF corresponding to P(170 < Height <= 185)')
plt.xlabel('Height (cm)')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
```

**روش ۲: انتگرال‌گیری عددی PDF**
باید $\int_{170}^{185} f_X(x) dx$ را محاسبه کنیم. می‌توانیم از `scipy.integrate.quad` استفاده کنیم (که روش انتگرال‌گیری عددی به نام cuadrature انجام می‌دهد).

```{code-cell} ipython3
# The first argument to quad is the function to integrate (our PDF)
# The next two arguments are the lower and upper limits of integration
prob_integral, integration_error = integrate.quad(height_dist.pdf, 170, 185)

print(f"P(170 < Height <= 185) using PDF integration: {prob_integral:.4f}")
print(f"Estimated integration error: {integration_error:.2e}") # Should be very small
```

همان‌طور که انتظار می‌رود، هر دو روش اساساً نتیجهٔ یکسانی می‌دهند (در دقت عددی). وقتی CDF در دسترس است، استفاده از آن معمولاً مستقیم‌تر و از نظر محاسباتی کارآمدتر است. انتگرال‌گیری وقتی لازم است که فقط تابع PDF را دارید (مثلاً توزیع سفارشی غیراستاندارد).

+++

### ۳. محاسبهٔ امید ریاضی، واریانس و صدک‌ها

اشیای `scipy.stats` روش‌های داخلی برای این آمارهای رایج دارند.

```{code-cell} ipython3
# Expected Value (Mean)
e_height = height_dist.mean()
print(f"Expected Height E[X]: {e_height:.2f} cm")

# Variance
var_height = height_dist.var()
print(f"Variance Var(X): {var_height:.2f} cm^2")

# Standard Deviation
std_height = height_dist.std()
print(f"Standard Deviation std(X): {std_height:.2f} cm") # Should match sigma_height

# Calculate Percentiles (Quantiles) using PPF (Percent Point Function)
percentile_95 = height_dist.ppf(0.95) # 95th percentile
median = height_dist.ppf(0.50)       # 50th percentile (median)
q1 = height_dist.ppf(0.25)           # 25th percentile (Q1)
q3 = height_dist.ppf(0.75)           # 75th percentile (Q3)

print(f"25th Percentile (Q1) of Height: {q1:.2f} cm")
print(f"Median Height (Q2): {median:.2f} cm") # Should be equal to the mean for Normal dist.
print(f"75th Percentile (Q3) of Height: {q3:.2f} cm")
print(f"95th Percentile of Height: {percentile_95:.2f} cm")
```

**محاسبهٔ گشتاورها با انتگرال‌گیری عددی**

می‌توانیم گشتاورهایی مانند $E[X]$ و $E[X^2]$ را با `integrate.quad` و تعاریف زیر محاسبه کنیم:
$E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$
$E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) dx$

به‌جای $(-\infty, \infty)$ روی بازهٔ عملی وسیع انتگرال می‌گیریم، مثلاً $\mu \pm 10\sigma$.

```{code-cell} ipython3
# Define functions representing x*f(x) and x^2*f(x)
def integrand_mean(x):
  """Function x * pdf(x) for calculating E[X]"""
  return x * height_dist.pdf(x)

def integrand_mean_square(x):
  """Function x^2 * pdf(x) for calculating E[X^2]"""
  return x**2 * height_dist.pdf(x)

# Integrate over a wide range (practically equivalent to -inf to +inf for Normal)
lower_bound = height_dist.ppf(1e-8) # Very small percentile
upper_bound = height_dist.ppf(1 - 1e-8) # Very large percentile

e_height_integral, _ = integrate.quad(integrand_mean, lower_bound, upper_bound)
e_height_sq_integral, _ = integrate.quad(integrand_mean_square, lower_bound, upper_bound)

# Calculate variance from integrated moments
var_height_integral = e_height_sq_integral - (e_height_integral)**2

print(f"E[X] via integration: {e_height_integral:.2f}")
print(f"E[X^2] via integration: {e_height_sq_integral:.2f}")
print(f"Var(X) via integration (E[X^2] - E[X]^2): {var_height_integral:.2f}")
```

نتایج انتگرال‌گیری عددی به‌خوبی با روش‌های داخلی مطابقت دارند و درک ما از تعاریف را تأیید می‌کنند.

+++

### ۴. شبیه‌سازی داده و مقایسهٔ تجربی با نظری

می‌توانیم با روش `.rvs()` (Random VariateS) نمونه‌های تصادفی از توزیع بگیریم و نتایج (مانند هیستوگرام و آمار نمونه) را با توزیع نظری مقایسه کنیم. این تکنیک بنیادین در روش‌های مونت‌کارلو است (فصل ۱۸).

```{code-cell} ipython3
# Generate 10,000 random height samples
num_samples = 10000
# Set random_state for reproducibility - ensures we get the same 'random' samples each time
simulated_heights = height_dist.rvs(size=num_samples, random_state=42)

# Calculate empirical (sample) mean and std dev
empirical_mean = np.mean(simulated_heights)
empirical_std = np.std(simulated_heights) # Use np.std for population std dev estimate based on sample

print(f"Theoretical Mean: {mu_height:.2f}, Empirical Mean (from {num_samples} samples): {empirical_mean:.2f}")
print(f"Theoretical Std Dev: {sigma_height:.2f}, Empirical Std Dev (from {num_samples} samples): {empirical_std:.2f}")

# Plot histogram of simulated data vs theoretical PDF
plt.figure()
# Use density=True to normalize the histogram so its area sums to 1, making it comparable to the PDF
plt.hist(simulated_heights, bins=50, density=True, alpha=0.7, label='Simulated Heights Histogram')

# Overlay the theoretical PDF for comparison
plt.plot(x_height, pdf_values, 'r-', lw=2, label='Theoretical Normal PDF')

plt.title(f'Simulated Heights (N={num_samples}) vs Theoretical PDF')
plt.xlabel('Height (cm)')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
```

همان‌طور که نمودار نشان می‌دهد، هیستوگرام نمونه‌های تولیدشده به‌صورت تصادفی به‌شکل PDF نظری نزدیک است. علاوه بر این، میانگین و انحراف معیار نمونه‌ای محاسبه‌شده بسیار نزدیک به پارامترهای نظری ($\mu=177$، $\sigma=7$) توزیعی است که از آن نمونه‌گیری کرده‌ایم.

طبق قانون اعداد بزرگ (فصل ۱۴)، با افزایش تعداد نمونه‌ها (`num_samples`)، هیستوگرام تجربی بهتر PDF واقعی را تقریب می‌زند و آمار نمونه (مانند میانگین و انحراف معیار) به پارامترهای واقعی توزیع همگرا می‌شوند.

این بخش عملی نشان داد چگونه با `scipy.stats` با مفاهیم اصلی متغیرهای تصادفی پیوسته — PDF، CDF، امید ریاضی، صدک‌ها — کار کنیم. همچنین دیدیم انتگرال‌گیری عددی برای محاسبات و شبیه‌سازی برای تولید دادهٔ مطابق توزیع مشخص چگونه به مقایسهٔ نتایج تجربی با مدل‌های نظری کمک می‌کند.

در فصل بعد، توزیع‌های پیوسته مشخص و رایجی مانند یکنوا، نمایی و نرمال را با جزئیات بیشتر بررسی می‌کنیم و ویژگی‌ها و کاربردهای آن‌ها را می‌آموزیم.
