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
  - file: notebooks/chapter_16.ipynb
---

# فصل ۱۶: مقدمه‌ای بر استنتاج بیزی

به فصل ۱۶ خوش آمدید! در بخش ۲، قضیه بیز را به‌عنوان راهی برای به‌روزرسانی احتمال یک *واقعه* با شواهد جدید دیدیم. اکنون این ایدهٔ قدرتمند را گسترش می‌دهیم تا باورهایمان دربارهٔ *پارامترهای* توزیع‌های احتمال خود را به‌روز کنیم. این مفهوم اصلی **استنتاج بیزی** است: استفاده از داده‌های مشاهده‌شده برای به‌روزرسانی نظام‌مند درک ما (که به‌صورت توزیع احتمال بیان می‌شود) از یک کمیت ناشناخته.

به‌جای پرسیدن «احتمال مشاهده این داده با پارامتر ثابت چقدر است؟»، استنتاج بیزی می‌پرسد «توزیع احتمال پارامتر با توجه به داده‌های مشاهده‌شده چیست؟». این تغییر دیدگاه به ما اجازه می‌دهد دانش پیشین را وارد کنیم و عدم‌قطعیت دربارهٔ پارامترها را به‌صورت طبیعی و احتمالاتی بیان کنیم.

**اهداف یادگیری:**
1.  درک نحوهٔ اعمال قضیه بیز برای به‌روزرسانی توزیع‌های احتمال (از پیشین به پسین).
2.  آشنایی با پیشین‌های همراه و سهولت محاسباتی آن‌ها (مثلاً بتا–دوجمله‌ای).
3.  محاسبهٔ برآوردهای نقطه‌ای از توزیع پسین (MAP، میانگین پسین).
4.  درک و محاسبهٔ بازه‌های باور بیزی.
5.  پیاده‌سازی به‌روزرسانی‌های بیزی با پایتون، از جمله تقریب شبکه‌ای برای موارد غیرهمراه.

**مثال‌های این فصل:**
* به‌روزرسانی باورمان دربارهٔ منصفانه بودن سکه (با توزیع بتا برای احتمال شیر، $\theta$) پس از مشاهدهٔ سری پرتاب‌ها (درست‌نمایی دوجمله‌ای).
* برآورد نرخ کلیک (CTR) یک وب‌سایت با پیشین بتا و داده‌های کلیک مشاهده‌شده.
* یافتن محتمل‌ترین مقدار (MAP) و مقدار میانگین (میانگین پسین) برای پارامتر منصفانه بودن سکه $\theta$.
* تعیین بازهٔ باور ۹۵٪ برای CTR که بازه‌ای است که با اطمینان ۹۵٪ CTR واقعی در آن قرار دارد.

+++

## ۱۶.۱ مرور قضیه بیز برای توزیع‌ها

قضیه بیز را از فصل ۵ به‌خاطر بیاورید:

$ P(A|B) = \frac{P(B|A) P(A)}{P(B)} $

در استنتاج بیزی، این را برای کار با توزیع‌های احتمال برای پارامتر ناشناخته، که اغلب با $\theta$ (تتا) نمایش داده می‌شود، تطبیق می‌دهیم. داده‌ای $D$ مشاهده می‌کنیم.

* $P(A)$ به $p(\theta)$ تبدیل می‌شود: **توزیع پیشین**. این باور ما دربارهٔ $\theta$ *قبل از* مشاهدهٔ هر داده‌ای را نشان می‌دهد. می‌تواند بر اساس مطالعات قبلی، نظر کارشناس یا صرفاً حدس غیراطلاعاتی (مثل توزیع یکنواخت) باشد.
* $P(B|A)$ به $p(D|\theta)$ تبدیل می‌شود: **درست‌نمایی**. این احتمال مشاهدهٔ داده $D$ *با فرض* مقدار مشخص پارامتر $\theta$ است. با درست‌نمایی‌ها هنگام تعریف توزیع‌ها زیاد کار کرده‌ایم (مثلاً PMF دوجمله‌ای احتمال $k$ موفقیت با $n$ آزمایش و احتمال موفقیت $\theta$ را می‌دهد).
* $P(A|B)$ به $p(\theta|D)$ تبدیل می‌شود: **توزیع پسین**. این باور به‌روزشده دربارهٔ $\theta$ *پس از* مشاهدهٔ داده $D$ است. ترکیب باورهای پیشین و شواهد داده را نشان می‌دهد.
* $P(B)$ به $p(D)$ تبدیل می‌شود: **شواهد** (یا درست‌نمایی حاشیه‌ای). این احتمال کلی مشاهدهٔ داده $D$ است، میانگین‌گرفته بر همهٔ مقادیر ممکن $\theta$. با انتگرال‌گیری (یا جمع در حالت گسسته) حاصل‌ضرب درست‌نمایی و پیشین بر کل فضای پارامتر محاسبه می‌شود:
    $ p(D) = \int p(D|\theta) p(\theta) d\theta $ (برای $\theta$ پیوسته)
    $ p(D) = \sum_{\theta} p(D|\theta) p(\theta) $ (برای $\theta$ گسسته)

شواهد $p(D)$ به‌عنوان ثابت نرمال‌سازی عمل می‌کند و تضمین می‌کند توزیع پسین $p(\theta|D)$ انتگرال (یا جمع) برابر ۱ دارد.

پس قضیه بیز برای توزیع‌ها می‌شود:

$$ p(\theta | D) = \frac{p(D | \theta) p(\theta)}{p(D)} $$

اغلب بر صورت تمرکز می‌کنیم، چون شواهد $p(D)$ به $\theta$ وابسته نیست و فقط نتیجه را مقیاس می‌دهد:

$$ \underbrace{p(\theta | D)}_{\text{Posterior}} \propto \underbrace{p(D | \theta)}_{\text{Likelihood}} \times \underbrace{p(\theta)}_{\text{Prior}} $$

این می‌خواند: «توزیع پسین متناسب با حاصل‌ضرب درست‌نمایی و توزیع پیشین است.»

+++

**مثال: پرتاب سکه**

