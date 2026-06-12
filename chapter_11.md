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
  - file: notebooks/chapter_11.ipynb
---

# فصل ۱۱: توزیع‌های مشترک

**بخش ۴: چند متغیر تصادفی**

تا اینجا عمدتاً بر رفتار متغیرهای تصادفی تکی تمرکز کرده‌ایم. با این حال، پدیده‌های دنیای واقعی اغلب شامل مشاهده و تحلیل هم‌زمان چند کمیت تصادفی هستند. برای نمونه:

* قد یک فرد چه رابطه‌ای با وزن او دارد؟
* دما و رطوبت در یک روز مشخص چگونه بر مصرف برق اثر می‌گذارند؟
* در امور مالی، بازده سهام‌های مختلف چگونه با هم حرکت می‌کنند؟

برای پاسخ به چنین پرسش‌هایی باید بدانیم احتمال وقوع هم‌زمان چند متغیر تصادفی را چگونه مدل کنیم. این ما را به مفهوم **توزیع مشترک** می‌رساند. در این فصل می‌آموزیم رابطهٔ احتمالاتی بین دو یا چند متغیر تصادفی را چگونه توصیف کنیم و مفاهیم PMF، PDF و CDF را به چند بعد تعمیم دهیم.

+++

## توابع جرم احتمال مشترک (PMF)

با حالت گسسته آغاز می‌کنیم. فرض کنید دو متغیر تصادفی گسسته $X$ و $Y$ روی یک فضای احتمال یکسان تعریف شده‌اند. **تابع جرم احتمال مشترک (PMF)** آن‌ها احتمالی را می‌دهد که $X$ مقدار مشخص $x$ *و* $Y$ مقدار مشخص $y$ را *هم‌زمان* بگیرند.

$$ p_{X,Y}(x, y) = P(X=x, Y=y) $$

PMF مشترک باید دو شرط زیر را برآورده کند:
1. $p_{X,Y}(x, y) \ge 0$ برای همهٔ جفت‌های ممکن $(x, y)$.
2. $\sum_{x} \sum_{y} p_{X,Y}(x, y) = 1$، که در آن جمع روی همهٔ جفت‌های ممکن $(x, y)$ است.

**مثال: پرتاب دو تاس**

فرض کنید $X$ پیامد پرتاب یک تاس قرمز منصفانه و $Y$ پیامد پرتاب یک تاس آبی منصفانه باشد. هر دو $X$ و $Y$ می‌توانند مقادیر $\{1, 2, 3, 4, 5, 6\}$ را بگیرند. با فرض استقلال پرتاب‌ها، احتمال هر جفت مشخص $(x, y)$ برابر است با:

$$ p_{X,Y}(x, y) = P(X=x, Y=y) = P(X=x) P(Y=y) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} $$

برای همهٔ $x, y \in \{1, 2, 3, 4, 5, 6\}$.

می‌توانیم این PMF مشترک را به‌صورت جدول یا آرایهٔ دوبعدی نمایش دهیم:

| y\x | 1    | 2    | 3    | 4    | 5    | 6    |
|-----|------|------|------|------|------|------|
| **1** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |
| **2** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |
| **3** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |
| **4** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |
| **5** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |
| **6** | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 | 1/36 |

مجموع همهٔ درایه‌های جدول برابر $36 \times \frac{1}{36} = 1$ است.

+++

## توابع چگالی احتمال مشترک (PDF)

برای متغیرهای تصادفی پیوسته $X$ و $Y$ از **تابع چگالی احتمال مشترک (PDF)** با نماد $f_{X,Y}(x, y)$ استفاده می‌کنیم. این تابع برازندگی نسبی این را توصیف می‌کند که متغیرها جفت مقادیر مشخص $(x, y)$ را بگیرند.

برخلاف حالت گسسته، خود $f_{X,Y}(x, y)$ احتمال نیست. در عوض، احتمال‌ها با انتگرال‌گیری PDF مشترک روی ناحیه‌ای در صفحهٔ $xy$ به‌دست می‌آیند. احتمال اینکه جفت $(X, Y)$ در ناحیهٔ $A$ قرار گیرد برابر است با:

$$ P((X, Y) \in A) = \iint_A f_{X,Y}(x, y) \,dx \,dy $$

PDF مشترک باید موارد زیر را برآورده کند:
1. $f_{X,Y}(x, y) \ge 0$ برای همهٔ $(x, y)$.
2. $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \,dx \,dy = 1$.

**مثال مفهومی: قد و وزن**

