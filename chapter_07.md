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
  - file: notebooks/chapter_07.ipynb
---
# فصل ۷: توزیع‌های گسسته رایج

در فصل قبل، متغیرهای تصادفی گسسته را تعریف کردیم و آموختیم رفتار آن‌ها را با تابع جرم احتمال (PMF)، تابع توزیع تجمعی (CDF)، امید ریاضی و واریانس چگونه توصیف کنیم. اگرچه می‌توان PMF سفارشی برای هر موقعیت تعریف کرد، چند توزیع گسسته مشخص آن‌قدر در عمل تکرار می‌شوند که به‌طور گسترده مطالعه شده و نام‌گذاری شده‌اند.

این توزیع‌های «رایج» مدل‌های قدرتمندی برای انواع گسترده‌ای از فرایندهای دنیای واقعی هستند. درک ویژگی‌های آن‌ها و زمان به‌کارگیری‌شان برای مدل‌سازی احتمالاتی حیاتی است. در این فصل، نه توزیع گسسته بنیادین را بررسی می‌کنیم: Bernoulli، Binomial، Geometric، Negative Binomial، Poisson، Hypergeometric، Discrete Uniform، Categorical و Multinomial.

سناریویی را که هر توزیع مدل می‌کند، ویژگی‌های کلیدی آن (PMF، میانگین، واریانس) و نحوه کار کارآمد با آن‌ها با کتابخانه `scipy.stats` پایتون را بررسی می‌کنیم. این کتابخانه ابزارهایی برای محاسبه احتمال‌ها (PMF، CDF)، تولید نمونه تصادفی و موارد دیگر فراهم می‌کند و کار عملی ما را به‌طور قابل توجهی ساده می‌سازد.

:::{admonition} تمرکز بر درک، نه حفظ کردن
:class: tip

هنگام مطالعه این فصل به خاطر داشته باشید: **درک ساختار احتمالاتی زیربنایی مهم‌تر از حفظ فرمول‌هاست**.

برای هر توزیع روی این موارد تمرکز کنید:
- **چه زمانی استفاده شود**: چه سناریوی دنیای واقعی را مدل می‌کند؟
- **چرا کار می‌کند**: شهود پشت فرمول چیست؟
- **توزیع‌ها چگونه مرتبط‌اند**: چگونه به توزیع‌های دیگری که می‌شناسید متصل می‌شود؟

نگران حفظ کردن هر فرمول PMF نباشید — همیشه می‌توانید آن‌ها را جستجو کنید یا از `scipy.stats` استفاده کنید. در عوض، شهود بسازید درباره اینکه *چه زمانی* و *چرا* از هر توزیع استفاده کنید. این درک عمیق‌تر بسیار بیشتر از حفظ کردن به شما کمک می‌کند!
:::
```{code-cell} ipython3
:tags: [remove-input, remove-output]

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os

# Configure plots
plt.style.use('seaborn-v0_8-whitegrid')
```
## ۱. توزیع Bernoulli

توزیع Bernoulli یک آزمایش واحد با دو پیامد ممکن را مدل می‌کند: «موفقیت» (۱) یا «شکست» (۰).

:::{admonition} چرا با چیزی این‌قدر ساده شروع می‌کنیم؟
:class: note

توزیع Bernoulli ممکن است تقریباً به‌ظاهر بسیار ساده به نظر برسد — فقط یک آزمایش با دو پیامد! با این حال، فوق‌العاده مهم است زیرا:

- **بلوک سازنده بنیادین است**: چند توزیع کلیدی در این فصل (Binomial، Geometric، Negative Binomial) مستقیماً بر پایه تکرار آزمایش‌های Bernoulli ساخته می‌شوند، در حالی که Categorical توزیع Bernoulli را به بیش از دو پیامد تعمیم می‌دهد
- **رویدادهای دودویی تکی همه‌جا هستند**: بسیاری از سناریوهای دنیای واقعی شامل یک تصمیم بله/خیر، موفقیت/شکست یا روشن/خاموش هستند
- **الگوهای کلیدی را برقرار می‌کند**: ساختار $p$ و $(1-p)$ در سراسر نظریه احتمال ظاهر می‌شود
- **یادداشت ریاضی**: توزیع Bernoulli از نظر فنی فقط توزیع Binomial با $n=1$ است، اما به‌خاطر اهمیت بنیادین آن نام جداگانه‌ای دارد

مثل یاد گرفتن جمع قبل از ضرب فکر کنید — ساده، اما ضروری!
:::

**مثال ملموس**

فرض کنید یک آزمون غربالگری پزشکی برای بیماری در جمعیت پرخطر انجام می‌دهید. هر آزمون یا مثبت یا منفی است. از داده‌های اپیدمیولوژیک می‌دانید ۳۰٪ افراد این جمعیت نتیجه مثبت دارند.

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X = 1$ اگر نتیجه آزمون مثبت باشد (موفقیت)
- $X = 0$ اگر نتیجه آزمون منفی باشد (شکست)

احتمال‌ها:
- $P(X = 1) = 0.3$ (این پارامتر را $p$ می‌نامیم)
- $P(X = 0) = 0.7$ (که برابر $1 - p$ است)

**PMF برنولی**

برای هر متغیر تصادفی Bernoulli با احتمال موفقیت $p$، PMF برابر است با:
$$ P(X=k) = \begin{cases} p & \text{if } k=1 \\ 1-p & \text{if } k=0 \\ 0 & \text{otherwise} \end{cases} $$
این را می‌توان به‌صورت فشرده نیز نوشت:
$$P(X = k) = p^k (1-p)^{1-k} \text{ for } k \in \{0, 1\}$$
بسط این برای هر دو حالت تا کاملاً روشن شود:

##### وقتی k = 1 (موفقیت)

$$
\begin{align}
P(X=1) &= p^1 (1-p)^{1-1} \\
&= p^1 (1-p)^0 \\
&= p \times 1 \\
&= p
\end{align}
$$

##### وقتی k = 0 (شکست)

$$
\begin{align}
P(X=0) &= p^0 (1-p)^{1-0} \\
&= p^0 (1-p)^1 \\
&= 1 \times (1-p) \\
&= 1-p
\end{align}
$$

بیایید تأیید کنیم این برای مثال ما با $p = 0.3$ درست کار می‌کند:
- وقتی $k = 1$: $P(X=1) = (0.3)^1 (0.7)^0 = 0.3 \times 1 = 0.3$ ✓
- وقتی $k = 0$: $P(X=0) = (0.3)^0 (0.7)^1 = 1 \times 0.7 = 0.7$ ✓

**ویژگی‌های کلیدی**

- **سناریوها**: پرتاب سکه (شیر/خط)، بازرسی محصول (معیوب/سالم)، آزمون پزشکی (مثبت/منفی)، پرتاب آزاد (گل/خطا)
- **پارامتر**: $p$، احتمال موفقیت ($0 \le p \le 1$)
- **متغیر تصادفی**: $X \in \{0, 1\}$

**میانگین:** $E[X] = p$

**واریانس:** $Var(X) = p(1-p)$

**انحراف معیار:** $SD(X) = \sqrt{p(1-p)}$

**مصورسازی توزیع**

بیایید توزیع Bernoulli با $p = 0.3$ را مصور کنیم (مثال آزمون پزشکی بالا):
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_bernoulli_pmf_generic.svg'):
    os.remove('ch07_bernoulli_pmf_generic.svg')

# Create Bernoulli distribution for visualization (p=0.3)
p_viz = 0.3
bernoulli_viz = stats.bernoulli(p=p_viz)

# Calculate mean and std
mean_viz = bernoulli_viz.mean()
std_viz = bernoulli_viz.std()

# Plotting the PMF
k_values_viz = [0, 1]
pmf_values_viz = bernoulli_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, tick_label=["Failure (0)", "Success (1)"], color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.2f}, {mean_viz + std_viz:.2f}]')

plt.title(f"Bernoulli PMF (p={p_viz})")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_bernoulli_pmf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
PMF دو میله نشان می‌دهد: P(X=0) = 0.7 برای آزمون منفی و P(X=1) = 0.3 برای آزمون مثبت. خط چین قرمز میانگین ($p = 0.3$) را نشان می‌دهد و ناحیه سایه‌دار نارنجی میانگین ± ۱ انحراف معیار را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_bernoulli_cdf_generic.svg'):
    os.remove('ch07_bernoulli_cdf_generic.svg')

# Plotting the CDF
k_values_viz = [0, 1]
cdf_values_viz = bernoulli_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
# Add points to show the full step function including the start at 0
plt.step([-0.5] + k_values_viz, [0] + list(cdf_values_viz), where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

plt.title(f"Bernoulli CDF (p={p_viz})")
plt.xlabel("Outcome")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.ylim(0, 1.1)
plt.xlim(-0.5, 1.5)
plt.xticks([0, 1])
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_bernoulli_cdf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
CDF تابع پله‌ای را نشان می‌دهد: از ۰ برای x < 0 شروع می‌شود، در x=0 به ۰.۷ می‌پرد (مقدار وقتی پیامد ۰ است)، تا x=1 در ۰.۷ ثابت می‌ماند، سپس در x=1 به ۱.۰ می‌پرد (مقدار وقتی هر دو پیامد ۰ و ۱ را شامل می‌شود). خط چین قرمز میانگین را نشان می‌دهد.

یادداشت: اینجا P(X ≤ 0) = P(X = 0) = 0.7 زیرا X نمی‌تواند مقادیر منفی بگیرد؛ به‌طور کلی «X ≤ 0» یعنی «در ۰ یا پایین‌تر»، نه «دقیقاً ۰».

**خواندن PMF**

- **چه چیزی نشان می‌دهد:** ارتفاع هر میله احتمال همان پیامد دقیق را نشان می‌دهد
- **چگونه بخوانیم:** ارتفاع میله را ببینید تا P(X = k) را برای هر مقدار k مشخص بیابید
- **کاربرد عملی:** به سؤالاتی مثل «احتمال موفقیت چقدر است؟» یا «احتمال دقیقاً ۱ آزمون مثبت چقدر است؟» پاسخ دهید
- **ویژگی کلیدی:** مجموع ارتفاع همه میله‌ها باید ۱.۰ باشد (احتمال کل)
- **کمک‌های مصورسازی:** خط چین قرمز میانگین (امید ریاضی) را نشان می‌دهد و ناحیه سایه‌دار نارنجی میانگین ± ۱ انحراف معیار را نشان می‌دهد (جایی که ~۶۸٪ مقادیر معمولاً قرار می‌گیرند)

**خواندن CDF**

- **چه چیزی نشان می‌دهد:** احتمال تجمعی P(X ≤ k) تا و شامل هر مقدار k
- **چگونه بخوانیم:** ارتفاع در موقعیت k احتمال k یا کمتر موفقیت را به شما می‌گوید
- **چرا توابع پله‌ای؟** برای توزیع‌های گسسته، احتمال در پرش‌ها در هر مقدار ممکن تجمع می‌یابد. بین مقادیر ممکن، CDF ثابت می‌ماند (احتمال اضافه‌ای نیست)
- **هویت کلیدی:** پرش در k برابر P(X = k) است — اندازه هر پله بالا همان مقدار PMF است
- **کاربردهای عملی:**
  - P(X ≤ k) را مستقیماً با خواندن ارتفاع در k بیابید
  - P(X > k) را با محاسبه 1 - P(X ≤ k) بیابید
  - P(a < X ≤ b) را با محاسبه P(X ≤ b) - P(X ≤ a) بیابید
- **ویژگی کلیدی:** CDF پیوسته از راست است، همیشه افزایش می‌یابد (یا ثابت می‌ماند) و به ۱.۰ نزدیک می‌شود
- **کمک‌های مصورسازی:** خط چین قرمز میانگین (امید ریاضی) را به‌عنوان نقطه مرجع نشان می‌دهد

**یادداشت درباره مصورسازی CDF:** نمودارها از `where='post'` در نمودار پله‌ای برای ساخت توابع پله‌ای پیوسته از راست مناسب استفاده می‌کنند. یعنی CDF در هر مقدار بالا می‌پرد و آن مقدار را در احتمال تجمعی شامل می‌کند.

::::{admonition} مثال: آزمون تشخیصی پزشکی با p = 0.1
:class: tip

مدل‌سازی پیامد یک آزمون تشخیصی پزشکی واحد که احتمال نتیجه مثبت آن ۰.۱ است.

از [`scipy.stats.bernoulli`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bernoulli.html) برای محاسبه احتمال‌ها، محاسبه میانگین و واریانس، و تولید نمونه‌های تصادفی استفاده می‌کنیم.
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.bernoulli
p_positive = 0.1
bernoulli_rv = stats.bernoulli(p=p_positive)

# PMF: Probability of success (k=1) and failure (k=0)
print(f"P(X=1) (Positive Test): {bernoulli_rv.pmf(1):.2f}")
print(f"P(X=0) (Negative Test): {bernoulli_rv.pmf(0):.2f}")

# Mean and Variance
print(f"Mean (Expected Value): {bernoulli_rv.mean():.2f}")
print(f"Variance: {bernoulli_rv.var():.2f}")
```
:::{admonition} کار با متغیرهای تصادفی منجمد (Frozen) در scipy.stats
:class: note

وقتی `bernoulli_rv = stats.bernoulli(p=p_positive)` می‌نویسیم، یک **متغیر تصادفی منجمد (frozen random variable)** می‌سازیم — شیء توزیعی که پارامترهای آن قفل شده‌اند.

**مثل نیمه‌ناپذیری فکر کنید:** مشابه اشیای ناپذیر پایتون (رشته‌ها، tupleها) که پس از ساخت قابل تغییر نیستند، پارامترهای توزیع یک RV منجمد ثابت و غیرقابل تغییر هستند. تفاوت این است که RVهای منجمد فقط پارامترها (مثل p=0.1) را «منجمد» می‌کنند، نه کل شیء را.

**دو روش استفاده از scipy.stats:**

1. **غیرمنجمد** (هر بار پارامترها را پاس دهید):
   ```python
   stats.bernoulli.pmf(1, p=0.1)
   stats.bernoulli.cdf(0, p=0.1)
   stats.bernoulli.mean(p=0.1)
   ```
2. **منجمد** (یک‌بار پارامترها را تنظیم کنید، دوباره استفاده کنید):
   ```python
   rv = stats.bernoulli(p=0.1)  # Create frozen RV
   rv.pmf(1)                     # Use it multiple times
   rv.cdf(0)
   rv.mean()
   ```
**مزایای RVهای منجمد:**
- کد تمیزتر و خواناتر
- کارآمدتر (پارامترها یک‌بار اعتبارسنجی می‌شوند)
- عبور دادن توزیع‌ها به توابع آسان‌تر
- با الگوی مستندات scipy همخوان است

در سراسر این فصل، برای همه مثال‌ها از RVهای منجمد استفاده می‌کنیم. این رویکرد توصیه‌شده است وقتی با همان پارامترهای توزیع چندین بار کار می‌کنید.
:::
```{code-cell} ipython3
# Generate random samples
n_samples = 10
samples = bernoulli_rv.rvs(size=n_samples)
print(f"{n_samples} simulated test outcomes (1=Positive, 0=Negative):")
print(samples)
```
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_bernoulli_pmf.svg'):
    os.remove('ch07_bernoulli_pmf.svg')
```
```{code-cell} ipython3
# Plotting the PMF
k_values = [0, 1]
pmf_values = bernoulli_rv.pmf(k_values)

plt.figure(figsize=(8, 3.5))
plt.bar(k_values, pmf_values, tick_label=["Negative (0)", "Positive (1)"], color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Bernoulli PMF (p={p_positive})")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_bernoulli_pmf.svg', format='svg', bbox_inches='tight')
```
PMF احتمال هر پیامد را نشان می‌دهد. با p = 0.1، «Negative» احتمال ۰.۹ و «Positive» احتمال ۰.۱ دارد.
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_bernoulli_cdf.svg'):
    os.remove('ch07_bernoulli_cdf.svg')
```
```{code-cell} ipython3
# Plotting the CDF
cdf_values = bernoulli_rv.cdf(k_values)

plt.figure(figsize=(8, 3.5))
# Add points to show the full step function including the start at 0
plt.step([-0.5] + k_values, [0] + list(cdf_values), where='post', color='darkgreen', linewidth=2)
plt.title(f"Bernoulli CDF (p={p_positive})")
plt.xlabel("Outcome")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.ylim(0, 1.1)
plt.xlim(-0.5, 1.5)
plt.xticks([0, 1])
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_bernoulli_cdf.svg', format='svg', bbox_inches='tight')
```
CDF تابع پله‌ای را نشان می‌دهد: از ۰ برای x < 0 شروع می‌شود، در x=0 به ۰.۹ می‌پرد، تا x=1 در ۰.۹ ثابت می‌ماند، سپس در x=1 به ۱.۰ می‌پرد.

::::

**سؤالات مرور سریع**

1. یک بازرس کنترل کیفیت یک محصول را بررسی می‌کند. یا معیوب است یا سالم. آیا این سناریو با توزیع Bernoulli به‌خوبی مدل می‌شود؟ چرا یا چرا نه؟
```{admonition} پاسخ
:class: dropdown

**بله** — این سناریو کاملاً با الزامات توزیع Bernoulli سازگار است:
- **آزمایش واحد**: بررسی یک محصول
- **دو پیامد ممکن**: معیوب (موفقیت/۱) یا سالم (شکست/۰)
- **احتمال ثابت**: نرخ معیوب بودن برای هر محصول ثابت است

اگر نرخ معیوب بودن ۵٪ باشد، از Bernoulli(p=0.05) استفاده می‌کنیم.
```
2. برای توزیع Bernoulli با p = 0.3، مقدار P(X = 0) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**P(X = 0) = 1 - p = 0.7** — احتمال شکست برابر 1 - p است.
```
3. یک بازیکن بسکتبال ۷۵٪ نرخ موفقیت در پرتاب آزاد دارد. اگر یک پرتاب آزاد را به‌عنوان آزمایش Bernoulli مدل کنیم، میانگین و واریانس چقدر است؟
```{admonition} پاسخ
:class: dropdown

**میانگین = 0.75، واریانس = 0.75 × 0.25 = 0.1875**

با فرمول‌های E[X] = p و Var(X) = p(1-p):
- E[X] = 0.75
- Var(X) = 0.75 × (1 - 0.75) = 0.75 × 0.25 = 0.1875
```
4. یک تاس شش‌وجهی را یک‌بار می‌اندازید. آیا این با توزیع Bernoulli به‌خوبی مدل می‌شود؟
```{admonition} پاسخ
:class: dropdown

**خیر** — توزیع Bernoulli دقیقاً **دو پیامد ممکن** می‌خواهد. پرتاب تاس ۶ پیامد دارد (1, 2, 3, 4, 5, 6)، پس Bernoulli مستقیماً اعمال نمی‌شود.

**با این حال**، *می‌توانید* از Bernoulli استفاده کنید اگر آزمایش را با پیامد دودویی بازتعریف کنید:
- «آیا تاس ۶ نشان می‌دهد؟» (بله/خیر) → Bernoulli با p = 1/6
- «آیا نتیجه زوج است؟» (بله/خیر) → Bernoulli با p = 1/2

نکته کلیدی: Bernoulli دقیقاً دو پیامد می‌خواهد.
```
5. درست یا نادرست: یک متغیر تصادفی Bernoulli فقط می‌تواند مقادیر ۰ و ۱ بگیرد.
```{admonition} پاسخ
:class: dropdown

**درست** — طبق تعریف، متغیر تصادفی Bernoulli دارای X ∈ {0, 1} است، که:
- X = 1 نمایانگر «موفقیت» با احتمال p است
- X = 0 نمایانگر «شکست» با احتمال 1-p است

این دو تنها پیامد ممکن هستند.
```
+++
## ۲. توزیع Binomial

توزیع Binomial تعداد موفقیت‌ها در *تعداد ثابتی* از آزمایش‌های مستقل Bernoulli را مدل می‌کند، جایی که هر آزمایش همان احتمال موفقیت را دارد.

**مثال ملموس**

فرض کنید یک سکه منصفانه را ۱۰ بار می‌اندازید. هر پرتاب یک آزمایش Bernoulli با p = 0.5 (احتمال شیر) است. چند شیر می‌گیرید؟

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = تعداد شیرها در ۱۰ پرتاب
- $X$ می‌تواند مقادیر 0, 1, 2, ..., 10 بگیرد

احتمال‌ها:
- $P(X = 0)$ = احتمال ۰ شیر (همه خط)
- $P(X = 5)$ = احتمال دقیقاً ۵ شیر
- $P(X = 10)$ = احتمال ۱۰ شیر (همه شیر)

**PMF دوجمله‌ای**

برای $n$ آزمایش مستقل با احتمال موفقیت $p$:
$$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} $$
for $k = 0, 1, \dots, n$

که $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ ضریب دوجمله‌ای (تعداد روش‌های انتخاب $k$ موفقیت از $n$ آزمایش) است.

:::{admonition} درک فرمول Binomial
:class: note

