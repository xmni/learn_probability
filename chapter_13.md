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
  - file: notebooks/chapter_13.ipynb
---

# فصل ۱۳: توابع چند متغیر تصادفی

+++

در فصل‌های پیشین، متغیرهای تصادفی تکی و سپس جفت‌ها یا گروه‌هایی از متغیرها (توزیع مشترک، کوواریانس، همبستگی) را بررسی کردیم. اکنون گام بعدی را برمی‌داریم: وقتی چند متغیر تصادفی را با توابع ریاضی ترکیب می‌کنیم چه می‌شود؟

برای مثال، اگر $X$ درآمد محصول A و $Y$ درآمد محصول B باشد، ممکن است به توزیع درآمد کل $Z = X + Y$ علاقه‌مند باشیم. یا اگر $X$ و $Y$ مختصات باشند، شاید بخواهیم توزیع فاصله از مبدأ، یعنی $R = \sqrt{X^2 + Y^2}$ را بدانیم.

این فصل روش‌های یافتن توزیع چنین متغیرهای ترکیبی را بررسی می‌کند و بر مجموع‌ها، تفاضل‌ها، حاصل‌ضرب‌ها، نسبت‌ها، تبدیل‌های عمومی و آماره‌های ترتیبی تمرکز دارد. خواهیم دید چگونه نتایج نظری به‌دست می‌آیند و شبیه‌سازی چگونه بینش تجربی — به‌ویژه وقتی راه‌حل‌های تحلیلی پیچیده‌اند — فراهم می‌کند.

+++

## توزیع مجموع‌ها، تفاضل‌ها، حاصل‌ضرب‌ها و نسبت‌ها

یکی از رایج‌ترین عملیات‌ها یافتن توزیع مجموع دو یا چند متغیر تصادفی است.

+++

### مجموع متغیرهای تصادفی مستقل

فرض کنید $X$ و $Y$ دو متغیر تصادفی مستقل‌اند و $Z = X + Y$. یافتن توزیع $Z$ با تکنیکی به نام **کانولوشن** انجام می‌شود.

* **حالت گسسته:** اگر $X$ و $Y$ گسسته با PMFهای $p_X(k)$ و $p_Y(k)$ باشند، PMF متغیر $Z = X + Y$ با فرمول کانولوشن داده می‌شود:
    $$P(Z=z) = p_Z(z) = \sum_{k} P(X=k, Y=z-k)$$ 
    از آنجا که $X$ و $Y$ مستقل‌اند، $P(X=k, Y=z-k) = P(X=k)P(Y=z-k) = p_X(k)p_Y(z-k)$. بنابراین:
    $$p_Z(z) = \sum_{k} p_X(k) p_Y(z-k)$$ 
    جمع روی همهٔ مقادیر ممکن $k$ برای $X$ است.
    
    *مثال:* اگر $X \sim Poisson(\lambda_1)$ و $Y \sim Poisson(\lambda_2)$ مستقل باشند، آنگاه $Z = X+Y \sim Poisson(\lambda_1 + \lambda_2)$.

* **حالت پیوسته:** اگر $X$ و $Y$ پیوسته با PDFهای $f_X(x)$ و $f_Y(y)$ باشند، PDF متغیر $Z = X + Y$ با انتگرال کانولوشن داده می‌شود:
    $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x) \, dx$$ 
    همچنین می‌توانید نقش $X$ و $Y$ را جابه‌جا کنید: $f_Z(z) = \int_{-\infty}^{\infty} f_X(z-y) f_Y(y) \, dy$.
    
    *مثال:* اگر $X \sim N(\mu_1, \sigma_1^2)$ و $Y \sim N(\mu_2, \sigma_2^2)$ مستقل باشند، آنگاه $Z = X+Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$.
    *مثال:* اگر $X \sim Uniform(0, 1)$ و $Y \sim Uniform(0, 1)$ مستقل باشند، آنگاه $Z = X+Y$ **توزیع مثلثی** روی $(0, 2)$ دارد. بعداً آن را شبیه‌سازی می‌کنیم.

+++

### تفاضل‌ها، حاصل‌ضرب‌ها و نسبت‌ها

یافتن توزیع تفاضل‌ها ($Z=X-Y$)، حاصل‌ضرب‌ها ($Z=XY$) یا نسبت‌ها ($Z=X/Y$) نیز با روش‌های تبدیل یا روش‌های شبیه به کانولوشن امکان‌پذیر است، اما فرمول‌ها پیچیده‌تر می‌شوند.