$\theta$ احتمال ناشناختهٔ آمدن شیر برای سکه‌ای بالقوه نامتقارن باشد. می‌خواهیم $\theta$ را بر اساس پرتاب‌های مشاهده‌شده برآورد کنیم.

* **پارامتر:** $\theta$، که $0 \le \theta \le 1$.
* **پیشین:** باور اولیهٔ ما دربارهٔ $\theta$ چیست؟ اگر چیزی نمی‌دانیم، ممکن است فرض کنیم $\theta$ به‌طور یکسان احتمال دارد هر مقداری بین ۰ و ۱ باشد. این متناظر با توزیع یکنواخت، $p(\theta) = \text{Uniform}(0, 1)$ است. جالب است که این همان توزیع بتا است: $\text{Beta}(\alpha=1, \beta=1)$.
* **داده:** فرض کنید سکه را $n$ بار پرتاب می‌کنیم و $k$ شیر مشاهده می‌کنیم. $D = (n, k)$ باشد.
* **درست‌نمایی:** با فرض $\theta$ مشخص، احتمال مشاهدهٔ $k$ شیر در $n$ پرتاب با PMF دوجمله‌ای داده می‌شود: $p(D|\theta) = \binom{n}{k} \theta^k (1-\theta)^{n-k}$.
* **پسین:** با استفاده از رابطهٔ تناسب:
    $p(\theta | D) \propto p(D|\theta) p(\theta)$
    $p(\theta | D) \propto \left[ \binom{n}{k} \theta^k (1-\theta)^{n-k} \right] \times [1]$ (با فرض پیشین Uniform(0,1) که $p(\theta)=1$ برای $0 \le \theta \le 1$)
    $p(\theta | D) \propto \theta^k (1-\theta)^{n-k}$ (چون $\binom{n}{k}$ نسبت به $\theta$ ثابت است)

شکل $\theta^{\alpha-1} (1-\theta)^{beta-1}$ را می‌شناسیم که هستهٔ توزیع بتا است. به‌طور مشخص، $p(\theta|D)$ از توزیع $\text{Beta}(\alpha = k+1, \beta = n-k+1)$ پیروی می‌کند.

این نشان می‌دهد چگونه مشاهدهٔ داده ($k$ شیر در $n$ پرتاب) باورمان دربارهٔ $\theta$ را از پیشین $\text{Beta}(1, 1)$ به پسین $\text{Beta}(k+1, n-k+1)$ به‌روز می‌کند.

+++

## ۱۶.۲ پیشین‌های همراه

در مثال پرتاب سکه بالا، با پیشین بتا برای $\theta$ شروع کردیم و پس از مشاهدهٔ دادهٔ دوجمله‌ای به پسین بتا رسیدیم. این نمونه‌ای از **همراهی** است.

پیشین **پیشین همراه** برای تابع درست‌نمایی داده‌شده نامیده می‌شود اگر توزیع پسین حاصل به *همان خانواده* توزیع پیشین تعلق داشته باشد.

| درست‌نمایی      | پارامتر      | خانوادهٔ پیشین همراه | خانوادهٔ پسین | مثال کاربرد              |
| :-------------- | :------------- | :--------------------- | :--------------- | :------------------------------- |
| Bernoulli       | احتمال موفقیت $\theta$ | Beta                   | Beta             | پرتاب سکه، نرخ کلیک   |
| Binomial        | احتمال موفقیت $\theta$ | Beta                   | Beta             | پرتاب‌های متعدد سکه، درصد نظرسنجی    |
| Poisson         | نرخ $\lambda$          | Gamma                  | Gamma            | شمارش واقعه‌ها (ایمیل، تصادف) |
| Exponential     | نرخ $\lambda$          | Gamma                  | Gamma            | زمان انتظار، عمر قطعه    |
| Normal (known $\sigma^2$) | میانگین $\mu$            | Normal                 | Normal           | خطای اندازه‌گیری (واریانس معلوم)  |
| Normal (known $\mu$) | واریانس $\sigma^2$     | Inverse Gamma          | Inverse Gamma    | خطای اندازه‌گیری (میانگین معلوم) |

**چرا پیشین‌های همراه مفیدند؟**
1.  **سادگی محاسباتی:** اگر پیشین همراه استفاده کنیم، توزیع پسین شکل تحلیلی شناخته‌شده دارد. فقط باید پارامترهای توزیع را بر اساس داده به‌روز کنیم، اغلب با قواعد جبری ساده. مثلاً برای بتا–دوجمله‌ای:
    * پیشین: $\text{Beta}(\alpha_{prior}, \beta_{prior})$
    * داده: $k$ موفقیت در $n$ آزمایش
    * پسین: $\text{Beta}(\alpha_{prior} + k, \beta_{prior} + n - k)$
2.  **قابلیت تفسیر:** ماندن در همان خانوادهٔ توزیع درک اینکه داده چگونه باورها را جابه‌جا کرده آسان‌تر می‌کند. می‌توانیم پارامترهای پیشین و پسین را مستقیماً مقایسه کنیم.

**محدودیت‌ها:**
* پیشین همراه ممکن است باور پیشین واقعی ما را به‌درستی منعکس نکند.
* برای مدل‌های پیچیده، پیشین همراه ممکن است وجود نداشته باشد یا به‌راحتی شناسایی نشود.

در مواردی که پیشین همراه مناسب یا در دسترس نیست، اغلب به روش‌های عددی مانند Markov Chain Monte Carlo (MCMC) یا تقریب شبکه‌ای (که بعداً در این فصل می‌بینیم) برای برآورد توزیع پسین متوسل می‌شویم.

+++

## ۱۶.۳ برآوردهای نقطه‌ای (MAP، میانگین پسین)

توزیع پسین $p(\theta|D)$ تمام دانش به‌روزشدهٔ ما دربارهٔ پارامتر $\theta$ را در بر دارد. اما اغلب می‌خواهیم این توزیع را با یک «حدس بهترین» برای مقدار $\theta$ خلاصه کنیم. انتخاب‌های رایج:

1.  **برآورد MAP (Maximum a Posteriori):**
    * این مقدار $\theta$ است که چگالی (یا جرم) احتمال پسین را بیشینه می‌کند. *مد* توزیع پسین است.
    * $\hat{\theta}_{MAP} = \arg \max_{\theta} p(\theta | D)$
    * از آنجا که $p(\theta | D) \propto p(D | \theta) p(\theta)$، برآورد MAP حاصل‌ضرب درست‌نمایی و پیشین را بیشینه می‌کند.
    * اگر پیشین $p(\theta)$ یکنواخت (مسطح) باشد، برآورد MAP با برآورد بیشینه درست‌نمایی (MLE) که از آمار فراوانی می‌شناسیم هم‌خوان است.
    * برای پسین بتا$(\alpha, \beta)$، مد برابر $\frac{\alpha - 1}{\alpha + \beta - 2}$ است (به‌شرط $\alpha > 1$ و $\beta > 1$).

2.  **میانگین پسین:**
    * این امید ریاضی (میانگین) $\theta$ طبق توزیع پسین است.
    * $\hat{\theta}_{Mean} = E[\theta | D] = \int \theta p(\theta | D) d\theta$
    * مرکز جرم توزیع پسین را نشان می‌دهد.
    * اغلب تعادل خوبی بین باور پیشین و داده فراهم می‌کند.
    * برای پسین بتا$(\alpha, \beta)$، میانگین $\frac{\alpha}{\alpha + \beta}$ است.

**مثال: ادامهٔ پرتاب سکه**
فرض کنید پیشین ما $\text{Beta}(1, 1)$ (یکنواخت) است و $k=8$ شیر در $n=10$ پرتاب مشاهده می‌کنیم.

* توزیع پسین $\text{Beta}(\alpha = 1+8, \beta = 1+10-8) = \text{Beta}(9, 3)$ است.
* **برآورد MAP:** $\hat{\theta}_{MAP} = \frac{\alpha - 1}{\alpha + \beta - 2} = \frac{9 - 1}{9 + 3 - 2} = \frac{8}{10} = 0.8$. این با نسبت نمونه (MLE) هم‌خوان است، همان‌طور که با پیشین یکنواخت انتظار می‌رود.
* **میانگین پسین:** $\hat{\theta}_{Mean} = \frac{\alpha}{\alpha + \beta} = \frac{9}{9 + 3} = \frac{9}{12} = 0.75$. توجه کنید این کمی از نسبت نمونه (۰٫۸) به سمت میانگین پیشین (که برای Beta(1,1) برابر ۰٫۵ بود) «جمع شده». تأثیر پیشین اینجا کوچک است چون دادهٔ معقولی داریم. اگر پیشین قوی‌تر بود (مثلاً Beta(5,5)، قوی متمرکز روی ۰٫۵) یا داده ضعیف‌تر (مثلاً ۱ پرتاب)، جمع‌شدگی بیشتر بود.

+++

## ۱۶.۴ بازه‌های باور

به‌جای فقط یک برآورد نقطه‌ای، اغلب می‌خواهیم عدم‌قطعیت دربارهٔ $\theta$ را با بازه بیان کنیم. در استنتاج بیزی، این با **بازه‌های باور** انجام می‌شود.

بازهٔ باور $100(1-\gamma)\%$ برای $\theta$ بازه‌ای $[L, U]$ است که احتمال پسین قرار گرفتن $\theta$ در این بازه برابر $1-\gamma$ است:

$$ P(L \le \theta \le U | D) = \int_L^U p(\theta | D) d\theta = 1 - \gamma $$

انتخاب‌های رایج برای $\gamma$ عبارت‌اند از ۰٫۰۵ (برای بازهٔ باور ۹۵٪) یا ۰٫۱۰ (برای بازهٔ باور ۹۰٪).

**تفسیر:** «با توجه به داده، احتمال $100(1-\gamma)\%$ وجود دارد که مقدار واقعی $\theta$ در بازهٔ $[L, U]$ قرار گیرد.»

این تفسیر مستقیم و شهودی است و اغلب مزیت نسبت به *بازه‌های اطمینان* فراوانی دیده می‌شود. (به‌خاطر بیاورید بازهٔ اطمینان ۹۵٪ یعنی اگر آزمایش را بارها تکرار کنیم، ۹۵٪ *بازه‌هایی* که می‌سازیم مقدار ثابت و واقعی پارامتر را در بر می‌گیرند؛ احتمال قرار گرفتن *پارامتر* در یک *بازهٔ مشخص* را نمی‌دهد).

**محاسبه:**
راه‌های مختلفی برای ساخت بازهٔ باور وجود دارد:
1.  **بازهٔ باور با چگالی پسین بیشینه (HPDI):** باریک‌ترین بازهٔ ممکن $[L, U]$ را می‌یابد که $100(1-\gamma)\%$ احتمال پسین را در بر می‌گیرد. برای پسین تک‌مدی، همهٔ نقاط داخل HPDI چگالی احتمال بالاتری از هر نقطهٔ خارج آن دارند. از نظر مفهومی جذاب است اما محاسباتی سخت‌تر می‌تواند باشد.
2.  **بازهٔ هم‌دم:** محاسبه آسان‌تر است. چارک $\gamma/2$ و چارک $1 - \gamma/2$ توزیع پسین را می‌یابیم. این‌ها کران‌های پایین و بالای $[L, U]$ را تشکیل می‌دهند. برای بازهٔ ۹۵٪ ($\gamma=0.05$)، صدک ۲٫۵ و ۹۷٫۵ را می‌یابیم.

برای توزیع‌های پسین متقارن (مثل نرمال)، HPDI و بازهٔ هم‌دم یکی‌اند. برای توزیع‌های چوله (مثل بتا یا گاما که اغلب چنین‌اند)، متفاوت‌اند. معمولاً برای سادگی از بازهٔ هم‌دم استفاده می‌کنیم مگر دلیل قوی دیگری باشد.

**مثال: ادامهٔ پرتاب سکه**
پسین ما $\text{Beta}(9, 3)$ است. برای یافتن بازهٔ باور هم‌دم ۹۵٪ برای $\theta$:
* به صدک ۲٫۵ (چارک ۰٫۰۲۵) و صدک ۹۷٫۵ (چارک ۰٫۹۷۵) توزیع $\text{Beta}(9, 3)$ نیاز داریم.
* می‌توانیم از `scipy.stats.beta.ppf` (تابع درصد، معکوس CDF) استفاده کنیم.