فرض کنید $X$ قد (بر حسب متر) و $Y$ وزن (بر حسب کیلوگرم) یک بزرگسال انتخاب‌شدهٔ تصادفی را نمایش دهد. انتظار داریم افراد بلندتر معمولاً سنگین‌تر باشند، پس این متغیرها احتمالاً مستقل نیستند. توزیع مشترک آن‌ها ممکن است با **توزیع نرمال دوبعدی** مدل شود. PDF مشترک $f_{X,Y}(x, y)$ سطحی زنگوله‌ای روی صفحهٔ $xy$ خواهد بود که احتمالاً حول میانگین قد و وزن متمرکز است و در امتداد خط مورب کشیده شده تا رابطهٔ مثبت بین قد و وزن را منعکس کند. حجم زیر کل این سطح باید برابر ۱ باشد.

+++

## توزیع‌های حاشیه‌ای

اغلب توزیع مشترک چند متغیر را داریم، اما به توزیع تنها یکی از آن‌ها — صرف‌نظر از بقیه — علاقه‌مندیم. این را **توزیع حاشیه‌ای** می‌نامند.

**حالت گسسته:**

برای یافتن PMF حاشیه‌ای $X$، یعنی $p_X(x)$، PMF مشترک $p_{X,Y}(x, y)$ را روی همهٔ مقادیر ممکن $y$ جمع می‌کنیم:

$$ p_X(x) = P(X=x) = \sum_{y} P(X=x, Y=y) = \sum_{y} p_{X,Y}(x, y) $$

به‌طور مشابه، برای PMF حاشیه‌ای $Y$، یعنی $p_Y(y)$:

$$ p_Y(y) = P(Y=y) = \sum_{x} P(X=x, Y=y) = \sum_{x} p_{X,Y}(x, y) $$

در مثال دو تاس، احتمال حاشیه‌ای $P(X=3)$ با جمع احتمال‌های ستون متناظر با $x=3$ به‌دست می‌آید:
$P(X=3) = \sum_{y=1}^{6} p_{X,Y}(3, y) = \sum_{y=1}^{6} \frac{1}{36} = 6 \times \frac{1}{36} = \frac{1}{6}$. همان‌طور که برای یک تاس منصفانه انتظار می‌رود.

**حالت پیوسته:**

برای یافتن PDF حاشیه‌ای $X$، یعنی $f_X(x)$، PDF مشترک $f_{X,Y}(x, y)$ را نسبت به همهٔ مقادیر ممکن $y$ انتگرال می‌گیریم:

$$ f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \,dy $$

به‌طور مشابه، برای PDF حاشیه‌ای $Y$، یعنی $f_Y(y)$:

$$ f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \,dx $$

در مثال قد ($X$) و وزن ($Y$)، انتگرال‌گیری PDF نرمال دوبعدی $f_{X,Y}(x, y)$ نسبت به $y$ از $-\infty$ تا $\infty$ توزیع حاشیه‌ای قد، یعنی $f_X(x)$ را می‌دهد که خود معمولاً توزیع نرمال است.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

**کار عملی: PMFهای حاشیه‌ای از PMF مشترک**

بیایید PMF مشترک مثال دو تاس را نمایش دهیم و PMFهای حاشیه‌ای را محاسبه کنیم.

```{code-cell} ipython3
# Joint PMF for two independent dice rolls
# Rows represent Y (die 2), Columns represent X (die 1)
joint_pmf_dice = np.ones((6, 6)) / 36
```

```{code-cell} ipython3
print("Joint PMF (P(X=x, Y=y)):")
print(joint_pmf_dice)
print(f"\nSum of all joint probabilities: {np.sum(joint_pmf_dice):.2f}")
```

```{code-cell} ipython3
# Calculate marginal PMF for X (sum over rows for each column)
marginal_pmf_X = np.sum(joint_pmf_dice, axis=0) # axis=0 sums over rows
print("\nMarginal PMF for X (P(X=x)):")
print(marginal_pmf_X)
print(f"Sum of marginal P(X=x): {np.sum(marginal_pmf_X):.2f}")
```

```{code-cell} ipython3
# Calculate marginal PMF for Y (sum over columns for each row)
marginal_pmf_Y = np.sum(joint_pmf_dice, axis=1) # axis=1 sums over columns
print("\nMarginal PMF for Y (P(Y=y)):")
print(marginal_pmf_Y)
print(f"Sum of marginal P(Y=y): {np.sum(marginal_pmf_Y):.2f}")
```

