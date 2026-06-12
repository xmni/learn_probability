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
  - file: notebooks/chapter_19.ipynb
---

# فصل ۱۹: (اختیاری) پیمایش‌های بیشتر

+++

**به فصل پایانی خوش آمدید!** این فصل نگاهی کوتاه به چند حوزهٔ جذاب می‌اندازد که بر پایه‌های احتمالی که ساخته‌ایم بنا شده‌اند. این موضوعات اغلب مبنای دوره‌های پیشرفته‌تر در آمار، یادگیری ماشین، نظریهٔ اطلاعات و مالی کمی هستند.

به اثبات‌های دقیق یا جزئیات کامل نمی‌پردازیم، بلکه هدف درک شهودی و نمایش کاربردهای ساده با پایتون است. این فصل را نقطهٔ آغاز یادگیری بیشتر خود بدانید.

به این موضوعات می‌پردازیم:
* **نظریهٔ اطلاعات:** کمی‌سازی اطلاعات و مقایسهٔ توزیع‌ها (آنتروپی، واگرایی KL).
* **فرایندهای تصادفی:** مدل‌سازی سامانه‌هایی که در طول زمان به‌صورت تصادفی تکامل می‌یابند (فرایند پواسون، حرکت براونی).
* **توابع تولیدکننده:** ابزارهای ریاضی قدرتمند برای تحلیل توزیع‌ها (MGF، PGF).

+++

## مقدمه‌ای بر نظریهٔ اطلاعات

+++

نظریهٔ اطلاعات، که توسط کلود شانون بنیان‌گذاری شد، با کمی‌سازی اطلاعات، فشرده‌سازی داده و محدودیت‌های ارتباطی سروکار دارد. دو مفهوم بنیادین آنتروپی و واگرایی کولبک-لایbler (KL) هستند.

+++

### آنتروپی

+++

آنتروپی میانگین سطح «اطلاعات»، «غافلگیری» یا «عدم‌قطعیت» ذاتی در پیامدهای ممکن یک متغیر تصادفی را می‌سنجد. برای متغیر تصادفی گسستهٔ $X$ با تابع جرم احتمال $p(x)$، آنتروپی $H(X)$ به‌صورت زیر تعریف می‌شود:

$$ H(X) = - \sum_{x} p(x) \log_b p(x) $$

پایهٔ $b$ لگاریتم واحد را تعیین می‌کند (معمولاً پایهٔ ۲ برای بیت و پایهٔ $e$ برای nat).

* **آنتروپی بالا:** پیامدها تقریباً به‌طور یکسان محتمل‌اند (عدم‌قطعیت بالا). پرتاب یک سکهٔ منصفانه آنتروپی بیشتری از یک سکهٔ شدیداً مغرض دارد.
* **آنتروپی پایین:** یک پیامد بسیار محتمل‌تر از بقیه است (عدم‌قطعیت پایین).

**مثال:** یک تاس شش‌وجهی منصفانه را با تاسی که شدیداً وزن‌دار است مقایسه کنید؛ در تاس دوم P(نتیجه=۱)=۰٫۹ و P(نتیجه=i)=۰٫۰۲ برای i=2..6. تاس منصفانه آنتروپی بیشتری دارد چون نتیجه کمتر قابل پیش‌بینی است.

بیایید آنتروپی متن انگلیسی (که «e» رایج و «z» نادر است) را با نویسه‌های تصادفی (که همهٔ حروف به‌طور یکسان محتمل‌اند) مقایسه کنیم. متن انگلیسی آنتروپی کمتری دارد چون بسامد حروف ناهمگن است و قابل پیش‌بینی‌تر از نویسه‌های تصادفی است.

```{code-cell} ipython3
import numpy as np
from scipy.stats import entropy

# Example: Entropy of a fair die vs. a biased die

# Fair die probabilities
p_fair = np.array([1/6] * 6)

# Biased die probabilities (P(1)=0.5, others equal)
p_biased = np.array([0.5, 0.1, 0.1, 0.1, 0.1, 0.1]) 
# Ensure it sums to 1
assert np.isclose(p_biased.sum(), 1.0)

# Calculate entropy (using base 2 for bits)
entropy_fair = entropy(p_fair, base=2)
entropy_biased = entropy(p_biased, base=2)

print(f"Entropy of fair die: {entropy_fair:.4f} bits")
print(f"Entropy of biased die: {entropy_biased:.4f} bits")

# Higher entropy means more uncertainty/unpredictability
```

### واگرایی کولبک-لایbler (KL)

+++

