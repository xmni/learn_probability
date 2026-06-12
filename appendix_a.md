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
  - file: notebooks/appendix_a.ipynb
---

# پیوست الف: راهنمای عمیق راه‌اندازی Python/Jupyter

+++

## مقدمه

به جنبهٔ عملی احتمال خوش آمدید! این کتاب به‌شدت بر استفاده از پایتون و کتابخانه‌های مشخص در محیط Jupyter Notebook برای کاوش مفاهیم، اجرای شبیه‌سازی‌ها و مصورسازی نتایج تکیه دارد. این پیوست راهنمای مفصلی برای راه‌اندازی این محیط روی رایانهٔ شما ارائه می‌دهد.

هدف ما اطمینان از این است که بتوانید:
1.  پایتون را نصب کنید.
2.  Jupyter Notebookها را اجرا کنید.
3.  کتابخانه‌های علمی اصلی — NumPy، SciPy، Matplotlib و Seaborn — را نصب و تأیید کنید.
4.  به مثال‌های کد کتاب دسترسی داشته باشید.

حتی اگر با پایتون آشنایی دارید، توصیه می‌کنیم برای اطمینان از داشتن همان راه‌اندازی مورد استفاده در سراسر کتاب، مرور سریعی انجام دهید.

+++

## ۱. نصب پایتون: توزیع Anaconda

ساده‌ترین راه برای نصب همزمان پایتون و کتابخانه‌های علمی ضروری، استفاده از **Anaconda Distribution** است. Anaconda پایتون، Jupyter، بسیاری از کتابخانه‌های اصلی (مانند NumPy، SciPy، Matplotlib، Pandas) و یک مدیر بسته (`conda`) را که نصب و مدیریت محیط‌ها را ساده می‌کند، یکجا فراهم می‌کند.

**مراحل:**

1.  **دانلود:** به وب‌سایت Anaconda Distribution بروید: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2.  **انتخاب نصب‌کننده:** نصب‌کنندهٔ مناسب سیستم‌عامل خود (Windows، macOS، Linux) را دانلود کنید. آخرین نسخهٔ Python 3.x را انتخاب کنید.
3.  **اجرای نصب‌کننده:** فایل دانلودشده را اجرا کنید. دستورالعمل‌های روی صفحه را دنبال کنید.
    * **توصیه:** مگر دلیل خاصی دارید، تنظیمات پیش‌فرض را بپذیرید. این معمولاً شامل افزودن Anaconda به متغیر محیطی PATH سیستم می‌شود (اگرچه نصب‌کننده ممکن است برای کاربران پیشرفته توصیهٔ مخالف بدهد، برای مبتدیان اغلب ساده‌تر است).
    * برای نصب Anaconda فقط برای کاربر خود، **نیازی** به دسترسی مدیر سیستم ندارید که اغلب کافی است.

**تأیید:**

پس از تکمیل نصب، ترمینال یا command prompt سیستم را باز کنید:
* **Windows:** در منوی Start عبارت `Anaconda Prompt` را جستجو کرده و آن را باز کنید.
* **macOS:** برنامهٔ `Terminal` را باز کنید (در Applications > Utilities).
* **Linux:** ترمینال استاندارد خود را باز کنید.

در ترمینال، دستور زیر را تایپ کرده و Enter بزنید:

```bash
python --version
```

باید خروجی مشابه `Python 3.x.y` (مثلاً `Python 3.10.9`) ببینید که نشان می‌دهد پایتون نصب و در دسترس است. اگر خطایی مانند "command not found" دریافت کردید، نصب ممکن است درست تکمیل نشده باشد یا Anaconda به PATH اضافه نشده باشد (ممکن است نیاز به نصب مجدد یا افزودن دستی داشته باشید؛ مستندات Anaconda را ببینید).

+++

## ۲. Jupyter Notebookها

Jupyter Notebookها محیطی تعاملی مبتنی بر مرورگر فراهم می‌کنند که در آن می‌توانید کد پایتون بنویسید و اجرا کنید، متن توضیحی (مانند همین!) اضافه کنید، معادلات ریاضی بگنجانید و مصورسازی‌ها را نمایش دهید — همه در یک سند. Anaconda با Jupyter از پیش نصب‌شده عرضه می‌شود.

**راه‌اندازی JupyterLab (رابط توصیه‌شده):**

1.  Anaconda Prompt (Windows) یا Terminal (macOS/Linux) را باز کنید.
2.  به پوشه‌ای بروید که می‌خواهید notebookها را در آن نگه دارید (یا جایی که کد کتاب را دانلود کرده‌اید). می‌توانید از دستور `cd` (change directory) استفاده کنید. مثلاً:
    ```bash
    # Example for Windows - navigate to a 'ProbBook' folder on the C drive
    cd C:\Users\YourUsername\Documents\ProbBook 
    
    # Example for macOS/Linux - navigate to a 'ProbBook' folder in your home directory
    cd ~/Documents/ProbBook 
    ```