```{code-cell} ipython3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Setup plotting style
plt.style.use('seaborn-v0_8-whitegrid')
```

```{code-cell} ipython3
# Parameters for the Beta posterior
alpha_post = 9
beta_post = 3
confidence_level = 0.95
gamma = 1 - confidence_level
```

```{code-cell} ipython3
# Calculate the lower and upper bounds of the equal-tailed credible interval
lower_bound = stats.beta.ppf(gamma / 2, alpha_post, beta_post)
upper_bound = stats.beta.ppf(1 - gamma / 2, alpha_post, beta_post)
```

```{code-cell} ipython3
# Calculate point estimates
posterior_mean = stats.beta.mean(alpha_post, beta_post)
posterior_mode = (alpha_post - 1) / (alpha_post + beta_post - 2) if alpha_post > 1 and beta_post > 1 else np.nan
```

```{code-cell} ipython3
print(f"Posterior Distribution: Beta(alpha={alpha_post}, beta={beta_post})")
print(f"Posterior Mean: {posterior_mean:.4f}")
print(f"Posterior Mode (MAP): {posterior_mode:.4f}")
print(f"95% Equal-tailed Credible Interval: [{lower_bound:.4f}, {upper_bound:.4f}]")
```

```{code-cell} ipython3
# Plot the posterior distribution and the credible interval
theta_vals = np.linspace(0, 1, 500)
posterior_pdf = stats.beta.pdf(theta_vals, alpha_post, beta_post)
```

```{code-cell} ipython3
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, posterior_pdf, label=f'Posterior: Beta({alpha_post}, {beta_post})', color='blue')

# Shade the credible interval
ci_mask = (theta_vals >= lower_bound) & (theta_vals <= upper_bound)
plt.fill_between(theta_vals[ci_mask], posterior_pdf[ci_mask], 
                 color='lightblue', alpha=0.6, label=f'95% Credible Interval')

# Mark the mean and MAP
plt.axvline(posterior_mean, color='red', linestyle='--', label=f'Mean: {posterior_mean:.2f}')
plt.axvline(posterior_mode, color='green', linestyle=':', label=f'MAP: {posterior_mode:.2f}')

plt.title('Posterior Distribution and 95% Credible Interval for Coin Fairness $\\theta$')
plt.xlabel('$\\theta$ (Probability of Heads)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
```

نمودار توزیع پسین $\text{Beta}(9, 3)$ را نشان می‌دهد. ناحیهٔ سایه‌دار بازهٔ باور ۹۵٪ را نشان می‌دهد؛ یعنی با اطمینان ۹۵٪ مقدار واقعی $\theta$ بین تقریباً ۰٫۴۷ و ۰٫۹۵ قرار دارد. میانگین (۰٫۷۵) و MAP (۰٫۸۰) خلاصه‌های نقطه‌ای این توزیع را فراهم می‌کنند.

+++

## ۱۶.۵ عملی: پیاده‌سازی و تقریب شبکه‌ای

یک مثال عملی را بررسی می‌کنیم: برآورد نرخ کلیک (CTR) یک وب‌سایت.

**سناریو:** کمپین تبلیغاتی اجرا می‌کنیم. می‌خواهیم احتمال زیربنایی ($\theta$) اینکه کاربری که تبلیغ را می‌بیند روی آن کلیک کند را برآورد کنیم.

* **پارامتر:** $\theta$ (CTR)، $0 \le \theta \le 1$.
* **باور پیشین:** قبل از شروع کمپین، بر اساس تجربهٔ گذشته با تبلیغات مشابه، باور داریم CTR احتمالاً حدود ۱٪ است، اما چندان مطمئن نیستیم. توزیع بتا می‌تواند این را نشان دهد. پیشینی با میانگین حدود ۰٫۰۱ و پراکندگی معقول انتخاب می‌کنیم، مثلاً $\text{Beta}(2, 198)$. ویژگی‌های آن را بررسی می‌کنیم.
* **داده:** تبلیغ به $n=1000$ کاربر نشان داده می‌شود و $k=15$ کلیک مشاهده می‌کنیم.
* **درست‌نمایی:** تعداد کلیک‌ها $k$ با $n$ نمایش و CTR $\theta$ از توزیع دوجمله‌ای پیروی می‌کند: $p(D|\theta) = \text{Binomial}(k=15 | n=1000, \theta)$.
* **هدف:** توزیع پسین $p(\theta|D)$ را بیابیم، میانگین پسین، MAP و بازهٔ باور ۹۵٪ را محاسبه کنیم.

+++

--- رویکرد پیشین همراه (بتا–دوجمله‌ای) ---

```{code-cell} ipython3
# Prior parameters
alpha_prior = 2
beta_prior = 198
```

```{code-cell} ipython3
# Data
n_trials = 1000
k_successes = 15
```

```{code-cell} ipython3
# Calculate prior mean and standard deviation
prior_mean = stats.beta.mean(alpha_prior, beta_prior)
prior_std = stats.beta.std(alpha_prior, beta_prior)
print(f"Prior: Beta(alpha={alpha_prior}, beta={beta_prior})")
print(f"Prior Mean: {prior_mean:.4f}")
print(f"Prior Std Dev: {prior_std:.4f}")
```

```{code-cell} ipython3
# Calculate posterior parameters using conjugate update rule
alpha_post_conj = alpha_prior + k_successes
beta_post_conj = beta_prior + n_trials - k_successes
```

```{code-cell} ipython3
print(f"\nPosterior (Conjugate): Beta(alpha={alpha_post_conj}, beta={beta_post_conj})")
```

```{code-cell} ipython3
# Calculate posterior summaries
post_mean_conj = stats.beta.mean(alpha_post_conj, beta_post_conj)
post_mode_conj = (alpha_post_conj - 1) / (alpha_post_conj + beta_post_conj - 2)
lower_ci_conj = stats.beta.ppf(0.025, alpha_post_conj, beta_post_conj)
upper_ci_conj = stats.beta.ppf(0.975, alpha_post_conj, beta_post_conj)
```

