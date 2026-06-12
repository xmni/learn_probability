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
  - file: notebooks/chapter_12.ipynb
---

# فصل ۱۲: استقلال، کوواریانس و همبستگی

## مقدمه

در فصل پیشین، نحوهٔ توصیف هم‌زمان توزیع‌های احتمال چند متغیر تصادفی را با توزیع‌های مشترک بررسی کردیم. دیدیم چگونه توزیع‌های حاشیه‌ای و شرطی را از توزیع مشترک به‌دست آوریم. اکنون عمیق‌تر به روابط *بین* متغیرهای تصادفی می‌پردازیم.

چگونه می‌توان سنجید که آیا دانستن مقدار یک متغیر دربارهٔ دیگری اطلاعاتی به ما می‌دهد؟ آیا کاملاً بی‌ربط‌اند (مستقل)؟ یا تمایل دارند با هم حرکت کنند یا در جهت مخالف؟ این فصل سه مفهوم بنیادین برای توصیف این روابط را معرفی می‌کند:

1.  **استقلال:** قوی‌ترین شکل «بی‌ربطی»، جایی که مقدار یک متغیر هیچ اطلاعاتی دربارهٔ مقدار دیگری نمی‌دهد.
2.  **کوواریانس:** معیاری برای *جهت* رابطهٔ خطی بین دو متغیر.
3.  **همبستگی:** معیاری *استانداردشده* برای *قدرت و جهت* رابطهٔ خطی بین دو متغیر.

همچنین می‌بینیم این مفاهیم چگونه بر واریانس مجموع متغیرهای تصادفی اثر می‌گذارند — محاسبه‌ای حیاتی در حوزه‌هایی مانند مالی (واریانس سبد) و مهندسی (انتشار خطا).

**اهداف یادگیری:**

* تعریف و پیامدهای استقلال برای متغیرهای تصادفی را درک کنید.
* کوواریانس را تعریف، محاسبه و تفسیر کنید.
* ضریب همبستگی را تعریف، محاسبه، تفسیر کنید و ویژگی‌های آن را بشناسید.
* بیاموزید واریانس مجموع متغیرهای تصادفی را با در نظر گرفتن کوواریانس آن‌ها محاسبه کنید.
* این مفاهیم را با پایتون (NumPy، Pandas، Matplotlib/Seaborn) برای شبیه‌سازی، محاسبه و مصورسازی به‌کار ببرید.

```{code-cell} ipython3
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, uniform

# Set default plot style
plt.style.use('seaborn-v0_8-darkgrid')
# Set seed for reproducibility
np.random.seed(42)
```

## استقلال متغیرهای تصادفی

از فصل ۵ به‌خاطر بیاورید که دو واقعهٔ $A$ و $B$ مستقل‌اند اگر $P(A \cap B) = P(A)P(B)$. این مفهوم را به متغیرهای تصادفی تعمیم می‌دهیم.

**تعریف:** دو متغیر تصادفی $X$ و $Y$ **مستقل**‌اند اگر برای *هر* مجموعهٔ $A$ و $B$ (به‌ترتیب در دامنهٔ $X$ و $Y$)، واقعه‌های $\{X \in A\}$ و $\{Y \in B\}$ مستقل باشند. یعنی:

$$ P(X \in A, Y \in B) = P(X \in A) P(Y \in B) $$

این معادل است با اینکه تابع توزیع مشترک آن‌ها به حاصل‌ضرب توابع توزیع حاشیه‌ای فاکتور شود:

* **گسسته:** $P(X=x, Y=y) = P(X=x) P(Y=y)$ برای همهٔ مقادیر ممکن $x, y$. (PMF مشترک = حاصل‌ضرب PMFهای حاشیه‌ای)
* **پیوسته:** $f_{X,Y}(x,y) = f_X(x) f_Y(y)$ برای همهٔ $x, y$. (PDF مشترک = حاصل‌ضرب PDFهای حاشیه‌ای)

**شهود:** اگر $X$ و $Y$ مستقل باشند، دانستن پیامد $X$ هیچ اطلاعاتی دربارهٔ پیامد $Y$ نمی‌دهد و بالعکس.

