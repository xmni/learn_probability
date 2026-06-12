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
  - file: notebooks/chapter_01.ipynb
---

# فصل ۱: مقدمه‌ای بر احتمال و راه‌اندازی پایتون

به «احتمال در عمل: سفری عملی با پایتون» خوش آمدید! این فصل اول، پایه‌های کاوش ما را می‌گذارد. ابتدا می‌فهمیم احتمال چیست و چرا در بسیاری از حوزه‌ها مفهومی بنیادین است. سپس ابزارهای ضروری پایتونی را که در سراسر کتاب از آن‌ها استفاده می‌کنیم معرفی می‌کنیم و شما را در راه‌اندازی محیط کار و انجام چند عملیات پایه راهنمایی می‌کنیم.

+++

## ۱.۱ احتمال چیست؟ چرا مهم است؟

در هستهٔ خود، **احتمال** زبان ریاضی است که با آن **عدم‌قطعیت** را توصیف و کمی‌سازی می‌کنیم. روشی برای سنجش احتمال یا شانس وقوع یک رویداد مشخص از میان مجموعه‌ای از پیامدهای ممکن است. احتمال را به‌صورت عددی بین ۰ و ۱ (شامل هر دو) بیان می‌کنیم:

* احتمال **۰** یعنی رویداد غیرممکن است.
* احتمال **۱** یعنی رویداد قطعی است.
* احتمالی بین ۰ و ۱ درجه‌های مختلف محتمل بودن را نشان می‌دهد (مثلاً ۰٫۵ یعنی ۵۰٪ شانس، مانند فرود آمدن یک سکهٔ منصفانه روی شیر).

**چرا احتمال مهم است؟**

عدم‌قطعیت در تقریباً هر جنبه‌ای از دنیای اطراف ما ذاتی است. احتمال راهی نظام‌مند برای استدلال، مدل‌سازی و تصمیم‌گیری در برابر این عدم‌قطعیت فراهم می‌کند. کاربردهای آن گسترده است و حوزه‌های متعددی را در بر می‌گیرد:

* **علوم:** مدل‌سازی مکانیک کوانتومی، پیش‌بینی پیامدهای آزمایشگاهی، تحلیل وراثت ژنتیکی.
* **مهندسی:** ارزیابی یکپارچگی سازه تحت تنش، طراحی سامانه‌های قابل‌اعتماد، مدیریت ترافیک شبکه‌های ارتباطی.
* **مالی و اقتصاد:** قیمت‌گذاری اختیار معامله و مشتقات، مدیریت سبد سرمایه‌گذاری، پیش‌بینی حرکت بازار، ارزیابی ریسک اعتباری.
* **پزشکی:** ارزیابی اثربخشی درمان‌های جدید، درک انتقال بیماری، تفسیر آزمون‌های تشخیصی.
* **یادگیری ماشین و هوش مصنوعی:** ساخت فیلتر هرزنامه، آموزش مدل‌های پیش‌بینی، طراحی سامانه‌های توصیه‌گر، کمی‌سازی اطمینان مدل.
* **بازی و قمار:** محاسبهٔ شانس، توسعهٔ راهبردهای بازی.
* **زندگی روزمره:** پیش‌بینی آب‌وهوا، تصمیم‌گیری دربارهٔ خرید بیمه، درک نظرسنجی‌ها.

**مثال:** تصور کنید شرکتی در حال بررسی عرضهٔ محصول جدیدی است. داده‌های تحقیقات بازار بینش می‌دهند، اما قطعی نیستند. احتمال به کمی‌سازی ریسک کمک می‌کند. بر اساس نتایج نظرسنجی، تحلیل رقبا و پیش‌بینی‌های اقتصادی، شرکت ممکن است برآورد کند:

* P(High Success) = 0.2 (۲۰٪ شانس فروش بالا)
* P(Moderate Success) = 0.5 (۵۰٪ شانس فروش متوسط)
* P(Failure) = 0.3 (۳۰٪ شانس شکست)

این احتمال‌ها، همراه با سود/زیان بالقوه برای هر سناریو، به شرکت اجازه می‌دهند تصمیم آگاهانه‌تری بگیرد که آیا پاداش بالقوه، ریسک را توجیه می‌کند یا نه.

در سراسر این کتاب خواهیم دید که احتمال چگونه ما را از شهود مبهم دربارهٔ عدم‌قطعیت به تحلیل دقیق و کمی می‌برد؛ اغلب با کمک قدرت محاسباتی پایتون.

+++

## ۱.۲ معرفی ابزارها

