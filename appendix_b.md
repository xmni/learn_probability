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
  - file: notebooks/appendix_b.ipynb
---

# پیوست ب: مرجع کتابخانه‌های ضروری

این پیوست مرجع سریعی برای پرکاربردترین توابع و مفاهیم کتابخانه‌های اصلی پایتون مورد استفاده در سراسر این کتاب ارائه می‌دهد. جامع نیست اما موارد ضروری برای شبیه‌سازی، محاسبه و مصورسازی احتمال را پوشش می‌دهد.

## ۱. کتابخانه‌های استاندارد پایتون

### `math`

- `math.factorial(n)`: محاسبهٔ $n!$
- `math.comb(n, k)`: محاسبهٔ ضریب دوجمله‌ای $\binom{n}{k}$ («انتخاب k از n»). نیاز به Python 3.8+.
- `math.perm(n, k)`: محاسبهٔ تبدیلات $P(n, k) = \frac{n!}{(n-k)!}$. نیاز به Python 3.8+.
- `math.exp(x)`: محاسبهٔ $e^x$.
- `math.log(x, [base])`: محاسبهٔ لگاریتم $x$. لگاریتم طبیعی ($\ln x$) اگر پایه حذف شود، در غیر این صورت $\log_{\text{base}} x$.
- `math.sqrt(x)`: محاسبهٔ جذر $\sqrt{x}$.

## ۲. NumPy (`import numpy as np`)

### ساخت آرایه

- `np.array([list])`: ساخت آرایهٔ NumPy از یک فهرست پایتون.
- `np.arange(start, stop, step)`: ساخت آرایه با مقادیر یکنواخت در بازه (stop شامل نمی‌شود).
- `np.linspace(start, stop, num)`: ساخت آرایه با `num` مقدار یکنواخت بین `start` و `stop` (شامل هر دو).
- `np.zeros(shape)`, `np.ones(shape)`: ساخت آرایه‌هایی با شکل داده‌شده پر از ۰ یا ۱.
- `np.eye(N)`: ساخت ماتریس همانی $N \times N$.

### نمونه‌گیری تصادفی (`np.random`)

- `np.random.seed(integer)`: تنظیم بذر تصادفی برای تکرارپذیری.
- `np.random.rand(d0, d1, ...)`: تولید اعداد تصادفی یکنواخت روی $[0, 1)$.
- `np.random.randn(d0, d1, ...)`: تولید اعداد تصادفی از توزیع نرمال استاندارد ($N(0, 1)$).
- `np.random.randint(low, high, size)`: تولید اعداد صحیح تصادفی از `low` (شامل) تا `high` (غیرشامل).
- `np.random.choice(a, size, replace=True, p=None)`: نمونه‌گیری تصادفی از آرایهٔ یک‌بعدی `a`. `replace` نمونه‌گیری با/بدون جایگزینی را کنترل می‌کند. `p` امکان تعیین احتمال هر عنصر در `a` را می‌دهد.

### عملیات و ریاضی آرایه

- عملگرهای حسابی استاندارد (`+`، `-`، `*`، `/`، `**`) به‌صورت عنصر به عنصر عمل می‌کنند.
- `np.sum(a)`, `np.mean(a)`, `np.std(a)`, `np.var(a)`: محاسبهٔ مجموع، میانگین، انحراف معیار ($\sigma$) و واریانس ($\sigma^2$) عناصر آرایه.
- `np.min(a)`, `np.max(a)`: یافتن کمینه و بیشینه.
- `np.argmin(a)`, `np.argmax(a)`: یافتن اندیس کمینه و بیشینه.
- `np.sqrt(a)`, `np.exp(a)`, `np.log(a)`, `np.sin(a)` و غیره: توابع ریاضی عنصر به عنصر.
- `np.dot(a, b)` یا `a @ b`: ضرب ماتریسی / ضرب داخلی.
- `a.T`: ترانهادهٔ آرایهٔ `a`.

### اندیس‌گذاری و برش

- برش استاندارد پایتون `a[start:stop:step]` برای هر بعد کار می‌کند.
- اندیس‌گذاری بولی: `a[boolean_array]` یا `a[a > 5]` عناصری را که شرط True است انتخاب می‌کند.
- اندیس‌گذاری پیشرفته: `a[[1, 4, 0]]` سطرها/عناصر مشخص را با فهرست اندیس‌ها انتخاب می‌کند.

## ۳. SciPy (`import scipy`)

### توابع ویژه (`scipy.special`)