3.  دستور زیر را تایپ کرده و Enter بزنید:
    ```bash
    jupyter lab
    ```
4.  این باید به‌طور خودکار یک برگهٔ جدید در مرورگر پیش‌فرض باز کند و رابط JupyterLab را نمایش دهد. پنجرهٔ ترمینال باید هنگام استفاده از JupyterLab باز بماند.

**راه‌اندازی Jupyter Notebook کلاسیک (جایگزین):**

اگر رابط کلاسیک را ترجیح می‌دهید، به‌جای آن از این دستور استفاده کنید:
```bash
jupyter notebook
```

**استفادهٔ پایه از Jupyter:**

* **رابط:** JupyterLab معمولاً مرورگر فایل را در سمت چپ و ناحیهٔ کار اصلی را در سمت راست نشان می‌دهد. می‌توانید فایل‌های notebook موجود `.ipynb` را باز کنید یا جدید بسازید (File > New > Notebook).
* **سلول‌ها:** notebookها از سلول‌ها تشکیل شده‌اند. دو نوع اصلی عبارت‌اند از:
    * **سلول‌های کد:** حاوی کد پایتون برای اجرا. یک سلول کد را انتخاب کرده و `Shift + Enter` (یا دکمهٔ Run) بزنید تا کد اجرا شود. خروجی زیر سلول ظاهر می‌شود.
    * **سلول‌های Markdown:** حاوی متن قالب‌بندی‌شده (با نحو Markdown)، مانند این سلول. `Shift + Enter` را برای رندر Markdown بزنید.
* **هسته (Kernel):** «موتور» اجرای کد. اگر گیر کردید می‌توانید هسته را راه‌اندازی مجدد کنید (Kernel > Restart Kernel...).
* **ذخیره:** notebookها به‌طور خودکار ذخیره می‌شوند، اما می‌توانید دستی از File > Save Notebook ذخیره کنید.
* **بستن:** برگهٔ مرورگر را ببندید. در ترمینالی که Jupyter را راه‌اندازی کردید، `Ctrl + C` بزنید (ممکن است دو بار لازم باشد) و در صورت درخواست، خاموش‌سازی را تأیید کنید.

+++

## ۳. نصب/تأیید کتابخانه‌های اصلی

Anaconda معمولاً مهم‌ترین کتابخانه‌های این کتاب را به‌طور خودکار نصب می‌کند. این‌ها شامل موارد زیرند:

* **NumPy:** بستهٔ بنیادین محاسبات عددی، به‌ویژه آرایه‌ها (`np`).
* **SciPy:** کتابخانهٔ محاسبات علمی و فنی بر پایهٔ NumPy (`scipy`). به‌شدت از `scipy.stats`، `scipy.special` و `scipy.integrate` استفاده می‌کنیم.
* **Matplotlib:** کتابخانهٔ اصلی رسم نمودار (`plt`).
* **Pandas:** کتابخانهٔ دستکاری و تحلیل داده (اغلب همراه NumPy، `pd`). اگرچه تمرکز اصلی نیست، برای کار با مجموعه‌داده‌ها در مثال‌ها مفید است.

**Seaborn**، کتابخانهٔ مصورسازی مبتنی بر Matplotlib که رابط سطح‌بالایی برای رسم نمودارهای آماری جذاب فراهم می‌کند (`sns`)، گاهی ممکن است جداگانه نصب شود.

**بررسی و نصب کتابخانه‌ها:**

1.  **با Conda (توصیه‌شده با Anaconda):**
    Anaconda Prompt یا Terminal را باز کرده و از `conda install` استفاده کنید:
    ```bash
    conda install numpy scipy matplotlib pandas seaborn
    ```
    Conda بررسی می‌کند بسته‌ها نصب باشند و در صورت نیاز به‌روزرسانی یا نصب می‌کند.

2.  **با Pip (جایگزین):**
    اگر از Anaconda استفاده نمی‌کنید یا pip را ترجیح می‌دهید:
    ```bash
    pip install numpy scipy matplotlib pandas seaborn
    ```
    *توجه: معمولاً توصیه می‌شود در یک محیط فقط از یک مدیر بسته (`conda` یا `pip`) استفاده کنید تا از تداخل احتمالی جلوگیری شود.*

**تأیید:**

بهترین راه تأیید، ساخت یک Jupyter Notebook جدید و اجرای سلول کد زیر است. اگر بدون پیام `ImportError` اجرا شود، کتابخانه‌های اصلی شما آماده‌اند.

```{code-cell} ipython3
# Verification Cell: Import Core Libraries

import math
import platform # Moved import to the top
import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
import scipy.special
import scipy.integrate
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Check versions (optional, but good for debugging)
print(f"Python version: {platform.python_version()}") 
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"SciPy version: {scipy.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"Seaborn version: {sns.__version__}")

# Basic functionality test
try:
    arr = np.array([1, 2, 3])
    mean_val = np.mean(arr)
    binom_prob = stats.binom.pmf(k=1, n=2, p=0.5)
    plt.figure()
    sns.histplot([1, 2, 2, 3, 3, 3])
    plt.close() # Prevents plot from displaying here
    print("\nCore libraries imported and basic functions tested successfully!")
except Exception as e:
    print(f"\nAn error occurred during testing: {e}")
    print("Please check your installations.")
```

