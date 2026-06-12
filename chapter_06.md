---
jupytext:
  formats: ipynb,md:myst
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
  - file: notebooks/chapter_06.ipynb
---

# فصل ۶: متغیرهای تصادفی گسسته

به بخش سوم سفرمان خوش آمدید! پایه‌ای محکم در احتمال پایه، شمارش، احتمال شرطی و استقلال ساخته‌ایم. اکنون مفهومی محوری را معرفی می‌کنیم که نظریه احتمال و تحلیل داده را به هم پیوند می‌دهد: **متغیر تصادفی**. متغیرهای تصادفی امکان توصیف کمی پیامدهای پدیده‌های تصادفی را فراهم می‌کنند. در این فصل، به‌طور خاص بر **متغیرهای تصادفی گسسته** تمرکز می‌کنیم؛ یعنی متغیرهایی که تعداد محدود یا شمارا بی‌نهایت مقدار می‌گیرند. خواهیم آموخت که رفتار آن‌ها را با تابع جرم احتمال (PMF) و تابع توزیع تجمعی (CDF) چگونه توصیف کنیم و با اندازه‌هایی مانند امید ریاضی (میانگین) و واریانس چگونه خلاصه کنیم.

+++

## متغیر تصادفی چیست؟

در بسیاری از آزمایش‌ها، خود پیامد خاص اهمیت ندارد؛ بلکه برخی ویژگی عددی مرتبط با آن پیامد برای ما مهم است.

**تعریف:** **متغیر تصادفی** متغیری است که مقدار آن یک پیامد عددی از یک پدیده تصادفی است. به‌صورت رسمی‌تر، تابعی است که هر پیامد در فضای نمونه $\Omega$ را به یک عدد حقیقی نگاشت می‌کند.

معمولاً متغیرهای تصادفی را با حروف بزرگ (مثلاً $X, Y, Z$) و مقادیر مشخص آن‌ها را با حروف کوچک (مثلاً $x, y, z$) نمایش می‌دهیم.

**انواع متغیرهای تصادفی:**
1.  **متغیر تصادفی گسسته:** متغیر تصادفی‌ای که فقط می‌تواند تعداد محدود یا شمارا بی‌نهایت مقدار متمایز بگیرد. اغلب با فرایندهای شمارشی مرتبط است.
2.  **متغیر تصادفی پیوسته:** متغیر تصادفی‌ای که می‌تواند هر مقداری در یک بازه یا محدوده معین بگیرد. اغلب با فرایندهای اندازه‌گیری مرتبط است. (این موضوع را در فصل ۸ پوشش می‌دهیم).

**مثال:** پرتاب یک تاس شش‌وجهی منصفانه را در نظر بگیرید.
* فضای نمونه $\Omega = \{1, 2, 3, 4, 5, 6\}$ است.
* می‌توانیم متغیر تصادفی $X$ را به‌عنوان عدد روی تاس پس از پرتاب تعریف کنیم. $X$ هر پیامد (که در این مورد خود عدد است) را به خودش نگاشت می‌کند.
* $X$ یک **متغیر تصادفی گسسته** است زیرا فقط می‌تواند مقادیر $\{1, 2, 3, 4, 5, 6\}$ را بگیرد.

**مثال دیگر:** دو بار پرتاب سکه را در نظر بگیرید.
* فضای نمونه $\Omega = \{HH, HT, TH, TT\}$ است.
* $Y$ را متغیر تصادفی نماینده *تعداد شیر* به‌دست‌آمده در نظر بگیرید.
* $Y$ پیامدها را به اعداد نگاشت می‌کند: $Y(HH) = 2$، $Y(HT) = 1$، $Y(TH) = 1$، $Y(TT) = 0$.
* $Y$ یک **متغیر تصادفی گسسته** است زیرا فقط می‌تواند مقادیر $\{0, 1, 2\}$ را بگیرد.

+++

## تابع جرم احتمال (PMF)

برای یک متغیر تصادفی گسسته، می‌خواهیم احتمال مرتبط با هر مقدار ممکن آن را بدانیم. این موضوع در تابع جرم احتمال (PMF) بیان می‌شود.

**تعریف:** **تابع جرم احتمال (PMF)** متغیر تصادفی گسسته $X$ تابعی است که با $p_X(x)$ یا به‌اختصار $p(x)$ نمایش داده می‌شود و احتمال برابر بودن دقیق $X$ با مقدار $x$ را می‌دهد.

$$
p_X(x) = P(X = x)
$$

یک PMF معتبر باید دو شرط زیر را برآورده کند:
1.  $p_X(x) \ge 0$ برای همه مقادیر ممکن $x$. (احتمال‌ها نمی‌توانند منفی باشند).
2.  $\sum_{x} p_X(x) = 1$، که در آن جمع روی همه مقادیر ممکن $x$ که $X$ می‌تواند بگیرد گرفته می‌شود. (مجموع احتمال‌ها باید ۱ باشد).

:::{admonition} مثال: PMF تاس منصفانه
:class: tip dropdown

برای پرتاب تاس منصفانه، $X$ را پیامد در نظر بگیرید. مقادیر ممکن $\{1, 2, 3, 4, 5, 6\}$ هستند. از آنجا که تاس منصفانه است، هر پیامد احتمال $\frac{1}{6}$ دارد. PMF به‌صورت زیر است:

$$
p_X(x) =
\begin{cases}
1/6 & \text{if } x \in \{1, 2, 3, 4, 5, 6\} \\
0 & \text{otherwise}
\end{cases}
$$

بنابراین $P(X=1) = 1/6$، $P(X=2) = 1/6$، ...، $P(X=6) = 1/6$.