**مثال:**
* فرض کنید $X$ پیامد پرتاب یک سکهٔ منصفانه (۰ برای خط، ۱ برای شیر) باشد. $P(X=0)=0.5, P(X=1)=0.5$.
* فرض کنید $Y$ پیامد پرتاب یک تاس شش‌وجهی منصفانه ({1, 2, 3, 4, 5, 6}) باشد. $P(Y=y)=1/6$ برای $y \in \{1, ..., 6\}$.
با فرض اینکه پرتاب سکه و تاس بر یکدیگر اثر نگذارند، $X$ و $Y$ مستقل‌اند. احتمال شیر ($X=1$) و آمدن ۴ ($Y=4$) برابر است با:
$P(X=1, Y=4) = P(X=1)P(Y=4) = (0.5) \times (1/6) = 1/12$.

**ضد‌مثال:**
* فرض کنید $H$ قد یک فرد و $W$ وزن او باشد. شهوداً افراد بلندتر تمایل به سنگین‌تر بودن دارند. دانستن اینکه کسی بسیار بلند است ($H$ بزرگ) احتمال بزرگ بودن وزن ($W$) را بیشتر می‌کند. بنابراین $H$ و $W$ معمولاً مستقل *نیستند*. انتظار نداریم $f_{H,W}(h,w) = f_H(h) f_W(w)$.

+++

### بررسی استقلال

در عمل، اغلب بر اساس ماهیت فیزیکی فرایندهای تولیدکنندهٔ متغیرهای تصادفی (مانند پرتاب‌های جداگانهٔ سکه) *فرض* می‌کنیم مستقل‌اند. اگر توزیع مشترک را داشته باشیم، می‌توانیم بررسی کنیم آیا به حاصل‌ضرب حاشیه‌ای‌ها فاکتور می‌شود. اگر فقط داده داریم، آزمون دقیق استقلال پیچیده است (شامل آزمون‌های فرض آماری فراتر از احتمال پایه). به‌زودی می‌بینیم که محاسبهٔ *همبستگی* سرنخی می‌دهد (اگر همبستگی غیرصفر باشد، وابسته‌اند؛ اگر صفر باشد، *ممکن است* مستقل باشند).

+++

## کوواریانس

اگر متغیرها مستقل نباشند، وابسته‌اند. کوواریانس معیاری است که *جهت* رابطهٔ خطی بین دو متغیر تصادفی را توصیف می‌کند.

**تعریف:** **کوواریانس** بین دو متغیر تصادفی $X$ و $Y$، با نماد $\mathrm{Cov}(X, Y)$ یا $\sigma_{XY}$، برابر است با:

$$ \mathrm{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] $$

این فرمول امید ریاضی حاصل‌ضرب انحراف‌های $X$ و $Y$ از میانگین‌هایشان را محاسبه می‌کند.

فرمول راحت‌تر برای محاسبه اغلب این است:

$$ \mathrm{Cov}(X, Y) = E[XY] - E[X]E[Y] $$

**تفسیر:**

* **$\mathrm{Cov}(X, Y) > 0$**: رابطهٔ خطی *مثبت* را نشان می‌دهد. وقتی $X$ بالاتر از میانگینش است، $Y$ تمایل دارد بالاتر از میانگینش باشد و بالعکس. (مثال: قد و وزن).
* **$\mathrm{Cov}(X, Y) < 0$**: رابطهٔ خطی *منفی* را نشان می‌دهد. وقتی $X$ بالاتر از میانگینش است، $Y$ تمایل دارد پایین‌تر از میانگینش باشد و بالعکس. (مثال: دما و هزینهٔ گرمایش).
* **$\mathrm{Cov}(X, Y) = 0$**: *عدم رابطهٔ خطی* را نشان می‌دهد. شرط لازم برای استقلال است، اما کافی نیست (بیشتر در ادامه).

**ویژگی‌ها:**

1.  $\mathrm{Cov}(X, X) = E[(X - E[X])^2] = \mathrm{Var}(X)$
2.  $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$ (متقارن)
3.  $\mathrm{Cov}(aX + b, cY + d) = ac \mathrm{Cov}(X, Y)$ برای ثابت‌های $a, b, c, d$. (مقیاس‌بندی بر کوواریانس اثر می‌گذارد)
4.  $\mathrm{Cov}(X+Y, Z) = \mathrm{Cov}(X, Z) + \mathrm{Cov}(Y, Z)$ (توزیع‌پذیر)
5.  اگر $X$ و $Y$ مستقل باشند، آنگاه $E[XY] = E[X]E[Y]$ و در نتیجه $\mathrm{Cov}(X, Y) = 0$.