## ۴. دریافت کد کتاب

همهٔ Jupyter Notebookهای حاوی مثال‌های کد و تمرین‌های این کتاب به‌صورت آنلاین در دسترس‌اند، معمولاً در یک مخزن GitHub.

* **مکان:** برای URL دقیق مخزن GitHub به پیش‌گفتار یا وب‌سایت همراه کتاب مراجعه کنید (مثلاً `https://github.com/snowch/learn_probability`).

**نحوهٔ دانلود:**

1.  **دانلود ZIP:** ساده‌ترین راه اغلب رفتن به صفحهٔ اصلی مخزن GitHub در مرورگر و جستجوی دکمهٔ سبز «Code» است. با کلیک روی آن معمولاً گزینهٔ «Download ZIP» ظاهر می‌شود. فایل را دانلود کرده و در مکان مناسبی روی رایانه (مثلاً پوشهٔ `ProbBook` که ممکن است قبلاً ساخته باشید) از حالت فشرده خارج کنید.
2.  **با Git (پیشرفته‌تر):** اگر با Git آشنا هستید، می‌توانید مخزن را clone کنید. ترمینال یا Anaconda Prompt را باز کرده، به محل مورد نظر بروید و اجرا کنید:
    ```bash
    git clone https://github.com/snowch/learn_probability.git
    ```
    این روش دریافت به‌روزرسانی‌های بعدی با `git pull` را آسان‌تر می‌کند.

پس از دانلود، می‌توانید JupyterLab یا Jupyter Notebook را از پوشهٔ حاوی کد راه‌اندازی کنید و باید فایل‌های `.ipynb` آمادهٔ باز شدن را ببینید.

+++

## ۵. عیب‌یابی پایه

اگر با مشکل روبه‌رو شدید، چند مسئلهٔ رایج و پیشنهادها:

* **`command not found` (مثلاً `python`، `jupyter`، `conda`):** این معمولاً یعنی Anaconda/Python در PATH سیستم نیست. سعی کنید از `Anaconda Prompt` استفاده کنید، زیرا از پیش پیکربندی شده است. اگر از ترمینال استاندارد استفاده می‌کنید، ممکن است نیاز به نصب مجدد Anaconda (با انتخاب گزینهٔ «Add to PATH»، اگر برای سطح راحتی شما مناسب است) یا پیکربندی دستی PATH داشته باشید (مستندات Anaconda را ببینید).
* **`ImportError: No module named 'some_library'`:** کتابخانهٔ مشخص (مثلاً `seaborn`) در محیط پایتونی که Jupyter از آن استفاده می‌کند نصب نیست. در Anaconda Prompt/Terminal از `conda install some_library` یا `pip install some_library` استفاده کنید. مطمئن شوید در همان محیطی نصب می‌کنید که Jupyter از آن اجرا می‌شود (معمولاً محیط «base» اگر محیط دیگری نساخته‌اید).
* **کد بی‌پایان اجرا می‌شود یا crash می‌کند:** هستهٔ Jupyter را راه‌اندازی مجدد کنید (Kernel > Restart Kernel...). این اغلب مشکلات ناشی از متغیرهایی با حالت‌های غیرمنتظره را حل می‌کند.
* **نمودارها نمایش داده نمی‌شوند:** مطمئن شوید `%matplotlib inline` را اجرا کرده‌اید (معمولاً در ابتدای notebookها) یا خطاهای خاص در کد رسم را بررسی کنید.
* **خطاهای دسترسی (conda/pip):** اگر Anaconda را در سطح سیستم نصب کرده‌اید، ممکن است برای نصب بسته‌های جدید به دسترسی مدیر نیاز داشته باشید. Anaconda Prompt را «به‌عنوان Administrator» (Windows) اجرا کنید یا از `sudo` (macOS/Linux، با احتیاط) استفاده کنید.
* **جستجوی کمک:** پیام خطا را در موتور جستجو مانند Google کپی کنید. عباراتی مانند `python`، `jupyter`، `conda` و نام کتابخانه را اضافه کنید. Stack Overflow ([stackoverflow.com](https://stackoverflow.com)) منبع عالی برای خطاهای برنامه‌نویسی است.

+++

## ۶. گام‌های بعدی

با راه‌اندازی و تأیید محیط، آمادهٔ ورود به دنیای احتمال با پایتون هستید! اکنون می‌توانید به **فصل ۱: مقدمه‌ای بر احتمال و راه‌اندازی پایتون** بروید تا سفر عملی خود را آغاز کنید.

مطمئن شوید می‌توانید notebook فصل ۱ همراه با مطالب کتاب را باز کرده و چند سلول کد اول را اجرا کنید. کدنویسی و کاوش مبارک!