مجموع برابر است با $6 \times \frac{1}{6} = 1$.
:::

بیایید این PMF را در پایتون نمایش دهیم و مصور کنیم.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_discrete

# Set plot style
plt.style.use('seaborn-v0_8-whitegrid')
```

:::{dropdown} پیاده‌سازی پایتون

این کد PMF تاس منصفانه را با تعریف مقادیر ممکن و احتمال‌های آن‌ها می‌سازد. از یک dictionary برای نمایش PMF به‌منظور جستجوی آسان استفاده می‌کنیم و بررسی می‌کنیم که مجموع احتمال‌ها ۱ باشد.

```{code-cell} ipython3
from pprint import pprint

# Define the possible outcomes (values) and their probabilities for the die roll
die_values = np.arange(1, 7) # Possible values x: 1, 2, 3, 4, 5, 6
die_probs = np.array([1/6] * 6) # P(X=x) for each value

# Create a dictionary for easier lookup
die_pmf_dict = {val: prob for val, prob in zip(die_values, die_probs)}
print("PMF Dictionary:")
pprint(die_pmf_dict)
print(f"\nSum of probabilities: {sum(die_pmf_dict.values()):.10f}")
```
:::

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Visualize the PMF
plt.figure(figsize=(8, 4))
plt.bar(die_values, die_probs, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Outcome (x)")
plt.ylabel("Probability P(X=x)")
plt.title("Probability Mass Function (PMF) of a Fair Die Roll")
plt.xticks(die_values)
plt.ylim(0, 0.2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('ch06_pmf_die.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_pmf_die.svg
---
width: 80%
---
PMF پرتاب تاس منصفانه که احتمال یکنواخت ۱/۶ برای هر پیامد را نشان می‌دهد.
```

+++

## تابع توزیع تجمعی (CDF)

گاهی نه فقط احتمال *دقیقاً* برابر بودن $X$ با یک مقدار خاص، بلکه احتمال *کمتر یا مساوی* بودن $X$ با آن مقدار برای ما مهم است. این موضوع در تابع توزیع تجمعی (CDF) بیان می‌شود.

**تعریف:** **تابع توزیع تجمعی (CDF)** متغیر تصادفی $X$ (گسسته یا پیوسته)، که با $F_X(x)$ یا به‌اختصار $F(x)$ نمایش داده می‌شود، احتمال این را می‌دهد که $X$ مقداری کمتر یا مساوی $x$ بگیرد.

$$
F_X(x) = P(X \le x)
$$

برای متغیر تصادفی گسسته $X$، CDF با جمع مقادیر PMF برای همه پیامدهای کمتر یا مساوی $x$ محاسبه می‌شود:

$$
F_X(x) = \sum_{k \le x} p_X(k)
$$

**ویژگی‌های CDF:**

1.  $0 \le F_X(x) \le 1$ برای همه $x$.
2.  $F_X(x)$ تابعی ناکاهشی از $x$ است: اگر $a < b$، آنگاه $F_X(a) \le F_X(b)$.
3.  $\lim_{x \to -\infty} F_X(x) = 0$ و $\lim_{x \to +\infty} F_X(x) = 1$.
4.  برای متغیر تصادفی گسسته، CDF تابع پله‌ای است که در نقاطی که PMF مثبت است افزایش می‌یابد.
5.  $P(X > x) = 1 - F_X(x)$.
6.  $P(a < X \le b) = F_X(b) - F_X(a)$ برای $a < b$.
7.  $P(X=x) = F_X(x) - \lim_{y \to x^-} F_X(y)$ (اندازه پرش در $x$).

:::{admonition} مثال: محاسبات CDF برای تاس منصفانه
:class: tip dropdown

برای پرتاب تاس منصفانه $X$:

$$
\begin{align*}
F_X(0) &= P(X \le 0) = 0 \\
F_X(1) &= P(X \le 1) = P(X=1) = 1/6 \\
F_X(2) &= P(X \le 2) = P(X=1) + P(X=2) = 1/6 + 1/6 = 2/6 \\
F_X(3) &= P(X \le 3) = P(X=1) + P(X=2) + P(X=3) = 3/6 \\
&\vdots \\
F_X(6) &= P(X \le 6) = 6/6 = 1 \\
F_X(6.5) &= P(X \le 6.5) = P(X \le 6) = 1
\end{align*}
$$
:::

بیایید CDF را محاسبه و مصور کنیم.

:::{dropdown} پیاده‌سازی پایتون

این کد نحوه محاسبه CDF را با جمع تجمعی مقادیر PMF نشان می‌دهد. سپس تابع `die_cdf_func(x)` را می‌سازیم که CDF را در هر نقطه ارزیابی می‌کند و مقادیر کمتر از ۱، بیشتر از ۶ و مقادیر بین آن‌ها را مدیریت می‌کند.

```{code-cell} ipython3
from pprint import pprint

# Setup: Define die values and probabilities
die_values = np.arange(1, 7)  # Possible values: 1, 2, 3, 4, 5, 6
die_probs = np.array([1/6] * 6)  # Equal probability for fair die

# Calculate the CDF values
die_cdf_values = np.cumsum(die_probs)
print("CDF Values:")
for i, cdf_val in enumerate(die_cdf_values, start=1):
    print(f"  F({i}) = {cdf_val:.4f}")

# Create a function representation of the CDF
def die_cdf_func(x):
    if x < 1:
        return 0.0
    elif x >= 6:
        return 1.0
    else:
        # For values between die outcomes, CDF remains constant at the last "step"
        # So we find which die value we've passed and return that CDF value
        idx = np.searchsorted(die_values, x, side='right') - 1
        return die_cdf_values[idx]

# Test the function at non-integer values to see step function behavior
print("\nTesting CDF between steps:")
print(f"  F(0.5) = {die_cdf_func(0.5):.4f}  (before first outcome)")
print(f"  F(3.7) = {die_cdf_func(3.7):.4f}  (between 3 and 4, stays at F(3))")
print(f"  F(10)  = {die_cdf_func(10):.4f}  (after last outcome)")
```
:::