فرمول PMF دوجمله‌ای احتمال و شمارش را ترکیب می‌کند:
$$P(X=k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$
**تجزیه فرمول:**
- **$p^k$**: احتمال $k$ موفقیت — هر موفقیت یک آزمایش مستقل Bernoulli با احتمال $p$ است
- **$(1-p)^{n-k}$**: احتمال $(n-k)$ شکست — هر شکست یک آزمایش مستقل Bernoulli با احتمال $1-p$ است
- **$\binom{n}{k}$**: تعداد روش‌های چیدمان $k$ موفقیت در $n$ موقعیت آزمایش

**دیدگاه احتمالاتی (آزمایش‌های Bernoulli):**

هر دنباله مشخص از $k$ موفقیت و $(n-k)$ شکست احتمال $p^k(1-p)^{n-k}$ دارد (به‌خاطر استقلال آزمایش‌ها). مثلاً دنباله «موفقیت، موفقیت، شکست» احتمال $p \cdot p \cdot (1-p) = p^2(1-p)$ دارد.

این نشان می‌دهد چرا Binomial «موفقیت‌ها در آزمایش‌های تکراری Bernoulli را می‌شمارد»: از پایه با احتمال Bernoulli $p$ برای هر آزمایش ساخته شده است.

**دیدگاه ترکیبی (تکنیک‌های شمارش):**

ضریب دوجمله‌ای $\binom{n}{k}$ یک **ترکیب** است که تعداد روش‌های انتخاب $k$ مورد از $n$ مورد را وقتی ترتیب مهم نیست می‌شمارد (به [فصل ۳: ترکیبات](chapter_03.md#combinations-when-order-doesnt-matter) مراجعه کنید).

در این زمینه، **تعداد دنباله‌های مختلف** از $n$ آزمایش که دقیقاً $k$ موفقیت می‌دهند را می‌شمارد. مثلاً با $n=3$ آزمایش و $k=2$ موفقیت: $\binom{3}{2} = 3$ نمایانگر سه دنباله SSF، SFS و FSS است (که S=موفقیت، F=شکست).

**چرا ضرب می‌کنیم:** هر یک از $\binom{n}{k}$ دنباله احتمال یکسان $p^k(1-p)^{n-k}$ دارد. برای گرفتن احتمال کل دقیقاً $k$ موفقیت (به هر ترتیبی)، تعداد دنباله‌ها را در احتمال هر دنباله ضرب می‌کنیم.

**مثال مصور:** این‌طور برای $n=3$ آزمایش، $k=2$ موفقیت، با $p=0.6$ کار می‌کند:
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_binomial_formula_breakdown.svg'):
    os.remove('ch07_binomial_formula_breakdown.svg')

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --- Parameters ---
n, k, p = 3, 2, 0.6
q = 1 - p
prob_each = (p**k) * (q**(n-k))
total = 3 * prob_each

fig, ax = plt.subplots(figsize=(14, 8), constrained_layout=True)
ax.set_axis_off()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# ---------------- helpers ----------------
def rounded_box(ax, xy, w, h, fc, ec, lw=2, pad=0.012, r=0.02, z=3):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={pad},rounding_size={r}",
        transform=ax.transAxes,
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z
    )
    ax.add_patch(patch)
    return patch

def draw_sequence(ax, cx, cy, label):
    w, h = 0.14, 0.075
    rounded_box(ax, (cx - w/2, cy - h/2), w, h,
                fc="lightblue", ec="steelblue", lw=2.2, r=0.02)

    ax.text(cx, cy, label, transform=ax.transAxes,
            ha="center", va="center",
            fontsize=24, weight="bold", family="monospace", zorder=4)

    ax.text(cx, cy - 0.075, rf"${p:.1f}\times{p:.1f}\times{q:.1f}$",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=18, zorder=4)

    ax.text(cx, cy - 0.115, rf"$= {prob_each:.3f}$",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=18, weight="bold", zorder=4)

    # return (left, bottom, right, top) for arrow anchoring
    return (cx - w/2, cy - h/2, cx + w/2, cy + h/2)

# ---------------- layout ----------------
ax.text(0.5, 0.955, rf"Binomial Formula Breakdown: $n={n},\,k={k},\,p={p}$",
        transform=ax.transAxes, ha="center", va="top",
        fontsize=24, weight="bold", zorder=4)

# Top row: sequences
seq_y = 0.78
seq_boxes = {}
for lbl, x in [("SSF", 0.24), ("SFS", 0.50), ("FSS", 0.76)]:
    seq_boxes[lbl] = draw_sequence(ax, x, seq_y, lbl)

# Count box
count_w, count_h = 0.30, 0.08
count_xy = (0.5 - count_w/2, 0.56 - count_h/2)
rounded_box(ax, count_xy, count_w, count_h,
            fc="lightyellow", ec="orange", lw=2.2, r=0.02)

ax.text(0.5, 0.56, r"$\binom{3}{2}=3$ sequences",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=20, weight="bold", zorder=4)

# Formula block
ax.text(0.5, 0.44, "Formula:", transform=ax.transAxes,
        ha="center", va="center", fontsize=20, weight="bold", zorder=4)

ax.text(0.5, 0.385, r"$P(X=2)=\binom{3}{2}\cdot p^2\cdot (1-p)^1$",
        transform=ax.transAxes, ha="center", va="center", fontsize=18, zorder=4)

ax.text(0.5, 0.33, r"$=3\times 0.36\times 0.4$",
        transform=ax.transAxes, ha="center", va="center", fontsize=18, zorder=4)

# Result box (moved DOWN a bit)
res_w, res_h = 0.18, 0.075
res_center_y = 0.235  # was 0.26
res_xy = (0.5 - res_w/2, res_center_y - res_h/2)
rounded_box(ax, res_xy, res_w, res_h,
            fc="lightgreen", ec="green", lw=2.2, r=0.02)

ax.text(0.5, res_center_y, rf"$= {total:.3f}$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=20, weight="bold", zorder=4)

# ---- Callouts: arrows hit box edges and avoid overlaps ----
# Orange (label moved down a bit)
count_tip = (count_xy[0], count_xy[1] + count_h*0.55)  # left edge of yellow box
ax.annotate("Count sequences",
            xy=count_tip, xycoords=ax.transAxes,
            xytext=(0.08, 0.595), textcoords=ax.transAxes,  # moved down
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.10",
                            lw=2.5, color="orange",
                            shrinkA=6, shrinkB=8),
            fontsize=16, color="orange", weight="bold",
            ha="left", va="center", zorder=5)

# Blue -> right edge of FSS box
x0, y0, x1, y1 = seq_boxes["FSS"]
fss_tip = (x1, (y0 + y1) / 2)
ax.annotate("Each sequence\nhas same\nprobability",
            xy=fss_tip, xycoords=ax.transAxes,
            xytext=(0.88, 0.84), textcoords=ax.transAxes,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.18",
                            lw=2.5, color="steelblue",
                            shrinkA=6, shrinkB=10),
            fontsize=16, color="steelblue", weight="bold",
            ha="left", va="center", zorder=5)

# Green -> right edge of result box
res_tip = (res_xy[0] + res_w, res_xy[1] + res_h*0.55)
ax.annotate("Multiply!",
            xy=res_tip, xycoords=ax.transAxes,
            xytext=(0.78, 0.19), textcoords=ax.transAxes,  # nudged down
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.10",
                            lw=2.5, color="green",
                            shrinkA=6, shrinkB=10),
            fontsize=16, color="green", weight="bold",
            ha="left", va="center", zorder=5)

# Bottom explanation
why = (
    f"Why it works: Each sequence occurs with probability {total:.3f}/3 = {prob_each:.3f}, "
    f"and there are 3 ways to get exactly 2 successes, so total = 3 × {prob_each:.3f} = {total:.3f}."
)
ax.text(0.5, 0.10, why,
        transform=ax.transAxes, ha="center", va="center",
        fontsize=14, style="italic", wrap=True, zorder=4)

plt.savefig('ch07_binomial_formula_breakdown.svg', format='svg', bbox_inches='tight')
plt.show()
```
نمودار نشان می‌دهد اجزای فرمول چگونه با هم کار می‌کنند: دنباله‌ها را می‌شماریم (۳)، احتمال هر دنباله را محاسبه می‌کنیم (0.144)، و ضرب می‌کنیم تا احتمال کل دقیقاً ۲ موفقیت (0.432) به‌دست آید.
:::

بیایید تأیید کنیم این برای مثال پرتاب سکه ما (n=10, p=0.5) درست کار می‌کند:
$$
\begin{align}
P(X=5) &= \binom{10}{5} p^5 (1-p)^{10-5} \\
&= \binom{10}{5} (0.5)^5 (1-0.5)^5 \\
&= \binom{10}{5} (0.5)^5 (0.5)^5 \\
&= 252 \times 0.03125 \times 0.03125 \\
&\approx 0.246 \quad \checkmark
\end{align}
$$
**ویژگی‌های کلیدی**

- **سناریوها**: تعداد شیر در پرتاب سکه، اقلام معیوب در یک دسته، پرتاب‌های آزاد موفق، حدس‌های درست در آزمون، مشتریانی که خرید می‌کنند
- **پارامترها**:
    - $n$: تعداد آزمایش‌های مستقل
    - $p$: احتمال موفقیت در هر آزمایش ($0 \le p \le 1$)
- **متغیر تصادفی**: $X \in \{0, 1, 2, ..., n\}$

**میانگین:** $E[X] = np$

**واریانس:** $Var(X) = np(1-p)$

**انحراف معیار:** $SD(X) = \sqrt{np(1-p)}$

**مصورسازی توزیع**

بیایید توزیع Binomial با $n = 10$ و $p = 0.5$ را مصور کنیم (مثال پرتاب سکه ما):
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_binomial_pmf_generic.svg'):
    os.remove('ch07_binomial_pmf_generic.svg')

# Create Binomial distribution for visualization (n=10, p=0.5)
n_viz = 10
p_viz = 0.5
binomial_viz = stats.binom(n=n_viz, p=p_viz)

# Calculate mean and std
mean_viz = binomial_viz.mean()
std_viz = binomial_viz.std()

# Plotting the PMF
k_values_viz = np.arange(0, n_viz + 1)
pmf_values_viz = binomial_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.1f}, {mean_viz + std_viz:.1f}]')

plt.title(f"Binomial PMF (n={n_viz}, p={p_viz})")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Probability")
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_binomial_pmf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
PMF توزیع احتمال تعداد شیرها در ۱۰ پرتاب سکه را نشان می‌دهد. توزیع حول میانگین ($np = 5$) متقارن است زیرا $p = 0.5$. ناحیه سایه‌دار میانگین ± ۱ انحراف معیار ($\sqrt{np(1-p)} = \sqrt{2.5} \approx 1.58$) را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_binomial_cdf_generic.svg'):
    os.remove('ch07_binomial_cdf_generic.svg')

# Plotting the CDF
cdf_values_viz = binomial_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

plt.title(f"Binomial CDF (n={n_viz}, p={p_viz})")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_binomial_cdf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
CDF مقدار P(X ≤ k)، احتمال تجمعی k یا کمتر شیر را نشان می‌دهد. خط چین قرمز میانگین را نشان می‌دهد.

:::{admonition} مثال: تماس‌های فروش با n = 20, p = 0.15
:class: tip

مدل‌سازی تعداد تماس‌های فروش موفق از ۲۰ تماس، که هر تماس ۰.۱۵ احتمال موفقیت دارد.

نحوه استفاده از [`scipy.stats.binom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html) برای محاسبه احتمال‌ها، آمار و تولید نمونه‌های تصادفی را نشان می‌دهیم.

**تنظیم توزیع:**

شیء توزیع دوجمله‌ای را با پارامترهایمان (۲۰ آزمایش، احتمال موفقیت ۰.۱۵) می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.binom
n_calls = 20
p_success_call = 0.15
binomial_rv = stats.binom(n=n_calls, p=p_success_call)
```
**محاسبه احتمال‌های مشخص با PMF:**

احتمال دقیقاً ۵ فروش موفق از ۲۰ تماس چقدر است؟
```{code-cell} ipython3
# PMF: Probability of exactly k successes
k_successes = 5
print(f"P(X={k_successes} successes out of {n_calls}): {binomial_rv.pmf(k_successes):.4f}")
```
با احتمال ۱۰.۲۳٪، ۵ موفقیت نسبتاً محتمل است اما محتمل‌ترین پیامد نیست (مد در ۳ موفقیت است، مطابق میانگین np = 20 × 0.15 = 3).

**محاسبه احتمال‌های تجمعی با CDF:**

احتمال ۳ یا کمتر موفقیت چقدر است؟ یا بیش از ۳؟
```{code-cell} ipython3
# CDF: Probability of k or fewer successes
k_or_fewer = 3
print(f"P(X <= {k_or_fewer} successes out of {n_calls}): {binomial_rv.cdf(k_or_fewer):.4f}")
print(f"P(X > {k_or_fewer} successes out of {n_calls}): {1 - binomial_rv.cdf(k_or_fewer):.4f}")
print(f"P(X > {k_or_fewer} successes out of {n_calls}) (using sf): {binomial_rv.sf(k_or_fewer):.4f}")
```
۶۴.۸۵٪ احتمال ۳ یا کمتر موفقیت وجود دارد، یعنی ۳۵.۱۵٪ احتمال بیش از ۳ موفقیت.

**یادداشت درباره تابع بقا (`sf`):** متد `sf()` **تابع بقا (survival function)** را محاسبه می‌کند که P(X > k) = 1 - P(X ≤ k) است. اگرچه از نظر ریاضی معادل `1 - cdf(k)` است، استفاده مستقیم از `sf(k)` ترجیح دارد زیرا دقت عددی بهتری برای احتمال‌های بسیار کوچک یا بزرگ فراهم می‌کند و قصد کد را روشن‌تر می‌سازد.

**محاسبه میانگین و واریانس:**

بیایید فرمول‌های نظری E[X] = np و Var(X) = np(1-p) را تأیید کنیم:
```{code-cell} ipython3
# Mean and Variance
print(f"Mean (Expected number of successes): {binomial_rv.mean():.2f}")
print(f"Variance: {binomial_rv.var():.2f}")
print(f"Standard Deviation: {binomial_rv.std():.2f}")
```
طبق انتظار، میانگین ۳.۰۰ موفقیت (20 × 0.15) با انحراف معیار حدود ۱.۶ به‌دست می‌آید که تغییرپذیری متوسط حول میانگین را نشان می‌دهد.
```{code-cell} ipython3
# Generate random samples
n_simulations = 1000
samples = binomial_rv.rvs(size=n_simulations)
# print(f"\nSimulated number of successes in {n_calls} calls ({n_simulations} simulations): {samples[:20]}...") # Print first 20
```
این نمونه‌ها نمایانگر ۱۰۰۰ فروشنده مختلف هستند که هر کدام ۲۰ تماس می‌گیرند و تغییرپذیری طبیعی پیامدها را نشان می‌دهند.
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_binomial_pmf.svg'):
    os.remove('ch07_binomial_pmf.svg')
```
```{code-cell} ipython3
# Plotting the PMF
k_values = np.arange(0, n_calls + 1)
pmf_values = binomial_rv.pmf(k_values)

plt.figure(figsize=(8, 3.5))
plt.bar(k_values, pmf_values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Binomial PMF (n={n_calls}, p={p_success_call})")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Probability")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_binomial_pmf.svg', format='svg', bbox_inches='tight')
```
PMF توزیع احتمال تعداد تماس‌های موفق را نشان می‌دهد. با n = 20 و p = 0.15، توزیع حول np = 3 موفقیت (قله) متمرکز است. توزیع کمی چوله به راست است زیرا p < 0.5. توجه کنید ۰، ۱ یا ۲ موفقیت احتمال زیادی دارد، در حالی که بیش از ۸ موفقیت بسیار بعید است.
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_binomial_cdf.svg'):
    os.remove('ch07_binomial_cdf.svg')
```
```{code-cell} ipython3
# Plotting the CDF
cdf_values = binomial_rv.cdf(k_values)

plt.figure(figsize=(8, 3.5))
plt.step(k_values, cdf_values, where='post', color='darkgreen', linewidth=2)
plt.title(f"Binomial CDF (n={n_calls}, p={p_success_call})")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_binomial_cdf.svg', format='svg', bbox_inches='tight')
```
CDF مقدار P(X ≤ k)، احتمال تجمعی k یا کمتر تماس موفق را نشان می‌دهد. می‌بینیم P(X ≤ 3) ≈ 0.65 (مطابق محاسبه قبلی) و تا k = 8 تقریباً همه احتمال تجمع یافته (نزدیک ۱.۰).
```{admonition} پاسخ
:class: dropdown

**بله، این برای Binomial مناسب است.** همه الزامات را برآورده می‌کند: (1) تعداد ثابت آزمایش (n = 12 پرتاب)، (2) هر آزمایش مستقل است، (3) فقط دو پیامد در هر آزمایش (آوردن ۶ در مقابل نیاوردن ۶)، و (4) احتمال موفقیت ثابت (p = 1/6 برای هر پرتاب). پارامترها n = 12 و p = 1/6 خواهند بود.
```
2. برای توزیع Binomial با n = 8 و p = 0.25، امید ریاضی (میانگین) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**E[X] = np = 8 × 0.25 = 2** — امید ریاضی تعداد موفقیت‌ها در ۸ آزمایش برابر ۲ است.
```
3. یک بازیکن بسکتبال ۷۰٪ نرخ موفقیت در پرتاب آزاد دارد. ۱۵ پرتاب آزاد او را تماشا می‌کنید. آیا این سناریو با فرضیات توزیع Binomial سازگار است؟
```{admonition} پاسخ
:class: dropdown

**بله، این با توزیع Binomial سازگار است** با n = 15 و p = 0.7. هر پرتاب آزاد مستقل است، دو پیامد دارد (گل یا خطا) و احتمال موفقیت برای هر تلاش در ۰.۷ ثابت می‌ماند. می‌توانیم از این برای محاسبه احتمالاتی مثل «احتمال حداقل ۱۲ گل از ۱۵ چقدر است؟» استفاده کنیم.
```
4. برای توزیع Binomial(n=20, p=0.3)، واریانس چقدر است؟
```{admonition} پاسخ
:class: dropdown

**Var(X) = np(1-p) = 20 × 0.3 × 0.7 = 4.2**

با فرمول واریانس توزیع‌های Binomial.
```
5. درست یا نادرست: در توزیع Binomial، هر آزمایش باید همان احتمال موفقیت را داشته باشد.
```{admonition} پاسخ
:class: dropdown

**درست** — توزیع Binomial نیاز دارد:
1. تعداد ثابت آزمایش‌های مستقل (n)
2. هر آزمایش فقط دو پیامد (موفقیت/شکست)
3. **احتمال موفقیت ثابت (p) در همه آزمایش‌ها**
4. آزمایش‌ها مستقل باشند

اگر احتمال موفقیت از آزمایشی به آزمایش دیگر تغییر کند، Binomial اعمال نمی‌شود.
```
+++
## ۳. توزیع Geometric

توزیع Geometric تعداد آزمایش‌های مستقل Bernoulli لازم برای رسیدن به *اولین* موفقیت را مدل می‌کند.

**مثال ملموس**

پرتاب‌های آزاد می‌زنید تا اولین سبد را بزنید. هر پرتاب ۰.۴ احتمال موفقیت دارد. چند پرتاب طول می‌کشد تا اولین سبد را بزنید؟

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = شماره آزمایشی که اولین موفقیت در آن رخ می‌دهد
- $X$ می‌تواند مقادیر 1, 2, 3, ... بگیرد (اولین پرتاب، دومین پرتاب و غیره)

احتمال‌ها:
- $P(X = 1)$ = موفقیت در اولین پرتاب = 0.4
- $P(X = 2)$ = خطا در اول، موفقیت در دوم = $(1-0.4) \times 0.4 = 0.24$
- $P(X = 3)$ = خطا در دو اول، موفقیت در سوم = $(1-0.4)^2 \times 0.4 = 0.144$

**PMF هندسی**

برای آزمایش‌ها با احتمال موفقیت $p$:
$$ P(X=k) = (1-p)^{k-1} p $$
for $k = 1, 2, 3, \dots$

یعنی $k-1$ شکست متوالی و سپس یک موفقیت.

بیایید برای مثال ما (p=0.4) تأیید کنیم:
- $P(X=2) = (0.6)^1 (0.4) = 0.24$ ✓

:::{admonition} چرا این فرمول کار می‌کند
:class: note

فرمول $(1-p)^{k-1} p$ ساختار شهودی دارد:

- **$(1-p)^{k-1}$**: احتمال $k-1$ شکست متوالی
- **$p$**: احتمال موفقیت در آزمایش $k$-ام
- **ضرب آن‌ها**: چون آزمایش‌ها مستقل‌اند، احتمال‌ها را ضرب می‌کنیم

**مثال:** برای $P(X=3)$ با $p=0.4$:
- دو آزمایش اول باید شکست بخورند: $(0.6) \times (0.6) = 0.36$
- آزمایش سوم باید موفق باشد: $0.4$
- ترکیب: $0.36 \times 0.4 = 0.144$

به همین دلیل فرمول «آزمایش تا اولین موفقیت» را می‌گیرد — همه آزمایش‌های قبلی باید شکست بخورند و آزمایش نهایی موفق باشد.
:::

**مثال مصور:** این‌طور توزیع هندسی با $p=0.4$ (مثال پرتاب آزاد ما) کار می‌کند:
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_geometric_formula_breakdown.svg'):
    os.remove('ch07_geometric_formula_breakdown.svg')

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --- Parameters ---
p = 0.4
q = 1 - p  # 0.6

fig, ax = plt.subplots(figsize=(14, 10), constrained_layout=True)
ax.set_axis_off()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# ---------------- helpers ----------------
def rounded_box(ax, xy, w, h, fc, ec, lw=2, pad=0.012, r=0.02, z=3):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={pad},rounding_size={r}",
        transform=ax.transAxes,
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z
    )
    ax.add_patch(patch)
    return patch

def draw_sequence(ax, cx, cy, label, k, prob_val):
    w, h = 0.16, 0.07
    rounded_box(ax, (cx - w/2, cy - h/2), w, h,
                fc="lightblue", ec="steelblue", lw=2.2, r=0.02)

    ax.text(cx, cy, label, transform=ax.transAxes,
            ha="center", va="center",
            fontsize=20, weight="bold", family="monospace", zorder=4)

    # Formula showing the calculation
    if k == 1:
        formula_text = rf"${p:.1f}$"
    else:
        formula_text = rf"${q:.1f}^{{{k-1}}} \times {p:.1f}$"

    ax.text(cx, cy - 0.062, formula_text,
            transform=ax.transAxes, ha="center", va="top",
            fontsize=20, zorder=4)

    ax.text(cx, cy - 0.095, rf"$= {prob_val:.4f}$",
            transform=ax.transAxes, ha="center", va="top",
            fontsize=20, weight="bold", zorder=4)

    return (cx - w/2, cy - h/2, cx + w/2, cy + h/2)

# ---------------- layout ----------------
ax.text(0.5, 0.96, rf"Geometric Distribution: Trials Until First Success ($p={p}$)",
        transform=ax.transAxes, ha="center", va="top",
        fontsize=24, weight="bold", zorder=4)

# Draw sequences at different positions
sequences = [
    ("S", 1, 0.16, 0.86),           # Success on trial 1
    ("FS", 2, 0.34, 0.86),          # Fail then Success
    ("FFS", 3, 0.52, 0.86),         # Fail Fail then Success
    ("FFFS", 4, 0.70, 0.86),        # Fail Fail Fail then Success
    ("FFFFS", 5, 0.88, 0.86),       # Fail Fail Fail Fail then Success
]

seq_boxes = {}
for label, k, x, y in sequences:
    prob_val = (q ** (k-1)) * p
    seq_boxes[label] = draw_sequence(ax, x, y, label, k, prob_val)

# Explanation box
expl_w, expl_h = 0.70, 0.11
expl_xy = (0.5 - expl_w/2, 0.66 - expl_h/2)
rounded_box(ax, expl_xy, expl_w, expl_h,
            fc="lightyellow", ec="orange", lw=2.2, r=0.02)

ax.text(0.5, 0.695, "Each sequence shows trials until first success",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, weight="bold", zorder=4)
ax.text(0.5, 0.635, "Probability decreases exponentially with more failures",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=22, style="italic", zorder=4)

# Formula block
ax.text(0.5, 0.545, "General Formula:", transform=ax.transAxes,
        ha="center", va="center", fontsize=20, weight="bold", zorder=4)

ax.text(0.5, 0.495, r"$P(X=k) = (1-p)^{k-1} \cdot p$",
        transform=ax.transAxes, ha="center", va="center", fontsize=20, zorder=4)

ax.text(0.5, 0.45, r"$P(X=k) = (\text{fail})^{k-1} \times \text{succeed}$",
        transform=ax.transAxes, ha="center", va="center", fontsize=18, zorder=4)

ax.text(0.5, 0.405, "where $k$ is the trial number of first success",
        transform=ax.transAxes, ha="center", va="center", fontsize=16, zorder=4)

# Key insight box
key_w, key_h = 0.68, 0.15
key_xy = (0.5 - key_w/2, 0.25 - key_h/2)
rounded_box(ax, key_xy, key_w, key_h,
            fc="lightgreen", ec="green", lw=2.2, r=0.02)

ax.text(0.5, 0.305, "Key Insight:",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, weight="bold", zorder=4)
ax.text(0.5, 0.260, rf"All trials before the $k$-th must fail: $(1-p)^{{k-1}}$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=20, zorder=4)
ax.text(0.5, 0.220, rf"The $k$-th trial must succeed: $p$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=20, zorder=4)
ax.text(0.5, 0.185, r"(Each trial is independent)",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=16, style="italic", zorder=4)

# ---- Callouts ----
# Arrow pointing to decreasing probabilities
x0, y0, x1, y1 = seq_boxes["S"]
ax.annotate("Most likely:\nsucceed early",
            xy=(x0, y1), xycoords=ax.transAxes,
            xytext=(0.05, 0.66), textcoords=ax.transAxes,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.3",
                            lw=2.5, color="green",
                            shrinkA=6, shrinkB=8),
            fontsize=18, color="green", weight="bold",
            ha="center", va="center", zorder=5)

# Arrow pointing to later trials
x0, y0, x1, y1 = seq_boxes["FFFFS"]
ax.annotate("Less likely:\nmany failures",
            xy=(x1, y1), xycoords=ax.transAxes,
            xytext=(0.95, 0.66), textcoords=ax.transAxes,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.3",
                            lw=2.5, color="red",
                            shrinkA=6, shrinkB=8),
            fontsize=18, color="red", weight="bold",
            ha="center", va="center", zorder=5)