**نکتهٔ مهم:** مقدار کوواریانس به واحدهای $X$ و $Y$ بستگی دارد. برای مثال، $\mathrm{Cov}(\text{Height in cm}, \text{Weight in kg})$ بسیار بزرگ‌تر از $\mathrm{Cov}(\text{Height in m}, \text{Weight in kg})$ خواهد بود، هرچند رابطهٔ زیربنایی یکسان است. این قضاوت دربارهٔ *قدرت* رابطه تنها از کوواریانس را دشوار می‌کند.

+++

### محاسبهٔ کوواریانس با NumPy

تابع `np.cov()` در NumPy ماتریس کوواریانس را محاسبه می‌کند. برای دو آرایهٔ یک‌بعدی `x` و `y`، `np.cov(x, y)` ماتریس ۲×۲ زیر را برمی‌گرداند:

$$
\begin{pmatrix}
\mathrm{Var}(X) & \mathrm{Cov}(X, Y) \\
\mathrm{Cov}(Y, X) & \mathrm{Var}(Y)
\end{pmatrix}
$$

معمولاً به عناصر خارج از قطر، یعنی $\mathrm{Cov}(X, Y)$، علاقه‌مندیم.

```{code-cell} ipython3
# Simulate two potentially related variables
n_samples = 1000
# X: Standard normal
x_samples = np.random.randn(n_samples)
# Y: Linearly related to X plus some noise
noise = np.random.randn(n_samples) * 0.5
y_samples_pos = 2 * x_samples + 1 + noise # Positive relationship
y_samples_neg = -1.5 * x_samples + 3 + noise # Negative relationship
y_samples_indep = np.random.randn(n_samples) # Independent

# Calculate covariance matrices
cov_matrix_pos = np.cov(x_samples, y_samples_pos)
cov_matrix_neg = np.cov(x_samples, y_samples_neg)
cov_matrix_indep = np.cov(x_samples, y_samples_indep)

# Extract the covariance values
cov_xy_pos = cov_matrix_pos[0, 1]
cov_xy_neg = cov_matrix_neg[0, 1]
cov_xy_indep = cov_matrix_indep[0, 1]

print(f"Covariance Matrix (X, Y_pos):\n{cov_matrix_pos}\n")
print(f"Cov(X, Y_pos): {cov_xy_pos:.4f}")
print(f"Cov(X, Y_neg): {cov_xy_neg:.4f}")
print(f"Cov(X, Y_indep): {cov_xy_indep:.4f}")
```

همان‌طور که انتظار می‌رود:
* `Cov(X, Y_pos)` مثبت است و نشان می‌دهد تمایل به افزایش هم‌زمان دارند.
* `Cov(X, Y_neg)` منفی است و نشان می‌دهد وقتی یکی افزایش می‌یابد، دیگری تمایل به کاهش دارد.
* `Cov(X, Y_indep)` نزدیک صفر است، سازگار با استقلال (یا حداقل عدم رابطهٔ خطی). مقدار کوچک غیرصفر به‌دلیل نوسان نمونه‌گیری تصادفی است.

+++

## ضریب همبستگی

برای غلبه بر وابستگی به واحد در کوواریانس و به‌دست آوردن معیاری از *قدرت* رابطهٔ خطی، از **ضریب همبستگی** استفاده می‌کنیم.

**تعریف:** ضریب همبستگی پیرسون بین دو متغیر تصادفی $X$ و $Y$، با نماد $\rho(X, Y)$، $\rho_{XY}$، یا گاهی $\mathrm{Corr}(X,Y)$، به‌صورت زیر تعریف می‌شود:

$$ \rho(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X) \mathrm{Var}(Y)}} $$

که در آن $\sigma_X$ و $\sigma_Y$ انحراف‌های معیار $X$ و $Y$ هستند، با فرض غیرصفر بودن آن‌ها.

**ویژگی‌ها:**

1.  **بازه:** $-1 \le \rho(X, Y) \le 1$. ضریب همبستگی بی‌بعد است.
2.  **رابطهٔ خطی:**
    * $\rho(X, Y) = 1$: رابطهٔ خطی مثبت کامل ($Y = aX + b$ با $a > 0$).
    * $\rho(X, Y) = -1$: رابطهٔ خطی منفی کامل ($Y = aX + b$ با $a < 0$).
    * $\rho(X, Y) = 0$: *عدم* رابطهٔ خطی.