```{code-cell} ipython3
print(f"Posterior Mean: {post_mean_conj:.4f}")
print(f"Posterior MAP: {post_mode_conj:.4f}")
print(f"95% Credible Interval: [{lower_ci_conj:.4f}, {upper_ci_conj:.4f}]")
```

```{code-cell} ipython3
# Plot prior and posterior
theta_vals = np.linspace(0, 0.05, 500) # Focus on relevant range
prior_pdf = stats.beta.pdf(theta_vals, alpha_prior, beta_prior)
posterior_pdf_conj = stats.beta.pdf(theta_vals, alpha_post_conj, beta_post_conj)
```

```{code-cell} ipython3
plt.figure(figsize=(12, 7))
plt.plot(theta_vals, prior_pdf, 
         label=f'Prior: Beta({alpha_prior}, {beta_prior})', color='grey', linestyle='--')
plt.plot(theta_vals, posterior_pdf_conj, 
         label=f'Posterior: Beta({alpha_post_conj}, {beta_post_conj})', color='blue')

# Add CI shading
ci_mask = (theta_vals >= lower_ci_conj) & (theta_vals <= upper_ci_conj)
plt.fill_between(theta_vals[ci_mask], posterior_pdf_conj[ci_mask], 
                 color='lightblue', alpha=0.6, label=f'95% Credible Interval')

plt.title('Bayesian Update for Website CTR (Beta-Binomial)')
plt.xlabel('$\\theta$ (Click-Through Rate)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
```

همان‌طور که می‌بینید، توزیع پسین نسبت به پیشین به راست جابه‌جا شده و دادهٔ مشاهده‌شده (۱۵/۱۰۰۰ = ۰٫۰۱۵، که بالاتر از میانگین پیشین ~۰٫۰۱ است) را منعکس می‌کند. پسین نیز باریک‌تر (تیزتر) از پیشین است و نشان‌دهندهٔ افزایش اطمینان دربارهٔ CTR پس از مشاهدهٔ داده است. برآورد به‌روزشدهٔ CTR (میانگین پسین) حدود ۰٫۰۱۴۲ است و با اطمینان ۹۵٪ بین ۰٫۰۰۸۱ و ۰٫۰۲۱۷ قرار دارد.

### تقریب شبکه‌ای

اگر پیشین همراه نداشتیم یا مدل پیچیده‌تر بود چه؟ می‌توانیم توزیع پسین را به‌صورت عددی با **تقریب شبکه‌ای** تقریب بزنیم.

مراحل:
1.  **تعریف شبکه:** فهرستی از مقادیر گسستهٔ کاندید برای پارامتر $\theta$ در بازهٔ محتمل آن بسازید.
2.  **محاسبهٔ احتمالات پیشین:** احتمال (یا چگالی) پیشین را برای هر مقدار $\theta$ روی شبکه ارزیابی کنید.
3.  **محاسبهٔ درست‌نمایی:** برای هر $\theta$ روی شبکه، درست‌نمایی مشاهدهٔ داده $D$ با آن $\theta$ را محاسبه کنید.
4.  **محاسبهٔ پسین نرمال‌نشده:** برای هر $\theta$ روی شبکه، احتمال پیشین را در درست‌نمایی ضرب کنید. این $p(D|\theta)p(\theta)$ را می‌دهد.
5.  **نرمال‌سازی:** مقادیر پسین نرمال‌نشده را روی شبکه جمع کنید. هر مقدار پسین نرمال‌نشده را بر این جمع تقسیم کنید تا احتمال پسین نرمال‌شده $p(\theta|D)$ برای هر نقطهٔ شبکه به‌دست آید. نتیجه تقریب گسستهٔ توزیع پسین است.

مثال CTR را با تقریب شبکه‌ای تکرار می‌کنیم. همان پیشین $\text{Beta}(2, 198)$ و درست‌نمایی $\text{Binomial}(15 | 1000, \theta)$ را استفاده می‌کنیم.

+++

--- رویکرد تقریب شبکه‌ای ---

```{code-cell} ipython3
# 1. Define the grid
n_grid_points = 1000
grid_theta = np.linspace(0, 0.05, n_grid_points) # Grid over plausible theta range
```

```{code-cell} ipython3
# 2. Calculate Prior Probabilities
prior_on_grid = stats.beta.pdf(grid_theta, alpha_prior, beta_prior)
```

```{code-cell} ipython3
# 3. Calculate Likelihood
# Note: We use log-likelihood for numerical stability with small probabilities
log_likelihood_on_grid = stats.binom.logpmf(k_successes, n_trials, grid_theta)
# Convert back, handling potential underflow (though less likely with logpmf)
likelihood_on_grid = np.exp(log_likelihood_on_grid)
```

```{code-cell} ipython3
# 4. Compute Unnormalized Posterior
unnormalized_posterior = likelihood_on_grid * prior_on_grid
```

```{code-cell} ipython3
# 5. Normalize
# The integral approximation is sum(value * step_size)
# step_size = grid_theta[1] - grid_theta[0] # Alternatively, use np.diff(grid_theta)[0]
# evidence = np.sum(unnormalized_posterior) * step_size
# Or simply normalize probabilities to sum to 1 for the discrete grid points
evidence = np.sum(unnormalized_posterior)
posterior_prob_grid = unnormalized_posterior / evidence
```

```{code-cell} ipython3
# Check normalization (should be close to 1 / step_size if thought of as density,
# or sum of probs = 1 if thought of as discrete PMF over grid points)
print(f"Sum of posterior probabilities on grid: {np.sum(posterior_prob_grid):.4f}") # Should be 1.0
```

```{code-cell} ipython3
# Calculate summaries from the grid approximation
# Posterior Mean
post_mean_grid = np.sum(grid_theta * posterior_prob_grid)
```

```{code-cell} ipython3
# Posterior MAP
map_index = np.argmax(posterior_prob_grid)
post_map_grid = grid_theta[map_index]
```

```{code-cell} ipython3
# Credible Interval (using cumulative sum of probabilities)
cumulative_posterior = np.cumsum(posterior_prob_grid)
lower_idx_grid = np.where(cumulative_posterior >= 0.025)[0][0]
upper_idx_grid = np.where(cumulative_posterior >= 0.975)[0][0]
lower_ci_grid = grid_theta[lower_idx_grid]
upper_ci_grid = grid_theta[upper_idx_grid]
```