واگرایی KL می‌سنجد یک توزیع احتمال $P$ چقدر از توزیع احتمال مورد انتظار دوم $Q$ منحرف است. اغلب به‌عنوان سود اطلاعاتی هنگام گذار از توزیع پیشین $Q$ به توزیع پسین $P$ تفسیر می‌شود.

برای توزیع‌های گسستهٔ $P$ و $Q$ تعریف‌شده روی یک فضای نمونهٔ مشترک، واگرایی KL از $Q$ به $P$ برابر است با:

$$ D_{KL}(P || Q) = \sum_{x} P(x) \log_b \frac{P(x)}{Q(x)} $$

ویژگی‌های کلیدی:
* $D_{KL}(P || Q) \ge 0$
* $D_{KL}(P || Q) = 0$ اگر و فقط اگر $P = Q$
* **متقارن نیست:** به‌طور کلی $D_{KL}(P || Q) \neq D_{KL}(Q || P)$.

**مثال:** اگر تاس وزن‌دار را با توزیع یک تاس منصفانه مدل کنیم، چقدر اطلاعات از دست می‌رود؟

```{code-cell} ipython3
# Example: KL Divergence between biased and fair die

# Note: scipy.stats.entropy(P, Q) calculates KL divergence D_KL(P || Q)

# How different is the biased distribution (P) from the fair one (Q)?
kl_pq = entropy(pk=p_biased, qk=p_fair, base=2) 

# How different is the fair distribution (P) from the biased one (Q)?
kl_qp = entropy(pk=p_fair, qk=p_biased, base=2)

print(f"KL Divergence D_KL(Biased || Fair): {kl_pq:.4f} bits")
print(f"KL Divergence D_KL(Fair || Biased): {kl_qp:.4f} bits")

# The non-zero values indicate the distributions are different.
# The asymmetry shows the 'direction' matters.
```

## مقدمه‌ای بر فرایندهای تصادفی

+++

فرایند تصادفی مجموعه‌ای از متغیرهای تصادفی است که معمولاً بر حسب زمان نمایه‌گذاری شده‌اند، $\{X(t) | t \in T\}$. سامانه‌هایی را توصیف می‌کند که به‌صورت تصادفی تکامل می‌یابند.

* **زنجیره‌های مارکوف (فصل ۱۷):** زمان گسسته، فضای حالت گسسته، ویژگی بی‌حافظگی.
* **فرایند پواسون:** زمان پیوسته، وقوع گسستهٔ رویدادها به‌صورت تصادفی.
* **حرکت براونی:** زمان پیوسته، فضای حالت پیوسته، مدل‌سازی حرکت تصادفی.

+++

### فرایند پواسون

+++

فرایند پواسون تعداد رویدادهای رخ‌داده در یک بازهٔ زمانی را می‌شمارد. با نرخ میانگین ثابت $\lambda$ (رویداد در واحد زمان) مشخص می‌شود.

ویژگی‌های کلیدی:
1.  تعداد رویدادها در هر بازه‌ای به طول $t$ از توزیع پواسون با میانگین $\lambda t$ پیروی می‌کند.
2.  تعداد رویدادها در بازه‌های زمانی مجزا مستقل‌اند.
3.  زمان *بین* رویدادهای متوالی از توزیع نمایی با نرخ $\lambda$ (میانگین $1/\lambda$) پیروی می‌کند.

**مثال:** مدل‌سازی ورود مشتریان به فروشگاه، رویدادهای واپاشی رادیواکتیو یا دریافت ایمیل، با فرض نرخ میانگین ثابت و استقلال رویدادها.

بیایید زمان‌های ورود رویدادها در یک فرایند پواسون را شبیه‌سازی کنیم.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

# Parameters
lambda_rate = 2  # Average events per time unit (e.g., per hour)
total_time = 10 # Simulate over 10 time units
num_events_to_simulate = 30 # Approximate number (actual might differ)

# Inter-arrival times follow Exponential(lambda)
# We can simulate these times and sum them to get arrival times
inter_arrival_times = expon.rvs(scale=1/lambda_rate, size=num_events_to_simulate)

# Calculate arrival times by cumulative sum
arrival_times = np.cumsum(inter_arrival_times)

# Filter events that occur within the total_time
arrival_times = arrival_times[arrival_times <= total_time]

# Plot the arrival times
plt.figure(figsize=(10, 2))
plt.eventplot(arrival_times, orientation='horizontal', colors='blue')
plt.xlabel('Time')
plt.yticks([])
plt.title(f'Simulated Poisson Process Arrivals ($\lambda$={lambda_rate})')
plt.grid(True, axis='x')
plt.xlim(0, total_time)
plt.show()