برای آغاز سفر عملی خود به ابزارهای مناسب نیاز داریم. عمدتاً از پایتون همراه با چند کتابخانهٔ قدرتمند برای محاسبات علمی، تحلیل داده و مصورسازی استفاده می‌کنیم.

1.  **Python:** زبان برنامه‌نویسی سطح‌بالا و چندمنظوره که به خوانایی و اکوسیستم گستردهٔ کتابخانه‌هایش شهرت دارد. انتخابی عالی هم برای یادگیری مفاهیم و هم برای پیاده‌سازی کاربردهای عملی است.

2.  **Jupyter Notebooks:** محیط محاسباتی تعاملی که امکان ساخت و به‌اشتراک‌گذاری سندهایی حاوی کد زنده، معادلات، مصورسازی‌ها و متن روایی را می‌دهد. برای تحلیل اکتشافی، یادگیری گام‌به‌گام و ارائهٔ نتایج ایده‌آل‌اند. برای همهٔ مثال‌هایمان از Jupyter Notebook (یا محیط‌های سازگار مانند JupyterLab، Google Colab، VS Code Notebooks) استفاده می‌کنیم.

3.  **NumPy (Numerical Python):** بستهٔ بنیادین محاسبات عددی در پایتون. موارد زیر را فراهم می‌کند:
    * شیء آرایهٔ N-بعدی قدرتمند (`ndarray`).
    * توابع برای عملیات ریاضی، جبر خطی، تولید اعداد تصادفی و موارد دیگر.
    * پایه‌ای که بسیاری از کتابخانه‌های علمی دیگر بر آن بنا شده‌اند.
    * **مثال:** شبیه‌سازی ۱۰ پرتاب سکه (۰ برای خط، ۱ برای شیر):
                                             
      ```python
      import numpy as np
      flips = np.random.randint(0, 2, size=10)
      print(flips) # Output might be: [0 1 1 0 1 0 0 1 0 1]
      ```

4.  **Matplotlib & Seaborn:** کتابخانه‌های مصورسازی داده.
    * **Matplotlib:** کتابخانه‌ای جامع برای ساخت مصورسازی‌های ایستا، پویا و تعاملی. کنترل دقیق بر نمودارها را فراهم می‌کند.
    * **Seaborn:** بر پایهٔ Matplotlib ساخته شده و رابط سطح‌بالایی برای رسم نمودارهای آماری جذاب و آموزنده، اغلب با کد کمتر، ارائه می‌دهد. از هر دو استفاده می‌کنیم؛ Seaborn برای نمودارهای سریع و استاندارد و Matplotlib برای سفارشی‌سازی.
    * **مثال:** ساخت یک هیستوگرام ساده (مثال کامل را در بخش عملی خواهیم دید).

5.  **SciPy (Scientific Python):** کتابخانه‌ای که بر NumPy بنا شده و مجموعهٔ بزرگی از الگوریتم‌ها و توابع برای محاسبات علمی و فنی فراهم می‌کند. به‌طور خاص از ماژول `scipy.stats` آن استفاده می‌کنیم که ابزارهایی برای موارد زیر دارد:
    * کار با طیف گسترده‌ای از توزیع‌های احتمال (محاسبهٔ احتمال‌ها، تولید اعداد تصادفی، برازش توزیع‌ها به داده).
    * انجام آزمون‌های آماری.
    * **مثال:** محاسبهٔ احتمال دقیقاً ۳ شیر در ۵ پرتاب سکهٔ منصفانه با استفاده از توزیع دوجمله‌ای (بیشتر در فصول بعد).

نگران نباشید اگر الان زیاد به نظر می‌رسد. توابع و مفاهیم این کتابخانه‌ها را به‌تدریج و در جایی که لازم باشد در سراسر کتاب معرفی می‌کنیم. نکتهٔ کلیدی این است که ابتدا با محیط و عملیات پایه راحت شوید.

+++

## ۱.۳ عملی: راه‌اندازی و عملیات پایه

بیایید دست به کار شویم! این بخش راه‌اندازی محیط کار و امتحان چند فرمان پایه را گام‌به‌گام توضیح می‌دهد.

### ۱.۳.۱ راه‌اندازی محیط

ساده‌ترین راه برای نصب پایتون و کتابخانه‌های لازم، نصب **Anaconda Distribution** است. Anaconda پایتون، Jupyter، NumPy، SciPy، Matplotlib و بسیاری کتابخانه‌های علمی مفید دیگر را در یک بستهٔ نصب آسان جمع می‌کند.