3.  **تقارن:** $\rho(X, Y) = \rho(Y, X)$.
4.  **ناورایی نسبت به تبدیل خطی:** $\rho(aX + b, cY + d) = \mathrm{sign}(ac) \rho(X, Y)$، با فرض $a \ne 0, c \ne 0$. مقیاس‌بندی و جابه‌جایی متغیرها بزرگی همبستگی را تغییر نمی‌دهد، فقط ممکن است علامت را عوض کند.
5.  **استقلال به معنای همبستگی صفر:** اگر $X$ و $Y$ مستقل باشند، آنگاه $\mathrm{Cov}(X, Y) = 0$ و در نتیجه $\rho(X, Y) = 0$.

**هشدار مهم: همبستگی به معنای علیت نیست!** صرف همبسته بودن دو متغیر به این معنا نیست که یکی علت دیگری است. ممکن است متغیر پنهان (مخدوش‌کننده)‌ای هر دو را تحت تأثیر قرار دهد. (مثال کلاسیک: فروش بستنی و نرخ جرم‌و جنایت همبسته‌اند، اما هر دو ناشی از آب‌وهمای گرم‌ترند).

**هشدار مهم ۲: همبستگی صفر به معنای استقلال نیست!** همبستگی تنها وابستگی *خطی* را می‌سنجد. ممکن است $X$ و $Y$ به‌شدت وابستهٔ غیرخطی باشند، اما همبستگی صفر داشته باشند.