print(f"Number of events simulated in {total_time} time units: {len(arrival_times)}")
# Compare to expected number: lambda * T = 2 * 10 = 20
# The actual number is random and follows Poisson(lambda*T)
```

### حرکت براونی

+++

حرکت براونی (یا فرایند وینر) $W(t)$ حرکت تصادفی ذرات معلق در سیال را مدل می‌کند، یا به‌طور کلی‌تر پدیده‌هایی با نوسانات تصادفی پیوسته.

ویژگی‌های کلیدی (حرکت براونی استاندارد):
1.  $W(0) = 0$.
2.  افزایش‌های مستقل: برای هر $0 \le s < t < u < v$، افزایش‌های $W(t) - W(s)$ و $W(v) - W(u)$ متغیرهای تصادفی مستقل‌اند.
3.  افزایش‌های نرمال: برای هر $0 \le s < t$، افزایش $W(t) - W(s)$ نرمال با میانگین ۰ و واریانس $t - s$ توزیع شده است. $W(t) \sim \mathcal{N}(0, t)$.
4.  مسیرهای پیوسته: تابع $W(t)$ در $t$ پیوسته است.

**حرکت براونی هندسی (GBM):** اغلب در مالی برای مدل‌سازی قیمت سهام به‌کار می‌رود. فرایند $S(t)$ از GBM پیروی می‌کند اگر معادلهٔ دیفرانسیل تصادفی زیر را ارضا کند:
$$ dS(t) = \mu S(t) dt + \sigma S(t) dW(t) $$
که در آن $\mu$ رانش (نرخ میانگین بازده) و $\sigma$ نوسان‌پذیری (انحراف معیار بازده‌ها) است و $dW(t)$ افزایش یک فرایند وینر است.

راه‌حل را می‌توان به‌صورت زیر نوشت:
$$ S(t) = S(0) \exp\left( (\mu - \frac{\sigma^2}{2})t + \sigma W(t) \right) $$

**مثال:** شبیه‌سازی یک مسیر سادهٔ قیمت سهام با GBM.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# Parameters for Geometric Brownian Motion
S0 = 100     # Initial stock price
mu = 0.05    # Expected annual return (drift)
sigma = 0.2  # Annual volatility 
T = 1.0      # Time horizon in years
N = 252      # Number of time steps (e.g., trading days in a year)
dt = T / N   # Time step size

# Simulate the Wiener process increments (standard normal)
dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=N)

# Calculate the cumulative sum of increments to get W(t)
# Need W(t) at each step, so we need the cumulative sum
W = np.cumsum(dW)

# Add W(0)=0 at the beginning
W = np.insert(W, 0, 0.0)

# Time points
t = np.linspace(0.0, T, N + 1)

# Calculate the GBM path
S_t = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

# Plot the simulated stock price path
plt.figure(figsize=(10, 6))
plt.plot(t, S_t)
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.title(f'Simulated Geometric Brownian Motion Path\n($S_0$={S0}, $\mu$={mu}, $\sigma$={sigma})')
plt.grid(True)
plt.show()
```

## توابع تولیدکننده

+++

توابع تولیدکننده ابزارهای قدرتمند در احتمال و ترکیبیات هستند. دنبالهٔ احتمال‌های یک توزیع را در یک تابع واحد رمزگذاری می‌کنند. مشتق‌ها و دستکاری‌های این تابع می‌توانند ویژگی‌هایی مانند گشتاورها (میانگین، واریانس) و توزیع مجموع متغیرهای تصادفی مستقل را آشکار کنند.

+++

### توابع تولید احتمال (PGF)

+++

برای متغیرهای تصادفی گسستهٔ با مقادیر صحیح نامنفی $X$ (مانند پواسون، دوجمله‌ای، هندسی) به‌کار می‌روند. PGF به‌صورت زیر تعریف می‌شود:

$$ G_X(z) = E[z^X] = \sum_{k=0}^{\infty} P(X=k) z^k $$

ویژگی‌ها:
* $G_X(1) = \sum P(X=k) = 1$
* $E[X] = G'_X(1)$ (مشتق اول در z=1)
* $Var(X) = G''_X(1) + G'_X(1) - [G'_X(1)]^2$
* اگر $X$ و $Y$ مستقل باشند، آنگاه $G_{X+Y}(z) = G_X(z) G_Y(z)$.

+++

### توابع تولید گشتاور (MGF)

+++

برای متغیرهای تصادفی گسسته و پیوسته قابل استفاده‌اند. MGF به‌صورت زیر تعریف می‌شود:

$$ M_X(t) = E[e^{tX}] $$