```{code-cell} ipython3
# Verify the results match the expected 1/6 for each outcome
dice_outcomes = np.arange(1, 7)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(dice_outcomes, marginal_pmf_X, width=0.9)
plt.xlabel("Outcome X (Die 1)")
plt.ylabel("Probability P(X=x)")
plt.title("Marginal PMF of X")
plt.ylim(0, 0.2)

plt.subplot(1, 2, 2)
plt.bar(dice_outcomes, marginal_pmf_Y, width=0.9)
plt.xlabel("Outcome Y (Die 2)")
plt.ylabel("Probability P(Y=y)")
plt.title("Marginal PMF of Y")
plt.ylim(0, 0.2)

plt.tight_layout()
plt.show()
```

## توزیع‌های شرطی

توزیع شرطی توزیع احتمال یک متغیر را *با فرض* اینکه متغیر دیگر مقدار مشخصی گرفته است، به ما می‌دهد.

**تعریف:**

**PMF شرطی** $Y$ با فرض $X=x$ برابر است با:
$$ p_{Y|X}(y|x) = P(Y=y | X=x) = \frac{P(X=x, Y=y)}{P(X=x)} = \frac{p_{X,Y}(x, y)}{p_X(x)} $$
به‌شرط آنکه $p_X(x) > 0$.

**PDF شرطی** $Y$ با فرض $X=x$ برابر است با:
$$ f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)} $$
به‌شرط آنکه $f_X(x) > 0$.

توجه کنید که برای مقدار ثابت $x$، PMF شرطی $p_{Y|X}(y|x)$ یک PMF معتبر در $y$ است (جمع آن ۱ است) و PDF شرطی $f_{Y|X}(y|x)$ یک PDF معتبر در $y$ است (انتگرال آن ۱ است).

**مثال: دو تاس (حالت شرطی)**

توزیع احتمال پرتاب دوم ($Y$) با فرض اینکه پرتاب اول ($X$) برابر ۳ بوده چیست؟
با استفاده از فرمول: $p_{Y|X}(y|3) = \frac{p_{X,Y}(3, y)}{p_X(3)}$.
می‌دانیم $p_{X,Y}(3, y) = 1/36$ و $p_X(3) = 1/6$.
پس $p_{Y|X}(y|3) = \frac{1/36}{1/6} = \frac{6}{36} = \frac{1}{6}$ برای $y \in \{1, 2, 3, 4, 5, 6\}$.
این شهودی است: دانستن پیامد تاس منصفانهٔ اول، احتمال‌های تاس منصفانهٔ دوم را تغییر نمی‌دهد چون مستقل‌اند.

**مثال: قد و وزن (حالت شرطی)**

مثال قد ($X$) و وزن ($Y$) را در نظر بگیرید. توزیع شرطی $f_{Y|X}(y|x=1.8)$ توزیع وزن را به‌طور خاص برای افرادی با قد ۱٫۸ متر توصیف می‌کند. اگر قد و وزن همبستهٔ مثبت باشند، انتظار داریم میانگین این توزیع شرطی (میانگین وزن افراد ۱٫۸ متری) بیشتر از میانگین توزیع حاشیه‌ای وزن $f_Y(y)$ (میانگین وزن در همهٔ قدها) باشد.

+++

**کار عملی: PMFهای شرطی از PMF مشترک**

بیایید PMF شرطی $Y$ با فرض $X=3$ را برای مثال تاس محاسبه کنیم.

+++

به PMF مشترک و PMF حاشیه‌ای $X$ نیاز داریم
joint_pmf_dice (در بالا محاسبه شد)
marginal_pmf_X (در بالا محاسبه شد)

```{code-cell} ipython3
x_condition = 3 # Condition on X=3
index_x = x_condition - 1 # Array index is value - 1
```

```{code-cell} ipython3
# Get the probability P(X=3)
p_X_eq_3 = marginal_pmf_X[index_x]
print(f"Marginal P(X=3) = {p_X_eq_3:.4f}")
```

```{code-cell} ipython3
# Get the joint probabilities P(X=3, Y=y) for y=1..6
# This corresponds to the column where X=3 in the joint PMF table
joint_p_X3_Y = joint_pmf_dice[:, index_x]
print(f"\nJoint P(X=3, Y=y) for y=1..6: \n{joint_p_X3_Y}")
```