فرض کنید $X \sim \text{Uniform}(-1, 1)$ و $Y = X^2$. به‌وضوح $Y$ کاملاً به $X$ وابسته است.
$E[X] = 0$. $E[Y] = E[X^2] = \int_{-1}^{1} x^2 (1/2) dx = [x^3/6]_{-1}^1 = 1/3$.
$E[XY] = E[X^3] = \int_{-1}^{1} x^3 (1/2) dx = [x^4/8]_{-1}^1 = 0$.
$\mathrm{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0 - (0)(1/3) = 0$.
پس $\rho(X, Y) = 0$، هرچند $Y$ کاملاً توسط $X$ تعیین می‌شود.

+++

### محاسبه و مصورسازی همبستگی

می‌توانیم از `np.corrcoef()` یا متد `.corr()` در DataFrame پانداس استفاده کنیم. نمودارهای پراکندگی برای مصورسازی رابطه ضروری‌اند.

```{code-cell} ipython3
# Calculate correlation coefficients using the same samples
corr_matrix_pos = np.corrcoef(x_samples, y_samples_pos)
corr_matrix_neg = np.corrcoef(x_samples, y_samples_neg)
corr_matrix_indep = np.corrcoef(x_samples, y_samples_indep)

# Extract correlation values
corr_xy_pos = corr_matrix_pos[0, 1]
corr_xy_neg = corr_matrix_neg[0, 1]
corr_xy_indep = corr_matrix_indep[0, 1]

print(f"Correlation Matrix (X, Y_pos):\n{corr_matrix_pos}\n")
print(f"Corr(X, Y_pos): {corr_xy_pos:.4f}")
print(f"Corr(X, Y_neg): {corr_xy_neg:.4f}")
print(f"Corr(X, Y_indep): {corr_xy_indep:.4f}")

# Visualize the relationships
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharex=True, sharey=False)

axes[0].scatter(x_samples, y_samples_pos, alpha=0.6)
axes[0].set_title(f'Positive Correlation (rho approx {corr_xy_pos:.2f}$)')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y_pos')

axes[1].scatter(x_samples, y_samples_neg, alpha=0.6)
axes[1].set_title(f'Negative Correlation (rho approx {corr_xy_neg:.2f}$)')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y_neg')

axes[2].scatter(x_samples, y_samples_indep, alpha=0.6)
axes[2].set_title(f'Near Zero Correlation (rho approx {corr_xy_indep:.2f}$)')
axes[2].set_xlabel('X')
axes[2].set_ylabel('Y_indep')

plt.tight_layout()
plt.show()
```

نمودارهای پراکندگی روابطی را که ضریب‌های همبستگی نشان می‌دهند به‌صورت بصری تأیید می‌کنند. توجه کنید پراکندگی حول خط بالقوه چگونه بر بزرگی $\rho$ اثر می‌گذارد. در شبیه‌سازی ما، `Y_pos` رابطهٔ خطی قوی‌تری دارد (نویز نسبت به شیب کمتر) و در نتیجه $|\rho_{XY_{pos}}| > |\rho_{XY_{neg}}|$. حالت مستقل هیچ الگوی خطی مشخصی نشان نمی‌دهد.

+++

#### مثال: همبستگی بین ساعات مطالعه و نمرهٔ امتحان

بیایید داده‌ای شبیه‌سازی کنیم که در آن نمرهٔ امتحان به‌صورت خطی به ساعات مطالعه وابسته است، اما با کمی نوسان تصادفی.

```{code-cell} ipython3
n_students = 100
# Study hours: Uniformly distributed between 1 and 10 hours/week
study_hours = np.random.uniform(1, 10, n_students)
# Exam score: Base score + hours effect + random noise (normal)
base_score = 50
hours_effect = 5 * study_hours
noise = np.random.normal(0, 8, n_students) # Std dev of 8 points
exam_scores = base_score + hours_effect + noise
# Ensure scores are within a reasonable range (e.g., 0-100)
exam_scores = np.clip(exam_scores, 0, 100)

# Calculate Covariance and Correlation
cov_study_score = np.cov(study_hours, exam_scores)[0, 1]
corr_study_score = np.corrcoef(study_hours, exam_scores)[0, 1]

print(f"Covariance between Study Hours and Exam Score: {cov_study_score:.2f}")
print(f"Correlation between Study Hours and Exam Score: {corr_study_score:.2f}")

# Visualize
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores, alpha=0.7)
plt.title(f'Study Hours vs Exam Score (rho approx {corr_study_score:.2f}$)')
plt.xlabel('Study Hours per Week')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()
```

همبستگی مثبت رابطهٔ شبیه‌سازی‌شده را تأیید می‌کند: دانش‌آموزانی که بیشتر مطالعه می‌کنند تمایل به نمرهٔ بالاتر دارند. همبستگی ۱ نیست چون مؤلفهٔ نویز تصادفی وجود دارد (نمایانگر عوامل دیگری مانند استعداد ذاتی، اضطراب امتحان، شانس).

+++

## واریانس مجموع متغیرهای تصادفی

دانستن کوواریانس یا همبستگی هنگام محاسبهٔ واریانس مجموع یا تفاضل متغیرهای تصادفی حیاتی است.

**قضیه:** برای هر دو متغیر تصادفی $X$ و $Y$ و ثابت‌های $a$ و $b$:

$$ \mathrm{Var}(aX + bY) = a^2 \mathrm{Var}(X) + b^2 \mathrm{Var}(Y) + 2ab \mathrm{Cov}(X, Y) $$

**ایدهٔ اثبات:**
$\mathrm{Var}(aX + bY) = E[((aX + bY) - E[aX + bY])^2]$
$= E[(a(X - E[X]) + b(Y - E[Y]))^2]$
$= E[a^2(X - E[X])^2 + b^2(Y - E[Y])^2 + 2ab(X - E[X])(Y - E[Y])]$
با خطی بودن امید ریاضی:
$= a^2 E[(X - E[X])^2] + b^2 E[(Y - E[Y])^2] + 2ab E[(X - E[X])(Y - E[Y])]$
$= a^2 \mathrm{Var}(X) + b^2 \mathrm{Var}(Y) + 2ab \mathrm{Cov}(X, Y)$

**حالت ویژه: مجموع متغیرها ($a=1, b=1$)**

$$ \mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2 \mathrm{Cov}(X, Y) $$

**حالت ویژه: تفاضل متغیرها ($a=1, b=-1$)**

$$ \mathrm{Var}(X - Y) = \mathrm{Var}(X) + (-1)^2 \mathrm{Var}(Y) + 2(1)(-1) \mathrm{Cov}(X, Y) $$
$$ \mathrm{Var}(X - Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) - 2 \mathrm{Cov}(X, Y) $$

**ساده‌سازی مهم: متغیرهای مستقل**

اگر $X$ و $Y$ **مستقل** باشند، آنگاه $\mathrm{Cov}(X, Y) = 0$ و فرمول‌ها به‌طور قابل‌توجهی ساده می‌شوند:

$$ \mathrm{Var}(aX + bY) = a^2 \mathrm{Var}(X) + b^2 \mathrm{Var}(Y) \quad (\text{if independent}) $$
$$ \mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) \quad (\text{if independent}) $$
$$ \mathrm{Var}(X - Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) \quad (\text{if independent}) $$

