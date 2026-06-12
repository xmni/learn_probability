---
title: دانلود Notebookها
---

# دانلود Jupyter Notebookها

تمام فصل‌ها و مطالب به‌صورت Jupyter Notebook (`.ipynb`) در دسترس‌اند تا بتوانید دانلود کرده و به‌صورت محلی اجرا کنید.

## دانلود همه Notebookها

همه Notebookها در یک فایل zip:

📦 [**دانلود همه Notebookها (ZIP)**](../learn_probability_notebooks.zip)

## Notebookهای تکی

### بخش ۱ — مبانی احتمال

- [فصل ۱: مقدمه‌ای بر احتمال و راه‌اندازی پایتون](../notebooks/chapter_01.ipynb)
- [فصل ۲: فضاهای نمونه و رویدادها](../notebooks/chapter_02.ipynb)
- [فصل ۳: اصول احتمال و قواعد پایه](../notebooks/chapter_03.ipynb)

### بخش ۲ — احتمال شرطی و استقلال

- [فصل ۴: احتمال شرطی](../notebooks/chapter_04.ipynb)
- [فصل ۵: استقلال](../notebooks/chapter_05.ipynb)

### بخش ۳ — متغیرهای تصادفی و توزیع‌ها

- [فصل ۶: متغیرهای تصادفی گسسته](../notebooks/chapter_06.ipynb)
- [فصل ۷: متغیرهای تصادفی پیوسته](../notebooks/chapter_07.ipynb)
- [فصل ۸: امید ریاضی و واریانس](../notebooks/chapter_08.ipynb)
- [فصل ۹: توزیع‌های گسسته مهم](../notebooks/chapter_09.ipynb)
- [فصل ۱۰: توزیع‌های پیوسته مهم](../notebooks/chapter_10.ipynb)

### بخش ۴ — چند متغیر تصادفی

- [فصل ۱۱: توزیع‌های مشترک](../notebooks/chapter_11.ipynb)
- [فصل ۱۲: کوواریانس و همبستگی](../notebooks/chapter_12.ipynb)
- [فصل ۱۳: امید ریاضی شرطی](../notebooks/chapter_13.ipynb)

### بخش ۵ — قضایای حدی و اهمیت آن‌ها

- [فصل ۱۴: توابع مولد گشتاور](../notebooks/chapter_14.ipynb)
- [فصل ۱۵: قضیه حد مرکزی](../notebooks/chapter_15.ipynb)

### بخش ۶ — مباحث پیشرفته و کاربردها

- [فصل ۱۶: زنجیره‌های مارکوف](../notebooks/chapter_16.ipynb)
- [فصل ۱۷: فرآیندهای پواسون](../notebooks/chapter_17.ipynb)
- [فصل ۱۸: مقدمه‌ای بر آمار بیزی](../notebooks/chapter_18.ipynb)
- [فصل ۱۹: استنتاج آماری پایه](../notebooks/chapter_19.ipynb)
- [فصل ۲۰: روش‌های مونت‌کارلو](../notebooks/chapter_20.ipynb)
- [فصل ۲۱: کاربردها و مطالعات موردی](../notebooks/chapter_21.ipynb)

### تمرین‌ها و آزمایشگاه

- [تمرین‌های فصل ۴](../notebooks/chapter_04_exercises_a.ipynb)
- [آزمایشگاه فصل ۴](../notebooks/chapter_04_lab.ipynb)
- [آزمایشگاه فصل ۵](../notebooks/chapter_05_lab.ipynb)

### پیوست‌ها

- [پیوست الف: مقدمه برنامه‌نویسی پایتون](../notebooks/appendix_a.ipynb)
- [پیوست ب: مفاهیم ریاضی کلیدی](../notebooks/appendix_b.ipynb)
- [پیوست ج: مرجع توزیع‌های احتمال رایج](../notebooks/appendix_c.ipynb)
- [پیوست د: پاسخ تمرین‌های منتخب](../notebooks/appendix_d.ipynb)
- [پیوست ه: منابع بیشتر](../notebooks/appendix_e.ipynb)

## نحوه استفاده از Notebookهای دانلودشده

1. **فایل ZIP را استخراج کنید** (اگر آرشیو کامل را دانلود کرده‌اید)
2. **Jupyter را نصب کنید:** `pip install jupyter notebook`
3. **بسته‌های مورد نیاز را نصب کنید:** `pip install -r requirements.txt`
4. **Jupyter را اجرا کنید:** `jupyter notebook`
5. **هر Notebook را باز کرده و اجرا کنید**

## پیش‌نیازها

برای اجرای این Notebookها به Python 3.11+ و بسته‌های زیر نیاز دارید:

- jupyter-book
- matplotlib
- matplotlib-venn
- numpy
- pandas
- scipy
- seaborn
- sympy

نصب همه پیش‌نیازها:

```bash
pip install -r requirements.txt
```

## جایگزین: اجرا در ابر

نمی‌خواهید چیزی محلی نصب کنید؟ می‌توانید:

- 🚀 **در مرورگر اجرا کنید:** بیشتر صفحات گزینه JupyterLite تعاملی دارند
- ☁️ **در Binder اجرا کنید:** روی نشان Binder هر فصل کلیک کنید تا در ابر اجرا شود