برای $X$ گسسته: $M_X(t) = \sum_x e^{tx} P(X=x)$
برای $X$ پیوسته: $M_X(t) = \int_{-\infty}^{\infty} e^{tx} f_X(x) dx$

ویژگی‌ها:
* $M_X(0) = E[e^0] = 1$
* $E[X^n] = M_X^{(n)}(0)$ (مشتق nام در t=0)
* $E[X] = M'_X(0)$
* $Var(X) = E[X^2] - (E[X])^2 = M''_X(0) - [M'_X(0)]^2$
* اگر $X$ و $Y$ مستقل باشند، آنگاه $M_{X+Y}(t) = M_X(t) M_Y(t)$.
* یکتایی: اگر دو متغیر تصادفی MGF یکسان داشته باشند (در همسایگی ۰)، توزیع یکسانی دارند.

**مثال:** MGF توزیع نرمال $X \sim \mathcal{N}(\mu, \sigma^2)$ برابر است با $M_X(t) = \exp(\mu t + \frac{1}{2} \sigma^2 t^2)$.
بیایید میانگین و واریانس را با مشتق‌ها تأیید کنیم:
* $M'_X(t) = (\mu + \sigma^2 t) \exp(\mu t + \frac{1}{2} \sigma^2 t^2)$
   $E[X] = M'_X(0) = (\mu + 0) \exp(0) = \mu$
* $M''_X(t) = \sigma^2 \exp(\dots) + (\mu + \sigma^2 t)^2 \exp(\dots)$
   $E[X^2] = M''_X(0) = \sigma^2 \exp(0) + (\mu + 0)^2 \exp(0) = \sigma^2 + \mu^2$
* $Var(X) = E[X^2] - (E[X])^2 = (\sigma^2 + \mu^2) - (\mu)^2 = \sigma^2$

+++

در حالی که محاسبهٔ MGFها اغلب به حساب دیفرانسیل و انتگرال نیاز دارد، برخی کتابخانه‌ها مانند `scipy.stats` از ویژگی‌های مشتق‌شده از آن‌ها برای ارائهٔ گشتاورها استفاده می‌کنند.

```{code-cell} ipython3
from scipy.stats import norm

# Define a normal distribution object
mu = 5
sigma = 2
rv = norm(loc=mu, scale=sigma)

# SciPy provides methods to get moments directly
# These are consistent with what would be derived from the MGF
mean, var, skew, kurt = rv.stats(moments='mvsk')

print(f"Using scipy.stats for N(mu={mu}, sigma={sigma}):")
print(f"  Mean (E[X]): {mean:.4f} (Theoretical: {mu})" )
print(f"  Variance (Var(X)): {var:.4f} (Theoretical: {sigma**2})")

# Expected value of X^2 = Var(X) + (E[X])^2
ex2 = var + mean**2
print(f"  E[X^2]: {ex2:.4f} (Theoretical: {sigma**2 + mu**2})")

# Note: SciPy doesn't directly provide a symbolic MGF or its derivatives.
# Using MGFs is primarily an analytical technique.
```

## خلاصهٔ فصل

+++

این فصل مقدمه‌ای کوتاه بر چند موضوع پیشرفتهٔ احتمال ارائه داد:
* **نظریهٔ اطلاعات:** دیدیم آنتروپی چگونه عدم‌قطعیت را کمی‌سازی می‌کند (با `scipy.stats.entropy`) و واگرایی KL تفاوت بین توزیع‌ها را می‌سنجد.
* **فرایندهای تصادفی:** مدل‌هایی برای تکامل تصادفی در زمان را بررسی کردیم؛ شبیه‌سازی ورود رویدادها با **فرایند پواسون** (با `scipy.stats.expon` برای زمان‌های بین‌ورودی) و مدل‌سازی حرکت تصادفی پیوسته مانند قیمت سهام با **حرکت براونی هندسی** (با `numpy.random.normal` برای افزایش‌ها).
* **توابع تولیدکننده:** مفاهیم PGF و MGF را به‌عنوان ابزارهای ریاضی برای تحلیل توزیع‌ها و یافتن گشتاورها بررسی کردیم و نشان دادیم `scipy.stats` گشتاورهایی سازگار با نظریهٔ MGF برای توزیع‌های رایج مانند نرمال فراهم می‌کند.

این حوزه‌ها میدان‌های گسترده‌ای از مطالعه را تشکیل می‌دهند. امیدواریم این نگاه کوتاه علاقهٔ شما را برانگیخته و نشان داده باشد که مفاهیم بنیادین آموخته‌شده در سراسر این کتاب پله‌هایی به سوی تکنیک‌های مدل‌سازی احتمالاتی پیچیده‌تر و قدرتمندتر هستند.