**تعمیم به چند متغیر:**
برای $n$ متغیر تصادفی $X_1, X_2, ..., X_n$:

$$ \mathrm{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \mathrm{Var}(X_i) + \sum_{i \ne j} a_i a_j \mathrm{Cov}(X_i, X_j) $$
$$ \mathrm{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \mathrm{Var}(X_i) + 2 \sum_{i < j} a_i a_j \mathrm{Cov}(X_i, X_j) $$

اگر همهٔ $X_i$ مستقل باشند، آنگاه همهٔ $\mathrm{Cov}(X_i, X_j) = 0$ برای $i \ne j$ و:

$$ \mathrm{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \mathrm{Var}(X_i) \quad (\text{if independent}) $$

**مثال کاربردی: واریانس سبد**
فرض کنید سبد ساده‌ای با سرمایه‌گذاری $a$ در سهام A (بازده $X$) و سرمایه‌گذاری $b$ در سهام B (بازده $Y$) داریم. بازده کل $R = aX + bY$ است. ریسک (واریانس) سبد برابر است با:
$\mathrm{Var}(R) = a^2 \mathrm{Var}(X) + b^2 \mathrm{Var}(Y) + 2ab \mathrm{Cov}(X, Y)$.
اگر سهام‌ها همبستهٔ منفی داشته باشند ($\mathrm{Cov}(X, Y) < 0$)، واریانس سبد *کمتر* از نگه‌داشتن دارایی‌های غیرهمبسته می‌شود. این اصل تنوع‌بخشی است.

+++

### کار عملی: نمایش قواعد واریانس با شبیه‌سازی

بیایید قواعد واریانس را شبیه‌سازی و تأیید کنیم.

```{code-cell} ipython3
# Case 1: Independent Variables
n_samples = 100000
X_ind = np.random.normal(loc=5, scale=2, size=n_samples) # Mean=5, Var=4
Y_ind = np.random.normal(loc=10, scale=3, size=n_samples) # Mean=10, Var=9

# Theoretical values
var_X_th = 4
var_Y_th = 9
cov_XY_th_ind = 0 # Because independent
var_sum_th_ind = var_X_th + var_Y_th + 2 * cov_XY_th_ind
var_diff_th_ind = var_X_th + var_Y_th - 2 * cov_XY_th_ind

# Empirical values from simulation
var_X_emp = np.var(X_ind)
var_Y_emp = np.var(Y_ind)
cov_XY_emp_ind = np.cov(X_ind, Y_ind)[0, 1]
var_sum_emp_ind = np.var(X_ind + Y_ind)
var_diff_emp_ind = np.var(X_ind - Y_ind)

print("--- Independent Case ---")
print(f"Theoretical Var(X): {var_X_th:.4f}, Empirical Var(X): {var_X_emp:.4f}")
print(f"Theoretical Var(Y): {var_Y_th:.4f}, Empirical Var(Y): {var_Y_emp:.4f}")
print(f"Theoretical Cov(X, Y): {cov_XY_th_ind:.4f}, Empirical Cov(X, Y): {cov_XY_emp_ind:.4f}")
print(f"Theoretical Var(X+Y): {var_sum_th_ind:.4f}, Empirical Var(X+Y): {var_sum_emp_ind:.4f}")
print(f"Check: Var(X)+Var(Y) = {var_X_emp + var_Y_emp:.4f}")
print(f"Theoretical Var(X-Y): {var_diff_th_ind:.4f}, Empirical Var(X-Y): {var_diff_emp_ind:.4f}")
print(f"Check: Var(X)+Var(Y) = {var_X_emp + var_Y_emp:.4f}") # Should match Var(X-Y) for independent


# Case 2: Dependent Variables (Positively Correlated)
# Create Y based on X to induce correlation
Z = np.random.normal(loc=0, scale=1.5, size=n_samples) # Noise
Y_dep = 0.5 * X_ind + Z + 5 # Y depends on X

# Calculate empirical covariance and theoretical variance for Y_dep
cov_XY_emp_dep = np.cov(X_ind, Y_dep)[0, 1]
var_Y_emp_dep = np.var(Y_dep)
# Theoretical Var(Y_dep) = Var(0.5*X_ind + Z + 5) = Var(0.5*X_ind + Z) assuming X_ind and Z are independent
# = (0.5)^2 * Var(X_ind) + Var(Z) = 0.25 * 4 + (1.5)^2 = 1 + 2.25 = 3.25
var_Y_th_dep = 3.25
# Theoretical Cov(X, Y_dep) = Cov(X_ind, 0.5*X_ind + Z + 5)
# = Cov(X_ind, 0.5*X_ind) + Cov(X_ind, Z) + Cov(X_ind, 5)
# = 0.5 * Cov(X_ind, X_ind) + 0 + 0 = 0.5 * Var(X_ind) = 0.5 * 4 = 2
cov_XY_th_dep = 2

# Theoretical values for sums/differences
var_sum_th_dep = var_X_th + var_Y_th_dep + 2 * cov_XY_th_dep
var_diff_th_dep = var_X_th + var_Y_th_dep - 2 * cov_XY_th_dep

# Empirical values for sums/differences
var_sum_emp_dep = np.var(X_ind + Y_dep)
var_diff_emp_dep = np.var(X_ind - Y_dep)

print("\n--- Dependent Case (Positive Correlation) ---")
print(f"Empirical Var(X): {var_X_emp:.4f}") # Same X as before
print(f"Theoretical Var(Y_dep): {var_Y_th_dep:.4f}, Empirical Var(Y_dep): {var_Y_emp_dep:.4f}")
print(f"Theoretical Cov(X, Y_dep): {cov_XY_th_dep:.4f}, Empirical Cov(X, Y_dep): {cov_XY_emp_dep:.4f}")
print(f"Theoretical Var(X+Y_dep): {var_sum_th_dep:.4f}, Empirical Var(X+Y_dep): {var_sum_emp_dep:.4f}")
print(f"Check: Var(X)+Var(Y)+2Cov(X,Y) = {var_X_emp + var_Y_emp_dep + 2*cov_XY_emp_dep:.4f}")
print(f"Theoretical Var(X-Y_dep): {var_diff_th_dep:.4f}, Empirical Var(X-Y_dep): {var_diff_emp_dep:.4f}")
print(f"Check: Var(X)+Var(Y)-2Cov(X,Y) = {var_X_emp + var_Y_emp_dep - 2*cov_XY_emp_dep:.4f}")
```

نتایج شبیه‌سازی با محاسبات نظری بر اساس فرمول‌های واریانس، هم برای متغیرهای مستقل و هم وابسته، به‌خوبی مطابقت دارند. توجه کنید در حالت وابسته با کوواریانس مثبت، واریانس مجموع *افزایش* و واریانس تفاضل *کاهش* می‌یابد نسبت به حالت مستقل.

+++

## خلاصه

این فصل مفاهیم کلیدی برای درک روابط بین متغیرهای تصادفی را معرفی کرد:

* **استقلال:** متغیرها مستقل‌اند اگر دانستن مقدار یکی اطلاعاتی دربارهٔ دیگری ندهد. از نظر ریاضی، تابع توزیع مشترک آن‌ها به حاصل‌ضرب حاشیه‌ای‌ها فاکتور می‌شود.
* **کوواریانس:** جهت رابطهٔ *خطی* را می‌سنجد ($E[XY] - E[X]E[Y]$). کوواریانس مثبت یعنی تمایل به حرکت هم‌جهت؛ منفی یعنی حرکت در جهت مخالف؛ صفر یعنی عدم ارتباط خطی. بزرگی آن به واحدهای متغیرها بستگی دارد.
* **ضریب همبستگی ($\rho$):** معیار استانداردشده ($\frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$) برای قدرت و جهت رابطهٔ *خطی*، در بازهٔ $-1$ (خطی منفی کامل) تا $+1$ (خطی مثبت کامل). $\rho=0$ یعنی عدم رابطهٔ خطی، نه لزوماً استقلال.
* **واریانس مجموع:** واریانس مجموع (یا مجموع وزنی) به واریانس‌های فردی *و* کوواریانس بین متغیرها بستگی دارد: $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2 \mathrm{Cov}(X, Y)$. اگر متغیرها مستقل باشند، $\mathrm{Cov}(X,Y)=0$ و فرمول ساده می‌شود.

دیدیم چگونه کوواریانس و همبستگی را با NumPy و Pandas محاسبه کنیم، روابط را با نمودار پراکندگی مصور کنیم و قواعد واریانس را با شبیه‌سازی تأیید کنیم. این مفاهیم برای آمار چندمتغیره، یادگیری ماشین (انتخاب/مهندسی ویژگی)، مالی (نظریهٔ سبد) و بسیاری حوزه‌های دیگر که درک تعامل متغیرها حیاتی است، بنیادین‌اند.

+++

## تمرین‌ها

1.  **مفهومی:** مثالی از دو متغیر بدهید که انتظار دارید:
    a) همبستهٔ مثبت باشند.
    b) همبستهٔ منفی باشند.
    c) بدون همبستگی اما وابسته باشند.
    d) مستقل باشند.
    استدلال خود را توضیح دهید.