نمودار زیر CDF را به‌صورت تابع پله‌ای مصور می‌کند. توجه کنید که تابع در هر مقدار صحیح (جایی که تاس واقعاً می‌افتد) پرش می‌کند و بین اعداد صحیح ثابت می‌ماند. دایره‌های پر، مقدار CDF در هر نقطه را نشان می‌دهند و دایره‌های توخالی مقدار درست قبل از پرش را نشان می‌دهند.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Visualize the CDF
x_plot = np.linspace(-1, 8, 500) # Range for plotting
y_plot = [die_cdf_func(val) for val in x_plot]

plt.figure(figsize=(8, 4))
plt.plot(x_plot, y_plot, drawstyle='steps-post', linestyle='-', color='darkgreen')
# Add points at the jumps
plt.scatter(die_values, die_cdf_values, color='darkgreen', zorder=5)
plt.scatter(die_values, die_cdf_values - die_probs, facecolors='none', edgecolors='darkgreen', zorder=5)

plt.xlabel("Value (x)")
plt.ylabel("Cumulative Probability P(X ≤ x)")
plt.title("Cumulative Distribution Function (CDF) of a Fair Die Roll")
plt.xticks(np.arange(0, 8))
plt.yticks(np.linspace(0, 1, 7))
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.ylim(-0.05, 1.05)
plt.savefig('ch06_cdf_die.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_cdf_die.svg
---
width: 80%
---
CDF پرتاب تاس منصفانه که احتمال تجمعی را به‌صورت تابع پله‌ای نشان می‌دهد.
```

+++

## امید ریاضی (میانگین)

امید ریاضی یا میانگین یک متغیر تصادفی گسسته، میانگین وزنی مقادیر ممکن آن است که وزن‌ها همان احتمال‌ها (مقادیر PMF) هستند. این مقدار، میانگین بلندمدتی را نشان می‌دهد که اگر متغیر تصادفی را بارها مشاهده کنیم انتظار داریم.

**تعریف:** **امید ریاضی** (یا **میانگین**) متغیر تصادفی گسسته $X$، که با $E[X]$ یا $\mu_X$ نمایش داده می‌شود، به‌صورت زیر تعریف می‌شود:

$$
E[X] = \mu_X = \sum_{x} x \cdot p_X(x)
$$

که در آن جمع روی همه مقادیر ممکن $x$ که $X$ می‌تواند بگیرد گرفته می‌شود.

امید ریاضی لزوماً یکی از مقادیر ممکن $X$ نیست.

:::{admonition} مثال: محاسبه امید ریاضی
:class: tip dropdown

برای پرتاب تاس منصفانه $X$:

$$
\begin{align*}
E[X] &= (1 \times \frac{1}{6}) + (2 \times \frac{1}{6}) + (3 \times \frac{1}{6}) + (4 \times \frac{1}{6}) + (5 \times \frac{1}{6}) + (6 \times \frac{1}{6}) \\
&= \frac{1+2+3+4+5+6}{6} \\
&= \frac{21}{6} \\
&= 3.5
\end{align*}
$$

اگرچه تاس هرگز روی ۳٫۵ نمی‌افتد، میانگین بلندمدت بسیاری از پرتاب‌ها انتظار می‌رود ۳٫۵ باشد.
:::

:::{dropdown} پیاده‌سازی پایتون

این کد امید ریاضی را با استفاده از فرمول $E[X] = \sum x \cdot p_X(x)$ محاسبه می‌کند. از `np.sum()` برای محاسبه جمع وزنی مقادیر در احتمال‌ها استفاده می‌کنیم.

```{code-cell} ipython3
# Setup: Define die values and probabilities
die_values = np.arange(1, 7)  # Possible values: 1, 2, 3, 4, 5, 6
die_probs = np.array([1/6] * 6)  # Equal probability for fair die

# Calculate the expected value
expected_value = np.sum(die_values * die_probs)
# Alternatively using dot product:
# expected_value = np.dot(die_values, die_probs)

print(f"Theoretical Expected Value E[X]: {expected_value}")
```
:::

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Visualize the mean on the PMF plot
plt.figure(figsize=(8, 4))
plt.bar(die_values, die_probs, color='skyblue', edgecolor='black', alpha=0.7, label='PMF')
plt.axvline(expected_value, color='red', linestyle='--', linewidth=2, label=f'Expected Value E[X] = {expected_value:.1f}')
plt.xlabel("Outcome (x)")
plt.ylabel("Probability P(X=x)")
plt.title("PMF of a Fair Die Roll with Expected Value")
plt.xticks(die_values)
plt.ylim(0, 0.2)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('ch06_pmf_with_mean.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_pmf_with_mean.svg
---
width: 80%
---
PMF با امید ریاضی در ۳٫۵، میانگین نظری بلندمدت.
```

+++

## واریانس و انحراف معیار

در حالی که امید ریاضی مرکز توزیع را به ما می‌دهد، واریانس و انحراف معیار *پراکندگی* یا *گسترش* مقادیر متغیر تصادفی حول میانگین را اندازه می‌گیرند.

**تعریف:** **واریانس** متغیر تصادفی $X$، که با $Var(X)$ یا $\sigma_X^2$ نمایش داده می‌شود، امید ریاضی مربع اختلاف $X$ از میانگین $E[X] = \mu_X$ است.

$$
Var(X) = \sigma_X^2 = E[(X - \mu_X)^2]
$$

برای متغیر تصادفی گسسته، این مقدار به‌صورت زیر محاسبه می‌شود:

$$
Var(X) = \sum_{x} (x - \mu_X)^2 \cdot p_X(x)
$$

اغلب از فرمول محاسباتی ساده‌تر زیر برای واریانس استفاده می‌شود:

$$
Var(X) = E[X^2] - (E[X])^2
$$

که در آن $E[X^2] = \sum_{x} x^2 \cdot p_X(x)$.

**تعریف:** **انحراف معیار** متغیر تصادفی $X$، که با $SD(X)$ یا $\sigma_X$ نمایش داده می‌شود، ریشه مثبت واریانس است.

$$
SD(X) = \sigma_X = \sqrt{Var(X)}
$$

انحراف معیار اغلب ترجیح داده می‌شود زیرا همان واحد متغیر تصادفی $X$ را دارد.

:::{admonition} مثال: محاسبه واریانس و انحراف معیار
:class: tip dropdown

برای پرتاب تاس منصفانه $X$، می‌دانیم $\mu_X = 3.5$.

ابتدا $E[X^2]$ را محاسبه می‌کنیم:

$$
\begin{align*}
E[X^2] &= (1^2 \times \frac{1}{6}) + (2^2 \times \frac{1}{6}) + (3^2 \times \frac{1}{6}) + (4^2 \times \frac{1}{6}) + (5^2 \times \frac{1}{6}) + (6^2 \times \frac{1}{6}) \\
&= \frac{1 + 4 + 9 + 16 + 25 + 36}{6} \\
&= \frac{91}{6} \approx 15.167
\end{align*}
$$

اکنون واریانس را محاسبه می‌کنیم:

$$
\begin{align*}
Var(X) &= E[X^2] - (E[X])^2 \\
&= \frac{91}{6} - (3.5)^2 \\
&= \frac{91}{6} - (7/2)^2 \\
&= \frac{91}{6} - \frac{49}{4} \\
&= \frac{182}{12} - \frac{147}{12} \\
&= \frac{35}{12} \approx 2.917
\end{align*}
$$

و انحراف معیار:

$$
SD(X) = \sigma_X = \sqrt{\frac{35}{12}} \approx \sqrt{2.917} \approx 1.708
$$
:::

:::{dropdown} پیاده‌سازی پایتون

این کد واریانس را با فرمول محاسباتی $Var(X) = E[X^2] - (E[X])^2$ محاسبه می‌کند. همچنین محاسبه جایگزین با تعریف $E[(X - \mu)^2]$ را نشان می‌دهیم تا تأیید کنیم هر دو روش نتیجه یکسانی می‌دهند.

```{code-cell} ipython3
# Setup: Define die values and probabilities
die_values = np.arange(1, 7)  # Possible values: 1, 2, 3, 4, 5, 6
die_probs = np.array([1/6] * 6)  # Equal probability for fair die
expected_value = np.sum(die_values * die_probs)  # E[X] = 3.5

# Calculate E[X^2]
e_x_squared = np.sum((die_values**2) * die_probs)
print(f"E[X^2]: {e_x_squared:.4f} (Exact: 91/6)")

# Calculate Variance using the computational formula
variance = e_x_squared - (expected_value**2)
print(f"Theoretical Variance Var(X): {variance:.4f} (Exact: 35/12)")

# Alternatively, calculate using the definition: E[(X - mu)^2]
variance_def = np.sum(((die_values - expected_value)**2) * die_probs)
print(f"Variance using definition: {variance_def:.4f}")

# Calculate Standard Deviation
std_dev = np.sqrt(variance)
print(f"Theoretical Standard Deviation SD(X): {std_dev:.4f} (Exact: sqrt(35/12))")
```
:::

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Visualize the standard deviation on the PMF plot
plt.figure(figsize=(10, 5))
plt.bar(die_values, die_probs, color='skyblue', edgecolor='black', alpha=0.7, label='PMF')
plt.axvline(expected_value, color='red', linestyle='--', linewidth=2, label=f'E[X] = {expected_value:.1f}')

# Add lines for +/- 1 standard deviation
plt.axvline(expected_value + std_dev, color='orange', linestyle=':', linewidth=2, label=f'E[X] ± σ ≈ {expected_value+std_dev:.2f}')
plt.axvline(expected_value - std_dev, color='orange', linestyle=':', linewidth=2, label=f'E[X] - σ ≈ {expected_value-std_dev:.2f}')

# Add lines for +/- 2 standard deviations
plt.axvline(expected_value + 2*std_dev, color='purple', linestyle=':', linewidth=2, label=f'E[X] ± 2σ ≈ {expected_value+2*std_dev:.2f}')
plt.axvline(expected_value - 2*std_dev, color='purple', linestyle=':', linewidth=2, label=f'E[X] - 2σ ≈ {expected_value-2*std_dev:.2f}')

plt.xlabel("Outcome (x)")
plt.ylabel("Probability P(X=x)")
plt.title("PMF, Mean, and Standard Deviation Bands for a Fair Die Roll")
plt.xticks(die_values)
plt.ylim(0, 0.2)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('ch06_pmf_with_std.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_pmf_with_std.svg
---
width: 100%
---
PMF با میانگین و باندهای انحراف معیار که پراکندگی توزیع را نشان می‌دهد.
```

+++

## توابع یک متغیر تصادفی

اغلب به کمیتی علاقه‌مندیم که از یک متغیر تصادفی مشتق شده باشد. اگر $X$ متغیر تصادفی و $g$ تابعی باشد، آنگاه $Y = g(X)$ نیز متغیر تصادفی است.

اگر $X$ گسسته با PMF $p_X(x)$ باشد، می‌توانیم PMF $Y = g(X)$ را که با $p_Y(y)$ نمایش داده می‌شود، با جمع احتمال همه $x$‌هایی که $g(x) = y$ پیدا کنیم:

$$
\begin{align*}
p_Y(y) &= P(Y=y) \\
&= P(g(X)=y) \\
&= \sum_{x: g(x)=y} p_X(x)
\end{align*}
$$

```{admonition} خواندن نمادگذاری
:class: note

نمادگذاری $\sum_{x: g(x)=y}$ به این معناست که «جمع روی همه $x$‌هایی که $g(x) = y$». دو‌نقطه (:) به معنای «به‌گونه‌ای که» یا «که در آن» است. این روشی فشرده برای نوشتن جمع شرطی است — فقط جملاتی را می‌آوریم که شرط $g(x)=y$ برقرار باشد.

**مثال:** $X$ را پرتاب تاس منصفانه و $Y = X^2$ در نظر بگیرید. برای یافتن $p_Y(4) = P(Y=4)$:
$$p_Y(4) = \sum_{x: x^2=4} p_X(x)$$

فقط $x=2$ شرط $x^2=4$ را برآورده می‌کند، پس:
$$p_Y(4) = p_X(2) = \frac{1}{6}$$

مقادیر دیگر ($x \in \{1, 3, 4, 5, 6\}$) شرط $x^2=4$ را برآورده *نمی‌کنند*، بنابراین در جمع نمی‌آیند.
```

### امید ریاضی تابعی از متغیر تصادفی (LOTUS)

نتیجه بسیار مفیدی که گاهی **قانون آماردان ناخودآگاه** (Law of the Unconscious Statistician یا LOTUS) نامیده می‌شود، امکان محاسبه امید ریاضی $Y=g(X)$ را بدون یافتن صریح PMF $Y$ می‌دهد.

**تعریف:** برای متغیر تصادفی گسسته $X$ با PMF $p_X(x)$ و تابع $g$، امید ریاضی $Y = g(X)$ برابر است با:

$$
E[g(X)] = \sum_{x} g(x) \cdot p_X(x)
$$

این را با تعریف $E[X]$ مقایسه کنید:

$$
\begin{align*}
E[X] &= \sum_{x} x \cdot p_X(x) \\
E[g(X)] &= \sum_{x} g(x) \cdot p_X(x)
\end{align*}
$$

توجه کنید که در جمع، به‌سادگی $x$ را با $g(x)$ جایگزین می‌کنیم. همین روشی است که قبلاً $E[X^2]$ را با آن محاسبه کردیم، جایی که $g(x) = x^2$.

:::{admonition} مثال: PMF و امید ریاضی Y = X²
:class: tip dropdown

$X$ را پیامد پرتاب تاس منصفانه در نظر بگیرید. $Y = X^2$. PMF و امید ریاضی $Y$ چیست؟

* مقادیر ممکن $X$ برابر $\{1, 2, 3, 4, 5, 6\}$ هستند، هر کدام با احتمال $1/6$.
* مقادیر ممکن $Y = X^2$ برابر $\{1^2, 2^2, 3^2, 4^2, 5^2, 6^2\} = \{1, 4, 9, 16, 25, 36\}$ هستند.
* از آنجا که هر $x$ به یک $y=x^2$ یکتا نگاشت می‌شود، احتمال هر $y$ همان احتمال $x$ متناظر است.
* PMF $Y$ به‌صورت زیر است:
    $p_Y(y) = 1/6$ برای $y \in \{1, 4, 9, 16, 25, 36\}$، و در غیر این صورت $0$.

**محاسبه E[Y] با استفاده از PMF $Y$:**

$$
\begin{align*}
E[Y] = \sum_{y} y \cdot p_Y(y) &= (1 \times \frac{1}{6}) + (4 \times \frac{1}{6}) + (9 \times \frac{1}{6}) + (16 \times \frac{1}{6}) + (25 \times \frac{1}{6}) + (36 \times \frac{1}{6}) \\
&= \frac{1+4+9+16+25+36}{6} \\
&= \frac{91}{6}
\end{align*}
$$

**روش جایگزین با استفاده از LOTUS:**

$$
\begin{align*}
E[Y] = E[X^2] &= \sum_{x=1}^{6} x^2 \cdot p_X(x) \\
&= \sum_{x=1}^{6} x^2 \cdot \frac{1}{6} \\
&= \frac{1^2+2^2+3^2+4^2+5^2+6^2}{6} \\
&= \frac{91}{6}
\end{align*}
$$

این محاسبه قبلی $E[X^2]$ را تأیید می‌کند.
:::

:::{dropdown} پیاده‌سازی پایتون

این کد دو روش برای محاسبه $E[Y]$ که $Y = X^2$ را نشان می‌دهد: اول با یافتن PMF $Y$ و استفاده مستقیم از آن، و دوم با استفاده از LOTUS برای محاسبه مستقیم از $X$ بدون یافتن PMF $Y$. هر دو روش نتیجه یکسانی می‌دهند.

```{code-cell} ipython3
from pprint import pprint

# Setup: Define die values and probabilities
die_values = np.arange(1, 7)  # Possible values: 1, 2, 3, 4, 5, 6
die_probs = np.array([1/6] * 6)  # Equal probability for fair die

# Define the function g(x) = x^2
def g(x):
  return x**2

# Possible values for X and Y
x_values = die_values
y_values = g(x_values)

# PMF for Y (since g(x) is one-to-one for x in {1..6}, probs are the same)
y_probs = die_probs

# PMF dictionary for Y
y_pmf_dict = {val_y: prob for val_y, prob in zip(y_values, y_probs)}
print("PMF Dictionary for Y=X^2:")
pprint(y_pmf_dict)

# Calculate E[Y] using the PMF of Y
expected_value_y = np.sum(y_values * y_probs)
print(f"\nE[Y] calculated using PMF of Y: {expected_value_y:.4f} (Exact: 91/6)")

# Calculate E[Y] = E[g(X)] using LOTUS
expected_value_y_lotus = np.sum(g(x_values) * die_probs)
print(f"E[Y] calculated using LOTUS E[g(X)]: {expected_value_y_lotus:.4f} (Exact: 91/6)")
```
:::

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Visualize the PMF of Y = X^2
plt.figure(figsize=(8, 4))
plt.bar(y_values, y_probs, color='lightcoral', edgecolor='black', alpha=0.7)
plt.xlabel("Outcome (y = x^2)")
plt.ylabel("Probability P(Y=y)")
plt.title("Probability Mass Function (PMF) of Y = X^2 (Squared Die Roll)")
plt.xticks(y_values)
plt.ylim(0, 0.2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('ch06_pmf_y_squared.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_pmf_y_squared.svg
---
width: 80%
---
PMF $Y = X^2$ که توزیع تبدیل‌شده را نشان می‌دهد.
```

+++

## کار عملی: شبیه‌سازی و مقایسه

قانون اعداد بزرگ (که بعداً مطالعه می‌کنیم) می‌گوید اگر یک متغیر تصادفی را بارها شبیه‌سازی کنیم، میانگین پیامدها (*میانگین نمونه*) باید به امید ریاضی نظری $E[X]$ نزدیک شود. به‌طور مشابه، واریانس پیامدها (*واریانس نمونه*) باید به $Var(X)$ نزدیک شود. بیایید این را برای مثال پرتاب تاس بررسی کنیم.

کارهایی که انجام می‌دهیم:
1.  تعداد زیادی پرتاب تاس منصفانه با `numpy.random.randint` شبیه‌سازی می‌کنیم.
2.  میانگین نمونه و واریانس نمونه پیامدهای شبیه‌سازی‌شده را محاسبه می‌کنیم.
3.  این نتایج تجربی را با مقادیر نظری ($E[X]=3.5$، $Var(X) \approx 2.917$) مقایسه می‌کنیم.
4.  توزیع پیامدهای شبیه‌سازی‌شده (PMF تجربی) را مصور می‌کنیم و با PMF نظری مقایسه می‌کنیم.
5.  CDF تجربی را مصور می‌کنیم و با CDF نظری مقایسه می‌کنیم.

```{code-cell} ipython3
# Setup: Calculate theoretical values
die_values = np.arange(1, 7)
die_probs = np.array([1/6] * 6)
expected_value = np.sum(die_values * die_probs)  # E[X] = 3.5
variance = np.sum((die_values**2) * die_probs) - expected_value**2  # Var(X) = 35/12
std_dev = np.sqrt(variance)  # SD(X)

# Number of simulations
num_simulations = 10000

# Simulate die rolls
simulated_rolls = np.random.randint(1, 7, size=num_simulations)

# Calculate empirical mean and variance
sample_mean = np.mean(simulated_rolls)
sample_variance = np.var(simulated_rolls, ddof=1)  # ddof=1 for unbiased estimator
sample_std_dev = np.std(simulated_rolls, ddof=1)

# Compare empirical vs theoretical
print(f"--- Comparison after {num_simulations} simulations ---")
print(f"Theoretical E[X]: {expected_value:.4f}")
print(f"Sample Mean:      {sample_mean:.4f}")
print(f"Difference (Mean): {abs(sample_mean - expected_value):.4f}\n")

print(f"Theoretical Var(X): {variance:.4f}")
print(f"Sample Variance:    {sample_variance:.4f}")
print(f"Difference (Var):   {abs(sample_variance - variance):.4f}\n")

print(f"Theoretical SD(X): {std_dev:.4f}")
print(f"Sample Std Dev:     {sample_std_dev:.4f}")
print(f"Difference (SD):    {abs(sample_std_dev - std_dev):.4f}")
```

+++

### مصورسازی توزیع‌های تجربی در برابر نظری

اکنون فراوانی نتایج شبیه‌سازی‌شده را رسم می‌کنیم و با احتمال‌های نظری (PMF) مقایسه می‌کنیم، و همین کار را برای توزیع‌های تجمعی (CDF) انجام می‌دهیم.

```{code-cell} ipython3
# Calculate empirical PMF and CDF
unique_outcomes, counts = np.unique(simulated_rolls, return_counts=True)
empirical_pmf = counts / num_simulations
empirical_cdf = np.cumsum(empirical_pmf)
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Create comparison plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Empirical PMF vs Theoretical PMF
ax1.bar(unique_outcomes, empirical_pmf, color='lightgreen', alpha=0.7, label=f'Empirical PMF (N={num_simulations})')
ax1.plot(die_values, die_probs, 'ro--', markersize=8, label='Theoretical PMF (1/6)')
ax1.set_xlabel("Outcome")
ax1.set_ylabel("Probability / Relative Frequency")
ax1.set_title("Empirical vs Theoretical PMF")
ax1.set_xticks(die_values)
ax1.set_ylim(0, max(np.max(empirical_pmf), np.max(die_probs)) * 1.1)
ax1.legend()
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Empirical CDF vs Theoretical CDF
ax2.step(unique_outcomes, empirical_cdf, where='post', color='orange', linewidth=2, label=f'Empirical CDF (N={num_simulations})')
x_plot_cdf = np.linspace(-1, 8, 500)
y_plot_cdf = [die_cdf_func(val) for val in x_plot_cdf]
ax2.plot(x_plot_cdf, y_plot_cdf, 'b--', linewidth=2, label='Theoretical CDF')
ax2.scatter(die_values, die_cdf_values, color='blue', zorder=5, s=50)
ax2.set_xlabel("Outcome")
ax2.set_ylabel("Cumulative Probability")
ax2.set_title("Empirical vs Theoretical CDF")
ax2.set_xticks(np.arange(0, 8))
ax2.set_yticks(np.linspace(0, 1, 7))
ax2.set_ylim(-0.05, 1.05)
ax2.legend()
ax2.grid(True, which='both', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('ch06_empirical_vs_theoretical.svg', format='svg', bbox_inches='tight')
plt.show()
```

```{figure} ch06_empirical_vs_theoretical.svg
---
width: 100%
figclass: full-width
---
مقایسه توزیع‌های تجربی (شبیه‌سازی‌شده) و نظری که همگرایی را نشان می‌دهد.
```

همان‌طور که از نتایج شبیه‌سازی و نمودارها مشخص است، مقادیر تجربی (میانگین نمونه، واریانس نمونه، PMF/CDF تجربی) که از تعداد زیادی شبیه‌سازی به‌دست می‌آیند، به‌خوبی به مقادیر نظری که استخراج کردیم نزدیک می‌شوند. این ارتباط بین نظریه احتمال و مشاهدات یا شبیه‌سازی‌های دنیای واقعی را نشان می‌دهد.

+++

## خلاصه

در این فصل، مفهوم بنیادین متغیر تصادفی گسسته را معرفی کردیم.

* **متغیر تصادفی** به هر پیامد یک آزمایش تصادفی یک مقدار عددی نسبت می‌دهد.
* **متغیر تصادفی گسسته** تعداد محدود یا شمارا بی‌نهایت مقدار می‌گیرد.
* **تابع جرم احتمال (PMF)**، $p_X(x) = P(X=x)$، احتمال هر مقدار ممکن $x$ را می‌دهد.
* **تابع توزیع تجمعی (CDF)**، $F_X(x) = P(X \le x)$، احتمال تجمعی تا مقدار $x$ را می‌دهد.
* **امید ریاضی (میانگین)**، $E[X] = \sum x \cdot p_X(x)$، میانگین بلندمدت را نشان می‌دهد.
* **واریانس**، $Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$، پراکندگی حول میانگین را اندازه می‌گیرد.
* **انحراف معیار**، $SD(X) = \sqrt{Var(X)}$، پراکندگی را با همان واحد اصلی اندازه می‌گیرد.
* می‌توانیم **توابع متغیرهای تصادفی**، $Y = g(X)$، را تحلیل کنیم و PMF آن‌ها را با جمع احتمال‌ها بیابیم: $p_Y(y) = \sum_{x: g(x)=y} p_X(x)$.
* **LOTUS (قانون آماردان ناخودآگاه)** امکان محاسبه مستقیم امید ریاضی توابع را می‌دهد: $E[g(X)] = \sum g(x) p_X(x)$.
* شبیه‌سازی با پایتون (`numpy`) امکان تولید داده تجربی را می‌دهد که با افزایش تعداد شبیه‌سازی‌ها به توزیع‌های احتمال نظری و پارامترهای آن‌ها همگرا می‌شود.

در فصل بعد، چند خانواده مهم از توزیع‌های گسسته را که سناریوهای رایج دنیای واقعی را مدل می‌کنند بررسی می‌کنیم.

+++

---

## تمرین‌ها

1.  **سکه نامتوازن:** سکه‌ای نامتوازن در نظر بگیرید که احتمال آمدن شیر (H) برابر $P(H) = 0.7$ است. $X$ را متغیر تصادفی نماینده تعداد شیر در یک پرتاب واحد در نظر بگیرید (پس $X=1$ برای شیر و $X=0$ برای خط).
    a.  PMF $X$ چیست؟
    b.  CDF $X$ چیست؟ آن را رسم کنید.
    c.  امید ریاضی $E[X]$ را محاسبه کنید.
    d.  واریانس $Var(X)$ و انحراف معیار $SD(X)$ را محاسبه کنید.

    ```{admonition} پاسخ
    :class: dropdown

    a) PMF: $P(X=0) = 0.3$، $P(X=1) = 0.7$

    b) CDF: $F(x) = 0$ برای $x < 0$؛ $F(x) = 0.3$ برای $0 \le x < 1$؛ $F(x) = 1$ برای $x \ge 1$

    c) $E[X] = 0 \times 0.3 + 1 \times 0.7 = 0.7$

    d) $E[X^2] = 0^2 \times 0.3 + 1^2 \times 0.7 = 0.7$

    $Var(X) = E[X^2] - (E[X])^2 = 0.7 - 0.49 = 0.21$

    $SD(X) = \sqrt{0.21} \approx 0.458$
    ```

2.  **مجموع دو تاس:** $X$ را متغیر تصادفی نماینده مجموع پیامدهای پرتاب دو تاس شش‌وجهی منصفانه در نظر بگیرید.
    a.  مقادیر ممکن $X$ چیست؟
    b.  PMF $X$ را تعیین کنید. (راهنما: ۳۶ پیامد هم‌احتمال برای جفت تاس وجود دارد.)
    c.  $E[X]$ را محاسبه کنید. آیا روش ساده‌تری غیر از استفاده مستقیم از PMF وجود دارد؟ (راهنما: خطی بودن امید ریاضی)
    d.  $Var(X)$ را محاسبه کنید. (راهنما: واریانس مجموع متغیرهای مستقل)
    e.  $P(X > 7)$ را بیابید.
    f.  $P(X \text{ is even})$ را بیابید.

    ```{admonition} پاسخ
    :class: dropdown

    a) مقادیر ممکن: $\{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$

    b) PMF: برای هر مجموع پیامدها را بشمارید. مثلاً $P(X=7) = 6/36 = 1/6$ (شش حالت: 1+6، 2+5، 3+4، 4+3، 5+2، 6+1)

    c) با خطی بودن: $E[X] = E[D_1] + E[D_2] = 3.5 + 3.5 = 7$

    d) برای تاس‌های مستقل: $Var(X) = Var(D_1) + Var(D_2) = 35/12 + 35/12 = 70/12 \approx 5.833$

    e) $P(X > 7) = P(X \in \{8,9,10,11,12\}) = (5+4+3+2+1)/36 = 15/36 = 5/12$

    f) شمارش مجموع‌های زوج: $P(X \text{ is even}) = 18/36 = 1/2$
    ```

3.  **ارزش بازی:** £2 برای بازی می‌پردازید. تاس شش‌وجهی منصفانه می‌اندازید. اگر ۶ بیاید، £5 برنده می‌شوید (£2 خودتان به‌علاوه £3 سود). اگر ۴ یا ۵ بیاید، £2 برنده می‌شوید (£2 خودتان را پس می‌گیرید). اگر ۱، ۲ یا ۳ بیاید، چیزی برنده نمی‌شوید (£2 خود را از دست می‌دهید). $W$ را متغیر تصادفی نماینده *سود خالص* شما از یک بار بازی در نظر بگیرید.
    a.  مقادیر ممکن $W$ چیست؟
    b.  PMF $W$ را تعیین کنید.
    c.  سود خالص مورد انتظار $E[W]$ را محاسبه کنید. آیا این بازی منصفانه است؟ (بازی منصفانه $E[W]=0$ دارد).
    d.  واریانس $Var(W)$ را محاسبه کنید.

    ```{admonition} پاسخ
    :class: dropdown

    a) مقادیر ممکن: $\{-2, 0, 3\}$ (خالص: باخت £2، سر به سر، سود £3)

    b) PMF:
    - $P(W=-2) = 3/6 = 1/2$ (آمدن 1، 2 یا 3)
    - $P(W=0) = 2/6 = 1/3$ (آمدن 4 یا 5)
    - $P(W=3) = 1/6$ (آمدن 6)

    c) $E[W] = (-2)(1/2) + (0)(1/3) + (3)(1/6) = -1 + 0 + 0.5 = -0.5$

    منصفانه نیست؛ باخت مورد انتظار £0.50 در هر بازی

    d) $E[W^2] = 4(1/2) + 0(1/3) + 9(1/6) = 2 + 0 + 1.5 = 3.5$

    $Var(W) = 3.5 - (-0.5)^2 = 3.5 - 0.25 = 3.25$
    ```

4.  **مقایسه شبیه‌سازی:** پرتاب دو تاس منصفانه و محاسبه مجموع آن‌ها را $10{,}000$ بار شبیه‌سازی کنید.
    a.  میانگین نمونه و واریانس نمونه مجموع‌های شبیه‌سازی‌شده را محاسبه کنید.
    b.  آن‌ها را با مقادیر نظری که در تمرین ۲ محاسبه کردید مقایسه کنید.
    c.  PMF تجربی مجموع‌های شبیه‌سازی‌شده را رسم کنید و با PMF نظری تمرین ۲ مقایسه کنید.

    ```{admonition} راهنما
    :class: tip

    از `np.random.randint(1, 7, size=(10000, 2))` برای شبیه‌سازی دو تاس 10000 بار استفاده کنید، سپس در امتداد محور 1 جمع بگیرید.
    ```

---

+++

*(پیوست راه‌حل‌ها/راهنماها)*

:::{dropdown} کد نمونه برای تمرین ۱
```{code-cell} ipython3
# تمرین ۱: سکهٔ نامتوازن
p_heads = 0.7
p_tails = 1 - p_heads

# a) PMF
x_values_coin = np.array([0, 1]) # 0 for Tails, 1 for Heads
pmf_coin = np.array([p_tails, p_heads])
pmf_coin_dict = {val: prob for val, prob in zip(x_values_coin, pmf_coin)}
print(f"Ex 1(a) - PMF: {pmf_coin_dict}")

# b) CDF
cdf_coin_values = np.cumsum(pmf_coin)
def coin_cdf_func(x):
    if x < 0: return 0.0
    if x >= 1: return 1.0
    return cdf_coin_values[0] # P(X<=0)

# c) Expected Value
ex_coin = np.sum(x_values_coin * pmf_coin)
print(f"Ex 1(c) - E[X]: {ex_coin}")

# d) Variance
ex2_coin = np.sum((x_values_coin**2) * pmf_coin)
var_coin = ex2_coin - ex_coin**2
sd_coin = np.sqrt(var_coin)
print(f"Ex 1(d) - Var(X): {var_coin:.4f}")
print(f"Ex 1(d) - SD(X): {sd_coin:.4f}")
```
:::