```{code-cell} ipython3
# Calculate conditional PMF P(Y=y | X=3) = P(X=3, Y=y) / P(X=3)
if p_X_eq_3 > 0:
    conditional_pmf_Y_given_X3 = joint_p_X3_Y / p_X_eq_3
    print(f"\nConditional P(Y=y | X=3) for y=1..6: \n{conditional_pmf_Y_given_X3}")
    print(f"Sum of conditional probabilities: {np.sum(conditional_pmf_Y_given_X3):.2f}")

    # Plot the conditional PMF
    plt.figure(figsize=(5, 4))
    plt.bar(dice_outcomes, conditional_pmf_Y_given_X3, width=0.9)
    plt.xlabel("Outcome Y (Die 2)")
    plt.ylabel("Probability P(Y=y | X=3)")
    plt.title("Conditional PMF of Y given X=3")
    plt.ylim(0, 0.2)
    plt.show()
else:
    print("\nCannot calculate conditional PMF as P(X=3) is zero.")
```

## توابع توزیع تجمعی مشترک (CDF)

**تابع توزیع تجمعی مشترک (CDF)** $F_{X,Y}(x, y)$ احتمالی را می‌دهد که $X$ کمتر یا مساوی $x$ *و* $Y$ کمتر یا مساوی $y$ باشد.

$$ F_{X,Y}(x, y) = P(X \le x, Y \le y) $$

**حالت گسسته:**
$$ F_{X,Y}(x, y) = \sum_{x_i \le x} \sum_{y_j \le y} p_{X,Y}(x_i, y_j) $$