2.  **محاسبه:** فرض کنید $X$ دارای $E[X]=2, \mathrm{Var}(X)=9$ و $Y$ دارای $E[Y]=-1, \mathrm{Var}(Y)=4$ و $\mathrm{Cov}(X, Y) = -3$. محاسبه کنید:
    a) $E[3X - 2Y + 5]$
    b) $\mathrm{Var}(X + Y)$
    c) $\mathrm{Var}(X - Y)$
    d) $\mathrm{Var}(3X - 2Y + 5)$
    e) $\rho(X, Y)$

3.  **شبیه‌سازی (همبستگی):**
    a) ۵۰۰ نمونه از $X \sim \text{Normal}(0, 1)$ تولید کنید.
    b) ۵۰۰ نمونه از $Y = -2X + \epsilon$ تولید کنید، که $\epsilon \sim \text{Normal}(0, \sigma^2)$ نویز است. $\sigma = 0.5$ و $\sigma = 2$ را امتحان کنید.
    c) برای هر مقدار $\sigma$، نمودار پراکندگی $X$ در برابر $Y$ بسازید و ضریب همبستگی نمونه $\rho(X, Y)$ را محاسبه کنید.
    d) سطح نویز $\sigma$ چگونه بر ضریب همبستگی اثر می‌گذارد؟ توضیح دهید چرا.