* **تفاضل:** $Z = X - Y = X + (-Y)$. اگر توزیع $-Y$ را بدانید، می‌توانید از کانولوشن استفاده کنید.
* **حاصل‌ضرب/نسبت:** این‌ها اغلب به روش تبدیل (در بخش بعد) یا با استفاده از توابع توزیع تجمعی نیاز دارند ($F_Z(z) = P(Z \le z) = P(X/Y \le z)$ و سپس مشتق‌گیری برای یافتن PDF $f_Z(z)$).

برای بسیاری از توابع پیچیده یا وقتی استنتاج تحلیلی غیرممکن است، شبیه‌سازی ابزاری قدرتمند برای تقریب توزیع حاصل می‌شود.

+++

## مقدمه‌ای بر تبدیل‌های چندمتغیره

فرض کنید جفت متغیرهای تصادفی $(X, Y)$ با PDF مشترک شناخته‌شدهٔ $f_{X,Y}(x, y)$ داریم. دو متغیر تصادفی جدید $U = g_1(X, Y)$ و $V = g_2(X, Y)$ تعریف می‌کنیم. چگونه PDF مشترک $(U, V)$، یعنی $f_{U,V}(u, v)$ را بیابیم؟

این به تکنیکی مشابه تغییر متغیر در حساب چندمتغیره نیاز دارد و از **ماتریس ژاکوبی** تبدیل استفاده می‌کند.

1.  **حل برای متغیرهای اصلی:** $x$ و $y$ را بر حسب $u$ و $v$ بیان کنید: $x = h_1(u, v)$ و $y = h_2(u, v)$.
2.  **محاسبهٔ دترمینان ژاکوبی:** دترمینان ژاکوبی $J$ برابر است با:
    $$ J = \det \begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u} $$ 
3.  **اعمال فرمول تبدیل:** PDF مشترک $(U, V)$ برابر است با:
    $$ f_{U,V}(u, v) = f_{X,Y}(h_1(u, v), h_2(u, v)) \cdot |J| $$ 
    که $|J|$ قدر مطلق دترمینان ژاکوبی است. این فرمول به‌شرط یک‌به‌یک بودن تبدیل روی ناحیهٔ مورد نظر معتبر است.