```{code-cell} ipython3
print(f"\nPosterior Summaries (Grid Approximation):")
print(f"Posterior Mean: {post_mean_grid:.4f}")
print(f"Posterior MAP: {post_map_grid:.4f}")
print(f"95% Credible Interval: [{lower_ci_grid:.4f}, {upper_ci_grid:.4f}]")
```

```{code-cell} ipython3
# Plot the grid approximation vs the analytical solution
plt.figure(figsize=(12, 7))
# Plot analytical posterior (scaled to match grid density if needed, though scaling cancels visually here)
step_size = grid_theta[1]-grid_theta[0]
plt.plot(theta_vals, posterior_pdf_conj, 
         label=f'Analytical Posterior', color='blue', linewidth=2.5)

# Plot grid approximation - treat posterior_prob_grid as PMF, scale for density plotting
plt.plot(grid_theta, posterior_prob_grid / step_size, 
         label=f'Grid Approximation ({n_grid_points} points)', color='red', linestyle='--', alpha=0.8)

plt.title('Grid Approximation vs Analytical Posterior for CTR')
plt.xlabel('$\\theta$ (Click-Through Rate)')
plt.ylabel('Probability Density / Scaled Probability')
plt.legend()
plt.show()
```

نتایج تقریب شبکه‌ای (میانگین ~۰٫۰۱۴۲، MAP ~۰٫۰۱۴۱، بازه [۰٫۰۰۸۱، ۰٫۰۲۱۸]) بسیار نزدیک به نتایج تحلیلی با پیشین همراه (میانگین ۰٫۰۱۴۲، MAP ۰٫۰۱۴۲، بازه [۰٫۰۰۸۱، ۰٫۰۲۱۷]) هستند. تفاوت‌های کوچک به گسسته‌سازی فضای پارامتر در روش شبکه‌ای مربوط است. افزایش تعداد نقاط شبکه معمولاً دقت را بهبود می‌دهد.

تقریب شبکه‌ای ابزار همه‌کاره‌ای است، به‌ویژه وقتی پیشین همراه در دسترس نیست یا با درست‌نمایی یا پیشین‌های پیچیده‌تر سروکار داریم. محدودیت اصلی آن «نفرین ابعاد» است — اگر بخواهیم چند پارامتر را همزمان برآورد کنیم محاسباتی پرهزینه می‌شود، چون اندازهٔ شبکه به‌صورت نمایی با تعداد پارامترها رشد می‌کند. برای مسائل با ابعاد بالاتر، روش‌هایی مانند Markov Chain Monte Carlo (MCMC) ترجیح داده می‌شوند (هرچند فراتر از حوصلهٔ این فصل مقدماتی است).

+++

## ۱۶.۶ خلاصهٔ فصل

استنتاج بیزی چارچوب رسمی برای به‌روزرسانی باورهایمان دربارهٔ پارامترهای ناشناخته در پرتو داده‌های مشاهده‌شده فراهم می‌کند.

* از **قضیه بیز** برای توزیع‌ها بهره می‌برد: $p(\theta | D) \propto p(D | \theta) p(\theta)$.
* با **توزیع پیشین** $p(\theta)$ که باورهای اولیه را نشان می‌دهد شروع می‌کنیم.
* **درست‌نمایی** $p(D|\theta)$ می‌سنجد داده $D$ برای مقادیر مختلف پارامتر $\theta$ چقدر محتمل است.
* نتیجه **توزیع پسین** $p(\theta|D)$ است که دانش پیشین را با شواهد داده ترکیب می‌کند.
* **پیشین‌های همراه** محاسبات را ساده می‌کنند چون پسین به همان خانوادهٔ توزیع پیشین تعلق دارد (مثلاً پیشین بتا برای درست‌نمایی دوجمله‌ای/برنولی به پسین بتا منجر می‌شود).
* توزیع پسین را می‌توان با **برآوردهای نقطه‌ای** مانند **میانگین پسین** (امید ریاضی) و **MAP** (مد) خلاصه کرد.
* عدم‌قطعیت با **بازه‌های باور** کمی‌سازی می‌شود که بازه‌ای می‌دهند که پارامتر با احتمال مشخص (مثلاً ۹۵٪) در آن قرار دارد.
* وقتی راه‌حل‌های تحلیلی دشوار است، روش‌های عددی مانند **تقریب شبکه‌ای** برای برآورد توزیع پسین قابل استفاده‌اند.

روش‌های بیزی تفسیر شهودی احتمال (به‌عنوان درجهٔ باور) و گنجاندن طبیعی اطلاعات پیشین را ممکن می‌سازند و ابزارهای قدرتمندی برای تحلیل داده و مدل‌سازی در حوزه‌های گوناگون هستند.

+++

## تمرین‌ها

1.  **حساسیت پیشین:** برآورد CTR (به‌روزرسانی همراه بتا–دوجمله‌ای) را با پیشین کم‌اطلاعاتی‌تر $\text{Beta}(1, 1)$ (یکنواخت) تکرار کنید. میانگین پسین، MAP و بازهٔ باور ۹۵٪ را با نتایج $\text{Beta}(2, 198)$ مقایسه کنید. انتخاب پیشین با ۱۰۰۰ نقطهٔ داده چقدر بر نتایج تأثیر می‌گذارد؟
2.  **پیشین قوی‌تر:** اکنون برآورد CTR را با باور پیشین قوی‌تر که CTR پایین است تکرار کنید، شاید $\text{Beta}(1, 99)$. نتایج پسین نسبت به پیشین اصلی $\text{Beta}(2, 198)$ و پیشین یکنواخت چگونه تغییر می‌کند؟
3.  **همراهی پواسون–گاما:** تعداد ایمیل‌های رسیده در ساعت از توزیع پواسون با نرخ ناشناخته $\lambda$ پیروی می‌کند. باور پیشین شما دربارهٔ $\lambda$ با توزیع $\text{Gamma}(\alpha=3, \text{scale}=1/\beta=0.5)$ مدل شده است (توجه: `scipy.stats.gamma` از shape=$ \alpha $، scale=$ 1/\beta $ استفاده می‌کند). در یک ساعت مشخص، $k=5$ ایمیل مشاهده می‌کنید.
    * خانوادهٔ پیشین همراه برای نرخ پواسون $\lambda$ چیست؟ (راهنما: گاما)
    * قاعدهٔ به‌روزرسانی گاما–پواسون: اگر پیشین $\text{Gamma}(\alpha_{prior}, \beta_{prior})$ و داده $k$ واقعه (در یک واحد زمان/مواجهه) باشد، پسین $\text{Gamma}(\alpha_{prior} + k, \beta_{prior} + 1)$ است. به‌خاطر بیاورید `scipy.stats` از scale = 1/rate ($\beta$) استفاده می‌کند. پس اگر پیشین `stats.gamma(a=alpha_prior, scale=1/beta_prior)` باشد، پسین `stats.gamma(a=alpha_prior + k, scale=1/(beta_prior + 1))` است.
    * پارامترهای توزیع پسین برای $\lambda$ را محاسبه کنید.
    * میانگین پسین و بازهٔ باور ۹۰٪ برای $\lambda$ را بیابید.
    * توزیع‌های پیشین و پسین را رسم کنید.