**حالت پیوسته:**
$$ F_{X,Y}(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{X,Y}(u, v) \,dv \,du $$

**ویژگی‌ها:**
1. $0 \le F_{X,Y}(x, y) \le 1$.
2. $F_{X,Y}(x, y)$ در هر دو $x$ و $y$ نارون‌یاب است.
3. $\lim_{x \to \infty, y \to \infty} F_{X,Y}(x, y) = 1$.
4. $\lim_{x \to -\infty} F_{X,Y}(x, y) = 0$ و $\lim_{y \to -\infty} F_{X,Y}(x, y) = 0$.

**مثال: دو تاس (CDF)**

مقدار $F_{X,Y}(2, 3) = P(X \le 2, Y \le 3)$ چیست؟
این احتمالی است که تاس اول ۱ یا ۲ باشد *و* تاس دوم ۱، ۲ یا ۳ باشد.
جفت‌های $(x, y)$ که این شرط را برآورده می‌کنند: (1,1)، (1,2)، (1,3)، (2,1)، (2,2)، (2,3).
تعداد این جفت‌ها $2 \times 3 = 6$ است. از آنجا که احتمال هر جفت $1/36$ است:
$F_{X,Y}(2, 3) = 6 \times \frac{1}{36} = \frac{1}{6}$.

**مثال: قد و وزن (CDF)**

$F_{X,Y}(1.8, 75) = P(\text{Height} \le 1.8\text{m AND } \text{Weight} \le 75\text{kg})$. این احتمالی است که فردی انتخاب‌شدهٔ تصادفی در این محدودهٔ خاص قد و وزن (یا کمتر) قرار گیرد. این مقدار با انتگرال‌گیری PDF مشترک $f_{X,Y}(x, y)$ روی ناحیه‌ای که $x \le 1.8$ و $y \le 75$ محاسبه می‌شود.

+++

## کار عملی: شبیه‌سازی و مصورسازی

راهی قدرتمند برای درک توزیع‌های مشترک، شبیه‌سازی و مصورسازی است. می‌توانیم نمونه‌های تصادفی از یک توزیع مشترک تولید کنیم و سپس با نمودارها رابطهٔ بین متغیرها را ببینیم.

**۱. شبیه‌سازی متغیرهای مستقل:**
اگر $X$ و $Y$ مستقل باشند، می‌توانیم آن‌ها را جداگانه از توزیع‌های حاشیه‌ای‌شان شبیه‌سازی کنیم و سپس نتایج را جفت کنیم. برای مثال دو تاس:

```{code-cell} ipython3
num_simulations = 5000
```

```{code-cell} ipython3
# Simulate X (die 1)
simulated_X = np.random.randint(1, 7, size=num_simulations)
```

```{code-cell} ipython3
# Simulate Y (die 2) - independently
simulated_Y = np.random.randint(1, 7, size=num_simulations)
```

```{code-cell} ipython3
# Combine into pairs
simulated_pairs = np.vstack((simulated_X, simulated_Y)).T # Transpose to get pairs
```

```{code-cell} ipython3
print("First 10 simulated pairs (X, Y):")
print(simulated_pairs[:10])
```

```{code-cell} ipython3
# Visualize the simulated pairs using a scatter plot (with jitter)
plt.figure(figsize=(6, 6))
sns.stripplot(x=simulated_X, y=simulated_Y, jitter=0.25, alpha=0.3, size=3)
plt.xlabel("Outcome X (Die 1)")
plt.ylabel("Outcome Y (Die 2)")
plt.title(f"Scatter Plot of {num_simulations} Independent Dice Rolls")
plt.grid(True, alpha=0.3)
plt.show()
```

نمودار پراکندگی نقاطی را نشان می‌دهد که تقریباً یکنواخت روی همهٔ ۳۶ پیامد ممکن پخش شده‌اند، همان‌طور که برای تاس‌های منصفانهٔ مستقل انتظار می‌رود.

**۲. شبیه‌سازی متغیرهای وابسته (نرمال دوبعدی):**
بیایید داده‌های قد و وزن را با فرض پیروی از توزیع نرمال دوبعدی شبیه‌سازی کنیم. باید میانگین‌ها، انحراف‌های معیار و همبستگی بین آن‌ها را مشخص کنیم.

```{code-cell} ipython3
from scipy.stats import multivariate_normal
```

```{code-cell} ipython3
num_samples = 2000
```

```{code-cell} ipython3
# Parameters (example values)
mean_height = 1.75 # meters
std_dev_height = 0.1
mean_weight = 75 # kg
std_dev_weight = 10
correlation = 0.7 # Positive correlation between height and weight
```

```{code-cell} ipython3
# Create the mean vector and covariance matrix
mean_vector = [mean_height, mean_weight]
```

```{code-cell} ipython3
# Covariance = correlation * std_dev_X * std_dev_Y
covariance = correlation * std_dev_height * std_dev_weight
covariance_matrix = [[std_dev_height**2, covariance],
                     [covariance, std_dev_weight**2]]
```

```{code-cell} ipython3
print("Mean Vector:", mean_vector)
print("Covariance Matrix:\n", covariance_matrix)
```

```{code-cell} ipython3
# Create the bivariate normal distribution object
bivariate_norm = multivariate_normal(mean=mean_vector, cov=covariance_matrix)
```

```{code-cell} ipython3
# Generate random samples
simulated_data = bivariate_norm.rvs(size=num_samples)
simulated_heights = simulated_data[:, 0]
simulated_weights = simulated_data[:, 1]
```

```{code-cell} ipython3
print(f"\nFirst 5 simulated (Height, Weight) pairs:\n{simulated_data[:5]}")
```

**۳. مصورسازی توزیع‌های مشترک:**

* **نمودار پراکندگی:** برای نشان دادن رابطه و چگالی نقاط شبیه‌سازی‌شده مناسب است.
* **هیستوگرام دوبعدی (نقشهٔ حرارتی):** فضا را به بازه‌ها تقسیم می‌کند و تعداد/چگالی هر بازه را با شدت رنگ نشان می‌دهد.
* **نمودار کانتور:** برای توزیع‌های پیوسته، خطوط چگالی احتمال ثابت را نشان می‌دهد (مانند خطوط ارتفاع روی نقشه).

```{code-cell} ipython3
# Scatter Plot
plt.figure(figsize=(7, 6))
plt.scatter(simulated_heights, simulated_weights, alpha=0.3)
plt.xlabel("Simulated Height (m)")
plt.ylabel("Simulated Weight (kg)")
plt.title("Scatter Plot of Simulated Height vs. Weight")
plt.grid(True, alpha=0.3)
plt.show()
```

```{code-cell} ipython3
# 2D Histogram
plt.figure(figsize=(8, 6))
# cmap='viridis' is a common colormap, you can experiment with others
hist, xedges, yedges, im = plt.hist2d(simulated_heights, simulated_weights, bins=30, cmap='viridis')
plt.colorbar(label='Counts per bin')
plt.xlabel("Simulated Height (m)")
plt.ylabel("Simulated Weight (kg)")
plt.title("2D Histogram of Simulated Height vs. Weight")
plt.grid(True, alpha=0.3)
plt.show()
```

```{code-cell} ipython3
# Seaborn offers jointplot for combined views
sns.jointplot(x=simulated_heights, y=simulated_weights, kind='hist', bins=30, cmap='viridis')
plt.suptitle("Seaborn Jointplot (Histogram)", y=1.02) # Adjust title position
plt.show()
```

```{code-cell} ipython3
# Contour Plot (overlayed on scatter or alone)
plt.figure(figsize=(7, 6))
sns.kdeplot(x=simulated_heights, y=simulated_weights, cmap="Blues", fill=True, levels=10)
#plt.scatter(simulated_heights, simulated_weights, alpha=0.1, s=5, color='grey') # Optional: overlay scatter
plt.xlabel("Simulated Height (m)")
plt.ylabel("Simulated Weight (kg)")
plt.title("Contour Plot (Kernel Density Estimate)")
plt.grid(True, alpha=0.3)
plt.show()
```

این نمودارها همبستگی مثبت را به‌وضوح نشان می‌دهند — افراد بلندتر شبیه‌سازی‌شده تمایل به سنگین‌تر بودن دارند. هیستوگرام دوبعدی و نمودار کانتور شکل چگالی احتمال مشترک را مصور می‌کنند؛ متمرکز حول میانگین‌ها و در امتداد قطر به‌دلیل همبستگی کشیده شده‌اند.

## خلاصه

این فصل مفاهیم بنیادین کار با چند متغیر تصادفی را معرفی کرد:
* **PMF/PDF مشترک:** احتمال یا چگالی وقوع هم‌زمان چند متغیر را توصیف می‌کنند.
* **توزیع‌های حاشیه‌ای:** با جمع یا انتگرال‌گیری سایر متغیرها، امکان تمرکز روی توزیع یک متغیر تکی را می‌دهند.
* **توزیع‌های شرطی:** توزیع یک متغیر را با فرض مقدار مشخصی از متغیر دیگر توصیف می‌کنند.
* **CDF مشترک:** احتمالی را می‌دهد که همهٔ متغیرها زیر آستانه‌های مشخصی قرار گیرند.

دیدیم این توزیع‌ها را چگونه به‌صورت ریاضی نمایش دهیم و در پایتون، به‌ویژه از طریق شبیه‌سازی و مصورسازی با NumPy، Matplotlib و Seaborn، با آن‌ها کار کنیم. درک توزیع‌های مشترک برای مدل‌سازی سامانه‌های پیچیده‌ای که چند عامل در آن‌ها تعامل دارند حیاتی است و راه را برای مفاهیمی مانند کوواریانس، همبستگی و استقلال — که در فصل بعد بررسی می‌کنیم — هموار می‌کند.

+++

---
**تمرین‌ها:**

1.  **پرتاب سکه:** فرض کنید $X$ تعداد شیر در ۲ پرتاب یک سکهٔ منصفانه و $Y$ پیامد پرتاب اول (۰ برای خط، ۱ برای شیر) باشد.
    * PMF مشترک $p_{X,Y}(x, y)$ را تعیین کنید. آن را به‌صورت جدول یا آرایهٔ دوبعدی نمایش دهید.
    * PMFهای حاشیه‌ای $p_X(x)$ و $p_Y(y)$ را محاسبه کنید.
    * PMF شرطی $p_{X|Y}(x|1)$ (توزیع تعداد کل شیرها با فرض شیر بودن پرتاب اول) را محاسبه کنید.
2.  **توزیع یکنواخت روی مربع:** فرض کنید $(X, Y)$ به‌طور یکنواخت روی مربعی با $0 \le x \le 2$ و $0 \le y \le 2$ توزیع شده‌اند.
    * PDF مشترک $f_{X,Y}(x, y)$ چیست؟ (به‌خاطر داشته باشید باید روی مربع به ۱ انتگرال بگیرد).
    * PDFهای حاشیه‌ای $f_X(x)$ و $f_Y(y)$ را بیابید. آیا $X$ و $Y$ مستقل‌اند؟
    * $P(X \le 1, Y \le 1)$ را محاسبه کنید.
    * $P(X+Y \le 1)$ را محاسبه کنید. (راهنما: ناحیه را روی مربع مصور کنید).
3.  **مصورسازی شبیه‌سازی:** شبیه‌سازی نرمال دوبعدی قد و وزن را تغییر دهید.
    * `correlation` را روی $-0.6$ بگذارید. نمونه‌ها و سه نمودار (پراکندگی، هیستوگرام دوبعدی، کانتور) را دوباره بسازید. نمودارها چگونه تغییر می‌کنند؟
    * `correlation` را روی ۰ بگذارید. نمونه‌ها و نمودارها را دوباره بسازید. اکنون نمودارها چگونه‌اند؟ این دربارهٔ رابطهٔ قد و وزن در این سناریوی شبیه‌سازی‌شده چه می‌گوید؟

+++