# Bottom explanation
ax.text(0.5, 0.10, "Example: P(X=3) means getting your first success on the 3rd trial.",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=19, style="italic", zorder=4)
ax.text(0.5, 0.068, "This requires exactly 2 failures followed by 1 success:",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=19, style="italic", zorder=4)
ax.text(0.5, 0.036, r"$P(X=3) = (0.6)^2 \times 0.4 = 0.36 \times 0.4 = 0.144$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=19, zorder=4)

plt.savefig('ch07_geometric_formula_breakdown.svg', format='svg', bbox_inches='tight')
plt.show()
```
نمودار نشان می‌دهد توزیع هندسی چگونه کار می‌کند: هر شکست اضافه قبل از موفقیت پیامد را کم‌محتمل‌تر می‌کند. احتمال به‌صورت نمایی کاهش می‌یابد — توجه کنید P(X=1) = 0.4000 بسیار بزرگ‌تر از P(X=5) = 0.0518 است.

**ویژگی‌های کلیدی**

- **سناریوها**: پرتاب سکه تا اولین شیر، درخواست شغل تا اولین پیشنهاد، تلاش برای قبولی در آزمون، ضربه تا اولین hit
- **پارامتر**: $p$، احتمال موفقیت در هر آزمایش ($0 < p \le 1$)
- **متغیر تصادفی**: $X \in \{1, 2, 3, ...\}$

**میانگین:** $E[X] = \frac{1}{p}$

**واریانس:** $Var(X) = \frac{1-p}{p^2}$

**انحراف معیار:** $SD(X) = \frac{\sqrt{1-p}}{p}$

**ارتباط با توزیع‌های دیگر:** توزیع Geometric از آزمایش‌های مستقل **Bernoulli** ساخته شده و حالت خاص **توزیع Negative Binomial** با $r=1$ است (منتظر فقط یک موفقیت به‌جای $r$ موفقیت).

:::{admonition} یادداشت
:class: note

`scipy.stats.geom` همان تعریف «شماره آزمایش» ما را استفاده می‌کند، جایی که $k \in \{1, 2, 3, ...\}$ آزمایشی را نشان می‌دهد که اولین موفقیت در آن رخ می‌دهد. PMF برابر $P(X=k) = (1-p)^{k-1}p$ برای $k \geq 1$ است.
:::

**مصورسازی توزیع**

بیایید توزیع Geometric با $p = 0.4$ را مصور کنیم (مثال پرتاب آزاد ما):
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_geometric_pmf_generic.svg'):
    os.remove('ch07_geometric_pmf_generic.svg')

# Create Geometric distribution for visualization (p=0.4)
p_viz = 0.4
geom_viz = stats.geom(p=p_viz)

# Calculate mean and std (adjusted for trial number definition)
mean_viz = 1 / p_viz
std_viz = np.sqrt((1 - p_viz) / p_viz**2)

# Plotting the PMF
k_values_viz = np.arange(1, 11)
pmf_values_viz = geom_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.1f}, {mean_viz + std_viz:.1f}]')

plt.title(f"Geometric PMF (p={p_viz})")
plt.xlabel("Trial Number (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values_viz)
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_geometric_pmf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
PMF احتمالات نزولی نمایی نشان می‌دهد — محتمل‌ترین موفقیت در چند آزمایش اول است. ناحیه سایه‌دار میانگین ± ۱ انحراف معیار را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_geometric_cdf_generic.svg'):
    os.remove('ch07_geometric_cdf_generic.svg')

# Plotting the CDF
cdf_values_viz = geom_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

plt.title(f"Geometric CDF (p={p_viz})")
plt.xlabel("Trial Number (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values_viz)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_geometric_cdf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
CDF مقدار P(X ≤ k) را نشان می‌دهد که با افزایش k به ۱ نزدیک می‌شود (در نهایت موفق می‌شوید). خط چین قرمز میانگین را نشان می‌دهد.

:::{admonition} مثال: آزمون گواهینامه با p = 0.6
:class: tip

مدل‌سازی تعداد تلاش‌های لازم برای قبولی در آزمون گواهینامه با احتمال قبولی ۰.۶.

از [`scipy.stats.geom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geom.html) برای بررسی احتمال‌ها و محاسبه امید ریاضی استفاده می‌کنیم. به‌خاطر داشته باشید تعریف scipy تعداد شکست‌ها قبل از اولین موفقیت را می‌شمارد، پس بین دو تفسیر جابه‌جا می‌شویم.

**تنظیم توزیع:**

توزیع هندسی با احتمال موفقیت ۰.۶ (نرخ قبولی ۶۰٪) می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.geom
p_pass = 0.6
geom_rv = stats.geom(p=p_pass)
```
**محاسبه احتمال‌های مشخص با PMF:**

احتمال قبولی برای اولین بار در تلاش سوم چقدر است؟ یعنی دو تلاش اول ناموفق و قبولی در سوم:
```{code-cell} ipython3
# PMF: Probability that the first success occurs on trial k (k=1, 2, ...)
k_trial = 3 # Third attempt
print(f"P(First pass on attempt {k_trial}): {geom_rv.pmf(k_trial):.4f}")
```
۹.۶٪ احتمال قبولی دقیقاً در تلاش سوم وجود دارد. این برابر (1-0.6)² × 0.6 = 0.4² × 0.6 = 0.096 محاسبه می‌شود.

**محاسبه احتمال‌های تجمعی با CDF:**

احتمال قبولی در ۲ تلاش اول چقدر است؟
```{code-cell} ipython3
# CDF: Probability that the first success occurs on or before trial k
k_or_before = 2
print(f"P(First pass on or before attempt {k_or_before}): {geom_rv.cdf(k_or_before):.4f}")
print(f"P(First pass takes more than {k_or_before} attempts): {1 - geom_rv.cdf(k_or_before):.4f}")
print(f"P(First pass takes more than {k_or_before} attempts) (using sf): {geom_rv.sf(k_or_before):.4f}")
```
۸۴٪ احتمال قبولی در ۲ تلاش وجود دارد، یعنی فقط ۱۶٪ احتمال نیاز به بیش از ۲ تلاش.

**محاسبه میانگین و واریانس:**

بیایید تعداد مورد انتظار تلاش‌های لازم را بیابیم:
```{code-cell} ipython3
# Mean and Variance
mean_trials = geom_rv.mean()
var_trials = geom_rv.var()
print(f"Mean number of attempts until first pass: {mean_trials:.2f}")
print(f"Variance of number of attempts: {var_trials:.2f}")
```
به‌طور میانگین ۱.۶۷ تلاش انتظار می‌رود (مطابق فرمول 1/p = 1/0.6). واریانس نسبتاً کم نشان می‌دهد بیشتر افراد در چند تلاش اول قبول می‌شوند.

**تولید نمونه‌های تصادفی:**

می‌توانیم شبیه‌سازی کنیم بسیاری از دانشجویان تا قبولی مکرراً آزمون می‌دهند:
```{code-cell} ipython3
# Generate random samples (trial numbers until first success)
n_simulations = 1000
samples_trials = geom_rv.rvs(size=n_simulations)
# print(f"\nSimulated number of attempts until first pass ({n_simulations} simulations): {samples_trials[:20]}...")
```
این ۱۰۰۰ نمونه تغییرپذیری طبیعی تعداد تلاش‌های مختلف دانشجویان را نشان می‌دهد.

**مصورسازی PMF:**

بیایید احتمال قبولی در هر شماره تلاش را مصور کنیم (۱۰ تلاش اول):
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_geometric_pmf.svg'):
    os.remove('ch07_geometric_pmf.svg')
```
```{code-cell} ipython3
# Plotting the PMF (using trial number k=1, 2, ...)
k_values_trials = np.arange(1, 11) # Plot first 10 trials
pmf_values = geom_rv.pmf(k_values_trials)

plt.figure(figsize=(8, 3.5))
plt.bar(k_values_trials, pmf_values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Geometric PMF (p={p_pass})")
plt.xlabel("Trial Number (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values_trials)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_geometric_pmf.svg', format='svg', bbox_inches='tight')
```
PMF احتمالات نزولی نمایی نشان می‌دهد — محتمل‌ترین قبولی در تلاش اول (۶۰٪)، سپس دوم (۲۴٪) و الی آخر. این کاهش نمایی «بی‌حافظه» منحصربه‌فرد توزیع Geometric است. میله‌ها پیشرونده کوچک‌تر می‌شوند و تا تلاش ۵ یا ۶ احتمال بسیار کم است.

**مصورسازی CDF:**

توزیع تجمعی احتمال قبولی تا یک تلاش مشخص را نشان می‌دهد:
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_geometric_cdf.svg'):
    os.remove('ch07_geometric_cdf.svg')
```
```{code-cell} ipython3
# Plotting the CDF (using trial number k=1, 2, ...)
cdf_values = geom_rv.cdf(k_values_trials)

plt.figure(figsize=(8, 3.5))
plt.step(k_values_trials, cdf_values, where='post', color='darkgreen', linewidth=2)
plt.title(f"Geometric CDF (p={p_pass})")
plt.xlabel("Trial Number (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values_trials)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_geometric_cdf.svg', format='svg', bbox_inches='tight')
```
CDF مقدار P(X ≤ k) را نشان می‌دهد که با افزایش شماره تلاش سریع به ۱ نزدیک می‌شود. تا تلاش ۲، ۸۴٪ احتمال قبولی وجود دارد و تا تلاش ۵ بیش از ۹۹٪. این تأیید می‌کند با p = 0.6 بیشتر افراد در چند تلاش اول قبول می‌شوند.

:::

**سؤالات مرور سریع**

1. سکه را تا اولین شیر پرتاب می‌کنید. کدام توزیع این را مدل می‌کند و پارامتر چیست؟
```{admonition} پاسخ
:class: dropdown

**توزیع Geometric با p = 0.5** — شمارش آزمایش‌ها تا اولین موفقیت، هر آزمایش احتمال موفقیت p = 0.5 دارد.
```
2. برای توزیع Geometric با p = 0.25، امید ریاضی (میانگین) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**E[X] = 1/p = 1/0.25 = 4** — امید ریاضی تعداد آزمایش‌ها تا اولین موفقیت.
```
3. با پشتیبانی تماس می‌گیرید و هر بار ۲۰٪ شانس وصل شدن دارید. با Geometric یا Binomial مدل کنید؟
```{admonition} پاسخ
:class: dropdown

**توزیع Geometric** — منتظر *اولین* موفقیت (وصل شدن) هستید، نه شمارش موفقیت‌ها در تعداد ثابت تماس. Geometric «چند تلاش تا موفقیت» را با p = 0.20 مدل می‌کند.

Binomial وقتی اعمال می‌شود که تعداد ثابتی تماس بگیرید و بشمارید چند تا وصل شد.
```
4. برای توزیع Geometric با p = 0.5 کدام محتمل‌تر است: موفقیت در آزمایش ۱ یا ۳؟
```{admonition} پاسخ
:class: dropdown

**آزمایش ۱ محتمل‌تر است** — PMF هندسی با k به‌صورت نمایی کاهش می‌یابد، پس P(X=1) > P(X=3).

به‌طور مشخص: P(X=1) = 0.5، در حالی که P(X=3) = (0.5)³ = 0.125
```
5. برای توزیع Geometric، چرا واریانس برابر (1-p)/p² است؟
```{admonition} پاسخ
:class: dropdown

فرمول واریانس Var(X) = (1-p)/p² افزایش عدم‌قطعیت با کاهش p را منعکس می‌کند:

- وقتی p بالاست (موفقیت آسان): واریانس کم است (قابل پیش‌بینی‌تر)
- وقتی p پایین است (موفقیت سخت): واریانس بالاست (ممکن است تلاش‌های زیادی لازم باشد یا زود خوش‌شانس شوید)

مثلاً:
- p = 0.5: Var(X) = 0.5/0.25 = 2
- p = 0.1: Var(X) = 0.9/0.01 = 90 (بسیار متغیرتر!)
```
+++
## ۴. توزیع Negative Binomial

توزیع Negative Binomial تعداد آزمایش‌های مستقل Bernoulli لازم برای دستیابی به *تعداد ثابتی* از موفقیت‌ها ($r$) را مدل می‌کند. توزیع Geometric را تعمیم می‌دهد (جایی که $r=1$).

:::{admonition} چرا «Negative Binomial»؟
:class: note

نام از ارتباط ریاضی با قضیه دوجمله‌ای با توان‌های منفی می‌آید، نه به‌خاطر منفی بودن چیزی! نام شهودی‌تر می‌تواند «دوجمله‌ای معکوس» باشد:

- **Binomial**: تعداد آزمایش‌ها را ثابت کن → موفقیت‌ها را بشمار
- **Negative Binomial**: تعداد موفقیت‌ها را ثابت کن → آزمایش‌ها را بشمار

مثل توزیع دوجمله‌ای «برعکس» فکر کنید.
:::

**مثال ملموس**

تاس می‌اندازید تا ۳ عدد شش بگیرید. هر پرتاب p = 1/6 احتمال آوردن شش دارد. چند پرتاب طول می‌کشد تا سومین شش را بگیرید؟

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = شماره آزمایشی که سومین شش در آن ظاهر می‌شود
- $X$ می‌تواند مقادیر 3, 4, 5, ... بگیرد (حداقل ۳ پرتاب، ممکن است بیشتر)

احتمال‌ها:
- $P(X = 3)$ = هر سه پرتاب شش باشند
- $P(X = 4)$ = ۲ شش در ۳ پرتاب اول، سپس شش در پرتاب ۴
- و الی آخر...

**PMF دوجمله‌ای منفی**

برای آزمایش‌ها با احتمال موفقیت $p$ و هدف $r$ موفقیت:
$$ P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r} $$
for $k = r, r+1, r+2, \dots$

**درک فرمول:** یعنی $r-1$ موفقیت در $k-1$ آزمایش اول، و آزمایش $k$-ام موفقیت $r$-ام است.

:::{admonition} به‌خاطر سپردن r در برابر k
:class: tip

**r** را «**r**equired» یا «**r**epeat» بدانید — تعداد ثابت هدف موفقیت‌هایی که نیاز دارید.

**k** را «it too**k** this many trials» بدانید — متغیر تعداد کل آزمایش‌ها.

در مثال تاس:
- **r = 3** (به **r** شش نیاز داریم — ثابت است)
- **k = ?** (ممکن است **k** = 3, 4, 5, ... آزمایش طول بکشد — متغیر است)

نکته کلیدی: **r ثابت است، k تصادفی است**
:::

:::{admonition} چرا این فرمول کار می‌کند
:class: note

برای شهود، بیایید ببینیم فرمول چگونه به سه بخش تقسیم می‌شود:

- **$\binom{k-1}{r-1}$**: انتخاب کدام $r-1$ از $k-1$ آزمایش اول موفقیت باشند (آزمایش $k$-ام باید موفقیت باشد، پس فقط موقعیت $r-1$ موفقیت را انتخاب می‌کنیم)
- **$p^r$**: احتمال $r$ موفقیت
- **$(1-p)^{k-r}$**: احتمال $k-r$ شکست

**مثال شهودی:** برای $r=3$ موفقیت در $k=5$ آزمایش با $p=0.4$:
- دقیقاً ۲ موفقیت در ۴ آزمایش اول لازم است: $\binom{4}{2} = 6$ روش (مثلاً SSFF، SFSF، SFFS، FSSF، FSFS، FFSS)
- هر چیدمان برای ۴ آزمایش اول احتمال $(0.4)^2 (0.6)^2$ دارد
- آزمایش ۵ باید موفق باشد: $0.4$
- **ترکیب:** $P(X=5) = \binom{4}{2} \times (0.4)^3 \times (0.6)^2 = 6 \times (0.4)^3 \times (0.6)^2 = 0.2304$

این نشان می‌دهد فرمول $P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$ هر سه بخش را چگونه ترکیب می‌کند.

ضریب دوجمله‌ای تضمین می‌کند همه چیدمان‌هایی را می‌شماریم که موفقیت $r$-ام دقیقاً در آزمایش $k$ رخ می‌دهد. (این را در نمودار زیر به‌صورت مصور می‌بینیم.)

**اکنون بیایید فرمول را به‌صورت مکانیکی روی مثال تاس اعمال کنیم** با پارامترهای مختلف: برای $P(X=4)$ (احتمال دقیقاً ۴ پرتاب برای سومین شش) با $r=3$ شش و $p=1/6$:

جایگذاری $k=4$، $r=3$، $p=1/6$ در فرمول:

\begin{align}
P(X=k) &= \binom{k-1}{r-1} p^r (1-p)^{k-r} \\
P(X=4) &= \binom{4-1}{3-1}(1/6)^3(5/6)^{4-3} \\
&= \binom{3}{2}(1/6)^3(5/6)^1 \\
&= 3 \times \frac{1}{216} \times \frac{5}{6} \\
&= \frac{15}{1296} \\
&\approx 0.0116
\end{align}
:::

**تجزیه مصور:** نمودار زیر نشان می‌دهد فرمول دوجمله‌ای منفی چگونه همه دنباله‌های ممکن را می‌شمارد و احتمال‌هایشان را ترکیب می‌کند:
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_negative_binomial_formula_breakdown.svg'):
    os.remove('ch07_negative_binomial_formula_breakdown.svg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- Settings ---
BOX_PAD = 0.01  # single, consistent pad for every rounded box (fixes uneven visible gaps)

# Create figure for formula breakdown
fig, ax = plt.subplots(figsize=(16, 16))

# Make axes fill the whole figure so "axes coords" behave predictably
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define all CONTENT heights (actual elements)
title_height = 0.03
subtitle_height = 0.025
param_box_height = 0.04
seq_box_height = 0.05
count_box_height = 0.08
prob_box_height = 0.15
result_box_height = 0.12
key_insight_text_height = 0.025
key_explain_text_height = 0.025
formula_box_height = 0.08

# Calculate total content height
total_content_height = (
    title_height +
    subtitle_height +
    param_box_height +
    seq_box_height * 2 +  # Two rows of sequence boxes
    count_box_height +
    prob_box_height +
    result_box_height +
    key_insight_text_height +
    key_explain_text_height +
    formula_box_height
)

# Calculate available space for gaps
top_margin = 0.02
bottom_margin = 0.03
usable_height = 1.0 - top_margin - bottom_margin
whitespace = usable_height - total_content_height

# Number of gaps between sections
num_gaps = 10

# Calculate uniform gap size
gap = whitespace / num_gaps

def add_box(x, y, w, h, edge, face, lw, z=1):
    """Consistent rounded box with a single pad value."""
    patch = mpatches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={BOX_PAD}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
        zorder=z
    )
    ax.add_patch(patch)
    return patch

# Build layout from top down with calculated gaps
current_y = 1.0 - top_margin

# Title
ax.text(0.5, current_y, "Negative Binomial Formula Breakdown",
        transform=ax.transAxes, ha="center", va="top",
        fontsize=26, weight="bold")
current_y -= title_height + gap

# Subtitle
ax.text(0.5, current_y, r"Example: $r=3$ successes, $k=5$ total trials, $p=0.4$",
        transform=ax.transAxes, ha="center", va="top",
        fontsize=19, style="italic")
current_y -= subtitle_height + gap

# Parameters box
param_box_bottom = current_y - param_box_height
add_box(0.05, param_box_bottom, 0.90, param_box_height,
        edge='purple', face='lavender', lw=2, z=1)
ax.text(0.5, param_box_bottom + param_box_height/2,
        "Need exactly 2 successes in first 4 trials, then success on 5th trial  (S = Success, F = Failure)",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=16.5, weight="bold", color="purple")
current_y = param_box_bottom - gap

# Sequence boxes - First row
sequences = ["SSFF•S", "SFSF•S", "SFFS•S", "FSSF•S", "FSFS•S", "FFSS•S"]
seq_row1_bottom = current_y - seq_box_height
for i in range(3):
    x_pos = 0.055 + i * 0.31
    add_box(x_pos, seq_row1_bottom, 0.27, seq_box_height,
            edge='darkblue', face='lightblue', lw=2.5, z=2)
    ax.text(x_pos + 0.135, seq_row1_bottom + seq_box_height/2, sequences[i],
            transform=ax.transAxes, ha="center", va="center",
            fontsize=20, weight="bold", family='monospace', zorder=3)

# Sequence boxes - Second row
current_y = seq_row1_bottom - gap
seq_row2_bottom = current_y - seq_box_height
for i in range(3):
    x_pos = 0.055 + i * 0.31
    add_box(x_pos, seq_row2_bottom, 0.27, seq_box_height,
            edge='darkblue', face='lightblue', lw=2.5, z=2)
    ax.text(x_pos + 0.135, seq_row2_bottom + seq_box_height/2, sequences[i+3],
            transform=ax.transAxes, ha="center", va="center",
            fontsize=20, weight="bold", family='monospace', zorder=3)
current_y = seq_row2_bottom - gap

# Counting explanation box
count_box_bottom = current_y - count_box_height
add_box(0.10, count_box_bottom, 0.80, count_box_height,
        edge='darkorange', face='lightyellow', lw=2.5, z=1)