4.  **شبیه‌سازی (واریانس مجموع):**
    a) فرض کنید $X \sim \text{Poisson}(\lambda=3)$ و $Y \sim \text{Poisson}(\lambda=5)$ و $X$ و $Y$ مستقل‌اند.
    b) ۱۰٬۰۰۰ نمونه برای $X$ و $Y$ تولید کنید.
    c) واریانس تجربی $X$، $Y$ و $X+Y$ را محاسبه کنید.
    d) واریانس نظری توزیع Poisson($\lambda$) برابر $\lambda$ است. $\mathrm{Var}(X+Y)$ تجربی را با پیش‌بینی نظری $\mathrm{Var}(X) + \mathrm{Var}(Y)$ (چون مستقل‌اند) مقایسه کنید. آیا نزدیک‌اند؟
    e) ویژگی شناخته‌شده این است که مجموع متغیرهای Poisson مستقل نیز Poisson است، پس $X+Y \sim \text{Poisson}(\lambda_X + \lambda_Y)$. واریانس نظری $X+Y$ بر اساس این ویژگی چیست؟ آیا با یافته‌های شما مطابقت دارد؟

5.  **همبستگی با Pandas:** یک مجموعه‌داده بارگذاری کنید (مثلاً مجموعهٔ `tips` از Seaborn: `tips = sns.load_dataset('tips')`). ماتریس همبستگی ستون‌های عددی (مثلاً `total_bill`، `tip`، `size`) را محاسبه کنید. همبستگی بین `total_bill` و `tip` را تفسیر کنید. این رابطه را با نمودار پراکندگی مصور کنید.

```{code-cell} ipython3
# Example code for Exercise 5 setup
# import seaborn as sns
# import pandas as pd
# tips = sns.load_dataset('tips')
# print(tips.head())
# numerical_tips = tips[['total_bill', 'tip', 'size']]
# correlation_matrix = numerical_tips.corr()
# print("\nCorrelation Matrix:")
# print(correlation_matrix)
# sns.scatterplot(data=tips, x='total_bill', y='tip')
# plt.title('Total Bill vs Tip Amount')
# plt.show()
```

```{code-cell} ipython3

```