- `scipy.special.perm(N, k)`: محاسبهٔ تبدیلات $P(N, k)$.
- `scipy.special.comb(N, k)`: محاسبهٔ ترکیبات $C(N, k) = \binom{N}{k}$.
- `scipy.special.gamma(z)`: تابع گاما $\Gamma(z)$.
- `scipy.special.gammaln(z)`: لگاریتم قدر مطلق تابع گاما، $\ln|\Gamma(z)|$.

### انتگرال‌گیری (`scipy.integrate`)

- `scipy.integrate.quad(func, a, b)`: محاسبهٔ انتگرال معین $\int_a^b f(x) dx$. نتیجهٔ انتگرال و خطای تخمینی را برمی‌گرداند.

### آمار (`scipy.stats`)

شیءهای توزیع (مثلاً `norm`، `binom`، `poisson`) با متدهای رایج:

- `dist.rvs(...)`: تولید متغیرهای تصادفی (نمونه).
- `dist.pmf(k, ...)`: تابع جرم احتمال $P(X=k)$ (برای توزیع‌های گسسته).
- `dist.pdf(x, ...)`: تابع چگالی احتمال $f(x)$ (برای توزیع‌های پیوسته).
- `dist.cdf(x, ...)`: تابع توزیع تجمعی $F(x) = P(X \le x)$.
- `dist.ppf(q, ...)`: تابع درصد (CDF معکوس یا تابع چندک). $x$ را می‌یابد که $F(x) = q$.
- `dist.sf(x, ...)`: تابع بقا $S(x) = 1 - F(x) = P(X > x)$.
- `dist.isf(q, ...)`: تابع بقای معکوس. $x$ را می‌یابد که $S(x) = q$.
- `dist.stats(moments='mvsk')`: محاسبهٔ میانگین ('m')، واریانس ('v')، چولگی ('s')، کشیدگی ('k').
- `dist.mean(...)`, `dist.median(...)`, `dist.var(...)`, `dist.std(...)`: محاسبهٔ گشتاور/آمارهٔ مشخص.
- `dist.interval(alpha, ...)`: محاسبهٔ بازه‌ای که `alpha` نسبت از چگالی احتمال را در بر می‌گیرد (مثلاً `alpha=0.95` برای بازهٔ ۹۵٪).

توزیع‌های رایج (پارامترها ممکن است اندکی با تعاریف کتاب درسی متفاوت باشند؛ مستندات را ببینید):

- `scipy.stats.bernoulli(p)`: برنولی (احتمال موفقیت `p`).
- `scipy.stats.binom(n, p)`: دوجمله‌ای (تعداد آزمایش `n`، احتمال موفقیت `p`).
- `scipy.stats.geom(p)`: هندسی (احتمال موفقیت `p`).
- `scipy.stats.nbinom(n, p)`: دوجمله‌ای منفی (تعداد موفقیت‌های هدف `n`، احتمال موفقیت `p`).
- `scipy.stats.poisson(mu)`: پواسون (نرخ `mu`، $\lambda$).
- `scipy.stats.hypergeom(M, n, N)`: فوق‌هندسی (M=اندازهٔ جامعه، n=تعداد دارای ویژگی، N=اندازهٔ نمونه).
- `scipy.stats.uniform(loc, scale)`: یکنواخت روی $[loc, loc+scale]$.
- `scipy.stats.expon(scale)`: نمایی (scale = $1/\lambda$، که $\lambda$ پارامتر نرخ است).
- `scipy.stats.norm(loc, scale)`: نرمال (گاوسی) (loc=میانگین $\mu$، scale=انحراف معیار $\sigma$).
- `scipy.stats.gamma(a, loc, scale)`: گاما (`a` پارامتر شکل $\alpha$ یا $k$).
- `scipy.stats.beta(a, b, loc, scale)`: بتا (`a`، `b` پارامترهای شکل $\alpha, \beta$).

## ۴. Matplotlib (`import matplotlib.pyplot as plt`)

### رسم پایه

- `plt.plot(x, y, [fmt], ...)`: نمودار خطی.
- `plt.scatter(x, y, ...)`: نمودار پراکندگی.
- `plt.bar(x, height, ...)`: نمودار میله‌ای عمودی.
- `plt.hist(data, bins=..., density=False, ...)`: هیستوگرام. `density=True` هیستوگرام را نرمال می‌کند تا چگالی احتمال شود.
- `plt.boxplot(data, ...)`: نمودار جعبه‌ای.

### سفارشی‌سازی و نمایش