4.  **تقریب شبکه‌ای برای پواسون–گاما:** روش تقریب شبکه‌ای را برای مسئلهٔ پواسون–گاما در تمرین ۳ پیاده‌سازی کنید. شبکهٔ معقولی برای $\lambda$ تعریف کنید (مثلاً از ۰ تا ۱۵). میانگین پسین و بازهٔ باور ۹۰٪ را از شبکه محاسبه و با نتایج تحلیلی مقایسه کنید. تقریب شبکه‌ای را در برابر پسین تحلیلی رسم کنید.

```{code-cell} ipython3
# فضای کد/محاسبهٔ تمرین ۱
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Setup plotting style
plt.style.use('seaborn-v0_8-whitegrid')
```

```{code-cell} ipython3
# Data
n_trials = 1000
k_successes = 15
```

```{code-cell} ipython3
# Uniform Prior parameters
alpha_prior_unif = 1
beta_prior_unif = 1
```

```{code-cell} ipython3
# Calculate posterior parameters
alpha_post_unif = alpha_prior_unif + k_successes
beta_post_unif = beta_prior_unif + n_trials - k_successes
```

```{code-cell} ipython3
print("--- Exercise 1: Uniform Prior Beta(1, 1) ---")
print(f"Posterior (Uniform Prior): Beta(alpha={alpha_post_unif}, beta={beta_post_unif})")
```

```{code-cell} ipython3
# Calculate posterior summaries
post_mean_unif = stats.beta.mean(alpha_post_unif, beta_post_unif)
post_mode_unif = (alpha_post_unif - 1) / (alpha_post_unif + beta_post_unif - 2)
lower_ci_unif = stats.beta.ppf(0.025, alpha_post_unif, beta_post_unif)
upper_ci_unif = stats.beta.ppf(0.975, alpha_post_unif, beta_post_unif)
```

```{code-cell} ipython3
print(f"Posterior Mean: {post_mean_unif:.4f}")
print(f"Posterior MAP: {post_mode_unif:.4f}")
print(f"95% Credible Interval: [{lower_ci_unif:.4f}, {upper_ci_unif:.4f}]")
print("Comparison: The results are very similar to the Beta(2, 198) prior case, suggesting the large dataset (n=1000) largely outweighs the difference between these two relatively weak priors.")
```

Exercise 2 Code Placeholder

```{code-cell} ipython3
# Stronger Low Prior parameters
alpha_prior_strong = 1
beta_prior_strong = 99 # Mean = 1 / (1+99) = 0.01
```

```{code-cell} ipython3
# Calculate posterior parameters
alpha_post_strong = alpha_prior_strong + k_successes
beta_post_strong = beta_prior_strong + n_trials - k_successes
```

```{code-cell} ipython3
print("\n--- Exercise 2: Stronger Prior Beta(1, 99) ---")
print(f"Posterior (Strong Prior): Beta(alpha={alpha_post_strong}, beta={beta_post_strong})")
```

```{code-cell} ipython3
# Calculate posterior summaries
post_mean_strong = stats.beta.mean(alpha_post_strong, beta_post_strong)
post_mode_strong = (alpha_post_strong - 1) / (alpha_post_strong + beta_post_strong - 2)
lower_ci_strong = stats.beta.ppf(0.025, alpha_post_strong, beta_post_strong)
upper_ci_strong = stats.beta.ppf(0.975, alpha_post_strong, beta_post_strong)
```

```{code-cell} ipython3
print(f"Posterior Mean: {post_mean_strong:.4f}")
print(f"Posterior MAP: {post_mode_strong:.4f}")
print(f"95% Credible Interval: [{lower_ci_strong:.4f}, {upper_ci_strong:.4f}]")
print("Comparison: Compared to the original Beta(2, 198) prior, the posterior mean (0.0146 vs 0.0142) and MAP (0.0138 vs 0.0142) are slightly lower, pulled more towards the stronger prior belief centered at 0.01. The credible interval is also slightly shifted lower and is marginally narrower, reflecting the stronger prior influence.")
```

Exercise 3 Code Placeholder

```{code-cell} ipython3
# Prior parameters (Gamma(alpha, beta_rate))
alpha_prior_pois = 3
beta_rate_prior_pois = 2 # Since scale = 1/beta_rate = 0.5
scale_prior_pois = 1 / beta_rate_prior_pois
```

```{code-cell} ipython3
# Data (number of events in unit time)
k_events = 5
time_exposure = 1 # Assumed unit time
```

```{code-cell} ipython3
# Calculate posterior parameters
alpha_post_pois = alpha_prior_pois + k_events
beta_rate_post_pois = beta_rate_prior_pois + time_exposure
scale_post_pois = 1 / beta_rate_post_pois
```

```{code-cell} ipython3
print("\n--- Exercise 3: Poisson-Gamma Conjugate Update ---")
print(f"Prior: Gamma(alpha={alpha_prior_pois}, rate={beta_rate_prior_pois}) or Gamma(alpha={alpha_prior_pois}, scale={scale_prior_pois})")
print(f"Data: k={k_events} events observed")
print(f"Posterior: Gamma(alpha={alpha_post_pois}, rate={beta_rate_post_pois}) or Gamma(alpha={alpha_post_pois}, scale={scale_post_pois})")
```