*مثال:* تبدیل دکارتی به قطبی.
فرض کنید $(X, Y)$ PDF مشترک $f_{X,Y}(x, y)$ دارند. تبدیل به مختصات قطبی را در نظر بگیرید: $R = \sqrt{X^2 + Y^2}$ و $\Theta = \arctan(Y/X)$. 
می‌خواهیم PDF مشترک $f_{R,\Theta}(r, \theta)$ را بیابیم.
تبدیل معکوس $x = r \cos \theta$ و $y = r \sin \theta$ است. 
دترمینان ژاکوبی:
$$ J = \det \begin{pmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{pmatrix} = (\cos \theta)(r \cos \theta) - (-r \sin \theta)(\sin \theta) = r \cos^2 \theta + r \sin^2 \theta = r $$ 
با فرض $r > 0$، $|J| = r$. پس:
$$ f_{R,\Theta}(r, \theta) = f_{X,Y}(r \cos \theta, r \sin \theta) \cdot r $$ 
اگر $X, Y \sim N(0, 1)$ مستقل باشند، آنگاه $f_{X,Y}(x, y) = \frac{1}{2\pi} e^{-(x^2+y^2)/2}$. 
با جایگذاری $x = r \cos \theta, y = r \sin \theta$، داریم $x^2+y^2 = r^2$. 
پس $f_{R,\Theta}(r, \theta) = \frac{1}{2\pi} e^{-r^2/2} \cdot r$. می‌بینیم این به تابعی از $r$ و $\theta$ تفکیک می‌شود و $R$ و $\Theta$ مستقل‌اند. انتگرال‌گیری نسبت به $\theta$ از ۰ تا $2\pi$ PDF حاشیه‌ای $R$ را می‌دهد: $f_R(r) = r e^{-r^2/2}$ برای $r > 0$ (توزیع رایلی)، و انتگرال‌گیری نسبت به $r$ PDF حاشیه‌ای $\Theta$ را می‌دهد: $f_\Theta(\theta) = \frac{1}{2\pi}$ برای $0 \le \theta < 2\pi$ (توزیع یکنواخت).

+++

## آماره‌های ترتیبی

فرض کنید نمونه‌ای از $n$ متغیر تصادفی مستقل و هم‌توزیع (i.i.d.) $X_1, X_2, \dots, X_n$ داریم. اگر این متغیرها را به‌ترتیب صعودی مرتب کنیم، **آماره‌های ترتیبی** به‌دست می‌آیند: $X_{(1)}, X_{(2)}, \dots, X_{(n)}$، که $X_{(1)} = \min(X_1, \dots, X_n)$ و $X_{(n)} = \max(X_1, \dots, X_n)$.

اغلب به توزیع این آماره‌های ترتیبی، به‌ویژه کمینه ($X_{(1)}$) و بیشینه ($X_{(n)}$)، علاقه‌مندیم.

فرض کنید CDF و PDF مشترک $X_i$ها به‌ترتیب $F(x)$ و $f(x)$ باشند.

* **توزیع بیشینه، $X_{(n)}$:**
    واقعهٔ $X_{(n)} \le x$ یعنی *همهٔ* $X_i$ها باید کمتر یا مساوی $x$ باشند. چون i.i.d. هستند:
    $$ F_{X_{(n)}}(x) = P(X_{(n)} \le x) = P(X_1 \le x, X_2 \le x, \dots, X_n \le x) = P(X_1 \le x) \cdots P(X_n \le x) = [F(x)]^n $$ 
    PDF با مشتق‌گیری از CDF به‌دست می‌آید:
    $$ f_{X_{(n)}}(x) = \frac{d}{dx} F_{X_{(n)}}(x) = n [F(x)]^{n-1} f(x) $$ 

* **توزیع کمینه، $X_{(1)}$:**
    واقعهٔ $X_{(1)} > x$ یعنی *همهٔ* $X_i$ها باید بزرگ‌تر از $x$ باشند. 
    $$ P(X_{(1)} > x) = P(X_1 > x, X_2 > x, \dots, X_n > x) = [P(X_1 > x)]^n = [1 - F(x)]^n $$ 
    بنابراین CDF برابر است با:
    $$ F_{X_{(1)}}(x) = P(X_{(1)} \le x) = 1 - P(X_{(1)} > x) = 1 - [1 - F(x)]^n $$ 
    PDF با مشتق‌گیری به‌دست می‌آید:
    $$ f_{X_{(1)}}(x) = \frac{d}{dx} F_{X_{(1)}}(x) = -n [1 - F(x)]^{n-1} (-f(x)) = n [1 - F(x)]^{n-1} f(x) $$ 

*مثال:* فرض کنید $X_1, \dots, X_n$ i.i.d. از $Exponential(\lambda)$ باشند. آنگاه $F(x) = 1 - e^{-\lambda x}$ برای $x \ge 0$. 
CDF کمینه برابر $F_{X_{(1)}}(x) = 1 - [1 - (1 - e^{-\lambda x})]^n = 1 - [e^{-\lambda x}]^n = 1 - e^{-n\lambda x}$. 
این CDF توزیع $Exponential(n\lambda)$ است. پس کمینهٔ $n$ متغیر نمایی i.i.d. نیز نمایی است، با نرخ $n$ برابر نرخ اصلی.

+++

## کار عملی: شبیه‌سازی‌ها و مقایسه‌ها

+++

### شبیه‌سازی مجموع دو متغیر تصادفی یکنواخت مستقل

انتظار داریم مجموع دو متغیر مستقل $Uniform(0, 1)$ توزیع مثلثی روی $(0, 2)$ را دنبال کند، با PDF:
$$ f_Z(z) = \begin{cases} z & 0 \le z \le 1 \\ 2-z & 1 < z \le 2 \\ 0 & \text{otherwise} \end{cases} $$ 
بیایید این را شبیه‌سازی کنیم و هیستوگرام مجموع‌های شبیه‌سازی‌شده را با PDF نظری مقایسه کنیم.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# --- Simulation Parameters ---
num_simulations = 100000

# --- Simulate Uniform Random Variables ---
# Generate pairs of independent Uniform(0, 1) variables
X = np.random.rand(num_simulations)
Y = np.random.rand(num_simulations)

# --- Calculate the Sum ---
Z = X + Y

# --- Define the Theoretical PDF ---
def triangular_pdf(z):
    if 0 <= z <= 1:
        return z
    elif 1 < z <= 2:
        return 2 - z
    else:
        return 0

# Vectorize the function for plotting
v_triangular_pdf = np.vectorize(triangular_pdf)

# --- Plotting ---
plt.figure(figsize=(10, 6))

# Plot histogram of simulated sums
plt.hist(Z, bins=50, density=True, alpha=0.7, label=f'Simulated Sums (n={num_simulations})')

# Plot theoretical PDF
z_values = np.linspace(0, 2, 400)
pdf_values = v_triangular_pdf(z_values)
plt.plot(z_values, pdf_values, 'r-', lw=2, label='Theoretical Triangular PDF')

plt.title('Sum of Two Independent Uniform(0, 1) Variables')
plt.xlabel('Z = X + Y')
plt.ylabel('Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
```

### شبیه‌سازی آماره‌های ترتیبی: کمینهٔ متغیرهای نمایی

بیایید کمینهٔ $n=5$ متغیر مستقل $Exponential(\lambda=1)$ را شبیه‌سازی کنیم. از نظر نظری $X_{(1)} \sim Exponential(n\lambda = 5)$. بیایید این را به‌صورت بصری تأیید کنیم.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# --- Simulation Parameters ---
num_simulations = 100000
n_variables = 5  # Number of exponential variables
lambda_rate = 1.0 # Rate parameter for individual variables

# --- Simulate Exponential Random Variables ---
# Generate n_variables sets of exponential random variables
# Each row is a simulation, each column is one X_i
exp_samples = np.random.exponential(scale=1.0/lambda_rate, size=(num_simulations, n_variables))

# --- Calculate the Minimum for each simulation ---
X_min = np.min(exp_samples, axis=1)

# --- Theoretical Distribution ---
# The minimum follows Exponential(n * lambda)
theoretical_rate = n_variables * lambda_rate
theoretical_dist = stats.expon(scale=1.0/theoretical_rate)

# --- Plotting ---
plt.figure(figsize=(10, 6))

# Plot histogram of simulated minimums
plt.hist(X_min, bins=50, density=True, alpha=0.7, label=f'Simulated Minima (n={n_variables}, $\lambda$={lambda_rate})')

# Plot theoretical PDF
x_values = np.linspace(X_min.min(), X_min.max(), 400)
pdf_values = theoretical_dist.pdf(x_values)
plt.plot(x_values, pdf_values, 'r-', lw=2, label=f'Theoretical Exponential PDF (rate={theoretical_rate:.1f})')

plt.title(f'Distribution of the Minimum of {n_variables} i.i.d. Exponential({lambda_rate}) Variables')
plt.xlabel('Value of Minimum ($X_{(1)}$)')
plt.ylabel('Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
```

## خلاصه

این فصل روش‌های یافتن توزیع توابع چند متغیر تصادفی را معرفی کرد. به‌طور خاص بررسی کردیم:

* **مجموع متغیرهای مستقل:** با کانولوشن (حالت گسسته و پیوسته). نتایج مهمی مانند مجموع Poissonهای مستقل که Poisson می‌شود و مجموع نرمال‌های مستقل که نرمال می‌شود را دیدیم.
* **تبدیل‌های چندمتغیره:** با دترمینان ژاکوبی برای یافتن PDF مشترک متغیرهای تبدیل‌شده، با مثال تبدیل دکارتی به قطبی.
* **آماره‌های ترتیبی:** استنتاج توزیع‌ها (CDF و PDF) برای کمینه ($X_{(1)}$) و بیشینه ($X_{(n)}$) یک نمونهٔ i.i.d.

از شبیه‌سازی برای تأیید تجربی نتایج نظری استفاده کردیم، مانند توزیع مثلثی حاصل از مجموع دو یکنواخت و توزیع نمایی حاصل از کمینهٔ نمایی‌ها. شبیه‌سازی وقتی استنتاج‌های تحلیلی بیش از حد پیچیده یا غیرممکن می‌شوند، ابزاری حیاتی است.

+++

## تمرین‌ها

1.  **مجموع دو Poisson:** فرض کنید $X \sim Poisson(2)$ و $Y \sim Poisson(3)$ مستقل‌اند. 
    a. توزیع $Z = X + Y$ چیست؟
    b. $P(Z=4)$ را محاسبه کنید.
    c. $X$ و $Y$ را بارها شبیه‌سازی کنید، مجموع $Z$ را محاسبه کنید و هیستوگرام مقادیر شبیه‌سازی‌شدهٔ $Z$ را بسازید. هیستوگرام را با PMF نظری بخش (a) مقایسه کنید.
2.  **بیشینهٔ یکنواخت‌ها:** فرض کنید $U_1, U_2, U_3$ i.i.d. از $Uniform(0, 1)$ باشند.
    a. CDF و PDF نظری $U_{(3)} = \max(U_1, U_2, U_3)$ را بیابید.
    b. $U_1, U_2, U_3$ را بارها شبیه‌سازی کنید، بیشینه در هر شبیه‌سازی را بیابید و هیستوگرام بسازید. آن را با PDF نظری بخش (a) مقایسه کنید.
3.  **نسبت نرمال‌ها (توزیع Cauchy):** فرض کنید $X \sim N(0, 1)$ و $Y \sim N(0, 1)$ مستقل‌اند. $X$ و $Y$ را بارها شبیه‌سازی کنید و نسبت $Z = X/Y$ را محاسبه کنید. هیستوگرام مقادیر $Z$ را رسم کنید. این توزیع شبیه چه توزیعی است؟ (توجه: توزیع نظری Cauchy است که ویژگی‌های غیرمعمولی مانند میانگین تعریف‌نشده دارد.)