- `plt.title('...')`, `plt.xlabel('...')`, `plt.ylabel('...')`: تنظیم عنوان و برچسب محورها.
- `plt.legend(['label1', 'label2'])`: افزودن راهنما (از آرگومان `label='...'` در دستورات plot استفاده کنید).
- `plt.grid(True)`: نمایش خطوط شبکه.
- `plt.xlim(min, max)`, `plt.ylim(min, max)`: تنظیم محدودهٔ محورها.
- `plt.figure(figsize=(width, height))`: ساخت شیء figure جدید با اندازهٔ مشخص به اینچ.
- `plt.subplot(nrows, ncols, index)`: ساخت محورها در شبکهٔ subplot.
- `plt.tight_layout()`: تنظیم پارامترهای نمودار برای چیدمان فشرده.
- `plt.show()`: نمایش figure فعلی.
- `plt.savefig('filename.png')`: ذخیرهٔ figure فعلی در فایل.

## ۵. Seaborn (`import seaborn as sns`)

بر پایهٔ Matplotlib ساخته شده و رابط سطح‌بالاتری برای نمودارهای آماری فراهم می‌کند.

### نمودارهای آماری رایج

- `sns.histplot(data=..., x=..., hue=..., kde=True)`: هیستوگرام با برآورد چگالی هسته (KDE) اختیاری.
- `sns.kdeplot(data=..., x=..., hue=...)`: رسم برآورد چگالی هسته.
- `sns.ecdfplot(data=..., x=..., hue=...)`: رسم تابع توزیع تجمعی تجربی.
- `sns.boxplot(data=..., x=..., y=..., hue=...)`: نمودار جعبه‌ای، به‌راحتی گروه‌بندی بر اساس متغیرهای طبقه‌ای.
- `sns.violinplot(data=..., x=..., y=..., hue=...)`: ترکیب نمودار جعبه‌ای با KDE.
- `sns.scatterplot(data=..., x=..., y=..., hue=..., size=...)`: نمودار پراکندگی پیشرفته.
- `sns.heatmap(data, annot=False, cmap=...)`: مصورسازی دادهٔ ماتریسی (مثلاً کوواریانس، ماتریس‌های گذار). `annot=True` مقادیر را نشان می‌دهد.
- `sns.pairplot(data, hue=...)`: رسم روابط دو به دو متغیرها در یک DataFrame.
- `sns.jointplot(data=..., x=..., y=..., kind='scatter'|'kde'|'hist')`: نمودار پراکندگی با توزیع‌های حاشیه‌ای روی محورها.

### زیبایی‌شناسی

- `sns.set_theme(style=..., palette=..., context=...)`: تنظیم پارامترهای زیبایی‌شناسی سراسری (مثلاً `style='whitegrid'`، `palette='viridis'`).

## ۶. Pandas (`import pandas as pd`)

عمدتاً برای بارگذاری، دستکاری و تحلیل اولیهٔ داده استفاده می‌شود.

### ساختارهای دادهٔ اصلی

- `pd.Series(data, index=...)`: آرایهٔ برچسب‌دار یک‌بعدی.
- `pd.DataFrame(data, index=..., columns=...)`: ساختار جدول‌مانند دو‌بعدی برچسب‌دار.

### بارگذاری/ذخیرهٔ داده

- `pd.read_csv('filepath')`, `pd.read_excel('filepath')`: بارگذاری داده از فایل.
- `df.to_csv('filepath')`, `df.to_excel('filepath')`: ذخیرهٔ DataFrame در فایل.

### انتخاب و بازرسی

- `df.head(n)`, `df.tail(n)`: مشاهدهٔ n سطر اول/آخر.
- `df.info()`: خلاصهٔ DataFrame (نوع اندیس، ستون‌ها، مقادیر غیرتهی، مصرف حافظه).
- `df.describe()`: تولید آماره‌های توصیفی برای ستون‌های عددی.
- `df['column']`, `df.column`: انتخاب یک ستون به‌عنوان Series.
- `df[['col1', 'col2']]`: انتخاب چند ستون به‌عنوان DataFrame.
- `df.loc[row_label, col_label]`: دسترسی به گروهی از سطرها/ستون‌ها با برچسب.
- `df.iloc[row_index, col_index]`: دسترسی به گروهی از سطرها/ستون‌ها با موقعیت عددی.
- اندیس‌گذاری بولی: `df[df['value'] > 0]`

### عملیات و آمار رایج

- `df['column'].mean()`, `.std()`, `.var()`, `.median()`, `.min()`, `.max()`, `.sum()`: آماره‌های ستونی.
- `df.corr()`: محاسبهٔ همبستگی دو به دو ستون‌ها.
- `df.cov()`: محاسبهٔ کوواریانس دو به دو ستون‌ها.
- `df['column'].value_counts()`: شمارش مقادیر یکتا در یک Series.
- `df.groupby('col_name').agg({'other_col': 'mean'})`: گروه‌بندی داده و اعمال توابع تجمیع.
- `df.apply(function, axis=0|1)`: اعمال تابع در امتداد یک محور.

```{code-cell} ipython3

```