1.  **دانلود Anaconda:** به [وب‌سایت Anaconda Distribution](https://www.anaconda.com/products/distribution) بروید و نصب‌کننده را برای سیستم‌عامل خود (Windows، macOS، Linux) دانلود کنید.
2.  **نصب Anaconda:** نصب‌کننده را اجرا کنید و دستورالعمل‌های روی صفحه را دنبال کنید. معمولاً توصیه می‌شود تنظیمات پیش‌فرض را بپذیرید مگر دلیل خاصی برای تغییر داشته باشید.
3.  **اجرای Jupyter Notebook/Lab:**
    * **با Anaconda Navigator:** Anaconda Navigator را باز کنید (که همراه Anaconda نصب شده) و «Jupyter Notebook» یا «JupyterLab» را اجرا کنید (JupyterLab رابط مدرن‌تری است).
    * **با Terminal/Command Prompt:** ترمینال (macOS/Linux) یا Anaconda Prompt (Windows) را باز کنید، `jupyter notebook` یا `jupyter lab` را تایپ کنید و Enter بزنید.

مرورگر وب باید باز شود و رابط Jupyter را نشان دهد؛ معمولاً فایل‌های پوشهٔ خانگی شما را نمایش می‌دهد.

**جایگزین (با pip):** اگر پایتون از قبل نصب دارید و ترجیح می‌دهید از Anaconda استفاده نکنید، می‌توانید کتابخانه‌ها را جداگانه با `pip`، نصب‌کنندهٔ بستهٔ پایتون، نصب کنید. ترمینال یا command prompt را باز کنید و اجرا کنید:
```bash
pip install numpy matplotlib seaborn scipy jupyterlab
```
سپس با تایپ `jupyter lab` در ترمینال، JupyterLab را اجرا کنید.

### ۱.۳.۲ استفادهٔ پایه از Jupyter

Jupyter Notebook از **سلول**‌ها تشکیل شده است. دو نوع اصلی عبارت‌اند از:

* **سلول‌های کد:** حاوی کد پایتونی که می‌توانید اجرا کنید.
* **سلول‌های Markdown:** حاوی متن، سرتیترها، فهرست‌ها، تصاویر و معادلات با قالب Markdown (مثل همین سلول!).

**عملیات کلیدی:**

* **اجرای سلول:** با کلیک روی سلول آن را انتخاب کنید و `Shift + Enter` بزنید (یا دکمهٔ «Run» در نوار ابزار). این کار کد را اجرا می‌کند (اگر سلول کد باشد) یا متن را رندر می‌کند (اگر Markdown باشد) و به سلول بعدی می‌رود. `Ctrl + Enter` سلول را اجرا می‌کند اما روی همان سلول می‌ماند.
* **تغییر نوع سلول:** از منوی کشویی نوار ابزار برای جابه‌جایی بین Code و Markdown استفاده کنید.
* **افزودن سلول:** از دکمهٔ `+` در نوار ابزار استفاده کنید.
* **ذخیره:** نوت‌بوک‌ها خودکار ذخیره می‌شوند، اما می‌توانید با `Ctrl + S` یا آیکون ذخیره، ذخیرهٔ اجباری انجام دهید.

**امتحان کنید:** یک سلول کد جدید بسازید، `print("Hello Probability!")` را تایپ کنید و با `Shift + Enter` اجرا کنید.

```{code-cell} ipython3
print("Hello Probability!")
```

### ۱.۳.۳ دستکاری‌های سادهٔ آرایه در NumPy

بیایید چند آرایهٔ NumPy بسازیم و عملیات پایه انجام دهیم. قرارداد استاندارد این است که NumPy را به‌صورت `np` وارد کنیم.

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
# Create a 1D array (vector) from a list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("1D Array:", my_array)
print("Type:", type(my_array))
print("Shape:", my_array.shape) # Shape is (5,) meaning 5 elements along one dimension
```

```{code-cell} ipython3
# Create a 2D array (matrix)
my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", my_2d_array)
print("Shape:", my_2d_array.shape) # Shape is (2, 3) meaning 2 rows, 3 columns
```

```{code-cell} ipython3
# Create arrays with specific values
zeros_array = np.zeros((2, 4)) # Array of zeros with shape (2, 4)
print("\nZeros Array:\n", zeros_array)
```

```{code-cell} ipython3
ones_array = np.ones(5) # Array of ones with shape (5,)
print("\nOnes Array:", ones_array)
```

```{code-cell} ipython3
# Create arrays with sequences
range_array = np.arange(0, 10, 2) # Like Python's range: start, stop (exclusive), step
print("\nRange Array:", range_array)
```

```{code-cell} ipython3
# Basic arithmetic operations (element-wise)
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
```

```{code-cell} ipython3
print("\nArray Addition:", arr1 + arr2)
print("Array Multiplication:", arr1 * arr2)
print("Adding a scalar:", arr1 + 100)
```

```{code-cell} ipython3
# Random numbers
# Generate 5 random numbers from a uniform distribution between 0 and 1
random_uniform = np.random.rand(5)
print("\nRandom Uniform:", random_uniform)
```

```{code-cell} ipython3
# Generate 6 random integers between 1 (inclusive) and 7 (exclusive) - simulating dice rolls
dice_rolls_example = np.random.randint(1, 7, size=6)
print("Simulated Dice Rolls:", dice_rolls_example)
```

### ۱.۳.۴ رسم نمودار پایه با Matplotlib

مصورسازی برای درک توزیع‌های احتمال و نتایج شبیه‌سازی حیاتی است. بیایید پرتاب‌های زیاد یک تاس شش‌وجهی استاندارد را شبیه‌سازی کنیم و هیستوگرام پیامدها را رسم کنیم. انتظار داریم اگر پرتاب‌ها زیاد باشند، هر پیامد (۱ تا ۶) تقریباً به‌یکسان محتمل باشد.

از `matplotlib.pyplot` استفاده می‌کنیم که معمولاً به‌صورت `plt` وارد می‌شود.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np # Ensure numpy is imported
```

```{code-cell} ipython3
# --- Simulation Parameters ---
num_rolls = 1000  # Let's simulate rolling the die 1000 times
die_sides = 6
```

```{code-cell} ipython3
# --- Simulate the Dice Rolls ---
# np.random.randint(low, high, size) generates integers from low (inclusive) to high (exclusive)
rolls = np.random.randint(1, die_sides + 1, size=num_rolls)
```

```{code-cell} ipython3
# --- Create the Histogram ---
# plt.hist() calculates and draws the histogram
# bins defines the edges of the bins. We want bins [1, 2), [2, 3), ..., [6, 7)
# We use np.arange(1, die_sides + 2) which gives [1, 2, 3, 4, 5, 6, 7]
# align='left' means the bar label corresponds to the left edge (e.g., label '1' for bin [1, 2))
# rwidth controls the relative width of the bars
plt.figure(figsize=(8, 5)) # Optional: sets the figure size
plt.hist(rolls, bins=np.arange(1, die_sides + 2), align='left', rwidth=0.8, color='skyblue', edgecolor='black')

# --- Add Labels and Title ---
plt.title(f'Histogram of {num_rolls} Dice Rolls')
plt.xlabel('Die Outcome')
plt.ylabel('Frequency (Count)')
plt.xticks(np.arange(1, die_sides + 1)) # Set ticks explicitly to 1, 2, ..., 6
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add horizontal grid lines
```

اگر سلول کد بالا را اجرا کنید، باید یک هیستوگرام ببینید. چون پرتاب‌ها تصادفی‌اند، میله‌ها کاملاً برابر نخواهند بود، به‌ویژه با فقط ۱۰۰۰ پرتاب. با این حال باید ببینید که فراوانی هر پیامد (۱ تا ۶) تقریباً مشابه است. با افزایش `num_rolls` (مثلاً به ۱۰۰۰۰ یا ۱۰۰۰۰۰ تغییر دهید و دوباره اجرا کنید)، میله‌ها باید ارتفاع نزدیک‌تری پیدا کنند؛ این مفهوم یکسان شدن احتمال‌ها در آزمایش‌های زیاد را نشان می‌دهد (که بعداً به‌طور رسمی قانون اعداد بزرگ می‌نامیم).

+++

## خلاصهٔ فصل

در این فصل، مفهوم بنیادین احتمال را به‌عنوان معیاری برای عدم‌قطعیت معرفی کردیم و اهمیت آن را در حوزه‌های گوناگون برجسته کردیم. همچنین با جعبه‌ابزار ضروری پایتون این کتاب آشنا شدیم: Jupyter Notebook، NumPy، Matplotlib و SciPy. در پایان، راه‌اندازی محیط را گام‌به‌گام پیش بردیم و عملیات پایه‌ای از جمله دستکاری آرایه با NumPy و رسم هیستوگرام با Matplotlib را انجام دادیم.

اکنون باید محیط پایتون کارا داشته باشید و درک پایه‌ای از اجرای کد و مصورسازی دادهٔ ساده در Jupyter Notebook.

در فصل بعد به زبان رسمی احتمال می‌پردازیم؛ واژه‌های کلیدی مانند فضای نمونه، رویداد و پیامد را تعریف می‌کنیم و اصول و قواعد بنیادین حاکم بر محاسبات احتمال را بررسی می‌کنیم.