ax.text(0.5, count_box_bottom + count_box_height * 0.70, r"Count all sequences:",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, weight="bold", color='darkorange', zorder=4)
ax.text(0.5, count_box_bottom + count_box_height * 0.30,
        r"6 ways to arrange 2 successes in first 4 trials = $\binom{4}{2} = \binom{k-1}{r-1} = 6$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=19, weight="bold", color='#CC6600', zorder=4)
current_y = count_box_bottom - gap

# Probability calculation box
prob_box_bottom = current_y - prob_box_height
add_box(0.08, prob_box_bottom, 0.84, prob_box_height,
        edge='darkgreen', face='lightgreen', lw=2.5, z=1)
ax.text(0.5, prob_box_bottom + prob_box_height * 0.85,
        "Each sequence has the same probability:",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, weight="bold", color='darkgreen', zorder=4)
ax.text(0.5, prob_box_bottom + prob_box_height * 0.62,
        r"First 4 trials (2 successes AND 2 failures): $(0.4)^2 \times (0.6)^2 = 0.0576$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=17, color='darkgreen', zorder=4)
ax.text(0.5, prob_box_bottom + prob_box_height * 0.40,
        r"5th trial (must succeed): $0.4$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=17, color='darkgreen', zorder=4)
ax.text(0.5, prob_box_bottom + prob_box_height * 0.16,
        r"Total: $0.0576 \times 0.4 = 0.02304$ per sequence",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=17, style="italic", color='darkgreen', zorder=4)
current_y = prob_box_bottom - gap

# Final result box
result_box_bottom = current_y - result_box_height
add_box(0.10, result_box_bottom, 0.80, result_box_height,
        edge='red', face='mistyrose', lw=3, z=1)
ax.text(0.5, result_box_bottom + result_box_height * 0.83,
        r"Multiply: count $\times$ probability (sequences are mutually exclusive)",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=17, style="italic", color='darkred', zorder=4)
ax.text(0.5, result_box_bottom + result_box_height * 0.50,
        r"$P(X=5) = 6 \times 0.02304 = 0.1382$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=21, weight="bold", color='red', zorder=4)
ax.text(0.5, result_box_bottom + result_box_height * 0.17,
        r"$= \binom{4}{2} \times (0.4)^3 \times (0.6)^2 = 0.1382$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=19, color='red', zorder=4)
current_y = result_box_bottom - gap

# Key insight text
key_insight_y = current_y - key_insight_text_height/2
ax.text(0.5, key_insight_y,
        "Key Insight: Last trial MUST be the r-th success!",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, style="italic", weight="bold", color='purple', zorder=4)
current_y -= key_insight_text_height + gap

# Explanation text
key_explain_y = current_y - key_explain_text_height/2
ax.text(0.5, key_explain_y,
        r"So we arrange $(r-1)$ successes in the first $(k-1)$ trials, then guarantee success on trial $k$.",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=16, style="italic", zorder=4)
current_y -= key_explain_text_height + gap

# General formula box
formula_box_bottom = current_y - formula_box_height
add_box(0.08, formula_box_bottom, 0.84, formula_box_height,
        edge='darkblue', face='aliceblue', lw=2.5, z=1)
ax.text(0.5, formula_box_bottom + formula_box_height * 0.65,
        r"General Formula:  $P(X = k) = \binom{k-1}{r-1} \times p^r \times (1-p)^{k-r}$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=18, weight="bold", color='darkblue', zorder=4)
ax.text(0.5, formula_box_bottom + formula_box_height * 0.25,
        r"where $X$ = trial number of $r$-th success, and $k \geq r$",
        transform=ax.transAxes, ha="center", va="center",
        fontsize=15, style="italic", color='darkblue', zorder=4)

plt.savefig('ch07_negative_binomial_formula_breakdown.svg', format='svg', bbox_inches='tight', pad_inches=0.25)
plt.show()
```
نمودار نشان می‌دهد فرمول دوجمله‌ای منفی چگونه کار می‌کند: دقیقاً $r-1$ موفقیت در $k-1$ آزمایش اول لازم است (که می‌تواند به $\binom{k-1}{r-1}$ روش چیده شود)، سپس آزمایش $k$-ام باید موفقیت باشد. هر یک از ۶ دنباله نشان‌داده‌شده احتمال یکسان دارد و در تعداد دنباله‌ها ضرب می‌کنیم تا احتمال کل به‌دست آید.

اکنون که فرمول و مصورسازی آن را فهمیدیم، بیایید ویژگی‌های اساسی توزیع دوجمله‌ای منفی را خلاصه کنیم:

**ویژگی‌های کلیدی**

- **سناریوها**: پرتاب سکه تا r شیر، بازرسی محصول تا یافتن r معیوب، مصاحبه تا r استخدام
- **پارامترها**:
    - $r$: تعداد هدف موفقیت‌ها ($r \ge 1$)
    - $p$: احتمال موفقیت در هر آزمایش ($0 < p \le 1$)
- **متغیر تصادفی**: $X \in \{r, r+1, r+2, ...\}$

**میانگین:** $E[X] = \frac{r}{p}$

**واریانس:** $Var(X) = \frac{r(1-p)}{p^2}$

**انحراف معیار:** $SD(X) = \frac{\sqrt{r(1-p)}}{p}$

**مصورسازی توزیع**

بیایید مثال تاس را مصور کنیم: توزیع Negative Binomial با $r = 3$ شش و $p = 1/6$:

:::{admonition} یادداشت
:class: note

`scipy.stats.nbinom` تعداد *شکست‌ها* قبل از موفقیت $r$-ام را می‌شمارد، نه کل آزمایش‌ها. در کد از تعریف scipy استفاده می‌کنیم اما نتایج را بر حسب کل آزمایش‌ها بیان می‌کنیم.
:::
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_negative_binomial_pmf_generic.svg'):
    os.remove('ch07_negative_binomial_pmf_generic.svg')

# Create Negative Binomial distribution for our die example (r=3, p=1/6)
r_viz = 3
p_viz = 1/6
nbinom_viz = stats.nbinom(n=r_viz, p=p_viz)

# Calculate mean and std
mean_viz = r_viz / p_viz
std_viz = np.sqrt(r_viz * (1 - p_viz)) / p_viz

# Plotting the PMF
k_values_viz = np.arange(r_viz, 45)  # Total trials from r to 45 (wider range for p=1/6)
pmf_values_viz = nbinom_viz.pmf(k_values_viz - r_viz)  # Adjust for scipy

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.1f}, {mean_viz + std_viz:.1f}]')

plt.title(f"Negative Binomial PMF: Rolling Until 3 Sixes (r={r_viz}, p=1/6)")
plt.xlabel("Total Number of Trials (k)")
plt.ylabel("Probability P(X=k)")
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_negative_binomial_pmf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
PMF توزیع حول امید ریاضی r/p = 3/(1/6) = 18 آزمایش متمرکز است. P(X=4) ≈ 0.0116 محاسبه‌شده را به‌صورت میله کوچک نزدیک دم چپ در k=4 می‌بینید. ناحیه سایه‌دار میانگین ± ۱ انحراف معیار را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_negative_binomial_cdf_generic.svg'):
    os.remove('ch07_negative_binomial_cdf_generic.svg')

# Plotting the CDF
cdf_values_viz = nbinom_viz.cdf(k_values_viz - r_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

plt.title(f"Negative Binomial CDF: Rolling Until 3 Sixes (r={r_viz}, p=1/6)")
plt.xlabel("Total Number of Trials (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_negative_binomial_cdf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
CDF مقدار P(X ≤ k)، احتمال تجمعی یافتن ۳ شش در k پرتاب را نشان می‌دهد. در k=4، CDF مقدار P(X ≤ 4) = P(X=3) + P(X=4) ≈ 0.0046 + 0.0116 ≈ 0.0162 را نشان می‌دهد که احتمال تجمعی بسیار کم در دم چپ است. خط چین قرمز میانگین (۱۸ آزمایش) را نشان می‌دهد.

:::{admonition} مثال: کنترل کیفیت با r = 3, p = 0.05
:class: tip

بازرس کنترل کیفیت قطعات الکترونیکی را آزمایش می‌کند تا ۳ معیوب پیدا کند. نرخ معیوب بودن p = 0.05 است.

از [`scipy.stats.nbinom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html) برای محاسبه احتمال نیاز به تعداد مشخصی آزمایش و محاسبه امید ریاضی استفاده می‌کنیم، با در نظر گرفتن تعریف scipy در شمارش شکست‌ها.

**تنظیم توزیع:**

ابتدا شیء توزیع دوجمله‌ای منفی را با پارامترهایمان می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.nbinom
r_defective = 3
p_defective = 0.05
nbinom_rv = stats.nbinom(n=r_defective, p=p_defective)
```
**محاسبه احتمال‌های مشخص با PMF:**

احتمال اینکه دقیقاً ۸۰ قطعه را آزمایش کنیم تا ۳ معیوب پیدا کنیم چقدر است؟ به‌خاطر داشته باشید scipy *شکست‌ها* (قطعات سالم) را می‌شمارد، پس باید تبدیل کنیم:
```{code-cell} ipython3
# PMF: Probability of needing k components tested to find r defective
k_components = 80
num_good = k_components - r_defective
if num_good >= 0:
    prob_k_components = nbinom_rv.pmf(num_good)
    print(f"P(Need exactly {k_components} components to find {r_defective} defective): {prob_k_components:.4f}")
else:
    print(f"Cannot find {r_defective} defective in fewer than {r_defective} components.")
```
این احتمال نسبتاً کم است (0.0074 یا 0.74%) زیرا ۸۰ قطعه دور از امید ریاضی است.

**محاسبه احتمال‌های تجمعی با CDF:**

اگر بخواهیم احتمال یافتن ۳ قطعه معیوب در ۱۰۰ آزمایش را بدانیم چه؟
```{code-cell} ipython3
# CDF: Probability of needing k or fewer components
k_or_fewer_components = 100
num_good_max = k_or_fewer_components - r_defective
if num_good_max >= 0:
    prob_k_or_fewer = nbinom_rv.cdf(num_good_max)
    print(f"P(Need {k_or_fewer_components} or fewer components to find {r_defective} defective): {prob_k_or_fewer:.4f}")
else:
    print(f"Cannot find {r_defective} defective in fewer than {r_defective} components.")
```
۸۸.۱۷٪ احتمال داریم هر ۳ قطعه معیوب را در ۱۰۰ آزمایش اول پیدا کنیم. منطقی است زیرا ۱۰۰ به‌مراتب بالاتر از امید ریاضی است (همان‌طور که پایین می‌بینیم).

**درک پارامetrize‌سازی scipy:**

Scipy's `nbinom` تعداد قطعات *غیرمعیوب* (سالم) را قبل از یافتن r قطعه معیوب می‌شمارد. این کمی با شمارش کل قطعات آزمایش‌شده متفاوت است:
```{code-cell} ipython3
# Mean and Variance (scipy's definition: number of non-defective items)
mean_good_scipy = nbinom_rv.mean()
var_good_scipy = nbinom_rv.var()
print(f"Mean number of good components before {r_defective} defective (scipy): {mean_good_scipy:.2f}")
print(f"Variance of good components before {r_defective} defective (scipy): {var_good_scipy:.2f}")
```
Scipy می‌گوید انتظار داریم ۵۷ قطعه سالم قبل از یافتن ۳ معیوب ببینیم.

**تبدیل به کل قطعات (تفسیر ما):**

برای اهداف عملی، اغلب به *کل* تعداد قطعاتی که باید آزمایش کنیم (سالم + معیوب) اهمیت می‌دهیم. می‌توانیم این را مستقیماً با فرمول‌های $E[X] = r/p$ و $Var(X) = r(1-p)/p^2$ محاسبه کنیم:
```{code-cell} ipython3
# Mean and Variance (our definition: total components tested)
mean_components = r_defective / p_defective
var_components = r_defective * (1 - p_defective) / p_defective**2
print(f"Mean number of components to test for {r_defective} defective: {mean_components:.2f}")
print(f"Variance of number of components: {var_components:.2f}")
```
به‌طور میانگین انتظار داریم ۶۰ قطعه در کل آزمایش کنیم تا ۳ معیوب پیدا کنیم (۵۷ سالم + ۳ معیوب). توجه کنید واریانس در هر دو پارامetrize‌سازی یکسان است (1140) — فقط توزیع را با افزودن ثابت r = 3 جابه‌جا می‌کنیم.

**تولید نمونه‌های تصادفی:**

می‌توانیم فرایند بازرسی را با تولید نمونه‌های تصادفی شبیه‌سازی کنیم. هر نمونه یک «دور» کامل آزمایش قطعات تا یافتن ۳ معیوب را نشان می‌دهد:
```{code-cell} ipython3
# Generate random samples (number of good components before r defective)
n_simulations = 1000
samples_good_nb = nbinom_rv.rvs(size=n_simulations)
# Convert to total components tested (good + r defective)
samples_components_nb = samples_good_nb + r_defective
# print(f"\nSimulated components tested to find {r_defective} defective ({n_simulations} sims): {samples_components_nb[:20]}...")
```
این نمونه‌ها می‌توانند برای شبیه‌سازی Monte Carlo یا تأیید محاسبات نظری استفاده شوند.
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_negative_binomial_pmf.svg'):
    os.remove('ch07_negative_binomial_pmf.svg')
```
```{code-cell} ipython3
# Plotting the PMF (using total components tested k = r, r+1, ...)
k_values_components = np.arange(r_defective, r_defective + 150) # Plot a range
pmf_values_nb = nbinom_rv.pmf(k_values_components - r_defective) # Adjust k for scipy

plt.figure(figsize=(8, 3.5))
plt.bar(k_values_components, pmf_values_nb, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Negative Binomial PMF (r={r_defective}, p={p_defective})")
plt.xlabel("Total Number of Components Tested (k)")
plt.ylabel("Probability P(X=k)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_negative_binomial_pmf.svg', format='svg', bbox_inches='tight')
```
PMF توزیع حول r/p = 60 قطعه با تغییرپذیری قابل توجه متمرکز است. توزیع چوله به راست است، یعنی دم بلندی از احتمالات وجود دارد که ممکن است به قطعات بسیار بیشتری از میانگین نیاز داشته باشیم. توجه کنید احتمال در k=80 (که قبلاً 0.0074 محاسبه کردیم) به‌صورت میله کوچک در دم راست ظاهر می‌شود.
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_negative_binomial_cdf.svg'):
    os.remove('ch07_negative_binomial_cdf.svg')
```
```{code-cell} ipython3
# Plotting the CDF (using total components tested k = r, r+1, ...)
cdf_values_nb = nbinom_rv.cdf(k_values_components - r_defective) # Adjust k for scipy

plt.figure(figsize=(8, 3.5))
plt.step(k_values_components, cdf_values_nb, where='post', color='darkgreen', linewidth=2)
plt.title(f"Negative Binomial CDF (r={r_defective}, p={p_defective})")
plt.xlabel("Total Number of Components Tested (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_negative_binomial_cdf.svg', format='svg', bbox_inches='tight')
```
CDF مقدار P(X ≤ k)، احتمال تجمعی یافتن ۳ مورد معیوب در k آزمایش را نشان می‌دهد. شکل منحنی S مشخصه CDFهاست. می‌بینیم تا k=100 آزمایش، CDF تقریباً به ۰.۸۸ می‌رسد (مطابق محاسبه ۸۸.۱۷٪). CDF در حدود k=53 از ۰.۵ عبور می‌کند، یعنی ۵۰٪ احتمال داریم ۵۳ یا کمتر آزمایش برای یافتن هر ۳ قطعه معیوب لازم باشد.

:::

**سؤالات مرور سریع**

1. سکه منصفانه را تا ۵ شیر پرتاب می‌کنید. کدام توزیع این را مدل می‌کند و پارامترها چیست؟
```{admonition} پاسخ
:class: dropdown

**Negative Binomial با r = 5, p = 0.5** — شمارش آزمایش‌ها تا رسیدن به r موفقیت، هر آزمایش p = 0.5 دارد.
```
2. برای توزیع Negative Binomial با r = 4 و p = 0.5، امید ریاضی (میانگین) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**E[X] = r/p = 4/0.5 = 8** — امید ریاضی تعداد آزمایش‌ها برای ۴ موفقیت.
```
3. بازیکن بسکتبال تا ۱۰ پرتاب موفق آزاد تمرین می‌کند. هر پرتاب ۷۰٪ نرخ موفقیت دارد. کدام توزیع و چرا؟
```{admonition} پاسخ
:class: dropdown

**Negative Binomial با r = 10, p = 0.7** — منتظر تعداد ثابتی موفقیت (r = 10) هستیم، نه فقط اولین موفقیت. هر آزمایش (پرتاب) مستقل با احتمال ثابت p = 0.7 است.

این Geometric *نیست* زیرا به ۱۰ موفقیت نیاز داریم، نه فقط ۱.
```
4. Negative Binomial چگونه به توزیع Geometric مرتبط است؟
```{admonition} پاسخ
:class: dropdown

**Geometric حالت خاص با r = 1 است** — Negative Binomial با r=1 با Geometric یکسان است.

- Geometric: منتظر اولین موفقیت
- Negative Binomial: منتظر موفقیت r-ام (r ≥ 1)
```
5. برای Negative Binomial، چرا واریانس r(1-p)/p² است؟
```{admonition} پاسخ
:class: dropdown

واریانس r(1-p)/p² با r و عدم‌قطعیت رشد می‌کند:

- **با r افزایش می‌یابد**: منتظر موفقیت‌های بیشتر یعنی آزمایش‌های بیشتر و تغییرپذیری بیشتر
- **با کاهش p افزایش می‌یابد**: احتمال موفقیت پایین‌تر یعنی عدم‌قطعیت بیشتر در زمان رسیدن به r موفقیت

مثلاً:
- r=1, p=0.5: Var = 1×0.5/0.25 = 2
- r=5, p=0.5: Var = 5×0.5/0.25 = 10 (با نیاز به موفقیت‌های بیشتر متغیرتر)
- r=5, p=0.2: Var = 5×0.8/0.04 = 100 (با p پایین بسیار متغیرتر!)
```
+++
## ۵. توزیع Poisson

توزیع Poisson تعداد رویدادهای رخ‌داده در بازه ثابتی از زمان یا فضا را مدل می‌کند وقتی رویدادها مستقل و با نرخ میانگین ثابت رخ می‌دهند.

**مثال ملموس**

به‌طور میانگین ۴ تماس مشتری در ساعت دریافت می‌کنید. در ساعت بعد چند تماس می‌گیرید؟

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = تعداد تماس‌ها در یک ساعت
- $X$ می‌تواند مقادیر 0, 1, 2, 3, ... (هر عدد صحیح نامنفی) بگیرد

نرخ میانگین $\lambda = 4$ تماس/ساعت است.

**PMF پواسون**

برای رویدادهایی با نرخ میانگین $\lambda$:
$$ P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots $$
که $e \approx 2.71828$ عدد اویلر است.

بیایید برای مثال ما (λ=4) تأیید کنیم:
- $P(X=4) = \frac{e^{-4} \times 4^4}{4!} \approx 0.195$ ✓

:::{admonition} چرا این فرمول کار می‌کند
:class: note

فرمول Poisson $\frac{e^{-\lambda} \lambda^k}{k!}$ از ریاضیات رویدادهای نادر برمی‌خیزد:

- **$\lambda^k / k!$**: «احتمال خام» $k$ رویداد بر اساس نرخ $\lambda$ را نشان می‌دهد
- **$e^{-\lambda}$**: عامل نرمال‌سازی که تضمین می‌کند مجموع احتمال‌ها ۱ شود

**شهود:** توزیع Poisson به‌عنوان حد توزیع Binomial برمی‌خیزد وقتی:
- بازه زمانی را به زیربازه‌های بسیار ریز تقسیم کنید ($n$ بسیار بزرگ)
- احتمال رویداد در هر زیربازه بسیار کوچک باشد ($p$ بسیار کوچک)
- نرخ میانگین $\lambda = np$ ثابت بماند

مثلاً «۴ تماس در ساعت» را می‌توان ۳۶۰۰ بازه یک‌ثانیه‌ای مدل کرد که هر ثانیه احتمال $p = 4/3600$ دریافت تماس دارد.

**چرا میانگین = واریانس = λ؟** این ویژگی منحصربه‌فرد ماهیت «بی‌حافظه» فرایند Poisson را منعکس می‌کند — رویدادها تصادفی و مستقل با نرخ میانگین ثابت رخ می‌دهند.
:::

**مصورسازی الگوریتمی:** نمودار زیر فرمول Poisson را به‌عنوان نیروهای رقیب مصور می‌کند و شهود می‌سازد چرا هر جزء وجود دارد:
```{code-cell} ipython3
:tags: [remove-input]

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
from scipy.special import factorial
import matplotlib.patches as mpatches

def create_poisson_visual(lam=4):
    """Poisson distribution visualization showing the 'forces' intuition"""
    k_max = 9
    k_vals = np.arange(k_max + 1)

    # Calculate components - the three "forces"
    numerator = np.power(lam, k_vals)  # Driver
    denominator = factorial(k_vals)     # Brake
    constant = np.exp(-lam)             # Scaler
    prob = poisson.pmf(k_vals, lam)

    # Setup figure - optimized for mobile viewing
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis('off')
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(0, 10)

    # Layout constants - narrower boxes
    box_width = 0.95
    box_height = 0.9
    gap = 0.2
    start_y = 6.5

    # Title
    ax.text((k_max * (box_width + gap))/2, 9.5,
            f'Visualizing Poisson: The Three Forces ($\lambda = {lam}$)',
            ha='center', fontsize=22, fontweight='bold', color='#333333')

    ax.text((k_max * (box_width + gap))/2, 9.0,
            f'Expected rate: {lam} events. Probability of exactly k events?',
            ha='center', fontsize=15, color='#555555')

    # Draw probability boxes for each k value
    for i, k in enumerate(k_vals):
        x = i * (box_width + gap)

        # Color intensity based on probability
        max_p = max(prob)
        alpha = 0.1 + 0.8 * (prob[i] / max_p)
        box_color = plt.cm.Blues(alpha)

        # Rounded rectangle for each k
        rect = mpatches.FancyBboxPatch((x, start_y), box_width, box_height,
                                   boxstyle="round,pad=0.1",
                                   facecolor=box_color, edgecolor='#2c3e50', linewidth=1.5)
        ax.add_patch(rect)

        # k label
        center_x = x + box_width/2
        center_y = start_y + box_height/2
        ax.text(center_x, center_y, f'k={k}',
                ha='center', va='center', fontsize=17, fontweight='bold',
                color='black' if alpha < 0.6 else 'white')

        # Formula and result below box - larger fonts, better spacing
        calc_text = f"$\\frac{{{lam}^{{{k}}} \\cdot e^{{-{lam}}}}}{{{int(denominator[i])}}}$"
        result_text = f"= {prob[i]:.4f}"

        ax.text(center_x, start_y - 0.35, calc_text,
                ha='center', va='top', fontsize=15, color='#333333')
        ax.text(center_x, start_y - 1.05, result_text,
                ha='center', va='top', fontsize=13, fontweight='bold', color='#333333')

    # The Three Forces - Explanatory boxes with better positioning

    # Force 1: The Driver (Numerator)
    bbox_driver = dict(boxstyle="round,pad=0.5", fc="#fae5d3", ec="#d35400", lw=1.5)
    ax.text(1.2, 3.3, "Force 1: The Driver\n(Numerator)\n\n" + r"$\lambda^k$" +
            "\n\nPushes UP exponentially.\nHigher λ or k → more likely.",
            ha='center', va='top', fontsize=12, bbox=bbox_driver, color='#873600')

    # Force 2: The Brake (Denominator)
    bbox_brake = dict(boxstyle="round,pad=0.5", fc="#d5f5e3", ec="#27ae60", lw=1.5)
    ax.text(5.2, 3.3, "Force 2: The Brake\n(Denominator)\n\n" + r"$k!$" +
            "\n\nPulls DOWN super-fast.\nEventually crushes\nthe numerator.",
            ha='center', va='top', fontsize=12, bbox=bbox_brake, color='#145a32')

    # Force 3: The Scaler (Constant)
    bbox_scaler = dict(boxstyle="round,pad=0.5", fc="#ebf5fb", ec="#2980b9", lw=1.5)
    ax.text(9.2, 3.3, "The Scaler\n(Constant)\n\n" + r"$e^{-\lambda}$" +
            "\n\nFixed dampener.\nEnsures total = 1.",
            ha='center', va='top', fontsize=12, bbox=bbox_scaler, color='#154360')

    # Phase arrows showing growth and decay - adjusted for narrower boxes
    # Growth phase
    peak_k = int(lam)
    if peak_k > 0 and peak_k * (box_width + gap) < 4.5 * (box_width + gap):
        arrow_y = 4.8
        ax.annotate("", xy=(peak_k * (box_width + gap), arrow_y), xytext=(0.3, arrow_y),
                   arrowprops=dict(arrowstyle="->", color="#d35400", lw=2.5))
        ax.text(peak_k * (box_width + gap) / 2, arrow_y + 0.15, "Driver Wins (Growth)",
               ha='center', va='bottom', color="#d35400", fontsize=11, fontweight='bold')

    # Decay phase
    if peak_k < k_max - 2:
        arrow_y = 4.8
        decay_start = max(peak_k + 1, 5) * (box_width + gap)
        decay_end = 10.5
        ax.annotate("", xy=(decay_end, arrow_y), xytext=(decay_start, arrow_y),
                   arrowprops=dict(arrowstyle="->", color="#27ae60", lw=2.5))
        ax.text((decay_end + decay_start)/2, arrow_y + 0.15, "Brake Wins (Decay)",
               ha='center', va='bottom', color="#27ae60", fontsize=11, fontweight='bold')

    # Peak indicator - shorter arrow to avoid overlap with subtitle
    peak_x = peak_k * (box_width + gap) + box_width/2
    ax.annotate(f"Peak near k={peak_k}\n(Forces Balanced)",
               xy=(peak_x, start_y + box_height),
               xytext=(peak_x, start_y + box_height + 0.9),
               arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
               ha='center', fontsize=10, va='bottom')

    # General Formula - centered properly for narrower layout
    ax.text(5.2, 0.8, r"General Formula: $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$",
            ha='center', fontsize=20,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.6', lw=2))

    plt.tight_layout()
    plt.show()

# Create the visualization with lambda = 4
create_poisson_visual(lam=4)
```
نمودار بالا توزیع Poisson (λ = 4) را با **استعاره سه نیرو** مصور می‌کند که توضیح می‌دهد هر جزء فرمول $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ چگونه توزیع احتمال را شکل می‌دهد:

**سه نیرو:**

1. **موتور (صورت: $\lambda^k$)** — در کادر نارنجی نشان‌داده شده، این نیرو احتمالات را به‌صورت نمایی بالا می‌برد. با افزایش k، وقتی λ بزرگ است صورت سریع رشد می‌کند. «احتمال خام» k رویداد بر اساس نرخ λ را نشان می‌دهد.

2. **ترمز (مخرج: $k!$)** — در کادر سبز نشان‌داده شده، این نیرو احتمالات را به‌صورت فوق‌نمایی پایین می‌کشد. رشد فاکتوریل نهایتاً صورت را برای kهای بزرگ خرد می‌کند و کاهش سریع در دم راست توزیع ایجاد می‌کند.

3. **مقیاس‌دهنده (ثابت: $e^{-\lambda}$)** — در کادر آبی نشان‌داده شده، عامل میرایی ثابتی است که توزیع را نرمال می‌کند تا مجموع احتمال‌ها ۱ شود.

**خواندن نمودار:**

- **کادرهای رنگی** (k=0 تا k=9): آبی تیره‌تر یعنی احتمال بالاتر. هر کادر فرمول و احتمال دقیق آن k را نشان می‌دهد.
- **فلش نارنجی** («موتور برنده است»): در بخش چپ (k < λ)، صورت سریع‌تر از مخرج رشد می‌کند و احتمالات افزایش می‌یابند.
- **فلش سبز** («ترمز برنده است»): در بخش راست (k > λ)، مخرج فاکتوریل صورت را پشت سر می‌گذارد و احتمالات سریع کاهش می‌یابند.
- **نشانگر قله**: جایی که نیروها در k ≈ λ متعادل‌اند، مد توزیع را نشان می‌دهد. برای λ = 4، قله در k = 4 با احتمال ≈ 0.195 (19.5%) است.

این «کشمکش» بین موتور و ترمز شکل زنگوله‌ای مشخصه توزیع Poisson را می‌سازد، با قله‌ای که نیروها در آن متعادل‌اند.

**ویژگی‌های کلیدی**

- **سناریوها**: ایمیل در ساعت، ورود مشتری در روز، غلط‌های تایپی در صفحه، تماس اورژانس در شیفت، معیوب در واحد سطح
- **پارامتر**: $\lambda$، میانگین تعداد رویدادها در بازه ($\lambda > 0$)
- **متغیر تصادفی**: $X \in \{0, 1, 2, ...\}$

**میانگین:** $E[X] = \lambda$

**واریانس:** $Var(X) = \lambda$

**انحراف معیار:** $SD(X) = \sqrt{\lambda}$

یادداشت: در توزیع Poisson میانگین و واریانس برابرند، پس انحراف معیار به‌سادگی جذر λ است.

**ارتباط با توزیع‌های دیگر:** توزیع Poisson تقریب **توزیع Binomial** است وقتی $n$ بزرگ، $p$ کوچک و $\lambda = np$ متوسط باشد. قاعده سرانگشتی: وقتی $n \ge 20$ و $p \le 0.05$ از تقریب Poisson استفاده کنید.

**مصورسازی توزیع**

بیایید توزیع Poisson با $\lambda = 4$ را مصور کنیم (مثال مرکز تماس ما):
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_poisson_pmf_generic.svg'):
    os.remove('ch07_poisson_pmf_generic.svg')

# Create Poisson distribution for visualization (λ=4)
lambda_viz = 4
poisson_viz = stats.poisson(mu=lambda_viz)

# Calculate mean and std
mean_viz = poisson_viz.mean()
std_viz = poisson_viz.std()

# Plotting the PMF
k_values_viz = np.arange(0, 15)
pmf_values_viz = poisson_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.1f}, {mean_viz + std_viz:.1f}]')

plt.title(f"Poisson PMF (λ={lambda_viz})")
plt.xlabel("Number of Events (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values_viz)
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_poisson_pmf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
PMF توزیع حول λ = 4 با احتمال معقول برای مقادیر نزدیک متمرکز است. ناحیه سایه‌دار میانگین ± ۱ انحراف معیار ($\sqrt{4} = 2$) را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input]

# Remove existing SVG if present
if os.path.exists('ch07_poisson_cdf_generic.svg'):
    os.remove('ch07_poisson_cdf_generic.svg')

# Plotting the CDF
cdf_values_viz = poisson_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.1f}')

plt.title(f"Poisson CDF (λ={lambda_viz})")
plt.xlabel("Number of Events (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values_viz)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_poisson_cdf_generic.svg', format='svg', bbox_inches='tight')
plt.show()
```
CDF مقدار P(X ≤ k) را نشان می‌دهد، مفید برای سؤالاتی مثل «احتمال ۶ یا کمتر تماس چقدر است؟» خط چین قرمز میانگین را نشان می‌دهد.

:::{admonition} مثال: ورود ایمیل با λ = 5
:class: tip

مدل‌سازی تعداد ایمیل‌های دریافتی در ساعت با نرخ میانگین λ = 5 ایمیل/ساعت.

از [`scipy.stats.poisson`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html) برای محاسبه احتمال مشاهده تعدادهای مختلف رویداد و تأیید برابری میانگین و واریانس استفاده می‌کنیم.

**تنظیم توزیع:**

توزیع Poisson با پارامتر نرخ λ = 5 (میانگین ۵ ایمیل در ساعت) می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.poisson
lambda_rate = 5
poisson_rv = stats.poisson(mu=lambda_rate)
```
**محاسبه احتمال‌های مشخص با PMF:**

احتمال دریافت دقیقاً ۳ ایمیل در یک ساعت مشخص چقدر است؟
```{code-cell} ipython3
# PMF: Probability of exactly k events
k_events = 3
print(f"P(X={k_events} emails in an hour | lambda={lambda_rate}): {poisson_rv.pmf(k_events):.4f}")
```
۱۴.۰۴٪ احتمال دریافت دقیقاً ۳ ایمیل وجود دارد. این پایین‌تر از میانگین ۵ است، پس کم‌محتمل‌تر از مقادیر نزدیک‌تر به ۵ است.

**محاسبه احتمال‌های تجمعی با CDF:**

احتمال دریافت ۶ یا کمتر ایمیل در یک ساعت چقدر است؟
```{code-cell} ipython3
# CDF: Probability of k or fewer events
k_or_fewer_events = 6
print(f"P(X <= {k_or_fewer_events} emails in an hour): {poisson_rv.cdf(k_or_fewer_events):.4f}")
print(f"P(X > {k_or_fewer_events} emails in an hour): {1 - poisson_rv.cdf(k_or_fewer_events):.4f}")
print(f"P(X > {k_or_fewer_events} emails in an hour) (using sf): {poisson_rv.sf(k_or_fewer_events):.4f}")
```
۷۶.۲۲٪ احتمال دریافت ۶ یا کمتر ایمیل وجود دارد، یعنی ۲۳.۷۸٪ احتمال دریافت بیش از ۶ ایمیل در یک ساعت.

**تأیید ویژگی کلیدی Poisson: میانگین برابر واریانس:**

ویژگی منحصربه‌فرد توزیع Poisson این است که E[X] = Var(X) = λ:
```{code-cell} ipython3
# Mean and Variance
print(f"Mean (Expected number of emails): {poisson_rv.mean():.2f}")
print(f"Variance: {poisson_rv.var():.2f}")
```
طبق انتظار، هم میانگین و هم واریانس برابر 5.00 هستند و ویژگی نظری توزیع Poisson را تأیید می‌کنند.

**تولید نمونه‌های تصادفی:**

می‌توانیم بسیاری دوره‌های یک‌ساعته را شبیه‌سازی کنیم تا تغییرپذیری ورود ایمیل‌ها را ببینیم:
```{code-cell} ipython3
# Generate random samples
n_simulations = 1000
samples = poisson_rv.rvs(size=n_simulations)
# print(f"\nSimulated number of emails per hour ({n_simulations} simulations): {samples[:20]}...")
```
این ۱۰۰۰ نمونه ساعات مختلف را نشان می‌دهند که هر کدام تعداد ایمیل‌های رسیده در آن ساعت را نشان می‌دهد.

**مصورسازی PMF:**

بیایید توزیع احتمال کامل برای تعدادهای مختلف ایمیل ببینیم:
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_poisson_pmf.svg'):
    os.remove('ch07_poisson_pmf.svg')
```
```{code-cell} ipython3
# Plotting the PMF
k_values = np.arange(0, 16) # Plot for k=0 to 15
pmf_values = poisson_rv.pmf(k_values)

plt.figure(figsize=(8, 3.5))
plt.bar(k_values, pmf_values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Poisson PMF (λ={lambda_rate})")
plt.xlabel("Number of Events (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_poisson_pmf.svg', format='svg', bbox_inches='tight')
```
PMF توزیع حول λ = 5 ایمیل متمرکز است، با بالاترین احتمالات در k = 4 و k = 5. توزیع برای این مقدار λ تقریباً متقارن است. مقادیر دور از ۵ (مثل 0-1 یا 11+) احتمال بسیار کم دارند. توجه کنید احتمال در k = 3 (که 0.1404 محاسبه کردیم) به‌صورت میله با ارتفاع متوسط ظاهر می‌شود.

**مصورسازی CDF:**

توزیع تجمعی به پاسخ سؤالات درباره بازه تعداد ایمیل‌ها کمک می‌کند:
```{code-cell} ipython3
:tags: [remove-cell]

# Remove existing SVG if present
if os.path.exists('ch07_poisson_cdf.svg'):
    os.remove('ch07_poisson_cdf.svg')
```
```{code-cell} ipython3
# Plotting the CDF
cdf_values = poisson_rv.cdf(k_values)

plt.figure(figsize=(8, 3.5))
plt.step(k_values, cdf_values, where='post', color='darkgreen', linewidth=2)
plt.title(f"Poisson CDF (λ={lambda_rate})")
plt.xlabel("Number of Events (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.show()
```
```{code-cell} ipython3
:tags: [remove-cell]

plt.savefig('ch07_poisson_cdf.svg', format='svg', bbox_inches='tight')
```
CDF مقدار P(X ≤ k)، احتمال تجمعی را نشان می‌دهد. می‌بینیم تا k = 6، CDF تقریباً به 0.76 می‌رسد (مطابق محاسبه 76.22%)، و تا k = 10 نزدیک 1.0 است، یعنی دریافت بیش از ۱۰ ایمیل در یک ساعت بسیار بعید است.

:::

**سؤالات مرور سریع**

1. مرکز تماس به‌طور میانگین ۱۲ تماس در ساعت دریافت می‌کند. کدام توزیع تعداد تماس‌ها در یک ساعت را مدل می‌کند و پارامتر چیست؟
```{admonition} پاسخ
:class: dropdown

**توزیع Poisson با λ = 12** — رویدادهایی که با نرخ میانگین ثابت در بازه ثابت رخ می‌دهند.
```
۲. برای توزیع Poisson با λ = 7، امید ریاضی و واریانس چقدر است؟
```{admonition} پاسخ
:class: dropdown

**امید ریاضی = 7، واریانس = 7** — برای Poisson، هر دو برابر λ هستند. این ویژگی منحصربه‌فرد توزیع Poisson است.
```
۳. تعداد غلط‌های املایی در یک صفحه تصادفی کتاب را می‌شمارید. میانگین ۲ غلط در هر صفحه است. کدام توزیع؟
```{admonition} پاسخ
:class: dropdown

**Poisson با λ = 2** — شمارش رویدادهای گسسته (غلط‌های املایی) در فضای ثابت (یک صفحه) با نرخ متوسط ثابت.

این با شرایط Poisson سازگار است:
- رویدادها مستقل رخ می‌دهند
- نرخ متوسط ثابت
- شمارش وقوع در بازه/فضای ثابت
```
۴. درست یا نادرست: در توزیع Poisson، امید ریاضی می‌تواند با واریانس متفاوت باشد.
```{admonition} پاسخ
:class: dropdown

**نادرست** — ویژگی کلیدی Poisson این است که امید ریاضی = واریانس = λ.

این ویژگی کمک می‌کند تشخیص دهید Poisson بهترین برازش نیست. اگر واریانس داده‌ها بسیار بزرگ‌تر یا کوچک‌تر از امید ریاضی باشد، توزیع‌های دیگر را در نظر بگیرید (مثلاً Negative Binomial برای overdispersion).
```
۵. Poisson چه زمانی می‌تواند Binomial را تقریب بزند؟
```{admonition} پاسخ
:class: dropdown

**وقتی n بزرگ، p کوچک و np متوسط است** — به‌طور مشخص:
- n ≥ 20 و p ≤ 0.05، یا
- n ≥ 100 و np ≤ 10

آنگاه Binomial(n, p) ≈ Poisson(λ = np)

مثال: Binomial(n=1000, p=0.003) ≈ Poisson(λ=3)

این به این دلیل کار می‌کند که رویدادهای نادر در آزمایش‌های زیاد مانند رویدادهایی با نرخ ثابت رفتار می‌کنند.
```
+++
## ۶. توزیع Hypergeometric

توزیع Hypergeometric تعداد موفقیت‌ها در نمونه‌ای را مدل می‌کند که *بدون جایگزینی* از جامعه‌ای متناهی کشیده شده است. این با Binomial متفاوت است که نمونه‌گیری با جایگزینی (یا جامعه نامتناهی) را فرض می‌کند.

**مثال ملموس**

۵ کارت از یک دسته استاندارد ۵۲ کارتی برمی‌دارید. چند آس می‌گیرید؟

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = تعداد آس‌ها در دست ۵ کارتی
- جامعه: N = ۵۲ کارت در مجموع
- موفقیت‌ها در جامعه: K = ۴ آس
- اندازه نمونه: n = ۵ کارت کشیده‌شده
- $X$ می‌تواند مقادیر ۰، ۱، ۲، ۳، ۴ بگیرد (بیش از ۴ آس ممکن نیست!)

**PMF فوق‌هندسی**

برای نمونه‌گیری بدون جایگزینی:
$$ P(X=k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}} $$
این برابر است با: (تعداد روش‌های انتخاب k موفقیت از K) × (تعداد روش‌های انتخاب n-k شکست از N-K) / (کل روش‌های انتخاب n مورد از N).

:::{admonition} چرا این فرمول کار می‌کند
:class: note

فرمول Hypergeometric از اصول شمارش استفاده می‌کند:

- **$\binom{N}{n}$** (مخرج): کل روش‌های انتخاب $n$ مورد از $N$ — یعنی همه نمونه‌های ممکن
- **$\binom{K}{k}$** (صورت): روش‌های انتخاب $k$ موفقیت از $K$ موفقیت موجود
- **$\binom{N-K}{n-k}$** (صورت): روش‌های انتخاب $n-k$ شکست از $N-K$ شکست موجود

**مثال:** کشیدن ۵ کارت با امید به ۲ آس (N=52, K=4, n=5, k=2):
- روش‌های انتخاب ۲ آس از ۴: $\binom{4}{2} = 6$
- روش‌های انتخاب ۳ غیرآس از ۴۸: $\binom{48}{3} = 17,296$
- روش‌های انتخاب هر ۵ کارت: $\binom{52}{5} = 2,598,960$
- احتمال: $\frac{6 \times 17,296}{2,598,960} \approx 0.040$

فرمول در اصل برابر است با: **(پیامدهای مطلوب) / (کل پیامدهای ممکن)** از احتمال پایه، با شمارش ترکیبی!
:::

**ویژگی‌های کلیدی**

- **سناریوها**: کارت از دسته، اقلام معیوب در دسته کوچک، ماهی‌های علامت‌گذاری‌شده در نمونه، انتخاب هیئت منصفه از مجموعه متناهی
- **پارامترها**:
    - $N$: اندازه کل جامعه
    - $K$: تعداد کل موفقیت‌ها در جامعه
    - $n$: اندازه نمونه ($n \le N$)
- **متغیر تصادفی**: $X$، محدود به $\max(0, n-(N-K)) \le X \le \min(n, K)$

**امید ریاضی:** $E[X] = n \frac{K}{N}$

**واریانس:** $Var(X) = n \frac{K}{N} \left(1 - \frac{K}{N}\right) \left(\frac{N-n}{N-1}\right)$

**انحراف معیار:** $SD(X) = \sqrt{n \frac{K}{N} \left(1 - \frac{K}{N}\right) \left(\frac{N-n}{N-1}\right)}$

عبارت $\frac{N-n}{N-1}$ *ضریب اصلاح جامعه متناهی* است. با $N \to \infty$، به ۱ نزدیک می‌شود و Hypergeometric → Binomial با $p = K/N$.

**مصورسازی توزیع**

بیایید توزیع Hypergeometric با N=52, K=4, n=5 را مصور کنیم (مثال کارت ما):
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_hypergeometric_pmf_generic.svg'):
    os.remove('ch07_hypergeometric_pmf_generic.svg')

# Create Hypergeometric distribution for visualization (N=52, K=4, n=5)
N_viz = 52
K_viz = 4
n_viz = 5
hypergeom_viz = stats.hypergeom(M=N_viz, n=K_viz, N=n_viz)

# Calculate mean and std
mean_viz = hypergeom_viz.mean()
std_viz = hypergeom_viz.std()

# Plotting the PMF
k_values_viz = np.arange(0, min(n_viz, K_viz) + 1)
pmf_values_viz = hypergeom_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.2f}, {mean_viz + std_viz:.2f}]')

plt.title(f"Hypergeometric PMF (N={N_viz}, K={K_viz}, n={n_viz})")
plt.xlabel("Number of Successes in Sample (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values_viz)
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_hypergeometric_pmf_generic.svg', format='svg', bbox_inches='tight')
```
PMF نشان می‌دهد محتمل‌ترین حالت ۰ آس است (حدود ۰.۶۶ احتمال)، گرفتن ۱ یا ۲ کم‌محتمل‌تر است. خط چین قرمز امید ریاضی را نشان می‌دهد و ناحیه سایه‌دار نارنجی امید ریاضی ± ۱ انحراف معیار را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_hypergeometric_cdf_generic.svg'):
    os.remove('ch07_hypergeometric_cdf_generic.svg')

# Plotting the CDF
cdf_values_viz = hypergeom_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

plt.title(f"Hypergeometric CDF (N={N_viz}, K={K_viz}, n={n_viz})")
plt.xlabel("Number of Successes in Sample (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values_viz)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_hypergeometric_cdf_generic.svg', format='svg', bbox_inches='tight')
```
CDF مقدار P(X ≤ k) را نشان می‌دهد و برای پرسش‌هایی مانند «احتمال حداکثر ۱ آس چقدر است؟» مفید است. خط چین قرمز امید ریاضی را نشان می‌دهد.

:::{admonition} مثال: بلیت‌های بخت‌آزمایی با N=100, K=20, n=10
:class: tip

مدل‌سازی تعداد بلیت‌های برنده در نمونه‌ای ۱۰تایی که از جعبه‌ای با ۱۰۰ بلیت (۲۰ برنده) کشیده شده است.

از [`scipy.stats.hypergeom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html) برای محاسبه احتمال‌های نمونه‌گیری بدون جایگزینی استفاده می‌کنیم و می‌بینیم امید ریاضی چگونه به نسبت جامعه مرتبط است.

**راه‌اندازی توزیع:**

یک توزیع hypergeometric برای کشیدن بدون جایگزینی می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.hypergeom
N_population = 100
K_successes_pop = 20
n_sample = 10
hypergeom_rv = stats.hypergeom(M=N_population, n=K_successes_pop, N=n_sample)
```
**محاسبه احتمال‌های مشخص با PMF:**

احتمال گرفتن دقیقاً ۳ بلیت برنده وقتی ۱۰ بلیت می‌کشیم چقدر است؟
```{code-cell} ipython3
# PMF: Probability of exactly k successes in the sample
k_successes_sample = 3
print(f"P(X={k_successes_sample} winning tickets in sample of {n_sample}): {hypergeom_rv.pmf(k_successes_sample):.4f}")
```
۲۰.۱۳٪ احتمال گرفتن دقیقاً ۳ برنده وجود دارد. این بیشتر از احتمال ۲ برنده است چون ۳ به مقدار مورد انتظار نزدیک‌تر است (در ادامه می‌بینید).

**محاسبه احتمال‌های تجمعی با CDF:**

احتمال گرفتن ۲ برنده یا کمتر چقدر است؟
```{code-cell} ipython3
# CDF: Probability of k or fewer successes in the sample
k_or_fewer_sample = 2
print(f"P(X <= {k_or_fewer_sample} winning tickets in sample): {hypergeom_rv.cdf(k_or_fewer_sample):.4f}")
print(f"P(X > {k_or_fewer_sample} winning tickets in sample): {1 - hypergeom_rv.cdf(k_or_fewer_sample):.4f}")
print(f"P(X > {k_or_fewer_sample} winning tickets in sample) (using sf): {hypergeom_rv.sf(k_or_fewer_sample):.4f}")
```
۶۷.۶۷٪ احتمال گرفتن ۲ برنده یا کمتر وجود دارد، یعنی ۳۲.۳۳٪ احتمال بیش از ۲ برنده.

**محاسبه امید ریاضی و واریانس:**

بیایید تأیید کنیم امید ریاضی با نسبت مورد انتظار از جامعه مطابقت دارد:
```{code-cell} ipython3
# Mean and Variance
print(f"Mean (Expected number of winning tickets in sample): {hypergeom_rv.mean():.2f}")
print(f"Variance: {hypergeom_rv.var():.2f}")
print(f"Standard Deviation: {hypergeom_rv.std():.2f}")
# Theoretical mean: E[X] = n * (K/N) = 10 * (20/100) = 2.0
```
طبق انتظار، امید ریاضی ۲.۰ برنده است که دقیقاً n × (K/N) = 10 × (20/100) = 10 × 0.2 است. چون ۲۰٪ جامعه برنده‌اند، انتظار داریم ۲۰٪ نمونه برنده باشد. اصلاح جامعه متناهی واریانس (۱.۴۴) را کوچک‌تر از نمونه‌گیری دوجمله‌ای با جایگزینی می‌کند.

**تولید نمونه‌های تصادفی:**

می‌توانیم کشیدن‌های متعدد ۱۰ بلیت را شبیه‌سازی کنیم:
```{code-cell} ipython3
# Generate random samples
n_simulations = 1000
samples = hypergeom_rv.rvs(size=n_simulations)
# print(f"\nSimulated number of winning tickets ({n_simulations} simulations): {samples[:20]}...")
```
این ۱۰۰۰ نمونه مجموعه‌های مختلف ۱۰ بلیت کشیده‌شده از جعبه را نشان می‌دهند و تغییرپذیری طبیعی پیامدها را نمایش می‌دهند.

**مصورسازی PMF:**

بیایید توزیع پیامدهای ممکن هنگام کشیدن ۱۰ بلیت را ببینیم:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_hypergeometric_pmf.svg'):
    os.remove('ch07_hypergeometric_pmf.svg')

# Plotting the PMF
# Determine possible k values: max(0, n-(N-K)) <= k <= min(n, K)
min_k = max(0, n_sample - (N_population - K_successes_pop))
max_k = min(n_sample, K_successes_pop)
k_values = np.arange(min_k, max_k + 1)
pmf_values = hypergeom_rv.pmf(k_values)

plt.figure(figsize=(8, 3.5))
plt.bar(k_values, pmf_values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Hypergeometric PMF (N={N_population}, K={K_successes_pop}, n={n_sample})")
plt.xlabel("Number of Successes in Sample (k)")
plt.ylabel("Probability P(X=k)")
plt.xticks(k_values)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_hypergeometric_pmf.svg', format='svg', bbox_inches='tight')
```
PMF حول ۲ برنده (مقدار مورد انتظار) متمرکز است و بالاترین احتمال‌ها در ۱، ۲ و ۳ برنده است. گرفتن ۰ برنده یا ۵+ برنده بسیار کم‌محتمل‌تر است. توزیع تقریباً زنگوله‌ای به نظر می‌رسد که برای Hypergeometric وقتی اندازه نمونه نسبت به جامعه کوچک است معمول است. توجه کنید k = 3 (که ۲۰.۱۳٪ محاسبه کردیم) یکی از بلندترین میله‌هاست.

**مصورسازی CDF:**

توزیع تجمعی کل احتمال گرفتن تا k برنده را نشان می‌دهد:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_hypergeometric_cdf.svg'):
    os.remove('ch07_hypergeometric_cdf.svg')

# Plotting the CDF
cdf_values = hypergeom_rv.cdf(k_values)

plt.figure(figsize=(8, 3.5))
plt.step(k_values, cdf_values, where='post', color='darkgreen', linewidth=2)
plt.title(f"Hypergeometric CDF (N={N_population}, K={K_successes_pop}, n={n_sample})")
plt.xlabel("Number of Successes in Sample (k)")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.xticks(k_values)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_hypergeometric_cdf.svg', format='svg', bbox_inches='tight')
```
CDF احتمال تجمعی را نشان می‌دهد. می‌بینیم P(X ≤ 2) ≈ 0.68 (مطابق محاسبه قبلی ۶۷.۶۷٪) و تا k = 5 تقریباً همه احتمال جمع شده (نزدیک ۱.۰).

:::

**سؤالات مرور سریع**

۱. ۷ کارت از دسته ۵۲ کارتی برمی‌دارید. می‌خواهید بدانید چند خشت می‌گیرید. کدام توزیع این را مدل می‌کند و پارامترها چیست؟
```{admonition} پاسخ
:class: dropdown

**Hypergeometric با N=52, K=13, n=7** — نمونه‌گیری بدون جایگزینی از جامعه متناهی (۱۳ خشت در ۵۲ کارت).
```
۲. برای توزیع Hypergeometric با N=50, K=10, n=5، مقدار مورد انتظار (امید ریاضی) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**E[X] = n(K/N) = 5 × (10/50) = 1** — تعداد مورد انتظار موفقیت‌ها در نمونه.
```
۳. بازرس کیفیت به‌طور تصادفی ۱۰ محصول از دسته ۱۰۰تایی (۱۵ معیوب) بدون جایگزینی انتخاب می‌کند. کدام توزیع؟
```{admonition} پاسخ
:class: dropdown

**Hypergeometric با N=100, K=15, n=10** — نمونه‌گیری بدون جایگزینی از جامعه متناهی.

این Binomial نیست چون:
- بدون جایگزینی نمونه‌گیری می‌کنیم
- اندازه نمونه (۱۰) نسبت به جامعه (۱۰۰) قابل توجه است
- هر کشیدن احتمال کشیدن‌های بعدی را تغییر می‌دهد
```
۴. تفاوت کلیدی بین توزیع‌های Binomial و Hypergeometric چیست؟
```{admonition} پاسخ
:class: dropdown

**Hypergeometric بدون جایگزینی** نمونه‌گیری می‌کند (جامعه متناهی)، در حالی که Binomial با جایگزینی (یا جامعه نامتناهی فرض می‌کند).

پیامدهای کلیدی:
- Hypergeometric: آزمایش‌ها مستقل نیستند (هر کشیدن بر بعدی اثر می‌گذارد)
- Binomial: آزمایش‌ها مستقل‌اند (احتمال ثابت p)

قاعده سرانگشتی: اگر N > 20n، Hypergeometric ≈ Binomial چون نمونه نسبت به جامعه کوچک است.
```
۵. Hypergeometric چه زمانی می‌تواند با Binomial تقریب زده شود؟
```{admonition} پاسخ
:class: dropdown

**وقتی جامعه بسیار بزرگ‌تر از نمونه است** — به‌طور مشخص، وقتی N > 20n.

در این حالت، Hypergeometric(N, K, n) ≈ Binomial(n, p=K/N)

مثال: کشیدن ۱۰ کارت از جامعه ۱۰۰۰ کارتی. نمونه کوچک تقریباً بر نسبت‌های جامعه اثر نمی‌گذارد، پس با/بدون جایگزینی نتایج تقریباً یکسان است.
```
+++
## ۷. توزیع Discrete Uniform

توزیع Discrete Uniform انتخاب یک پیامد از مجموعه‌ای متناهی را مدل می‌کند که همه پیامدها به‌طور برابر محتمل‌اند.

**مثال ملموس**

فرض کنید یک تاس شش‌وجهی منصفانه می‌اندازید. هر وجه (۱، ۲، ۳، ۴، ۵، ۶) احتمال برابر دارد.

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = عدد روی تاس
- $X$ می‌تواند مقادیر ۱، ۲، ۳، ۴، ۵، ۶ بگیرد

احتمال‌ها:
- $P(X = 1) = P(X = 2) = \cdots = P(X = 6) = \frac{1}{6}$

**PMF یکنواخت گسسته**

برای توزیع Discrete Uniform روی اعداد صحیح از $a$ تا $b$ (شامل):
$$ P(X=k) = \begin{cases} \frac{1}{b-a+1} & \text{if } k \in \{a, a+1, \ldots, b\} \\ 0 & \text{otherwise} \end{cases} $$
برای مثال تاس با $a = 1$ و $b = 6$:
- $P(X=k) = \frac{1}{6-1+1} = \frac{1}{6}$ برای $k \in \{1, 2, 3, 4, 5, 6\}$

:::{admonition} چرا این فرمول کار می‌کند
:class: note

توزیع Discrete Uniform ساده‌ترین توزیع احتمال است:

- **کل پیامدها**: $b - a + 1$ («+۱» هر دو انتها را می‌شمارد)
- **هر پیامد به‌طور برابر محتمل**: احتمال = $\frac{1}{n}$ (که $n$ تعداد پیامدهاست)

**مثال:** برای مقادیر ۵ تا ۱۵:
- کل مقادیر: $15 - 5 + 1 = 11$ مقدار
- هر کدام احتمال: $\frac{1}{11} \approx 0.091$

این مستقیماً تعریف کلاسیک احتمال را پیاده می‌کند: **(پیامدهای مطلوب) / (کل پیامدهای به‌طور برابر محتمل)**.
:::

**ویژگی‌های کلیدی**

- **سناریوها**: انداختن تاس منصفانه، انتخاب تصادفی از فهرست، انتخاب شماره بخت‌آزمایی، رقم تصادفی رمز
- **پارامترها**:
    - $a$: حداقل مقدار (عدد صحیح)
    - $b$: حداکثر مقدار (عدد صحیح، $b \ge a$)
- **متغیر تصادفی**: $X \in \{a, a+1, \ldots, b\}$

**امید ریاضی:** $E[X] = \frac{a+b}{2}$

**واریانس:** $Var(X) = \frac{(b-a+1)^2 - 1}{12}$

**انحراف معیار:** $SD(X) = \sqrt{\frac{(b-a+1)^2 - 1}{12}}$

**ارتباط با توزیع‌های دیگر:** توزیع Discrete Uniform حالت خاص **توزیع Categorical** است که همه $k$ دسته احتمال برابر $p_i = 1/k$ دارند. اگر پیامدها به‌طور برابر محتمل نیستند، از Categorical استفاده کنید.

**مصورسازی توزیع**

بیایید توزیع Discrete Uniform برای تاس منصفانه ($a = 1$, $b = 6$) را مصور کنیم:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_discrete_uniform_pmf.svg'):
    os.remove('ch07_discrete_uniform_pmf.svg')

# Create Discrete Uniform distribution for visualization (fair die)
a_viz = 1
b_viz = 6
from scipy.stats import randint
# scipy.stats.randint uses [low, high) so we add 1 to b
uniform_viz = randint(low=a_viz, high=b_viz+1)

# Calculate mean and std
mean_viz = uniform_viz.mean()
std_viz = uniform_viz.std()

# Plotting the PMF
k_values_viz = np.arange(a_viz, b_viz+1)
pmf_values_viz = uniform_viz.pmf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.bar(k_values_viz, pmf_values_viz, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

# Add mean ± 1 std region
plt.axvspan(mean_viz - std_viz, mean_viz + std_viz, alpha=0.2, color='orange',
            label=f'Mean ± 1 SD = [{mean_viz - std_viz:.2f}, {mean_viz + std_viz:.2f}]')

plt.title(f"Discrete Uniform PMF (a={a_viz}, b={b_viz})")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.ylim(0, 0.25)
plt.xticks(k_values_viz)
plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_discrete_uniform_pmf.svg', format='svg', bbox_inches='tight')
```
PMF شش میله برابر با احتمال ۱/۶ نشان می‌دهد که تاس منصفانه را نمایش می‌دهد. ناحیه سایه‌دار امید ریاضی ± ۱ انحراف معیار را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_discrete_uniform_cdf.svg'):
    os.remove('ch07_discrete_uniform_cdf.svg')

# Plotting the CDF
cdf_values_viz = uniform_viz.cdf(k_values_viz)

plt.figure(figsize=(10, 4))
plt.step(k_values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)

# Add mean line
plt.axvline(mean_viz, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_viz:.2f}')

plt.title(f"Discrete Uniform CDF (a={a_viz}, b={b_viz})")
plt.xlabel("Outcome")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.ylim(0, 1.1)
plt.xticks(k_values_viz)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_discrete_uniform_cdf.svg', format='svg', bbox_inches='tight')
```
CDF با گام‌های برابر ۱/۶ در هر مقدار افزایش می‌یابد و در مقدار بیشینه به ۱.۰ می‌رسد. خط چین قرمز امید ریاضی را نشان می‌دهد.

:::{admonition} مثال: انتخاب تصادفی از ۱ تا ۲۰
:class: tip

مدل‌سازی انتخاب تصادفی عدد صحیح از ۱ تا ۲۰ که هر عدد به‌طور برابر محتمل انتخاب شود.

از [`scipy.stats.randint`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.randint.html) برای محاسبه احتمال‌ها و تولید نمونه استفاده می‌کنیم.

**راه‌اندازی توزیع:**

یک توزیع یکنواخت گسسته روی اعداد صحیح ۱ تا ۲۰ می‌سازیم (توجه: scipy.stats.randint از بازه نیمه‌باز [low, high) استفاده می‌کند):
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Using scipy.stats.randint (note: uses [low, high) interval)
a_sel = 1
b_sel = 20
uniform_rv = stats.randint(low=a_sel, high=b_sel+1)
```
**محاسبه احتمال‌ها با PMF:**

چون همه مقادیر به‌طور برابر محتمل‌اند، هر مقدار احتمال یکسان دارد:
```{code-cell} ipython3
# PMF: Probability of any specific value
k_val = 7
print(f"P(X={k_val}): {uniform_rv.pmf(k_val):.4f}")
print(f"This equals 1/{b_sel-a_sel+1} = {1/(b_sel-a_sel+1):.4f}")
```
هر یک از ۲۰ مقدار احتمال ۱/۲۰ = ۰.۰۵ دارد. مقدار ۷ همان احتمال هر مقدار دیگر را دارد.

**محاسبه احتمال‌های تجمعی با CDF:**

احتمال انتخاب عددی ≤ ۱۰ چقدر است؟
```{code-cell} ipython3
# CDF: Probability of k or fewer
k_threshold = 10
print(f"P(X <= {k_threshold}): {uniform_rv.cdf(k_threshold):.4f}")
print(f"P(X > {k_threshold}): {uniform_rv.sf(k_threshold):.4f}")
```
۵۰٪ احتمال انتخاب ۱۰ یا کمتر (مقادیر ۱-۱۰) و ۵۰٪ بیش از ۱۰ (مقادیر ۱۱-۲۰) وجود دارد. منطقی است چون ۱۰ نقطه میانی است.

**محاسبه امید ریاضی و واریانس:**

بیایید تأیید کنیم امید ریاضی در مرکز بازه است:
```{code-cell} ipython3
# Mean and Variance
print(f"Mean (Expected value): {uniform_rv.mean():.2f}")
print(f"Theoretical mean (a+b)/2: {(a_sel+b_sel)/2:.2f}")
print(f"Variance: {uniform_rv.var():.2f}")
```
امید ریاضی ۱۰.۵۰ است، دقیقاً میان ۱ و ۲۰، مطابق فرمول (a+b)/2 = (1+20)/2 = 10.5.

**تولید نمونه‌های تصادفی:**

۱۰ انتخاب تصادفی تولید می‌کنیم:
```{code-cell} ipython3
# Generate random samples
n_samples = 10
samples = uniform_rv.rvs(size=n_samples)
print(f"{n_samples} random selections from 1 to {b_sel}:")
print(samples)
```
هر نمونه انتخاب تصادفی مستقل است و همه مقادیر به‌طور برابر محتمل‌اند.

**مصورسازی PMF:**

مصورسازی PMF ویژگی تعیین‌کننده توزیع یکنواخت — برابری کامل — را نشان می‌دهد:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_discrete_uniform_pmf_example.svg'):
    os.remove('ch07_discrete_uniform_pmf_example.svg')

# Plotting the PMF
k_values = np.arange(a_sel, b_sel+1)
pmf_values = uniform_rv.pmf(k_values)

plt.figure(figsize=(10, 4))
plt.bar(k_values, pmf_values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Discrete Uniform PMF (a={a_sel}, b={b_sel})")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_discrete_uniform_pmf_example.svg', format='svg', bbox_inches='tight')
```
هر ۲۰ مقدار احتمال برابر ۰.۰۵ (۱/۲۰) دارد. این توزیع تخت امضای یکنواخت گسسته است — هیچ مقداری محتمل‌تر از دیگری نیست.

**مصورسازی CDF:**

CDF پلکان خطی کامل نشان می‌دهد:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_discrete_uniform_cdf_example.svg'):
    os.remove('ch07_discrete_uniform_cdf_example.svg')

# Plotting the CDF
cdf_values = uniform_rv.cdf(k_values)

plt.figure(figsize=(10, 4))
plt.step(k_values, cdf_values, where='post', color='darkgreen', linewidth=2)
plt.title(f"Discrete Uniform CDF (a={a_sel}, b={b_sel})")
plt.xlabel("Value")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_discrete_uniform_cdf_example.svg', format='svg', bbox_inches='tight')
```
CDF با گام‌های برابر ۱/۲۰ = ۰.۰۵ افزایش می‌یابد، کاملاً خطی. در k=10، CDF دقیقاً ۰.۵ (میانه) است و محاسبه قبلی را تأیید می‌کند.

:::

**سؤالات مرور سریع**

۱. به‌طور تصادفی کارتی از دسته استاندارد (۵۲ کارت) انتخاب می‌کنید. اگر X شماره کارت (۱-۱۳، ۱=آس، ۱۱=سرباز، ۱۲=بیبی، ۱۳=شاه) باشد، کدام توزیع این را مدل می‌کند و پارامترها چیست؟
```{admonition} پاسخ
:class: dropdown

**توزیع Discrete Uniform با a = 1, b = 13** — هر شماره کارت به‌طور برابر محتمل است (۴ عدد از هر کدام در دسته).
```
۲. برای توزیع Discrete Uniform با a = 5 و b = 15، احتمال گرفتن دقیقاً ۱۰ چقدر است؟
```{admonition} پاسخ
:class: dropdown

**P(X = 10) = 1/(15-5+1) = 1/11 ≈ 0.091** — همه مقادیر در بازه به‌طور برابر محتمل‌اند.
```
۳. امید ریاضی توزیع Discrete Uniform روی اعداد صحیح ۱ تا ۱۰۰ چقدر است؟
```{admonition} پاسخ
:class: dropdown

**امید ریاضی = (1+100)/2 = 50.5** — امید ریاضی نقطه میانی بازه است.
```
۴. پیامد انداختن تاس شش‌وجهی منصفانه را مدل می‌کنید. از Discrete Uniform یا Categorical استفاده کنید؟
```{admonition} پاسخ
:class: dropdown

**توزیع Discrete Uniform** — چون تاس *منصفانه* است، همه پیامدها (۱-۶) با احتمال ۱/۶ به‌طور برابر محتمل‌اند.

از Discrete Uniform(a=1, b=6) استفاده کنید.

**توجه:** اگر تاس *سنگین* بود (احتمال‌های نابرابر)، از توزیع Categorical استفاده کنید.
```
۵. برای توزیع Discrete Uniform روی اعداد صحیح a تا b، چرا واریانس برابر $\frac{(b-a)(b-a+2)}{12}$ است؟
```{admonition} پاسخ
:class: dropdown

فرمول واریانس نشان می‌دهد مقادیر چقدر پراکنده‌اند:

- **بازه بزرگ‌تر (b-a)**: واریانس بیشتر — مقادیر پراکنده‌تر
- **شهود فرمول**: واریانس با *مربع* بازه رشد می‌کند، مشابه توزیع‌های یکنواخت پیوسته

**مثال:**
- Discrete Uniform(1, 6): واریانس = (6-1)(6-1+2)/12 = 5×7/12 ≈ 2.92
- Discrete Uniform(1, 100): واریانس = 99×101/12 ≈ 833.25

بازه بسیار بزرگ‌تر → واریانس بسیار بزرگ‌تر.
```
+++
## ۸. توزیع Categorical

توزیع Categorical یک آزمایش تکی با چند پیامد ممکن (بیش از ۲) را مدل می‌کند که هر پیامد احتمال خود را دارد. تعمیم توزیع Bernoulli به بیش از دو دسته است.

**مثال ملموس**

فرض کنید تاس شش‌وجهی سنگین می‌اندازید که وجه‌ها احتمال‌های متفاوت دارند:
- وجه ۱: احتمال ۰.۱
- وجه ۲: احتمال ۰.۱۵
- وجه ۳: احتمال ۰.۲۰
- وجه ۴: احتمال ۰.۲۵
- وجه ۵: احتمال ۰.۲۰
- وجه ۶: احتمال ۰.۱۰

این را با متغیر تصادفی $X$ مدل می‌کنیم:
- $X$ = وجهی که ظاهر می‌شود
- $X$ می‌تواند مقادیر $\{1, 2, 3, 4, 5, 6\}$ بگیرد
- هر مقدار احتمال خود را دارد: $P(X=1)=0.1, P(X=2)=0.15,$ و غیره

**PMF دسته‌ای**

برای توزیع Categorical با $k$ پیامد ممکن و احتمال‌های $p_1, p_2, \ldots, p_k$ که $\sum_{i=1}^k p_i = 1$:
$$ P(X=i) = p_i \quad \text{for } i = 1, 2, \ldots, k $$
برای مثال تاس سنگین:
- $P(X=1) = 0.1,\, P(X=2) = 0.15,\, P(X=3) = 0.20$
- $P(X=4) = 0.25,\, P(X=5) = 0.20,\, P(X=6) = 0.10$
- مجموع: $0.1 + 0.15 + 0.20 + 0.25 + 0.20 + 0.10 = 1.0$ ✓

:::{admonition} چرا این فرمول کار می‌کند
:class: note

PMF دسته‌ای ساده است — هر پیامد احتمال اختصاصی خود را دارد:

- **آزمایش تکی**: فقط یک پیامد رخ می‌دهد
- **هر پیامد $i$ احتمال $p_i$ دارد**: مستقیماً مشخص می‌شود
- **قید**: همه احتمال‌ها باید مجموع ۱ شوند (تضمین دقیقاً یک پیامد)

این عمومی‌ترین توزیع گسسته برای آزمایش تکی است — هر پیامد می‌تواند احتمال متفاوت داشته باشد. توزیع‌های ساده‌تر را تعمیم می‌دهد:
- اگر $k=2$: به **Bernoulli** تقلیل می‌یابد
- اگر همه $p_i = 1/k$: به **Discrete Uniform** تقلیل می‌یابد
:::

**ویژگی‌های کلیدی**

- **سناریوها**: تاس سنگین، انتخاب مشتری از دسته‌های منو، پاسخ نظرسنجی (چندگزینه‌ای)، وضعیت آب‌وهوا (آفتابی/ابری/بارانی/برفی)
- **پارامترها**:
    - $k$: تعداد دسته‌ها
    - $p_1, p_2, \ldots, p_k$: احتمال هر دسته (باید مجموع ۱ شود)
- **متغیر تصادفی**: $X \in \{1, 2, \ldots, k\}$

**امید ریاضی:** $E[X] = \sum_{i=1}^k i \cdot p_i$ (میانگین وزنی پیامدها)

**واریانس:** $Var(X) = \sum_{i=1}^k i^2 \cdot p_i - \left(\sum_{i=1}^k i \cdot p_i\right)^2$

**ارتباط با توزیع‌های دیگر:** Categorical **Bernoulli** را تعمیم می‌دهد (وقتی $k=2$) و حالت خاص **Discrete Uniform** است (وقتی همه $p_i$ برابرند). برای آزمایش‌های متعدد از **توزیع Multinomial** استفاده کنید.

**مصورسازی توزیع**

بیایید توزیع Categorical تاس سنگین را مصور کنیم:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_categorical_pmf.svg'):
    os.remove('ch07_categorical_pmf.svg')

# Create Categorical distribution for visualization (loaded die)
probs_viz = np.array([0.1, 0.15, 0.20, 0.25, 0.20, 0.10])
from scipy.stats import rv_discrete
values_viz = np.arange(1, 7)
categorical_viz = rv_discrete(values=(values_viz, probs_viz))

# Plotting the PMF
plt.figure(figsize=(8, 3.5))
plt.bar(values_viz, probs_viz, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Categorical PMF (Loaded Die)")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.ylim(0, 0.3)
plt.xticks(values_viz)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_categorical_pmf.svg', format='svg', bbox_inches='tight')
```
PMF احتمال‌های متفاوت هر وجه تاس سنگین را نشان می‌دهد.
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_categorical_cdf.svg'):
    os.remove('ch07_categorical_cdf.svg')

# Plotting the CDF
cdf_values_viz = categorical_viz.cdf(values_viz)

plt.figure(figsize=(8, 3.5))
plt.step(values_viz, cdf_values_viz, where='post', color='darkgreen', linewidth=2)
plt.title("Categorical CDF (Loaded Die)")
plt.xlabel("Outcome")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.ylim(0, 1.1)
plt.xticks(values_viz)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_categorical_cdf.svg', format='svg', bbox_inches='tight')
```
CDF با مقادیر متفاوت در هر مقدار افزایش می‌یابد و احتمال‌های متغیر را منعکس می‌کند.

:::{admonition} مثال: انتخاب محصول مشتری
:class: tip

یک کافی‌شاپ ترجیحات نوشیدنی مشتریان را ثبت می‌کند: ۴۰٪ قهوه، ۳۰٪ چای، ۲۰٪ آب‌میوه و ۱۰٪ آب.

این را با توزیع Categorical و [`scipy.stats.rv_discrete`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_discrete.html) مدل می‌کنیم.

**راه‌اندازی توزیع:**

یک توزیع دسته‌ای با احتمال‌های سفارشی برای هر دسته می‌سازیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Define the categorical distribution
choices = np.array([1, 2, 3, 4])  # 1=Coffee, 2=Tea, 3=Juice, 4=Water
probs = np.array([0.40, 0.30, 0.20, 0.10])
categorical_rv = stats.rv_discrete(values=(choices, probs))
```
**نمایش احتمال‌ها:**

احتمال هر انتخاب نوشیدنی را می‌بینیم:
```{code-cell} ipython3
# PMF: Probability of each choice
labels = ['Coffee', 'Tea', 'Juice', 'Water']
for i, (choice, label) in enumerate(zip(choices, labels)):
    print(f"P(X={choice}) [{label}]: {probs[i]:.2f}")
```
قهوه محتمل‌ترین انتخاب (۴۰٪) است، سپس چای (۳۰٪)، آب‌میوه (۲۰٪) و آب (۱۰٪). برخلاف توزیع یکنواخت، این احتمال‌ها متفاوت‌اند.

**محاسبه احتمال‌های تجمعی:**

احتمال انتخاب قهوه یا چای (دسته‌های ۱ یا ۲) چقدر است؟
```{code-cell} ipython3
# CDF: Probability of choice i or lower
print(f"P(X <= 2) [Coffee or Tea]: {categorical_rv.cdf(2):.2f}")
print(f"P(X > 2) [Juice or Water]: {1 - categorical_rv.cdf(2):.2f}")
```
۷۰٪ احتمال انتخاب قهوه یا چای و ۳۰٪ آب‌میوه یا آب وجود دارد.

**محاسبه امید ریاضی و واریانس:**

اگرچه امید ریاضی و واریانس برای داده دسته‌ای با شماره‌گذاری دلخواه کمتر قابل تفسیرند، scipy می‌تواند محاسبه کند:
```{code-cell} ipython3
# Mean and Variance
print(f"Mean (Expected value): {categorical_rv.mean():.2f}")
print(f"Variance: {categorical_rv.var():.2f}")
```
امید ریاضی ۲.۰۰ نشان می‌دهد انتخاب‌ها به سمت شماره‌های دسته پایین‌تر (قهوه و چای) وزن دارند.

**تولید نمونه‌های تصادفی:**

۱۰۰ مشتری را شبیه‌سازی می‌کنیم و می‌بینیم چند نفر هر نوشیدنی را انتخاب می‌کنند:
```{code-cell} ipython3
# Generate random samples
n_customers = 100
samples = categorical_rv.rvs(size=n_customers)
print(f"\nSimulated choices for {n_customers} customers:")
for i, label in enumerate(labels, 1):
    count = np.sum(samples == i)
    print(f"{label}: {count} ({count/n_customers:.1%})")
```
شمارش‌های شبیه‌سازی‌شده باید به احتمال‌های نظری (۴۰٪، ۳۰٪، ۲۰٪، ۱۰٪) نزدیک شوند با کمی تغییر تصادفی.

**مصورسازی PMF:**

نمودار میله‌ای احتمال‌های متفاوت هر دسته را به‌وضوح نشان می‌دهد:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_categorical_pmf_example.svg'):
    os.remove('ch07_categorical_pmf_example.svg')

# Plotting the PMF
plt.figure(figsize=(8, 3.5))
plt.bar(choices, probs, tick_label=labels, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Categorical PMF (Customer Drink Choice)")
plt.xlabel("Choice")
plt.ylabel("Probability")
plt.ylim(0, 0.5)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_categorical_pmf_example.svg', format='svg', bbox_inches='tight')
```
PMF ارتفاع میله‌های نابرابر نشان می‌دهد و آن را از توزیع یکنواخت گسسته متمایز می‌کند. قهوه (۴۰٪) بلندترین میله و آب (۱۰٪) کوتاه‌ترین است و ترجیحات مشتری را به‌وضوح مصور می‌کند.
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_categorical_cdf_example.svg'):
    os.remove('ch07_categorical_cdf_example.svg')

# Plotting the CDF
cdf_vals = categorical_rv.cdf(choices)

plt.figure(figsize=(8, 3.5))
plt.step(choices, cdf_vals, where='post', color='darkgreen', linewidth=2)
plt.xticks(choices, labels)
plt.title("Categorical CDF (Customer Drink Choice)")
plt.xlabel("Choice")
plt.ylabel("Cumulative Probability P(X <= k)")
plt.ylim(0, 1.1)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.savefig('ch07_categorical_cdf_example.svg', format='svg', bbox_inches='tight')
```
CDF احتمال‌های تجمعی در انتخاب‌های مرتب‌شده را نشان می‌دهد.

:::

**سؤالات مرور سریع**

۱. چراغ راهنمایی می‌تواند قرمز (۵۰٪)، زرد (۱۰٪) یا سبز (۴۰٪) باشد. کدام توزیع رنگ را هنگام رسیدن به تقاطع مدل می‌کند؟
```{admonition} پاسخ
:class: dropdown

**توزیع Categorical با k=3 دسته و احتمال‌های p₁=0.5, p₂=0.1, p₃=0.4** — آزمایش تکی با سه پیامد ممکن.
```
۲. برای توزیع Categorical با ۴ پیامد به‌طور برابر محتمل، P(X = 2) چقدر است؟
```{admonition} پاسخ
:class: dropdown

**P(X = 2) = 0.25** — برای پیامدهای به‌طور برابر محتمل، هر کدام احتمال ۱/۴ دارد.
```
۳. توزیع Categorical چه ارتباطی با توزیع Bernoulli دارد؟
```{admonition} پاسخ
:class: dropdown

**Bernoulli حالت خاص Categorical با k=2 است** — وقتی فقط دو دسته باشد، Categorical به Bernoulli تقلیل می‌یابد.

Categorical Bernoulli را از ۲ پیامد به k پیامد تعمیم می‌دهد.
```
۴. انتخاب یک مشتری از منوی ۵ قلمی با احتمال‌های [0.3, 0.25, 0.2, 0.15, 0.1] را مشاهده می‌کنید. از Categorical یا Multinomial استفاده کنید؟
```{admonition} پاسخ
:class: dropdown

**توزیع Categorical** — یک *آزمایش تکی* را مشاهده می‌کنید (یک مشتری یک انتخاب).

**تمایز کلیدی:**
- **Categorical**: آزمایش تکی، چند پیامد (این سناریو)
- **Multinomial**: آزمایش‌های متعدد، شمارش دفعات هر پیامد

اگر ۱۰۰ مشتری را مشاهده و شمارش کنید چند نفر هر قلم را انتخاب کردند، *آن* Multinomial است.
```
۵. چه زمانی می‌توانید توزیع Categorical را به‌عنوان Discrete Uniform مدل کنید؟
```{admonition} پاسخ
:class: dropdown

**وقتی همه k دسته احتمال برابر دارند** — اگر p₁ = p₂ = ... = pₖ = 1/k.

**مثال:**
- انداختن تاس منصفانه (۶ پیامد به‌طور برابر محتمل): می‌توان Categorical(p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) یا Discrete Uniform(a=1, b=6) استفاده کرد
- انداختن تاس سنگین (احتمال‌های نابرابر): باید Categorical استفاده شود

Discrete Uniform فقط حالت خاص Categorical است که همه احتمال‌ها برابرند.
```
+++
## ۹. توزیع Multinomial

توزیع Multinomial تعداد ثابتی آزمایش مستقل را مدل می‌کند که هر آزمایش چند پیامد ممکن (بیش از ۲) دارد و تعداد وقوع هر پیامد را می‌شماریم. تعمیم توزیع Binomial به بیش از دو دسته است.

**مثال ملموس**

فرض کنید تاس شش‌وجهی منصفانه ۲۰ بار می‌اندازید. می‌خواهیم بدانیم هر وجه (۱، ۲، ۳، ۴، ۵، ۶) چند بار ظاهر می‌شود.

این را با بردار تصادفی $\mathbf{X} = (X_1, X_2, X_3, X_4, X_5, X_6)$ مدل می‌کنیم که:
- $X_1$ = تعداد دفعات ظاهر شدن وجه ۱
- $X_2$ = تعداد دفعات ظاهر شدن وجه ۲
- ... و الی آخر
- قید: $X_1 + X_2 + X_3 + X_4 + X_5 + X_6 = 20$

احتمال‌های تاس منصفانه:
- $p_1 = p_2 = p_3 = p_4 = p_5 = p_6 = \frac{1}{6}$

**PMF چندجمله‌ای**

برای $n$ آزمایش مستقل با $k$ پیامد ممکن و احتمال‌های $p_1, p_2, \ldots, p_k$ که $\sum_{i=1}^k p_i = 1$:
$$ P(X_1=x_1, X_2=x_2, \ldots, X_k=x_k) = \frac{n!}{x_1! x_2! \cdots x_k!} \, p_1^{x_1} p_2^{x_2} \cdots p_k^{x_k} $$
که $x_1 + x_2 + \cdots + x_k = n$.

عبارت $\frac{n!}{x_1! x_2! \cdots x_k!}$ ضریب چندجمله‌ای است (بخش [فصل ۳: جایگشت اشیای یکسان](chapter_03.md#permutations-of-identical-objects) را ببینید).

برای مثال تاس، احتمال گرفتن دقیقاً (۳، ۴، ۲، ۵، ۴، ۲) از هر وجه:
$$
\begin{align}
P(X_1=3, X_2=4, X_3=2, X_4=5, X_5=4, X_6=2) &= \frac{20!}{3! \, 4! \, 2! \, 5! \, 4! \, 2!} \left(\frac{1}{6}\right)^{20} \\
&= 1.34 \times 10^{13} \times 3.39 \times 10^{-16} \\
&\approx 0.00454
\end{align}
$$
:::{admonition} چرا این فرمول کار می‌کند
:class: note

فرمول Multinomial ایده Binomial را به چند دسته گسترش می‌دهد:

- **$\frac{n!}{x_1! x_2! \cdots x_k!}$**: ضریب چندجمله‌ای می‌شمارد چند دنباله متفاوت از $n$ آزمایش دقیقاً $x_1$ وقوع دسته ۱، $x_2$ دسته ۲ و غیره تولید می‌کنند
- **$p_1^{x_1} p_2^{x_2} \cdots p_k^{x_k}$**: احتمال هر دنباله مشخص با آن شمارش‌ها

**مثال:** با ۳ آزمایش و پیامدها (A, A, B):
- $\frac{3!}{2! \, 1!} = 3$ چینش وجود دارد: AAB, ABA, BAA
- هر کدام احتمال $p_A^2 p_B^1$ دارد
- ترکیب: $3 \times p_A^2 p_B$

ضریب چندجمله‌ای مانند ضریب دوجمله‌ای است، اما برای توزیع $n$ مورد بین $k$ دسته به‌جای فقط ۲.
:::

**ویژگی‌های کلیدی**

- **سناریوها**: انداختن تاس n بار (شمارش هر وجه)، نظرسنجی با گزینه‌های چندگانه، خرید مشتری در دسته‌های محصول، فراوانی بازهای DNA در توالی
- **پارامترها**:
    - $n$: تعداد آزمایش‌ها
    - $k$: تعداد دسته‌ها
    - $p_1, p_2, \ldots, p_k$: احتمال هر دسته (باید مجموع ۱ شود)
- **متغیرهای تصادفی**: $X_1, X_2, \ldots, X_k$ که $X_i$ = شمارش دسته $i$ و $\sum_{i=1}^k X_i = n$

**امید ریاضی هر دسته:** $E[X_i] = n p_i$

**واریانس هر دسته:** $Var(X_i) = n p_i (1-p_i)$

**ارتباط با توزیع‌های دیگر:** Multinomial **Binomial** (وقتی $k=2$) و **Categorical** (آزمایش تکی به چند آزمایش) را تعمیم می‌دهد. هر شمارش دسته $X_i$ از توزیع **Binomial** با پارامترهای $(n, p_i)$ پیروی می‌کند.

**مصورسازی توزیع**

توزیع‌های Multinomial به‌دلیل چندمتغیره بودن مصورسازی دشوار دارند. حالت ساده با $k=3$ دسته را می‌بینیم:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_multinomial_marginal.svg'):
    os.remove('ch07_multinomial_marginal.svg')

# Simulate multinomial: rolling a 3-sided die 15 times
n_trials = 15
probs_3 = np.array([1/3, 1/3, 1/3])

# Generate many samples
n_sims = 10000
samples = np.random.multinomial(n_trials, probs_3, size=n_sims)

# Plot distribution of outcomes for Category 1 (marginal distribution)
category_1_counts = samples[:, 0]

plt.figure(figsize=(8, 3.5))
plt.hist(category_1_counts, bins=np.arange(0, n_trials+2)-0.5, density=True,
         color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Marginal Distribution of Category 1\n(Multinomial with n={n_trials}, k=3, all p=1/3)")
plt.xlabel("Count for Category 1")
plt.ylabel("Probability")
plt.xticks(range(0, n_trials+1))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('ch07_multinomial_marginal.svg', format='svg', bbox_inches='tight')
```
توزیع حاشیه‌ای هر دسته تکی در Multinomial در واقع Binomial است! اینجا دسته ۱ از Binomial(n=15, p=1/3) پیروی می‌کند.

**ارتباط با مثال تاس:** برای مصورسازی آسان‌تر به ۳ دسته ساده کردیم، اما همان اصل برای تاس شش‌وجهی (n=20 پرتاب) برقرار است. شمارش هر وجه از Binomial(n=20, p=1/6) پیروی می‌کند. هیستوگرام مشابه است اما حول 20/6 ≈ 3.33 به‌جای 15/3 = 5 متمرکز است.

:::{admonition} مثال: خرید محصول مشتری
:class: tip

یک فروشگاه خرید در ۴ دسته محصول را ثبت می‌کند: الکترونیک (۳۰٪)، پوشاک (۲۵٪)، لوازم خانگی (۲۵٪)، غذا (۲۰٪). ۵۰ مشتری را مشاهده و شمارش می‌کنیم چند نفر از هر دسته خرید می‌کنند.

از [`numpy.random.multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multinomial.html) برای کار با این توزیع استفاده می‌کنیم.

**تنظیم پارامترها و محاسبه مقادیر مورد انتظار:**

ابتدا پارامترهای multinomial را تعریف و شمارش‌های مورد انتظار را می‌بینیم:
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Define parameters
n_customers = 50
categories = ['Electronics', 'Clothing', 'Home Goods', 'Food']
probs = np.array([0.30, 0.25, 0.25, 0.20])

# Expected counts
expected_counts = n_customers * probs
print("Expected purchases per category:")
for cat, exp in zip(categories, expected_counts):
    print(f"  {cat}: {exp:.1f}")
```
با ۵۰ مشتری، انتظار ۱۵ خرید الکترونیک (۳۰٪)، ۱۲.۵ برای پوشاک و لوازم خانگی (۲۵٪) و ۱۰ برای غذا (۲۰٪) داریم.

**تولید یک نمونه:**

یک روز ۵۰ مشتری را شبیه‌سازی می‌کنیم و می‌بینیم چند نفر از هر دسته خرید می‌کنند:
```{code-cell} ipython3
# Generate one sample (one set of 50 customers)
one_sample = np.random.multinomial(n_customers, probs)
print(f"\nOne simulation of {n_customers} customers:")
for cat, count in zip(categories, one_sample):
    print(f"  {cat}: {count}")
print(f"Total: {np.sum(one_sample)}")
```
توجه کنید مجموع همیشه دقیقاً ۵۰ است — هر مشتری دقیقاً یک دسته انتخاب می‌کند. شمارش‌های فردی به‌دلیل تصادف حول مقادیر مورد انتظار متغیرند.

**تحلیل توزیع با شبیه‌سازی‌های متعدد:**

روزهای زیادی را شبیه‌سازی می‌کنیم تا تغییرپذیری شمارش هر دسته را بفهمیم:
```{code-cell} ipython3
# Generate many samples to see the distribution
n_sims = 10000
samples = np.random.multinomial(n_customers, probs, size=n_sims)

# Compute mean and std for each category
for i, cat in enumerate(categories):
    counts = samples[:, i]
    print(f"{cat}:")
    print(f"  Mean: {np.mean(counts):.2f} (theoretical: {n_customers * probs[i]:.2f})")
    print(f"  Std: {np.std(counts):.2f} (theoretical: {np.sqrt(n_customers * probs[i] * (1-probs[i])):.2f})")
```
میانگین‌های شبیه‌سازی‌شده باید نزدیک مقادیر نظری (n × p_i) باشند و انحراف‌های معیار از فرمول دوجمله‌ای √(n × p_i × (1-p_i)) پیروی کنند چون توزیع حاشیه‌ای هر دسته دوجمله‌ای است.

**مصورسازی توزیع‌های حاشیه‌ای:**

توزیع شمارش هر دسته را جداگانه رسم می‌کنیم:
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_multinomial_example.svg'):
    os.remove('ch07_multinomial_example.svg')

# Plot distributions for each category
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, (cat, ax) in enumerate(zip(categories, axes)):
    counts = samples[:, i]
    ax.hist(counts, bins=np.arange(0, n_customers+2)-0.5, density=True,
            color='skyblue', edgecolor='black', alpha=0.7)
    ax.axvline(expected_counts[i], color='red', linestyle='--', linewidth=2, label=f'Expected: {expected_counts[i]:.1f}')
    ax.set_title(f"{cat} (p={probs[i]})")
    ax.set_xlabel("Number of Purchases")
    ax.set_ylabel("Probability")
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('ch07_multinomial_example.svg', format='svg', bbox_inches='tight')
```
هر زیرنمودار توزیع یک دسته در ۱۰,۰۰۰ شبیه‌سازی را نشان می‌دهد. هیستوگرام‌ها زنگوله‌ای و حول مقادیر مورد انتظار (خطوط چین قرمز) متمرکزند. الکترونیک (p=0.30) بالاترین شمارش مورد انتظار (۱۵) و غذا (p=0.20) پایین‌ترین (۱۰) را دارد. توزیع حاشیه‌ای هر دسته دوجمله‌ای با پارامترهای (n=50, p=احتمال دسته) است، اما مهم است که این شمارش‌ها مستقل نیستند — باید مجموع ۵۰ شوند.

:::

**سؤالات مرور سریع**

۱. سکه منصفانه ۳۰ بار می‌اندازید و شیر و خط را می‌شمارید. کدام توزیع شمارش‌ها را مدل می‌کند؟
```{admonition} پاسخ
:class: dropdown

**توزیع Multinomial با n=30, k=2 و p₁=p₂=0.5** — یا معادل آن، Binomial(n=30, p=0.5) برای تعداد شیر، چون فقط ۲ دسته داریم.

وقتی k=2، Multinomial همان Binomial است.
```
۲. برای توزیع Multinomial با n=100 آزمایش و k=4 دسته به‌طور برابر محتمل، شمارش مورد انتظار هر دسته چقدر است؟
```{admonition} پاسخ
:class: dropdown

**E[X_i] = n × p_i = 100 × 0.25 = 25** — انتظار می‌رود هر دسته ۲۵ بار ظاهر شود.

چون هر ۴ دسته به‌طور برابر محتمل‌اند، p_i = 1/4 = 0.25 برای هر کدام.
```
۳. توزیع Multinomial چه ارتباطی با توزیع Binomial دارد؟
```{admonition} پاسخ
:class: dropdown

**Binomial حالت خاص Multinomial با k=2 است** — وقتی فقط دو دسته باشد، Multinomial به Binomial تقلیل می‌یابد.

Multinomial Binomial را از ۲ پیامد به k پیامد در آزمایش‌های متعدد تعمیم می‌دهد.
```
۴. تاس ۱۰۰ بار می‌اندازید و می‌شمارید هر وجه (۱-۶) چند بار ظاهر می‌شود. از Categorical یا Multinomial استفاده کنید؟
```{admonition} پاسخ
:class: dropdown

**توزیع Multinomial** — *آزمایش‌های متعدد* (۱۰۰ پرتاب) انجام می‌دهید و تعداد وقوع هر پیامد را می‌شمارید.

**تمایز کلیدی:**
- **Categorical**: آزمایش تکی، چند پیامد ممکن (یک پرتاب)
- **Multinomial**: آزمایش‌های متعدد، شمارش وقوع هر پیامد (۱۰۰ پرتاب)

برای تاس منصفانه از Multinomial(n=100, k=6, p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) استفاده کنید.
```
۵. در توزیع Multinomial، رابطه بین شمارش‌های دسته‌ای X₁, X₂, ..., Xₖ چیست؟
```{admonition} پاسخ
:class: dropdown

**باید مجموع n شوند** — قید: X₁ + X₂ + ... + Xₖ = n

چون هر آزمایش باید دقیقاً یک دسته داشته باشد، مجموع شمارش همه دسته‌ها برابر تعداد آزمایش‌هاست.

**پیامد مهم:** شمارش‌ها *مستقل نیستند* — اگر k-1 شمارش را بدانید، آخری را می‌توان تعیین کرد.

**مثال:** اگر n=100 و X₁=30, X₂=25, X₃=20 در حالت k=4 بدانید، X₄ باید ۲۵ باشد (چون 30+25+20+25=100).
```
+++
## ۱۰. روابط بین توزیع‌ها

درک ارتباط بین این توزیع‌ها بینش را عمیق‌تر می‌کند و تقریب‌های مفیدی فراهم می‌کند.

۱.  **Bernoulli به‌عنوان حالت خاص Binomial**: توزیع Binomial با $n=1$ آزمایش ($Binomial(1, p)$) معادل توزیع Bernoulli ($Bernoulli(p)$) است.

۲.  **Geometric به‌عنوان حالت خاص Negative Binomial**: توزیع Negative Binomial که تعداد آزمایش‌ها تا اولین موفقیت را مدل می‌کند ($r=1$) ($NegativeBinomial(1, p)$) معادل توزیع Geometric ($Geometric(p)$) است.

۳.  **تقریب Binomial برای Hypergeometric**: اگر اندازه جامعه $N$ بسیار بزرگ‌تر از اندازه نمونه $n$ باشد (مثلاً $N > 20n$)، کشیدن بدون جایگزینی (Hypergeometric) بسیار شبیه کشیدن با جایگزینی است. در این حالت، توزیع Hypergeometric($N, K, n$) را می‌توان با Binomial($n, p=K/N$) به‌خوبی تقریب زد. ضریب اصلاح جامعه متناهی $\frac{N-n}{N-1}$ به ۱ نزدیک می‌شود.

۴.  **تقریب Poisson برای Binomial**: اگر تعداد آزمایش‌ها $n$ در Binomial بزرگ و احتمال موفقیت $p$ کوچک باشد، به‌طوری که امید ریاضی $\lambda = np$ متوسط باشد، Binomial($n, p$) را می‌توان با Poisson($\lambda = np$) به‌خوبی تقریب زد. این مفید است چون PMF پواسون وقتی $n$ بزرگ است اغلب محاسبه‌اش از PMF دوجمله‌ای ساده‌تر است. قاعده سرانگشتی رایج: اگر $n \ge 20$ و $p \le 0.05$، یا $n \ge 100$ و $np \le 10$ از این تقریب استفاده کنید.

**مثال: تقریب Poisson برای Binomial**
$Binomial(n=1000, p=0.005)$ را در نظر بگیرید. اینجا $n$ بزرگ و $p$ کوچک است. امید ریاضی $\lambda = np = 1000 \times 0.005 = 5$ است. می‌توان با $Poisson(\lambda=5)$ تقریب زد.

بیایید مقادیر PMF هر دو توزیع را مقایسه کنیم تا ببینیم تقریب Poisson در عمل چقدر خوب کار می‌کند.
```{code-cell} ipython3
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Setup distributions
n_binom_approx = 1000
p_binom_approx = 0.005
lambda_approx = n_binom_approx * p_binom_approx

binom_rv_approx = stats.binom(n=n_binom_approx, p=p_binom_approx)
poisson_rv_approx = stats.poisson(mu=lambda_approx)

# Compare PMFs
k_vals_compare = np.arange(0, 15)
binom_pmf = binom_rv_approx.pmf(k_vals_compare)
poisson_pmf = poisson_rv_approx.pmf(k_vals_compare)

print(f"Comparing Binomial(n={n_binom_approx}, p={p_binom_approx}) and Poisson(lambda={lambda_approx:.1f})")
print("k\tBinomial P(X=k)\tPoisson P(X=k)\tDifference")
for k, bp, pp in zip(k_vals_compare, binom_pmf, poisson_pmf):
    print(f"{k}\t{bp:.6f}\t{pp:.6f}\t{abs(bp-pp):.6f}")
```
```{code-cell} ipython3
:tags: [remove-input, remove-output]

# Remove existing SVG if present
if os.path.exists('ch07_poisson_binomial_approximation.svg'):
    os.remove('ch07_poisson_binomial_approximation.svg')

# Plotting the comparison
plt.figure(figsize=(10, 4))
plt.bar(k_vals_compare - 0.2, binom_pmf, width=0.4, label=f'Binomial(n={n_binom_approx}, p={p_binom_approx})', align='center', color='skyblue', edgecolor='black', alpha=0.7)
plt.bar(k_vals_compare + 0.2, poisson_pmf, width=0.4, label=f'Poisson(lambda={lambda_approx:.1f})', align='center', color='lightcoral', edgecolor='black', alpha=0.7)
plt.title("Poisson Approximation to Binomial")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Probability")
plt.xticks(k_vals_compare)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('ch07_poisson_binomial_approximation.svg', format='svg', bbox_inches='tight')
```
نمودار توزیع Binomial(100, 0.03) (میله‌های آبی) را با تقریب Poisson(3.0) (میله‌های قرمز) مقایسه می‌کند. توزیع‌ها تقریباً یکسان‌اند و نشان می‌دهند وقتی n بزرگ و p کوچک است، Poisson تقریب عالی و محاسباتی ساده‌تری برای Binomial است.

۵.  **Categorical به‌عنوان تعمیم Bernoulli**: توزیع Categorical با $k=2$ دسته ($Categorical(p_1, p_2)$ که $p_1 + p_2 = 1$) معادل Bernoulli ($Bernoulli(p_1)$) است. Categorical Bernoulli را برای بیش از دو پیامد در آزمایش تکی گسترش می‌دهد.

۶.  **Multinomial به‌عنوان تعمیم Binomial**: توزیع Multinomial با $k=2$ دسته ($Multinomial(n, p_1, p_2)$ که $p_1 + p_2 = 1$) معادل Binomial ($Binomial(n, p_1)$) است. Multinomial Binomial را برای شمارش پیامدها در بیش از دو دسته گسترش می‌دهد.

۷.  **Discrete Uniform به‌عنوان حالت خاص Categorical**: توزیع Categorical که همه $k$ احتمال برابر دارند ($p_1 = p_2 = \cdots = p_k = \frac{1}{k}$) توزیع Discrete Uniform روی $k$ مقدار است. این بیشترین عدم‌قطعیت درباره پیامد آزمایش تکی را نشان می‌دهد.

۸.  **توزیع‌های حاشیه‌ای Multinomial دوجمله‌ای‌اند**: اگر $(X_1, X_2, \ldots, X_k) \sim Multinomial(n, p_1, p_2, \ldots, p_k)$، هر شمارش $X_i$ از Binomial پیروی می‌کند: $X_i \sim Binomial(n, p_i)$. منطقی است چون فقط موفقیت‌ها (دسته $i$) در برابر شکست‌ها (همه دسته‌های دیگر) در $n$ آزمایش را می‌شماریم.
+++
## خلاصه

در این فصل، نه توزیع بنیادین احتمال گسسته را بررسی کردیم:

* **Bernoulli**: آزمایش تکی، دو پیامد (موفقیت/شکست).
* **Binomial**: تعداد ثابت آزمایش مستقل، شمارش موفقیت‌ها.
* **Geometric**: تعداد آزمایش‌ها تا *اولین* موفقیت.
* **Negative Binomial**: تعداد آزمایش‌ها تا *تعداد ثابت* ($r$) موفقیت.
* **Poisson**: تعداد رویدادها در بازه ثابت زمان/فضا با نرخ متوسط داده‌شده.
* **Hypergeometric**: تعداد موفقیت‌ها در نمونه‌ای *بدون* جایگزینی از جامعه متناهی.
* **Discrete Uniform**: آزمایش تکی که همه پیامدها به‌طور برابر محتمل‌اند.
* **Categorical**: آزمایش تکی با چند پیامد ممکن، هر کدام با احتمال خود.
* **Multinomial**: تعداد ثابت آزمایش با چند پیامد ممکن، شمارش وقوع هر پیامد.

سناریوهایی را که هر توزیع مدل می‌کند، پارامترها، PMFها، امید ریاضی و واریانس را آموختیم. مهم‌تر، دیدیم چگونه از توابع `scipy.stats` (`pmf`, `cdf`, `rvs`, `mean`, `var`, `std`, `sf`) برای محاسبه، شبیه‌سازی و مصورسازی استفاده کنیم. روابط مهم را نیز بحث کردیم، از جمله:
- Bernoulli ↔ Binomial ↔ Categorical ↔ Multinomial (تعمیم‌ها)
- Discrete Uniform به‌عنوان حالت خاص Categorical
- تقریب Poisson برای Binomial
- تقریب Binomial برای Hypergeometric

تسلط بر این توزیع‌ها ابزار قدرتمندی برای مدل‌سازی پدیده‌های تصادفی در تحلیل داده، علم، مهندسی و کسب‌وکار فراهم می‌کند. در فصل‌های بعد به متغیرهای تصادفی پیوسته و توزیع‌های رایج متناظر می‌رویم.

**درخت تصمیم: انتخاب توزیع مناسب**

از این درخت تصمیم برای شناسایی توزیع متناسب با سناریوی خود استفاده کنید:
```{mermaid}
graph TD
    Start{چه چیزی را<br/>مدل می‌کنید؟}

    Start -->|آزمایش تکی| Single{چند<br/>پیامد؟}
    Start -->|آزمایش‌های متعدد| Multi{آزمایش‌های ثابت یا<br/>متغیر؟}
    Start -->|رویدادها در بازه| IntervalQ{نرخ متوسط<br/>ثابت؟}

    Single -->|فقط ۲| Bernoulli[Bernoulli]
    Single -->|بیش از ۲| MultiOut{همه پیامدها<br/>به‌طور برابر محتمل؟}

    MultiOut -->|بله| Uniform[Discrete Uniform]
    MultiOut -->|خیر| Categorical[Categorical]

    Multi -->|تعداد ثابت n| Fixed{چند پیامد<br/>در هر آزمایش؟}
    Multi -->|انتظار متغیر| Waiting{منتظر کدام<br/>موفقیت؟}

    Fixed -->|فقط ۲| TwoOut{نمونه‌گیری با یا<br/>بدون جایگزینی؟}
    Fixed -->|بیش از ۲| Multinomial[Multinomial]

    TwoOut -->|با جایگزینی<br/>یا جامعه نامتناهی| Binomial[Binomial]
    TwoOut -->|بدون جایگزینی<br/>جامعه متناهی| Hypergeometric[Hypergeometric]

    Waiting -->|اولین موفقیت| Geometric[Geometric]
    Waiting -->|موفقیت r-ام r>1| NegBinom[Negative Binomial]

    IntervalQ -->|بله| PoissonDist[Poisson]
    IntervalQ -->|سایر موارد| Other[بخش کاوش توزیع‌های<br/>بیشتر را ببینید]

    style Bernoulli fill:#e1f5ff
    style Binomial fill:#e1f5ff
    style Geometric fill:#e1f5ff
    style NegBinom fill:#e1f5ff
    style PoissonDist fill:#e1f5ff
    style Hypergeometric fill:#e1f5ff
    style Uniform fill:#ffe1f5
    style Categorical fill:#ffe1f5
    style Multinomial fill:#ffe1f5
```
**سؤالات کلیدی برای پرسیدن:**

۱. **چند آزمایش؟** تکی → Bernoulli/Categorical/Discrete Uniform. تعداد ثابت → Binomial/Multinomial/Hypergeometric. متغیر → Geometric/Negative Binomial.

۲. **چند پیامد در هر آزمایش؟** دو → Bernoulli/Binomial/Geometric/Negative Binomial. بیش از دو → Categorical/Multinomial/Discrete Uniform.

۳. **با یا بدون جایگزینی؟** با جایگزینی (یا جامعه نامتناهی) → Binomial. بدون جایگزینی (جامعه متناهی) → Hypergeometric.

۴. **چه چیزی را می‌شمارید؟** موفقیت‌ها در آزمایش‌های ثابت → Binomial/Multinomial. آزمایش‌ها تا موفقیت → Geometric/Negative Binomial. رویدادها در بازه → Poisson.

۵. **آیا احتمال‌ها برابرند؟** بله → Discrete Uniform. خیر → Categorical.

**مثال‌های کاربردی:**

- «یک بار سکه بیندازید» → Bernoulli (آزمایش تکی، ۲ پیامد)
- «۱۰ بار سکه بیندازید، شیرها را بشمارید» → Binomial (آزمایش‌های ثابت، ۲ پیامد، با جایگزینی)
- «تا رسیدن به ۶ تاس بیندازید» → Geometric (آزمایش‌های متغیر، منتظر اولین موفقیت)
- «۵ کارت از دسته بکشید، خشت‌ها را بشمارید» → Hypergeometric (آزمایش‌های ثابت، ۲ پیامد، بدون جایگزینی)
- «مشتریان رسیده در ساعت را بشمارید» → Poisson (رویدادها در بازه)
- «یک بار تاس بیندازید» → Discrete Uniform (آزمایش تکی، ۶ پیامد به‌طور برابر محتمل)
- «رنگ چراغ هنگام رسیدن» → Categorical (آزمایش تکی، ۳ پیامد با احتمال‌های متفاوت)
- «۲۰ بار تاس بیندازید، هر وجه را بشمارید» → Multinomial (آزمایش‌های ثابت، ۶ پیامد)

## کاوش توزیع‌های بیشتر

اگرچه این فصل نه توزیع گسسته بنیادین را پوشش می‌دهد، توزیع‌های بسیار دیگری برای سناریوهای تخصصی وجود دارند. نحوه یادگیری توزیع‌های فراتر از این فصل:

**چگونه یک توزیع جدید را یاد بگیریم:**

وقتی با توزیع جدیدی روبه‌رو می‌شوید، این گام‌ها را دنبال کنید:

۱. **سناریو را بفهمید**: چه فرایند دنیای واقعی را مدل می‌کند؟ چه تفاوتی با توزیع‌های آشنا دارد؟

۲. **پارامترها را شناسایی کنید**: چه مقادیری توزیع را تعریف می‌کنند؟ (مثل $n$ و $p$ برای Binomial، $\lambda$ برای Poisson)

۳. **PMF (یا PDF برای پیوسته) را مطالعه کنید**: احتمال‌ها چگونه محاسبه می‌شوند؟ فرمول چیست؟
   - PMF = تابع جرم احتمال (توزیع‌های گسسته، مانند این فصل)
   - PDF = تابع چگالی احتمال (توزیع‌های پیوسته، در فصل‌های ۸-۹)

۴. **ویژگی‌های کلیدی را بیاموزید**: امید ریاضی و واریانس چیست؟ ویژگی‌های خاصی دارد؟

۵. **روابط را کاوش کنید**: چه ارتباطی با توزیع‌های آشنا دارد؟ حالت خاص یا تعمیم چیزی آشناست؟

۶. **مثال‌ها را ببینید**: مثال‌های ملموس و مصورسازی برای ساخت شهود بیابید.

۷. **با کد تمرین کنید**: از `scipy.stats` یا کتابخانه‌های مشابه برای کار عملی با توزیع استفاده کنید.

**منابع کلیدی برای یادگیری توزیع‌های دیگر:**

۱. **ویکی‌پدیا** — هر توزیع مقاله جامعی با قالب استاندارد دارد:
   - تعریف و سناریو
   - پارامترها و پشتیبانی (مقادیر ممکن)
   - فرمول PMF (گسسته) یا PDF (پیوسته)
   - امید ریاضی، واریانس و سایر ویژگی‌ها
   - روابط با توزیع‌های دیگر
   - مثال‌ها و کاربردها
   - جستجو: «[نام توزیع] distribution» (مثلاً «Beta-Binomial distribution»)

۲. **مستندات SciPy** — ماژول `scipy.stats` پایتون بیش از ۱۰۰ توزیع دارد:
   - مرجع کامل: https://docs.scipy.org/doc/scipy/reference/stats.html
   - هر توزیع: PMF (گسسته) یا PDF (پیوسته)، CDF، امید ریاضی، واریانس، نمونه‌گیری تصادفی
   - شامل مثال‌های کد برای هر توزیع
   - توزیع‌های گسسته: `bernoulli`, `binom`, `geom`, `hypergeom`, `poisson`, `nbinom`, `randint` و بسیار دیگر

۳. **کاوشگرهای تعاملی توزیع**:
   - جستجو: «distribution explorer» یا «probability distribution visualizer»
   - این ابزارها پارامترها را تنظیم و تغییر توزیع را نشان می‌دهند
   - برای ساخت شهود درباره رفتار توزیع کمک می‌کند

۴. **کتاب‌های کلاسیک**:
   - *Introduction to Probability* اثر Bertsekas & Tsitsiklis
   - *A First Course in Probability* اثر Sheldon Ross
   - *Probability and Statistics* اثر DeGroot & Schervish
   - این‌ها با اثبات و استنتاج ریاضی دقیق ارائه می‌شوند

۵. **منابع آنلاین**:
   - **NIST Engineering Statistics Handbook**: مرجع جامع توزیع‌های رایج
   - **Wolfram MathWorld**: دانشنامه ریاضی با اطلاعات تفصیلی توزیع‌ها
   - **Stack Exchange (Cross Validated)**: سایت پرسش و پاسخ آمار

**مثال‌هایی از توزیع‌های گسسته دیگر:**

برخی توزیع‌هایی که ممکن است ببینید و در این فصل به‌تفصیل نپوشاندیم:

- **Beta-Binomial**: مانند Binomial، اما احتمال موفقیت $p$ خود تصادفی است (از آزمایش به آزمایش متغیر)
- **Logarithmic Distribution**: در بوم‌شناسی و نظریه اطلاعات
- **Zipf Distribution**: فراوانی کلمات، بازدید وب‌سایت (قانون توان)
- **Zero-Inflated Poisson**: Poisson با صفرهای اضافه، رایج در داده شمارشی
- **Conway-Maxwell-Poisson**: تعمیم Poisson با پارامتر پراکندگی اضافه
- **Benford's Law**: توزیع ارقام پیشرو در مجموعه‌داده‌های دنیای واقعی

**یافتن توزیع مناسب:**

اگر داده یا سناریو دارید و باید توزیع مناسب را بیابید:

۱. **فرایند را شناسایی کنید**: آزمایش تکی؟ آزمایش‌های ثابت؟ زمان انتظار؟ رویدادها در بازه؟

۲. **پشتیبانی را بررسی کنید**: متغیر تصادفی چه مقادیری می‌تواند بگیرد؟ (مثلاً ۰/۱، اعداد صحیح نامنفی، بازه متناهی)

۳. **پارامترها را در نظر بگیرید**: چه جنبه‌هایی از فرایند می‌توانند متغیر باشند؟ (احتمال موفقیت، نرخ، اندازه نمونه و غیره)

۴. **از درخت تصمیم** (در زیر) برای محدود کردن گزینه‌ها استفاده کنید

۵. **توزیع‌های نامزد را آزمایش کنید** با مصورسازی و آزمون‌های برازش

۶. **ادبیات حوزه را مطالعه کنید**: ببینید در رشته شما چه توزیع‌هایی رایج‌اند

:::{admonition} نکته کلیدی
:class: tip

درک ساختار احتمالاتی زیربنایی مهم‌تر از حفظ فرمول‌هاست. روی ساخت شهود درباره *چه زمانی* و *چرا* از هر توزیع استفاده کنید تمرکز کنید!
:::

## تمرین‌ها

۱. **ورود مشتریان:** میانگین مشتریان رسیده به کافه کوچک ۱۰ نفر در ساعت است. فرض کنید ورودها از توزیع Poisson پیروی می‌کنند.
    الف. احتمال رسیدن دقیقاً ۸ مشتری در یک ساعت مشخص چقدر است؟
    ب. احتمال رسیدن ۱۲ مشتری یا کمتر در یک ساعت مشخص چقدر است؟
    ج. احتمال رسیدن بیش از ۱۵ مشتری در یک ساعت مشخص چقدر است؟
    د. ۱۰۰۰ ساعت ورود مشتری را شبیه‌سازی و هیستوگرام نتایج را رسم کنید. با PMF نظری مقایسه کنید.
    ```{admonition} پاسخ
    :class: dropdown

    الف) با استفاده از توزیع Poisson با $\lambda = 10$:

    ```{code-cell} ipython3
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt

    lambda_cafe = 10
    cafe_rv = stats.poisson(mu=lambda_cafe)
    prob_8 = cafe_rv.pmf(8)
    print(f"P(Exactly 8 customers) = {prob_8:.4f}")
    ```
ب) احتمال ۱۲ مشتری یا کمتر:
    ```{code-cell} ipython3
    prob_12_or_fewer = cafe_rv.cdf(12)
    print(f"P(12 or fewer customers) = {prob_12_or_fewer:.4f}")
    ```
ج) احتمال بیش از ۱۵ مشتری:
    ```{code-cell} ipython3
    prob_over_15 = cafe_rv.sf(15)
    print(f"P(More than 15 customers) = {prob_over_15:.4f}")
    ```
د) شبیه‌سازی و مصورسازی:
    ```{code-cell} ipython3
    n_sim_hours = 1000
    sim_arrivals = cafe_rv.rvs(size=n_sim_hours)

    plt.figure(figsize=(10, 4))
    max_observed = np.max(sim_arrivals)
    bins = np.arange(0, max_observed + 2) - 0.5
    plt.hist(sim_arrivals, bins=bins, density=True, alpha=0.6, color='lightgreen', edgecolor='black', label='Simulated Arrivals')

    # Overlay theoretical PMF
    k_vals_cafe = np.arange(0, max_observed + 1)
    pmf_cafe = cafe_rv.pmf(k_vals_cafe)
    plt.plot(k_vals_cafe, pmf_cafe, 'ro-', linewidth=2, markersize=6, label='Theoretical PMF')

    plt.title(f'Simulated Customer Arrivals vs Poisson PMF (lambda={lambda_cafe})')
    plt.xlabel('Number of Customers per Hour')
    plt.ylabel('Probability / Density')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.xlim(-0.5, max_observed + 1.5)
    plt.show()
    ```
هیستوگرام به‌طور نزدیک با PMF نظری مطابقت دارد و مدل Poisson را تأیید می‌کند.
    ```

۲. **کنترل کیفیت:** یک دسته شامل ۵۰ قلم است که ۵ قلم آن معیوب است. ۸ قلم را به‌صورت تصادفی و بدون جایگزینی نمونه‌گیری می‌کنید.
    الف. چه توزیعی تعداد اقلام معیوب در نمونه شما را مدل می‌کند؟ پارامترها را بیان کنید.
    ب. احتمال اینکه دقیقاً ۱ قلم در نمونه شما معیوب باشد چقدر است؟
    ج. احتمال اینکه حداکثر ۲ قلم در نمونه شما معیوب باشد چقدر است؟
    د. تعداد مورد انتظار اقلام معیوب در نمونه شما چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    الف) این از توزیع Hypergeometric پیروی می‌کند زیرا بدون جایگزینی از یک جمعیت متناهی نمونه‌گیری می‌کنیم. پارامترها: $N=50$ (اندازه جمعیت)، $K=5$ (اقلام معیوب در جمعیت)، $n=8$ (اندازه نمونه).

    ```{code-cell} ipython3
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt

    N_qc = 50
    K_qc = 5
    n_qc = 8
    qc_rv = stats.hypergeom(M=N_qc, n=K_qc, N=n_qc)
    print(f"Distribution: Hypergeometric(N={N_qc}, K={K_qc}, n={n_qc})")
    ```
ب) احتمال دقیقاً ۱ قلم معیوب:
    ```{code-cell} ipython3
    prob_1_defective = qc_rv.pmf(1)
    print(f"P(Exactly 1 defective in sample) = {prob_1_defective:.4f}")
    ```
ج) احتمال حداکثر ۲ قلم معیوب:
    ```{code-cell} ipython3
    prob_at_most_2 = qc_rv.cdf(2)
    print(f"P(At most 2 defectives in sample) = {prob_at_most_2:.4f}")
    ```
د) تعداد مورد انتظار اقلام معیوب:
    ```{code-cell} ipython3
    expected_defective = qc_rv.mean()
    print(f"Expected number of defectives in sample = {expected_defective:.4f}")
    # Theoretical: E[X] = n * (K/N) = 8 * (5/50) = 0.8
    ```
    ```

۳. **موفقیت وب‌سایت:** یک قابلیت جدید وب‌سایت ۳٪ شانس استفاده توسط هر بازدیدکننده را دارد ($p=0.03$). فرض کنید بازدیدکنندگان مستقل هستند.
    الف. اگر ۱۰۰ بازدیدکننده به سایت بیایند، احتمال اینکه دقیقاً ۳ نفر از قابلیت استفاده کنند چقدر است؟ چه توزیعی اعمال می‌شود؟
    ب. احتمال اینکه ۵ بازدیدکننده یا کمتر از ۱۰۰ نفر از قابلیت استفاده کنند چقدر است؟
    ج. تعداد مورد انتظار کاربران از ۱۰۰ بازدیدکننده چقدر است؟
    د. یک توسعه‌دهنده قابلیت را تا اولین استفاده موفق کاربر بارها آزمایش می‌کند. احتمال وقوع اولین موفقیت در بازدیدکننده ۲۰ام چقدر است؟ چه توزیعی اعمال می‌شود؟
    ه. تعداد مورد انتظار بازدیدکنندگان تا مشاهده اولین موفقیت چقدر است؟
    و. تا مشاهده کاربر پنجم، چند بازدیدکننده مورد انتظار است؟ چه توزیعی اعمال می‌شود؟

    ```{admonition} پاسخ
    :class: dropdown

    الف) این از توزیع Binomial با $n=100$ آزمایش و $p=0.03$ پیروی می‌کند:

    ```{code-cell} ipython3
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt

    p_ws = 0.03
    n_ws = 100
    ws_binom_rv = stats.binom(n=n_ws, p=p_ws)
    prob_3_users = ws_binom_rv.pmf(3)
    print(f"Distribution: Binomial(n={n_ws}, p={p_ws})")
    print(f"P(Exactly 3 users) = {prob_3_users:.4f}")
    ```
ب) احتمال ۵ کاربر یا کمتر:
    ```{code-cell} ipython3
    prob_5_or_fewer = ws_binom_rv.cdf(5)
    print(f"P(5 or fewer users) = {prob_5_or_fewer:.4f}")
    ```
ج) تعداد مورد انتظار کاربران:
    ```{code-cell} ipython3
    expected_users = ws_binom_rv.mean()
    print(f"Expected number of users = {expected_users:.2f}")
    # Theoretical: E[X] = n*p = 100 * 0.03 = 3
    ```
د) این از توزیع Geometric پیروی می‌کند. احتمال وقوع اولین موفقیت در آزمایش ۲۰:
    ```{code-cell} ipython3
    ws_geom_rv = stats.geom(p=p_ws)
    prob_first_on_20 = ws_geom_rv.pmf(19)  # scipy counts 19 failures before success
    print(f"Distribution: Geometric(p={p_ws})")
    print(f"P(First success on trial 20) = {prob_first_on_20:.4f}")
    ```
ه) تعداد مورد انتظار بازدیدکنندگان تا اولین موفقیت:
    ```{code-cell} ipython3
    expected_trials_geom = 1 / p_ws
    print(f"Expected visitors until first success = {expected_trials_geom:.2f}")
    # Theoretical: E[X] = 1/p = 1/0.03 ≈ 33.33
    ```
و) این از توزیع Negative Binomial با $r=5$ موفقیت پیروی می‌کند:
    ```{code-cell} ipython3
    r_ws = 5
    expected_trials_nbinom = r_ws / p_ws
    print(f"Distribution: Negative Binomial(r={r_ws}, p={p_ws})")
    print(f"Expected visitors until 5th success = {expected_trials_nbinom:.2f}")
    # Theoretical: E[X] = r/p = 5/0.03 ≈ 166.67
    ```
    ```