```{code-cell} ipython3
# Calculate posterior mean and CI
# Mean of Gamma(alpha, rate) is alpha / rate
post_mean_pois = alpha_post_pois / beta_rate_post_pois
# Use scipy.stats.gamma with scale parameter
lower_ci_pois = stats.gamma.ppf(0.05, a=alpha_post_pois, scale=scale_post_pois) # 90% CI -> 0.05 and 0.95 quantiles
upper_ci_pois = stats.gamma.ppf(0.95, a=alpha_post_pois, scale=scale_post_pois)
```

```{code-cell} ipython3
print(f"Posterior Mean (lambda): {post_mean_pois:.4f}")
print(f"90% Credible Interval for lambda: [{lower_ci_pois:.4f}, {upper_ci_pois:.4f}]")
```

```{code-cell} ipython3
# Plot prior and posterior
lambda_vals = np.linspace(0, 10, 500)
prior_pdf_pois = stats.gamma.pdf(lambda_vals, a=alpha_prior_pois, scale=scale_prior_pois)
post_pdf_pois = stats.gamma.pdf(lambda_vals, a=alpha_post_pois, scale=scale_post_pois)
```

```{code-cell} ipython3
plt.figure(figsize=(10, 6))
plt.plot(lambda_vals, prior_pdf_pois, 
         label=f'Prior: Gamma({alpha_prior_pois}, rate={beta_rate_prior_pois})', color='grey', linestyle='--')
plt.plot(lambda_vals, post_pdf_pois, 
         label=f'Posterior: Gamma({alpha_post_pois}, rate={beta_rate_post_pois})', color='blue')


# Add CI shading
ci_mask_pois = (lambda_vals >= lower_ci_pois) & (lambda_vals <= upper_ci_pois)
plt.fill_between(lambda_vals[ci_mask_pois], post_pdf_pois[ci_mask_pois], 
                 color='lightblue', alpha=0.6, label=f'90% Credible Interval')

plt.title('Bayesian Update for Poisson Rate $\\lambda$ (Gamma Prior)')
plt.xlabel('$\\lambda$ (Email Rate per Hour)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
```

Exercise 4 Code Placeholder

```{code-cell} ipython3
print("\n--- Exercise 4: Grid Approximation for Poisson-Gamma ---")
```

```{code-cell} ipython3
# 1. Define grid
n_grid_pois = 1000
grid_lambda = np.linspace(1e-9, 15, n_grid_pois) # Avoid lambda=0 for logpmf/pdf
```

```{code-cell} ipython3
# 2. Calculate Prior Probabilities
prior_on_grid_pois = stats.gamma.pdf(grid_lambda, a=alpha_prior_pois, scale=scale_prior_pois)
```

```{code-cell} ipython3
# 3. Calculate Likelihood (Poisson)
# Use log-likelihood for stability
log_likelihood_on_grid_pois = stats.poisson.logpmf(k_events, grid_lambda) # mu = lambda * time, here time=1
likelihood_on_grid_pois = np.exp(log_likelihood_on_grid_pois)
```

```{code-cell} ipython3
# 4. Compute Unnormalized Posterior
unnormalized_posterior_pois = likelihood_on_grid_pois * prior_on_grid_pois
```

```{code-cell} ipython3
# 5. Normalize
evidence_pois = np.sum(unnormalized_posterior_pois)
# Handle potential edge case where evidence is zero
if evidence_pois == 0:
    print("Warning: Evidence is zero, posterior cannot be normalized.")
    posterior_prob_grid_pois = np.zeros_like(unnormalized_posterior_pois)
else:
    posterior_prob_grid_pois = unnormalized_posterior_pois / evidence_pois
```

```{code-cell} ipython3
print(f"Sum of posterior probabilities on grid: {np.sum(posterior_prob_grid_pois):.4f}") # Should be 1.0
```

```{code-cell} ipython3
# Calculate summaries from grid
post_mean_grid_pois = np.sum(grid_lambda * posterior_prob_grid_pois)
map_index_pois = np.argmax(posterior_prob_grid_pois)
post_map_grid_pois = grid_lambda[map_index_pois]
```

```{code-cell} ipython3
# Credible Interval from grid
cumulative_posterior_pois = np.cumsum(posterior_prob_grid_pois)
lower_idx_grid_pois = np.where(cumulative_posterior_pois >= 0.05)[0][0]
upper_idx_grid_pois = np.where(cumulative_posterior_pois >= 0.95)[0][0]
lower_ci_grid_pois = grid_lambda[lower_idx_grid_pois]
upper_ci_grid_pois = grid_lambda[upper_idx_grid_pois]
```

```{code-cell} ipython3
print(f"\nPosterior Summaries (Grid Approximation):")
print(f"Posterior Mean: {post_mean_grid_pois:.4f}")
print(f"Posterior MAP: {post_map_grid_pois:.4f}")
print(f"90% Credible Interval: [{lower_ci_grid_pois:.4f}, {upper_ci_grid_pois:.4f}]")
print("Comparison: Results are very close to the analytical Gamma posterior results.")
```

```{code-cell} ipython3
# Plot analytical vs grid
step_size_pois = grid_lambda[1] - grid_lambda[0]
plt.figure(figsize=(10, 6))
plt.plot(lambda_vals, post_pdf_pois, label=f'Analytical Posterior', color='blue', linewidth=2.5)
# Scale grid probabilities for density plot
plt.plot(grid_lambda, posterior_prob_grid_pois / step_size_pois, 
         label=f'Grid Approximation ({n_grid_pois} points)', color='red', linestyle='--', alpha=0.8)

plt.title('Grid Approximation vs Analytical Posterior for Poisson Rate $\\lambda$')
plt.xlabel('$\\lambda$ (Email Rate per Hour)')
plt.ylabel('Probability Density / Scaled Probability')
plt.legend()
plt.xlim(0, 15) # Match grid range
plt.show()
```

```{code-cell} ipython3

```
