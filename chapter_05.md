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
  - file: notebooks/chapter_05.ipynb
---

# فصل ۵: قضیه بیز و استقلال

+++

در فصل پیشین، احتمال شرطی را بررسی کردیم — اینکه چگونه احتمال یک واقعه با فرض وقوع واقعه دیگر تغییر می‌کند. اکنون به یکی از قدرتمندترین و پرکاربردترین نتایج حاصل از احتمال شرطی می‌پردازیم: **قضیه بیز**. این قضیه راهی رسمی برای به‌روزرسانی باورهای ما (احتمال‌ها) در پرتو شواهد جدید فراهم می‌کند. همچنین مفهوم **استقلال** بین واقعه‌ها را به‌صورت رسمی تعریف و بررسی می‌کنیم؛ ایده‌ای حیاتی برای ساده‌سازی محاسبات احتمال.

+++

## اهداف یادگیری:
* اثبات و تفسیر قضیه بیز را درک کنید.
* بین احتمال پیشین و پسین تمایز قائل شوید.
* قضیه بیز را برای حل مسائل، به‌ویژه سناریوهای آزمون تشخیصی، به‌کار ببرید.
* استقلال واقعه‌ها را تعریف و آزمون کنید.
* مفهوم استقلال شرطی را درک کنید.
* به‌روزرسانی‌های بیزی و بررسی استقلال را با شبیه‌سازی پایتون پیاده‌سازی کنید.

+++

## ۱. قضیه بیز: اثبات و تفسیر

+++

قضیه بیز راهی برای «معکوس کردن» احتمال‌های شرطی فراهم می‌کند. اگر $P(B|A)$ را بدانیم، قضیه بیز به یافتن $P(A|B)$ کمک می‌کند. نام آن از Reverend Thomas Bayes (1701-1761) گرفته شده است؛ او نخستین کسی بود که معادله‌ای ارائه داد که به شواهد جدید اجازه می‌دهد باورها را به‌روز کنند.

**اثبات:**

تعریف احتمال شرطی را به‌خاطر بیاورید:

1.  $P(A|B) = \frac{P(A \cap B)}{P(B)}$، به‌شرط $P(B) > 0$.
2.  $P(B|A) = \frac{P(B \cap A)}{P(A)}$، به‌شرط $P(A) > 0$.

از آنجا که $P(A \cap B) = P(B \cap A)$، می‌توانیم این معادلات را بازآرایی کنیم:

1.  $P(A \cap B) = P(A|B) P(B)$
2.  $P(B \cap A) = P(B|A) P(A)$

برابر قرار دادن آن‌ها می‌دهد:

$P(A|B) P(B) = P(B|A) P(A)$

تقسیم بر $P(B)$ (با فرض $P(B) > 0$)، **قضیه بیز** را به‌دست می‌دهد:

$$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$$

**تفسیر:**

$A$ را واقعه یا فرضیه‌ای که به آن علاقه‌مندیم (مثلاً «بیمار بیماری خاصی دارد»، «سکه نامتقارن است») و $B$ را شواهد یا داده‌های جدید مشاهده‌شده (مثلاً «بیمار نتیجه مثبت گرفت»، «در ۱۰ پرتاب ۸ شیر دیدیم») در نظر بگیرید.

- $P(A)$: **احتمال پیشین** — باور ما درباره $A$ *قبل از* دیدن شواهد $B$.
- $P(B\mid A)$: **درست‌نمایی** — احتمال مشاهده شواهد $B$ *با فرض* درست بودن $A$.
- $P(B)$: **احتمال شواهد** — احتمال کلی مشاهده $B$، صرف‌نظر از درست یا نادرست بودن $A$.  
  با استفاده از قانون احتمال کل و پارتیشن $\{A, A^c\}$:
  
$$
P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c).
$$
  
- $P(A\mid B)$: **احتمال پسین** — باور به‌روزشده ما درباره $A$ *پس از* مشاهده شواهد $B$.
قضیه بیز به ما می‌گوید چگونه باور پیشین $P(A)$ را به باور پسین $P(A|B)$ بر اساس درست‌نمایی شواهد $P(B|A)$ و احتمال کلی شواهد $P(B)$ به‌روز کنیم.

### ۱.۱ شهود بصری: قضیه بیز (مدل مساحتی)

می‌توانید قضیه بیز را مستقیماً از تصویر زیر به‌صورت یک **نسبت مساحتی** بخوانید:

- **صورت** = مساحت سایه‌دار هم‌پوشانی $A \cap B$
- **مخرج** = کل مساحت سایه‌دار $B$

پس طبق تعریف احتمال شرطی:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

اکنون هم‌پوشانی را با قانون ضرب بازنویسی کنید:

$$
P(A\cap B)=P(B\mid A)\,P(A),
$$

که شکل فشرده «بیزی» را می‌دهد:

$$
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}.
$$

برای اتصال *مستقیم* این به مدل مساحتی، مخرج را با تقسیم \(B\) به بخش داخل \(A\) و بخش داخل \(A^c\) باز کنید:

$$
\begin{align*}
P(B) &= P(B\cap A)+P(B\cap A^c) \\
&= P(B\mid A)P(A)+P(B\mid A^c)P(A^c).
\end{align*}
$$

در معادله بیزی جایگذاری کنید:

$$
\begin{align*}
P(A\mid B)
&=\frac{P(B\mid A)P(A)}{P(B\mid A)P(A)+P(B\mid A^c)P(A^c)}.
\end{align*}
$$

```{code-cell} ipython3
:tags: [remove-input, remove-output]

from pathlib import Path

def save_bayes_area_svg(
    filename="bayes-area.svg",
    pA=0.35,
    pB_given_A=0.70,
    pB_given_Ac=0.20,
    font_scale=2.0,
):
    pAc = 1 - pA
    pB = pB_given_A * pA + pB_given_Ac * pAc
    pA_given_B = (pB_given_A * pA) / pB

    def fmt(x):
        return f"{x:.4f}".rstrip("0").rstrip(".")

    # --- sizing ---
    L = 70
    box_w, box_h = 1200, 340
    W = box_w + 2 * L

    outline = "#111827"
    strip_fill = "#f8fafc"
    shade_fill = "#ef4444"
    shade_stroke = "#b91c1c"
    accentA = "#2563eb"
    accentAc = "#64748b"

    title_sz = int(22 * font_scale)
    text_sz  = int(14 * font_scale)
    num_sz   = int(13 * font_scale)
    big_sz   = int(18 * font_scale)

    def gap(sz, mult=1.25):
        return int(sz * mult)

    # layout
    y = 70
    title_y = y; y += gap(title_sz, 1.10)
    sub1_y  = y; y += gap(text_sz, 1.15)

    y0 = y + int(24 * font_scale)
    x0 = L
    y1 = y0 + box_h

    bottom1_y = y1 + int(44 * font_scale)
    bottom2_y = bottom1_y + gap(num_sz, 1.35)
    bottom3_y = bottom2_y + gap(big_sz, 1.10)
    bottom4_y = bottom3_y + gap(text_sz, 1.20)
    H = bottom4_y + int(40 * font_scale)

    # widths (to scale)
    wA  = box_w * pA
    wAc = box_w * pAc

    # heights (to scale)
    hA  = box_h * pB_given_A
    hAc = box_h * pB_given_Ac
    yA_shade  = y1 - hA
    yAc_shade = y1 - hAc

    cxA  = x0 + wA / 2
    cxAc = x0 + wA + wAc / 2

    area_A_and_B  = pB_given_A  * pA
    area_Ac_and_B = pB_given_Ac * pAc

    def txt(x, y, s, size, weight=400, fill=outline, anchor="middle", opacity=1.0):
        return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
                f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
                f'font-size="{size}" font-weight="{weight}" fill="{fill}" opacity="{opacity}">{s}</text>')

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>')

    # header
    parts.append(txt(L, title_y, "Bayes’ theorem — area model", title_sz, 800, outline, "start"))
    parts.append(txt(L, sub1_y,
                     "A is the entire vertical strip (including shaded). B is the shaded overlay.",
                     text_sz, 400, outline, "start"))

    # outer box
    parts.append(f'<rect x="{x0}" y="{y0}" width="{box_w}" height="{box_h}" fill="none" stroke="{outline}" stroke-width="2"/>')

    # strips
    parts.append(f'<rect x="{x0}" y="{y0}" width="{wA}" height="{box_h}" fill="{strip_fill}" stroke="{outline}" stroke-width="1"/>')
    parts.append(f'<rect x="{x0+wA}" y="{y0}" width="{wAc}" height="{box_h}" fill="{strip_fill}" stroke="{outline}" stroke-width="1"/>')

    # watermarks (smaller + lighter)
    parts.append(txt(cxA,  y0 + box_h*0.56, "A",  int(52*font_scale), 800, outline, opacity=0.05))
    parts.append(txt(cxAc, y0 + box_h*0.56, "Aᶜ", int(52*font_scale), 800, outline, opacity=0.05))

    # shaded B overlay
    parts.append(f'<rect x="{x0}" y="{yA_shade}" width="{wA}" height="{hA}" fill="{shade_fill}" fill-opacity="0.16" stroke="{shade_stroke}" stroke-width="1"/>')
    parts.append(f'<rect x="{x0+wA}" y="{yAc_shade}" width="{wAc}" height="{hAc}" fill="{shade_fill}" fill-opacity="0.16" stroke="{shade_stroke}" stroke-width="1"/>')

    # strong outlines for full strips (clarifies inclusion)
    parts.append(f'<rect x="{x0}" y="{y0}" width="{wA}" height="{box_h}" fill="none" stroke="{accentA}" stroke-width="3"/>')
    parts.append(f'<rect x="{x0+wA}" y="{y0}" width="{wAc}" height="{box_h}" fill="none" stroke="{accentAc}" stroke-width="3"/>')

    # corner labels (instead of big bold top labels)
    pad = int(14 * font_scale)
    parts.append(txt(x0 + wA - pad, y0 + int(26*font_scale), "A", int(15*font_scale), 800, outline, "end"))
    parts.append(txt(x0 + wA - pad, y0 + int(45*font_scale), f"P(A) = {fmt(pA)}", num_sz, 400, outline, "end"))

    parts.append(txt(x0 + box_w - pad, y0 + int(26*font_scale), "Aᶜ", int(15*font_scale), 800, outline, "end"))
    parts.append(txt(x0 + box_w - pad, y0 + int(45*font_scale), f"P(Aᶜ) = {fmt(pAc)}", num_sz, 400, outline, "end"))

    y_anchor = y1 - int(22 * font_scale)   # move up/down by changing 90
    
    line1_y = y_anchor
    line2_y = y_anchor + int(18 * font_scale)
    
    parts.append(txt(cxA,  line1_y, "A ∩ B", num_sz, 900, shade_stroke))
    parts.append(txt(cxA,  line2_y, f"P(B|A) = {fmt(pB_given_A)}", num_sz, 500, shade_stroke))
    
    parts.append(txt(cxAc, line1_y, "Aᶜ ∩ B", num_sz, 900, shade_stroke))
    parts.append(txt(cxAc, line2_y, f"P(B|Aᶜ) = {fmt(pB_given_Ac)}", num_sz, 500, shade_stroke))


    # bottom explanations
    parts.append(txt(cxA,  bottom1_y, f"area(A∩B) = P(B|A)·P(A) = {fmt(area_A_and_B)}", num_sz, 400, outline))
    parts.append(txt(cxAc, bottom1_y, f"area(Aᶜ∩B) = P(B|Aᶜ)·P(Aᶜ) = {fmt(area_Ac_and_B)}", num_sz, 400, outline))

    parts.append(txt(x0 + box_w/2, bottom3_y,
                     f"P(A|B) = area(A∩B) / area(B) = {fmt(pA_given_B)}",
                     big_sz, 900, accentA))
    parts.append(txt(x0 + box_w/2, bottom4_y,
                     f"area(B) = area(A∩B) + area(Aᶜ∩B) = P(B) = {fmt(pB)}",
                     text_sz, 400, outline))

    parts.append("</svg>")
    Path(filename).write_text("\n".join(parts), encoding="utf-8")
    return filename

save_bayes_area_svg("bayes-area.svg", pA=0.35, pB_given_A=0.70, pB_given_Ac=0.20, font_scale=2.0)
```

```{figure} bayes-area.svg
---
width: 100%
figclass: full-width
---
مدل مساحتی: $P(A\mid B)$ «سهم ناحیه سایه‌دار $B$ که در نوار $A$ قرار دارد» است.
```

**نحوه خواندن نمودار**

* مستطیل بیرونی فضای نمونه $S$ (همه پیامدهای ممکن) است.
* دو نوار عمودی پارتیشن $S$ را می‌سازند: یا در $A$ هستید یا در $A^c$ (هرگز هر دو، و بدون شکاف).

  * عرض نوارها متناسب با احتمال‌شان است: width$(A)=P(A)$ و width$(A^c)=P(A^c)$.
* پوشش سایه‌دار واقعه شواهد $B$ را نشان می‌دهد.
* درون هر نوار، **ارتفاع سایه‌دار** احتمال شرطی $B$ را در آن حالت رمزگذاری می‌کند:

  * در نوار $A$ ارتفاع $P(B\mid A)$ است، پس مساحت سایه‌دار
    $$
    \text{area}(A\cap B)=P(B\mid A)\,P(A).
    $$
  * در نوار $A^c$ ارتفاع $P(B\mid A^c)$ است، پس مساحت سایه‌دار
    $$
    \text{area}(A^c\cap B)=P(B\mid A^c)\,P(A^c).
    $$
* جمع دو مساحت سایه‌دار، کل ناحیه سایه‌دار را می‌دهد:
  $$
  \text{area}(B)=\text{area}(A\cap B)+\text{area}(A^c\cap B)=P(B).
  $$
  این **قانون احتمال کل** با پارتیشن $\{A, A^c\}$ است.
* قضیه بیز **نسبت مساحتی** متناظر است:
  $$
  P(A\mid B)=\frac{\text{area}(A\cap B)}{\text{area}(B)}.
  $$
  آن را این‌گونه بخوانید: *«با فرض اینکه در ناحیه سایه‌دار $B$ هستیم، چه کسری از آن درون $A$ قرار دارد؟»*

+++

## ۲. به‌روزرسانی باورها: احتمال پیشین و پسین

+++

ایده اصلی تفکر بیزی به‌روزرسانی باورهاست. با یک باور پیشین شروع می‌کنیم، داده (شواهد) جمع می‌کنیم و باور را به پسین به‌روز می‌کنیم. این پسین می‌تواند پیشین بعدی برای شواهد بعدی شود.

**مثال:** فرض کنید وب‌سایتی دارید و یک بنر تبلیغاتی جدید را آزمایش می‌کنید.

* **فرضیه (A):** بنر تبلیغاتی جدید مؤثر است (مثلاً نرخ کلیک بیش از ۵٪).
* **پیشین ( $P(A)$ ):** بر اساس کمپین‌های قبلی، ممکن است ابتدا باور داشته باشید ۳۰٪ احتمال دارد بنر جدید مؤثر باشد. پس $P(A) = 0.30$.
* **شواهد (B):** سابقه مرور یک بازدیدکننده را مشاهده می‌کنید (مثلاً قبلاً صفحات محصول مرتبط را دیده).
* **درست‌نمایی ( $P(B|A) $):** احتمال اینکه بازدیدکننده این سابقه مرور را *با فرض* مؤثر بودن تبلیغ داشته باشد. شاید تبلیغات مؤثر هدف‌گیری بهتری دارند، پس این می‌تواند بالا باشد، مثلاً $P(B|A) = 0.70$.
* **درست‌نمایی ( $P(B|A^c)$ ):** احتمال اینکه بازدیدکننده این سابقه مرور را *با فرض* *غیرمؤثر* بودن تبلیغ داشته باشد. این می‌تواند پایین‌تر باشد، مثلاً $P(B|A^c) = 0.20$.
* **احتمال شواهد ( $P(B)$ ):** با استفاده از قانون احتمال کل:
  
    $$
    \begin{align*}
    P(B) &= P(B|A)P(A) + P(B|A^c)P(A^c) \\
    &= (0.70)(0.30) + (0.20)(1 - 0.30) \\
    &= 0.21 + (0.20)(0.70) \\
    &= 0.21 + 0.14 = 0.35
    \end{align*}
    $$
  
* **پسین ( $P(A|B)$ ):** اکنون قضیه بیز را به‌کار ببرید:
  
    $$
    \begin{align*}
    P(A|B) &= \frac{P(B|A) P(A)}{P(B)} \\
    &= \frac{(0.70)(0.30)}{0.35} \\
    &= \frac{0.21}{0.35} = 0.60
    \end{align*}
    $$

پس از مشاهده سابقه مرور بازدیدکننده، باور شما به مؤثر بودن تبلیغ از ۳۰٪ (پیشین) به ۶۰٪ (پسین) افزایش یافت.

+++

## ۳. کاربردها: مثال آزمون تشخیصی

+++

یکی از کلاسیک‌ترین و شهودی‌ترین کاربردهای قضیه بیز، تفسیر نتایج آزمون‌های تشخیصی پزشکی است.

**سناریو:**
* بیماری خاصی ۱٪ جمعیت را تحت تأثیر قرار می‌دهد. (شیوع)
* آزمونی برای بیماری ۹۵٪ دقت دارد:
    * اگر فرد *بیمار* باشد، آزمون ۹۵٪ مواقع درست تشخیص می‌دهد. (حساسیت)
    * اگر فرد *بیمار نباشد*، آزمون ۹۵٪ مواقع درست تشخیص می‌دهد. (ویژگی)

```{admonition} حساسیت و ویژگی 
:class: dropdown
نگاه به ریشه و تعریف واژه‌های «sensitivity» و «specificity» قطعاً می‌تواند معانی آن‌ها را در این زمینه تقویت کند.

1. **حساسیت (Sensitivity):**  
   * **ریشه:** از واژه لاتین sentire، به معنای «احساس کردن» یا «درک کردن».  
   * **معنی عمومی:** کیفیت یا وضعیت حساس بودن؛ پاسخ‌دهی به محرک‌ها.  
   * **ارتباط با آزمون:** آزمون را چنین تصور کنید که باید حضور بیماری را «احساس» یا «درک» کند. آزمون **حساس** توانایی قوی *کشف* بیماری را وقتی واقعاً وجود دارد دارد. به محرک بیماری پاسخ می‌دهد. اگر بیماری باشد، آزمون حساس احتمالاً واکنش نشان می‌دهد (نتیجه مثبت). این با معنی فنی آن — شناسایی درست مثبت‌های واقعی — هم‌خوان است.  
2. **ویژگی (Specificity):**  
   * **ریشه:** از واژه لاتین specificus، مشتق از species (به معنای «گونه» یا «نوع») و facere (به معنای «ساختن»). اساساً «ساختن از یک نوع خاص».  
   * **معنی عمومی:** کیفیت خاص بودن؛ محدود شدن به مورد، شرط یا اثر خاص؛ دقیق یا exact بودن.  
   * **ارتباط با آزمون:** آزمون را برای یک هدف *خاص* — بیماری — طراحی‌شده تصور کنید. آزمون **ویژه** دقیق است و فقط به آن هدف *خاص* واکنش نشان می‌دهد. به چیزهای دیگر (مثل نبود بیماری یا شرایط دیگر) واکنش *نمی‌دهد*. افرادی که بیماری هدف *خاص* را *ندارند* را درست شناسایی می‌کند (نتیجه منفی). این با معنی فنی آن — شناسایی درست منفی‌های واقعی — هم‌خوان است.

**چگونه به درک کمک می‌کند:**

* **حساسیت:** به توانایی آزمون برای **احساس** یا **کشف** بیماری در صورت حضور آن مربوط است. حساسیت بالا یعنی کشف خوب.  
* **ویژگی:** به **خاص** یا **دقیق** بودن آزمون فقط برای بیماری مورد نظر مربوط است. ویژگی بالا یعنی آزمون فقط *شرایط خاص* مورد جستجو را علامت می‌زند و از علامت‌گذاری افراد سالم پرهیز می‌کند.

پس ریشه‌ها به قاب‌بندی مفاهیم کمک می‌کنند: حساسیت درباره *قدرت کشف* است، در حالی که ویژگی درباره *دقت* و *صحت هدف* است.
```

**سؤال:** اگر فردی به‌طور تصادفی نتیجه مثبت بگیرد، احتمال واقعی داشتن بیماری چقدر است؟

**واقعه‌ها را تعریف کنیم:**
* $D$: فرد بیمار است.
* $D^c$: فرد بیمار نیست.
* $Pos$: فرد نتیجه مثبت می‌گیرد.
* $Neg$: فرد نتیجه منفی می‌گیرد.

**آنچه می‌دانیم:**
* $P(D) = 0.01$ (احتمال پیشین داشتن بیماری — شیوع)
* $P(D^c) = 1 - P(D) = 0.99$
* $P(Pos|D) = 0.95$ (احتمال نتیجه مثبت *با فرض* داشتن بیماری — حساسیت)
* $P(Neg|D) = 1 - P(Pos|D) = 0.05$ (نرخ منفی کاذب)
* $P(Neg|D^c) = 0.95$ (احتمال نتیجه منفی *با فرض* نداشتن بیماری — ویژگی)
* $P(Pos|D^c) = 1 - P(Neg|D^c) = 0.05$ (نرخ مثبت کاذب)

**آنچه می‌خواهیم بیابیم:** $P(D|Pos)$ (احتمال داشتن بیماری *با فرض* نتیجه مثبت).

**قضیه بیز را به‌کار ببرید:**

$P(D|Pos) = \frac{P(Pos|D) P(D)}{P(Pos)}$

باید $P(Pos)$ را بیابیم. از قانون احتمال کل استفاده کنید:

$$
\begin{align*}
P(\text{Pos}) &= P(\text{Pos}|D)P(D) + P(\text{Pos}|D^c)P(D^c) \\
&= (0.95)(0.01) + (0.05)(0.99) \\
&= 0.0095 + 0.0495 \\
&= 0.0590
\end{align*}
$$

اکنون در قضیه بیز جایگذاری کنید:

$$
\begin{align*}
P(D|Pos) &= \frac{(0.95)(0.01)}{0.0590} \\
&= \frac{0.0095}{0.0590} \\
&\approx 0.161
\end{align*}
$$

**تفسیر:** حتی با نتیجه مثبت از یک آزمون ۹۵٪ دقیق، احتمال واقعی داشتن بیماری فقط حدود ۱۶.۱٪ است! این ضدشهود به نظر می‌رسد اما تأثیر قوی احتمال پیشین پایین (شیوع) بیماری را برجسته می‌کند. بیشتر نتایج مثبت از گروه بزرگ افراد سالم با مثبت کاذب می‌آید، نه از گروه کوچک بیماران با مثبت واقعی.

+++

## ۴. استقلال واقعه‌ها

+++

دو واقعه A و B **مستقل** نامیده می‌شوند اگر وقوع (یا عدم وقوع) یکی بر احتمال وقوع دیگری اثر نگذارد.

یعنی دو واقعه A و B **مستقل**ند اگر دانستن اینکه یکی رخ داده درباره وقوع دیگری چیزی به ما نگوید. احتمال‌هایشان به هم وابسته نیست.

### ۴.۱. تعریف رسمی

تعریف ریاضی رسمی استقلال بین دو واقعه این است که A و B مستقل‌اند اگر و فقط اگر:
$P(A \cap B) = P(A) P(B)$

```{admonition} توضیح
:class: dropdown

واقعه‌های **A** و **B** **مستقل**‌اند اگر و فقط اگر احتمال وقوع *هر دو* برابر حاصل‌ضرب احتمال‌های فردی‌شان باشد.

به‌صورت ریاضی:
$P(A \cap B) = P(A) \times P(B)$

* $P(A \cap B)$ یعنی «احتمال وقوع هم‌زمان A و B» (اشتراک A و B).
* $P(A)$ احتمال وقوع واقعه A است.
* $P(B)$ احتمال وقوع واقعه B است.

**چرا این فرمول استقلال را می‌گیرد؟**
این‌گونه فکر کنید: اگر واقعه‌ها واقعاً بر یکدیگر اثر نگذارند، شانس وقوع *هر دو* باید فقط ضرب ساده شانس‌های فردی باشد. اگر تأثیر (وابستگی) وجود داشت، این ضرب احتمال ترکیبی را درست منعکس نمی‌کرد.
```

```{admonition} مثال: پرتاب دو بار سکه منصفانه 🪙
:class: dropdown

پرتاب دو بار یک سکه منصفانه را در نظر بگیرید.

* **واقعه A**: شیر (H) در **پرتاب اول**.
* **واقعه B**: شیر (H) در **پرتاب دوم**.

می‌خواهیم بدانیم آیا این دو واقعه مستقل‌اند.

1.  **محاسبه $P(A)$**:
    احتمال شیر در یک پرتاب سکه منصفانه $\frac{1}{2}$ است.
    پس $P(A) = \frac{1}{2}$.

2.  **محاسبه $P(B)$**:
    پیامد پرتاب دوم تحت تأثیر پرتاب اول نیست. سکه حافظه ندارد. پس احتمال شیر در پرتاب دوم هم $\frac{1}{2}$ است.
    پس $P(B) = \frac{1}{2}$.

3.  **محاسبه $P(A \cap B)$**:
    این احتمال شیر در پرتاب اول **و** شیر در پرتاب دوم (HH) است.
    پیامدهای ممکن هنگام پرتاب دو بار سکه: HH, HT, TH, TT. ۴ پیامد به‌طور یکسان محتمل وجود دارد.
    فقط یکی HH است.
    پس $P(A \cap B) = \frac{1}{4}$.

4.  **بررسی فرمول استقلال**:
    اکنون بررسی می‌کنیم آیا $P(A \cap B) = P(A) \times P(B)$.
    * $P(A) \times P(B) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
    * قبلاً یافتیم $P(A \cap B) = \frac{1}{4}$.

5.  **نتیجه**:
    چون $P(A \cap B) = P(A) \times P(B)$ (زیرا $\frac{1}{4} = \frac{1}{4}$)، واقعه‌های A (شیر در پرتاب اول) و B (شیر در پرتاب دوم) **مستقل**‌اند.

این شهودی است: نتیجه پرتاب اول سکه احتمال شیر یا خط در پرتاب دوم را تغییر نمی‌دهد.
```

### ۴.۲. تعریف جایگزین (با استفاده از احتمال شرطی)

اگر $P(B) > 0$، A و B مستقل‌اند اگر و فقط اگر:

$P(A|B) = P(A)$

به‌طور مشابه، اگر $P(A) > 0$، استقلال یعنی:

$P(B|A) = P(B)$

این تعریف با شهود هم‌خوان است: دانستن وقوع B احتمال A را تغییر نمی‌دهد.

```{admonition} مثال: پرتاب تاس منصفانه
:class: dropdown

| تعریف واقعه                                  | محاسبه احتمال |
| :------------------------------------------------ | :---------------------- |
| **A**: «عدد زوج» = {2, 4, 6}       | $P(A) = 3/6 = 1/2$      |
| **B**: «عدد > 4» = {5, 6}            | $P(B) = 2/6 = 1/3$      |
| **A ∩ B**: «عدد زوج > 4» = {6}                | $P(A \cap B) = 1/6$     |

استقلال را بررسی کنیم:

آیا $P(A \cap B) = P(A) P(B)$؟

$$
\begin{align*}
P(A \cap B) &\stackrel{?}{=} P(A) P(B) \\
\frac{1}{6} &\stackrel{?}{=} \left(\frac{1}{2}\right) \times \left(\frac{1}{3}\right) \\
\frac{1}{6} &= \frac{1}{6} \quad \checkmark
\end{align*}
$$

بله، واقعه‌های A و B مستقل‌اند. 

دانستن اینکه پرتاب بزرگ‌تر از ۴ است احتمال زوج بودن را تغییر نمی‌دهد — هنوز 1/2 است:

$$
\begin{align*}
P(A|B) &= \frac{P(A \cap B)}{P(B)} \\
&= \frac{1/6}{1/3} \\
&= \frac{1}{6} \times 3 \\
&= \frac{3}{6} \\
&= \frac{1}{2} \\
&= P(A)
\end{align*}
$$

یعنی $P(A|B) = P(A)$
```

```{admonition} مثال: کشیدن کارت (بدون بازگرداندن)
:class: dropdown

A را واقعه «کارت اول کشیده‌شده آس باشد» در نظر بگیرید. $P(A) = 4/52$.
B را واقعه «کارت دوم کشیده‌شده آس باشد» در نظر بگیرید.

آیا A و B مستقل‌اند؟ شهوداً نه. اگر کارت اول آس بود، احتمال آس بودن کارت دوم تغییر می‌کند.

$P(B)$ را محاسبه کنیم. با استفاده از قانون احتمال کل:

$$
\begin{align*}
P(B) &= P(B|A)P(A) + P(B|A^c)P(A^c) \\
&= \left( \frac{3}{51} \right) \left( \frac{4}{52} \right)
   + \left( \frac{4}{51} \right) \left( \frac{48}{52} \right) \\
&= \frac{3 \times 4}{51 \times 52} + \frac{4 \times 48}{51 \times 52} \\
&= \frac{12}{2652} + \frac{192}{2652} \\
&= \frac{12 + 192}{2652} \\
&= \frac{204}{2652} = \frac{4}{52} = \frac{1}{13}
\end{align*}
$$

پس $P(B) = 1/13$.

اکنون اشتراک را محاسبه کنیم: $P(A \cap B) = P(\text{first is Ace AND second is Ace})$

$$
\begin{align*}
P(A \cap B) &= P(B|A)P(A) \\
&= \left( \frac{3}{51} \right) \left( \frac{4}{52} \right) \\
&= \frac{3 \times 4}{51 \times 52} \\
&= \frac{12}{2652} \\
&= \frac{1}{221}
\end{align*}
$$

استقلال را بررسی کنیم: 

آیا $P(A \cap B) = P(A)P(B)$؟

$$
\begin{align*}
\frac{1}{221} &\stackrel{?}{=} \left( \frac{4}{52} \right)
   \times \left( \frac{4}{52} \right) \\
&= \left( \frac{1}{13} \right) \times \left( \frac{1}{13} \right) \\
&= \frac{1}{169}
\end{align*}
$$

طبق انتظار، واقعه‌ها **مستقل نیستند**.
```

**نکته مهم:** استقلال را با ناسازگاری اشتباه نگیرید.
* واقعه‌های **ناسازگار** نمی‌توانند هم‌زمان رخ دهند ($A \cap B = \emptyset$، پس $P(A \cap B) = 0$).
* واقعه‌های **مستقل** *می‌توانند* هم‌زمان رخ دهند، اما یکی بر احتمال دیگری اثر نمی‌گذارد.
اگر دو واقعه A و B احتمال غیرصفر داشته باشند، *نمی‌توانند* هم‌زمان ناسازگار و مستقل باشند. اگر ناسازگار بودند، $P(A \cap B) = 0$. اگر مستقل بودند، $P(A \cap B) = P(A)P(B) > 0$. این تناقض است.

+++

## ۵. استقلال شرطی

```{code-cell} ipython3
:tags: [remove-input, remove-output]

from pathlib import Path

def save_common_cause_svg():
    """Create two diagrams showing common cause pattern."""

    # Colors
    node_fill = "#1e293b"
    node_stroke = "#0f172a"
    arrow_color = "#3b82f6"
    arrow_blocked = "#94a3b8"
    text_color = "#ffffff"
    bg_color = "#ffffff"
    label_color = "#111827"
    highlight_color = "#ef4444"

    # Dimensions
    node_r = 60
    font_size = 18
    label_font = 14
    arrow_width = 3

    def make_arrow(x1, y1, x2, y2, color, dashed=False):
        """Create an arrow path."""
        # Shorten to stop at node edge
        dx, dy = x2 - x1, y2 - y1
        length = (dx**2 + dy**2)**0.5
        if length == 0:
            return ""
        ux, uy = dx/length, dy/length
        x1_adj = x1 + ux * node_r
        y1_adj = y1 + uy * node_r
        x2_adj = x2 - ux * (node_r + 15)
        y2_adj = y2 - uy * (node_r + 15)

        style = f'stroke-dasharray="8,4"' if dashed else ''

        return f'''
        <defs>
            <marker id="arrowhead-{color.replace("#","")}" markerWidth="10" markerHeight="10"
                    refX="9" refY="3" orient="auto">
                <polygon points="0 0, 10 3, 0 6" fill="{color}" />
            </marker>
        </defs>
        <line x1="{x1_adj}" y1="{y1_adj}" x2="{x2_adj}" y2="{y2_adj}"
              stroke="{color}" stroke-width="{arrow_width}" {style}
              marker-end="url(#arrowhead-{color.replace("#","")})" />
        '''

    def make_node(x, y, label, sublabel=""):
        """Create a circular node."""
        sub_part = f'<text x="{x}" y="{y+22}" text-anchor="middle" font-size="{label_font}" fill="{text_color}" opacity="0.8">{sublabel}</text>' if sublabel else ''
        return f'''
        <circle cx="{x}" cy="{y}" r="{node_r}" fill="{node_fill}" stroke="{node_stroke}" stroke-width="2"/>
        <text x="{x}" y="{y+6}" text-anchor="middle" font-size="{font_size}" font-weight="bold" fill="{text_color}">{label}</text>
        {sub_part}
        '''

    def make_block_symbol(x, y):
        """Create a blocking symbol (circled X)."""
        return f'''
        <circle cx="{x}" cy="{y}" r="25" fill="{highlight_color}" stroke="#b91c1c" stroke-width="2"/>
        <text x="{x}" y="{y+8}" text-anchor="middle" font-size="28" font-weight="bold" fill="#ffffff">⊗</text>
        '''

    # Image 1: Without context (apparent dependence)
    w1, h1 = 800, 300
    cx1, cy1 = w1 // 2, h1 // 2

    svg1_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w1}" height="{h1}" viewBox="0 0 {w1} {h1}">']
    svg1_parts.append(f'<rect width="{w1}" height="{h1}" fill="{bg_color}"/>')

    # Nodes
    x_h1, x_h2 = 200, 600
    svg1_parts.append(make_node(x_h1, cy1, "H₁", "Umbrellas"))
    svg1_parts.append(make_node(x_h2, cy1, "H₂", "Flashlights"))

    # Arrow from H1 to H2
    svg1_parts.append(make_arrow(x_h1, cy1, x_h2, cy1, arrow_color))

    # Label
    svg1_parts.append(f'<text x="{cx1}" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="{label_color}">Without Context: Information Appears to Flow</text>')
    svg1_parts.append(f'<text x="{cx1}" y="260" text-anchor="middle" font-size="14" fill="{label_color}">P(H₂ | H₁) ≠ P(H₂) — The events appear dependent</text>')

    svg1_parts.append('</svg>')

    # Image 2: With context (conditional independence)
    w2, h2 = 800, 400

    svg2_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w2}" height="{h2}" viewBox="0 0 {w2} {h2}">']
    svg2_parts.append(f'<rect width="{w2}" height="{h2}" fill="{bg_color}"/>')

    # Nodes - arranged in V shape
    cx2 = w2 // 2
    y_top = 130
    y_bottom = 310
    x_left = 200
    x_right = 600

    svg2_parts.append(make_node(cx2, y_top, "C", "Storm Warning"))
    svg2_parts.append(make_node(x_left, y_bottom, "H₁", "Umbrellas"))
    svg2_parts.append(make_node(x_right, y_bottom, "H₂", "Flashlights"))

    # Arrows from C to both H1 and H2
    svg2_parts.append(make_arrow(cx2, y_top, x_left, y_bottom, arrow_color))
    svg2_parts.append(make_arrow(cx2, y_top, x_right, y_bottom, arrow_color))

    # Blocked arrow between H1 and H2 (dashed and grayed)
    svg2_parts.append(make_arrow(x_left, y_bottom, x_right, y_bottom, arrow_blocked, dashed=True))

    # Block symbol in the middle
    svg2_parts.append(make_block_symbol(cx2, y_bottom))

    # Labels
    svg2_parts.append(f'<text x="{cx2}" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="{label_color}">With Context: Common Cause Blocks Information Flow</text>')
    svg2_parts.append(f'<text x="{cx2}" y="394" text-anchor="middle" font-size="14" fill="{label_color}">P(H₂ | H₁, C) = P(H₂ | C) — Conditionally independent given C</text>')

    svg2_parts.append('</svg>')

    # Save both files
    Path("common-cause-without-context.svg").write_text("\n".join(svg1_parts), encoding="utf-8")
    Path("common-cause-with-context.svg").write_text("\n".join(svg2_parts), encoding="utf-8")

    return "common-cause-without-context.svg", "common-cause-with-context.svg"

save_common_cause_svg()
```

```{admonition} چرا این بخش مهم است (و چرا پیچیده است)
:class: tip

استقلال شرطی یکی از ظریف‌ترین اما مهم‌ترین مفاهیم در احتمال است. بسیاری از پدیده‌های واقعی که در ابتدا پارادوکس به نظر می‌رسند را توضیح می‌دهد:

* چرا یک درمان ممکن است در کل مؤثر به نظر برسد اما در گروه‌های خاص بیمار بی‌اثر (یا حتی مضر) باشد
* چرا دو متغیر در داده‌ها همبسته به نظر برسند اما پس از لحاظ فاکتور پنهان واقعاً بی‌ارتباط باشند
* چگونه مخلوط کردن داده از منابع مختلف می‌تواند روابط spurious ایجاد کند

**بینش کلیدی:** دو واقعه می‌توانند وقتی زمینه را می‌دانید *مستقل* باشند، اما وقتی زمینه پنهان است *وابسته*. این ضدشهود است چون به استقلال به‌عنوان ویژگی مطلق عادت داریم، نه چیزی که به آنچه دیگر می‌دانیم بستگی دارد.

**عجله نکنید.** مفاهیم ظریف‌اند و احتمالاً باید این بخش را چند بار بخوانید. این کاملاً طبیعی است — استقلال شرطی زمان می‌برد تا درونی شود، اما پاداش آن برای درک آمار، علّیت و تحلیل داده بسیار بزرگ است.
```

گاهی دو واقعه در کل (در همان آزمایش) مرتبط به نظر می‌رسند، اما با شرط گذاشتن روی زمینه مرتبط **$C$** مستقل می‌شوند.

**$C$** را یک *کلید زمینه* در نظر بگیرید: اگر زمینه را ثابت کنید، $A$ و $B$ دیگر به یکدیگر اطلاعات نمی‌دهند.

---

:::{admonition} مثال: فروشگاه مواد غذایی (علّت مشترک)
:class: tip

این مثال نشان می‌دهد «شوک‌های» بیرونی چگونه رفتار را تحت تأثیر قرار می‌دهند و ارتباط ظاهری بین واقعه‌ها می‌سازند.

**سناریو:**
- متغیر $H_1$: فروش چتر افزایش می‌یابد.
- متغیر $H_2$: فروش چراغ‌قوه افزایش می‌یابد.
- شرط $C$: هشدار طوفان شدید صادر می‌شود.

**چرا درست است:**

متوجه می‌شوید هر بار مردم چتر می‌خرند، چراغ‌قوه هم می‌خرند. دو واقعه مرتبط به نظر می‌رسند. اما خرید چتر *علّت* خرید چراغ‌قوه نیست. هر دو پاسخ مستقل به هشدار طوفان ($C$) هستند.

وقتی می‌دانید طوفان می‌آید، دیدن کسی که چتر برمی‌دارد درباره موجودی چراغ‌قوه چیز جدیدی نمی‌گوید — طوفان قبلاً همه چیز لازم را گفته بود.

**به‌صورت ریاضی:**
$$
P(H_2 \mid H_1, C) = P(H_2 \mid C)
$$

```{admonition} نکته نمادگذاری
:class: note
نمادگذاری $P(H_2 \mid H_1, C)$ یعنی «احتمال $H_2$ با فرض $H_1$ و $C$» — ویرگول مخفف «و» است. این نمادگذاری را در بخش ۵.۱ با جزئیات بیشتر توضیح می‌دهیم.
```

این معادله می‌گوید: «با فرض اینکه هشدار طوفان صادر شده ($C$)، دانستن افزایش فروش چتر ($H_1$) اطلاعات اضافی درباره افزایش فروش چراغ‌قوه ($H_2$) نمی‌دهد.»

```{figure} common-cause-without-context.svg
---
width: 80%
figclass: full-width
---
**بدون دانستن زمینه:** وقتی از هشدار طوفان خبر نداریم، فروش چتر ($H_1$) و فروش چراغ‌قوه ($H_2$) وابسته به نظر می‌رسند. مشاهده یکی درباره دیگری اطلاعات می‌دهد.
```

```{figure} common-cause-with-context.svg
---
width: 80%
figclass: full-width
---
**با آشکار شدن زمینه:** وقتی از هشدار طوفان ($C$) مطلع می‌شویم، ارتباط بین $H_1$ و $H_2$ مسدود می‌شود. هشدار طوفان علّت مشترک هر دو واقعه است. با فرض $C$، دانستن فروش چتر درباره فروش چراغ‌قوه چیز جدیدی نمی‌گوید — آن‌ها مستقل شرطی‌اند.
```

**بینش کلیدی:** این الگو — جایی که علّت مشترک وابستگی ظاهری بین اثرها می‌سازد — یکی از مهم‌ترین مفاهیم در استقلال شرطی است. این ایده را در بخش‌های بعد رسمی می‌کنیم.

:::

+++

### ۵.۱. نمادگذاری و تعریف

قبل از بررسی استقلال شرطی، باید بدانیم چگونه با احتمال‌های شرطی شامل چند شرط کار کنیم.

#### شرطی‌سازی روی چند واقعه

وقتی $P(A \mid B, C)$ می‌نویسیم، احتمال واقعه $A$ را با فرض وقوع *هر دو* واقعه $B$ و $C$ می‌خواهیم. این معادل شرطی‌سازی روی اشتراک است:

$$
P(A \mid B, C) = P(A \mid B \cap C)
$$

ویرگول در بخش شرط، مخفف راحت اشتراک است. هر دو نمادگذاری در احتمال و آمار به‌طور متناوب استفاده می‌شوند.

```{admonition} خواندن نمادگذاری
:class: note

$P(A \mid B, C)$ را «احتمال $A$ با فرض $B$ و $C$» می‌خوانیم.

باور به‌روزشده ما درباره $A$ را نشان می‌دهد وقتی می‌دانیم $B$ و $C$ هر دو رخ داده‌اند.
```

```{admonition} مثال: پرتاب سکه
:class: dropdown

پرتاب سکه دو بار پس از انتخاب اینکه از کدام سکه استفاده شود:
- $H_1$ = «پرتاب اول شیر باشد»
- $H_2$ = «پرتاب دوم شیر باشد»
- $C$ = «سکه منصفانه را انتخاب کرده‌ایم»

آنگاه $P(H_2 \mid H_1, C)$ یعنی: «احتمال شیر بودن پرتاب دوم، با فرض اینکه پرتاب اول شیر بوده **و** سکه منصفانه انتخاب شده؟»

برای سکه منصفانه، دانستن پرتاب اول در پیش‌بینی پرتاب دوم کمکی نمی‌کند، پس:
$$
P(H_2 \mid H_1, C) = P(H_2 \mid C) = 0.5
$$

این معادله می‌گوید: «با فرض داشتن سکه منصفانه، یادگیری درباره پرتاب اول اطلاعات اضافی درباره پرتاب دوم نمی‌دهد.» این نمونه‌ای از استقلال شرطی است که در ادامه با جزئیات بررسی می‌کنیم.
```

```{admonition} مهم: ترتیب مهم نیست
:class: tip

ترتیب واقعه‌ها پس از خط شرط مهم نیست:
$$
P(A \mid B, C) = P(A \mid C, B) = P(A \mid B \cap C)
$$
```

#### تعریف رسمی استقلال شرطی

قبل از تعریف رسمی، به‌خاطر بیاورید استقلال را در بخش ۴ دیدیم. **استقلال شرطی** مفهومی مرتبط اما متمایز است: استقلالی که *درون* یک زمینه خاص برقرار است، حتی اگر واقعه‌ها در کل — وقتی زمینه‌ها مخلوط می‌شوند — وابسته باشند.

از نماد **$\perp$** («مستقل از») استفاده می‌کنیم. همچنین از **$\Longleftrightarrow$** (اگر و فقط اگر) برای نشان دادن معادل بودن دو گزاره استفاده می‌کنیم — هر کدام دیگری را imply می‌کند.

* **استقلال بدون شرط**
  $$
  A \perp B
  \quad\Longleftrightarrow\quad
  P(A\cap B)=P(A)\,P(B).
  $$

* **استقلال شرطی**
  $$
  A \perp B \mid C
  \quad\Longleftrightarrow\quad
  P(A\cap B \mid C)=P(A\mid C)\,P(B\mid C),
  \qquad P(C)>0.
  $$

**نحوه خواندن:** «در دنیایی که $C$ درست بودن آن معلوم است، $A$ و $B$ مانند واقعه‌های مستقل رفتار می‌کنند.»

+++

#### نمایش بصری: استقلال شرطی

نمودار ون زیر استقلال شرطی را نشان می‌دهد. وقتی بر وقوع واقعه $C$ شرط می‌گذاریم، توجه را به ناحیه $C$ محدود می‌کنیم. درون آن ناحیه، $A$ و $B$ مستقل‌اند؛ یعنی هم‌پوشانی $A$ و $B$ درون $C$ برابر آنچه از حاصل‌ضرب احتمال‌های شرطی‌شان انتظار داریم است.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# Create figure with three panels side by side
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

# Function to create a Venn diagram with specific highlighting
def create_venn_panel(ax, highlight_mode, title_text):
    """
    highlight_mode: 'A_and_C', 'B_and_C', or 'A_and_B_and_C'
    """
    # Create three-set Venn diagram
    v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('', '', ''), ax=ax)

    # Default: all regions in C are light, regions outside C are very light
    if v.get_patch_by_id('100'):  # A only
        v.get_patch_by_id('100').set_color('#f5f5f5')
        v.get_patch_by_id('100').set_alpha(0.5)
    if v.get_patch_by_id('010'):  # B only
        v.get_patch_by_id('010').set_color('#f5f5f5')
        v.get_patch_by_id('010').set_alpha(0.5)
    if v.get_patch_by_id('110'):  # A ∩ B only (not in C)
        v.get_patch_by_id('110').set_color('#e0e0e0')
        v.get_patch_by_id('110').set_alpha(0.4)

    # Color C regions based on highlight mode
    if highlight_mode == 'A_and_C':
        # Highlight all A ∩ C regions
        if v.get_patch_by_id('001'):  # C only
            v.get_patch_by_id('001').set_color('#ffe0b2')
            v.get_patch_by_id('001').set_alpha(0.5)
        if v.get_patch_by_id('011'):  # B ∩ C (not in A)
            v.get_patch_by_id('011').set_color('#ffe0b2')
            v.get_patch_by_id('011').set_alpha(0.5)
        if v.get_patch_by_id('101'):  # A ∩ C (not in B) - HIGHLIGHT
            v.get_patch_by_id('101').set_color('#ff9800')
            v.get_patch_by_id('101').set_alpha(0.85)
        if v.get_patch_by_id('111'):  # A ∩ B ∩ C - HIGHLIGHT
            v.get_patch_by_id('111').set_color('#ff9800')
            v.get_patch_by_id('111').set_alpha(0.85)
    elif highlight_mode == 'B_and_C':
        # Highlight all B ∩ C regions
        if v.get_patch_by_id('001'):  # C only
            v.get_patch_by_id('001').set_color('#ffe0b2')
            v.get_patch_by_id('001').set_alpha(0.5)
        if v.get_patch_by_id('101'):  # A ∩ C (not in B)
            v.get_patch_by_id('101').set_color('#ffe0b2')
            v.get_patch_by_id('101').set_alpha(0.5)
        if v.get_patch_by_id('011'):  # B ∩ C (not in A) - HIGHLIGHT
            v.get_patch_by_id('011').set_color('#ff9800')
            v.get_patch_by_id('011').set_alpha(0.85)
        if v.get_patch_by_id('111'):  # A ∩ B ∩ C - HIGHLIGHT
            v.get_patch_by_id('111').set_color('#ff9800')
            v.get_patch_by_id('111').set_alpha(0.85)
    else:  # 'A_and_B_and_C'
        # Highlight only the center region
        if v.get_patch_by_id('001'):  # C only
            v.get_patch_by_id('001').set_color('#ffe0b2')
            v.get_patch_by_id('001').set_alpha(0.5)
        if v.get_patch_by_id('101'):  # A ∩ C (not in B)
            v.get_patch_by_id('101').set_color('#ffe0b2')
            v.get_patch_by_id('101').set_alpha(0.5)
        if v.get_patch_by_id('011'):  # B ∩ C (not in A)
            v.get_patch_by_id('011').set_color('#ffe0b2')
            v.get_patch_by_id('011').set_alpha(0.5)
        if v.get_patch_by_id('111'):  # A ∩ B ∩ C - HIGHLIGHT
            v.get_patch_by_id('111').set_color('#ff6d00')
            v.get_patch_by_id('111').set_alpha(0.9)

    # Draw circles
    venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='solid', linewidth=2, ax=ax)

    # Add set labels
    label_A = v.get_label_by_id('A')
    if label_A:
        label_A.set_text('A')
        label_A.set_fontsize(16)

    label_B = v.get_label_by_id('B')
    if label_B:
        label_B.set_text('B')
        label_B.set_fontsize(16)

    label_C = v.get_label_by_id('C')
    if label_C:
        label_C.set_text('C')
        label_C.set_fontsize(16)

    # Add title below the diagram
    ax.text(0.5, -0.15, title_text,
            transform=ax.transAxes,
            fontsize=13, ha='center', va='top',
            fontweight='bold')

    return v

# Panel 1: P(A|C)
create_venn_panel(ax1, 'A_and_C', 'P(A | C)\nProportion of C that is in A')

# Panel 2: P(B|C)
create_venn_panel(ax2, 'B_and_C', 'P(B | C)\nProportion of C that is in B')

# Panel 3: P(A∩B|C)
create_venn_panel(ax3, 'A_and_B_and_C', 'P(A ∩ B | C)\nProportion of C in both A and B')

# Add overall title
fig.suptitle('Conditional Independence Formula Components: P(A ∩ B | C) = P(A | C) × P(B | C)',
             fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
fig.savefig("venn-conditional-independence.svg", format="svg", bbox_inches="tight", pad_inches=0.3)
```

```{figure} venn-conditional-independence.svg
---
width: 100%
figclass: full-width
---
مصورسازی سه‌پanelی اجزای فرمول استقلال شرطی. پanel چپ: $P(A \mid C)$ همه نواحی در $A$ و $C$ را برجسته می‌کند. پanel میانی: $P(B \mid C)$ همه نواحی در $B$ و $C$ را برجسته می‌کند. پanel راست: $P(A \cap B \mid C)$ فقط ناحیه در هر سه مجموعه را برجسته می‌کند. فرمول می‌گوید این نسبت‌ها برقرارند: $P(A \cap B \mid C) = P(A \mid C) \times P(B \mid C)$.
```

**مشاهده کلیدی از سه پanel:**

سه پanel بالا نشان می‌دهند هر جمله در فرمول استقلال شرطی با کدام نواحی درون $C$ متناظر است:

**تجزیه فرمول:** $P(A \cap B \mid C) = P(A \mid C) \times P(B \mid C)$

* **پanel چپ — $P(A \mid C)$:** نسبت ناحیه $C$ که در $A$ قرار دارد را نشان می‌دهد
  * نواحی نارنجی تیره همه بخش‌های $A$ که با $C$ هم‌پوشانی دارند

* **پanel میانی — $P(B \mid C)$:** نسبت ناحیه $C$ که در $B$ قرار دارد را نشان می‌دهد
  * نواحی نارنجی تیره همه بخش‌های $B$ که با $C$ هم‌پوشانی دارند

* **پanel راست — $P(A \cap B \mid C)$:** نسبت ناحیه $C$ که در *هر دو* $A$ و $B$ قرار دارد را نشان می‌دهد
  * ناحیه نارنجی تیره اشتراک مرکزی هر سه مجموعه است

:::{admonition} مهم: نسبت‌ها را ضرب می‌کنیم، نه مساحت‌ها را جمع!
:class: warning

توجه کنید ناحیه مرکزی $(A \cap B \cap C)$ در پanel چپ و میانی برجسته شده. ممکن است «شمارش دوباره» به نظر برسد، اما این مساحت‌ها را *جمع* نمی‌کنیم — **نسبت‌ها را ضرب** می‌کنیم.

وقتی $P(A \mid C) \times P(B \mid C)$ را محاسبه می‌کنیم، دو کسر را ضرب می‌کنیم: (مساحت نارنجی پanel چپ ÷ کل مساحت $C$) × (مساحت نارنجی پanel میانی ÷ کل مساحت $C$). این ضرب نسبت نشان‌داده‌شده در پanel راست را می‌دهد.

تحت استقلال شرطی، این ضرب نسبت‌ها دقیقاً برابر نسبت $C$ است که در هر دو $A$ و $B$ قرار دارد. اینکه ناحیه مرکزی در هر دو پanel چپ و میانی ظاهر می‌شود دقیقاً همان چیزی است که ضرب را با پanel راست هم‌خوان می‌کند.
:::

**رابطه استقلال:** استقلال شرطی یعنی وقتی دید خود را به ناحیه $C$ محدود می‌کنیم، این نسبت‌ها قانون ضرب را برآورده می‌کنند. نسبت در هر دو $A$ و $B$ (پanel راست) برابر حاصل‌ضرب نسبت‌های فردی (پanel چپ × پanel میانی) است. این تجسم بصری $P(A \cap B \mid C) = P(A \mid C) P(B \mid C)$ است.

این با نگاه به $A$ و $B$ در کل فضای نمونه — جایی که ممکن است وابسته باشند — متفاوت است. استقلال شرطی یعنی *پس از ثابت کردن زمینه* $C$ مستقل می‌شوند.

+++

---

:::{admonition} بررسی معادل شهودی‌تر (اختیاری، اما مفید)
:class: tip dropdown

اگر $P(B\cap C)>0$، آنگاه
$$
A \perp B \mid C
\quad\Longleftrightarrow\quad
P(A\mid B\cap C)=P(A\mid C).
$$

به‌طور متقارن، اگر $P(A\cap C)>0$ آنگاه
$$
P(B\mid A\cap C)=P(B\mid C).
$$

**تفسیر:** وقتی $C$ را می‌دانید، یادگیری $B$ **به‌روزرسانی بیشتری** درباره $A$ نمی‌دهد (و بالعکس).
:::

---

:::{admonition} هشدار: استقلال شرطی با استقلال یکی نیست
:class: warning

**این نکته‌ای حیاتی است که دانشجویان اغلب از دست می‌دهند:** $A \perp B \mid C$ به‌معنای $A \perp B$ **نیست**.

الگوی بسیار رایج:

* مستقل **در هر مقدار ثابت** $C$
* وابسته **پس از مخلوط کردن** (وقتی $C$ پنهان است)

پس استقلال شرطی درباره آنچه **درون** یک زمینه ثابت رخ می‌دهد است، نه پس از میانگین‌گیری روی زمینه‌ها.
:::

---

### ۵.۲. یک مثال کوچک بصری: دو پرتاب سکه انتخاب‌شده تصادفی

برای ملموس کردن استقلال شرطی، از یک مثال ساده استفاده می‌کنیم.

دو سکه داریم:

* سکه منصفانه (F): $P(H)=0.5$
* سکه نامتقارن (B): $P(H)=0.75$

یک سکه به‌طور یکنواخت تصادفی انتخاب کنید، سپس دو بار بیندازید.

فرض کنید:

* $H_1$ = «پرتاب اول شیر باشد»
* $H_2$ = «پرتاب دوم شیر باشد»
* $C$ = «سکه منصفانه را انتخاب کرده‌ایم» (پس $C^c$ = «سکه نامتقارن را انتخاب کرده‌ایم»)

#### بخش ۱: استقلال در هر زمینه

ابتدا ببینیم وقتی **می‌دانیم کدام سکه را داریم** چه می‌شود. بینش کلیدی: وقتی زمینه را ثابت کنید (سکه را بدانید)، دو پرتاب مستقل می‌شوند.

**آنچه باید توجه کنید:**

اگر **سکه را ثابت کنید** ($C$ یا $C^c$ را بدانید)، دو پرتاب مستقل‌اند: دانستن $H_1$ احتمال $H_2$ را تغییر نمی‌دهد. به‌صورت ریاضی:

$$
P(H_2\mid H_1, C) = P(H_2\mid C)
\quad\text{and}\quad
P(H_2\mid H_1, C^c) = P(H_2\mid C^c)
$$

یعنی احتمال مشترک در هر زمینه فاکتور می‌شود (به حاصل‌ضرب تقسیم می‌شود):

(factorization-formula)=
$$
P(H_1\cap H_2\mid C) = P(H_1\mid C)\,P(H_2\mid C)
$$

و به‌طور مشابه برای $C^c$. آن را مصور کنیم:

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_context(ax, p, title, cond_tex):
    """Draw a single context panel showing conditional independence."""
    p = max(0.0, min(1.0, float(p)))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)

    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, linewidth=2))

    # Draw strips for H1 and H2
    ax.add_patch(Rectangle((0, 0), p, 1, facecolor="#d9d9d9", edgecolor="none"))     # H1 strip
    ax.add_patch(Rectangle((0, 1-p), 1, p, facecolor="#c7c7c7", edgecolor="none"))   # H2 strip
    ax.add_patch(Rectangle((0, 1-p), p, p, facecolor="#9e9e9e", edgecolor="none"))   # overlap

    ax.add_patch(Rectangle((0, 0), p, 1, fill=False, linewidth=1.0))
    ax.add_patch(Rectangle((0, 1-p), 1, p, fill=False, linewidth=1.0))
    ax.add_patch(Rectangle((0, 1-p), p, p, fill=False, linewidth=1.2))

    # Labels
    ax.text(p/2, 0.03, r"$H_1$", ha="center", va="bottom", fontsize=12)
    ax.text(0.03, 1-p/2, r"$H_2$", ha="left", va="center", fontsize=12)
    ax.text(p/2, 1-p/2, r"$H_1\cap H_2$", ha="center", va="center", fontsize=12, color="white")

# Coin parameters
p_fair, p_biased = 0.50, 0.75

# Create figure with two panels side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

draw_context(ax1, p_fair,   title=r"Given $C$ = Fair coin ($P(H)=0.5$)",    cond_tex=r"C")
draw_context(ax2, p_biased, title=r"Given $C^c$ = Biased coin ($P(H)=0.75$)", cond_tex=r"C^c")

fig.suptitle(
    "Conditional independence: within each fixed context, the flips are independent",
    fontsize=14, fontweight="bold", y=1.02
)

plt.tight_layout()
fig.savefig("conditional-independence-contexts.svg", format="svg", bbox_inches="tight", pad_inches=0.3)
```

:::{figure} conditional-independence-contexts.svg
:width: 100%
figclass: full-width

**استقلال شرطی در هر زمینه.** هر پanel نوع سکه را ثابت می‌کند. درون پanel، هم‌پوشانی سایه‌دار $P(H_1\cap H_2\mid \text{context})$ را نشان می‌دهد و ابعاد نوارها $P(H_1\mid \text{context})$ و $P(H_2\mid \text{context})$ را.
:::

**بررسی عددی:**

برای **سکه منصفانه** (پanel چپ):
- $P(H_1\mid C) = 0.50$
- $P(H_2\mid C) = 0.50$
- $P(H_1\cap H_2\mid C) = 0.25$
- **بررسی فاکتورسازی:** $P(H_1\mid C) \times P(H_2\mid C) = 0.50 \times 0.50 = 0.25$ ✓

برای **سکه نامتقارن** (پanel راست):
- $P(H_1\mid C^c) = 0.75$
- $P(H_2\mid C^c) = 0.75$
- $P(H_1\cap H_2\mid C^c) = 0.5625$
- **بررسی فاکتورسازی:** $P(H_1\mid C^c) \times P(H_2\mid C^c) = 0.75 \times 0.75 = 0.5625$ ✓

در هر دو پanel، احتمال مشترک برابر حاصل‌ضرب حاشیه‌ای‌هاست. استقلال همین است.

---

#### بخش ۲: وقتی زمینه پنهان است (مخلوط‌سازی)

اکنون بخش شگفت‌انگیز: **وقتی نمی‌دانیم کدام سکه انتخاب شده**، پرتاب‌ها دیگر مستقل نیستند!

**چرا وابستگی پدید می‌آید:**

اگر **سکه را نمی‌دانید**، مشاهده $H_1$ درباره *کدام سکه احتمالاً دارید* اطلاعات می‌دهد. مثلاً:
- دیدن شیر در پرتاب اول، سکه نامتقارن را محتمل‌تر می‌کند
- این شیر بودن پرتاب دوم را محتمل‌تر می‌کند
- پس $H_1$ و $H_2$ وقتی زمینه پنهان است وابسته‌اند

**آماده‌سازی ریاضی:**

برای یافتن احتمال کلی هر دو پرتاب شیر وقتی نمی‌دانیم کدام سکه انتخاب شده، قانون احتمال کل را با پارتیشن $\{C, C^c\}$ به‌کار می‌بریم:

$$
\begin{align*}
P(H_1\cap H_2) &= P(H_1\cap H_2\mid C)P(C) \\
&\quad + P(H_1\cap H_2\mid C^c)P(C^c)
\end{align*}
$$

این همان اصل قبلی است که برای واقعه‌های تکی به‌کار بردیم (مثل $P(B) = P(B|A)P(A) + P(B|A^c)P(A^c)$)، اما اکنون روی اشتراک $H_1 \cap H_2$ اعمال شده. واقعه مشترک را به دو حالت ناسازگار (سکه منصفانه در برابر نامتقارن) می‌شکنیم و احتمال‌های وزنی‌شان را جمع می‌کنیم.

ببینیم مخلوط کردن دو زمینه چگونه وابستگی می‌سازد:

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_mixture(ax, w_fair, w_biased, p_fair, p_biased):
    w_fair = max(0.0, float(w_fair))
    w_biased = max(0.0, float(w_biased))
    tot = (w_fair + w_biased) if (w_fair + w_biased) > 0 else 1.0
    wf, wb = w_fair / tot, w_biased / tot

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(r"Context hidden (mixture)", fontsize=13, fontweight="bold", pad=10)

    # Center the box
    y0, h = 0.25, 0.50
    ax.add_patch(Rectangle((0, y0), 1, h, fill=False, linewidth=2))

    ax.add_patch(Rectangle((0, y0 + h*(1-wf)), 1, h*wf, facecolor="#e6e6e6", edgecolor="none"))
    ax.add_patch(Rectangle((0, y0),            1, h*wb, facecolor="#d1d1d1", edgecolor="none"))

    ax.text(0.02, y0 + h*(1-wf/2),
            rf"Fair context ($C$), weight $P(C)={w_fair:.2f}$",
            ha="left", va="center", fontsize=12, clip_on=False)

    ax.text(0.02, y0 + h*(wb/2),
            rf"Biased context ($C^c$), weight $P(C^c)={w_biased:.2f}$",
            ha="left", va="center", fontsize=12, clip_on=False)

# Coin parameters
p_fair, p_biased = 0.50, 0.75
w_fair, w_biased = 0.50, 0.50  # Equal probability of choosing each coin

# Create figure with just the mixture panel
fig, ax = plt.subplots(1, 1, figsize=(8, 5))

draw_mixture(ax, w_fair, w_biased, p_fair, p_biased)

plt.tight_layout()
fig.savefig("conditional-independence-mixture.svg", format="svg", bbox_inches="tight", pad_inches=0.4)
```

:::{figure} conditional-independence-mixture.svg
:width: 70%

**اثر مخلوط‌سازی.** وقتی نمی‌دانیم کدام سکه انتخاب شده، باید دو زمینه (منصفانه و نامتقارن) را با احتمال‌هایشان به‌عنوان وزن ترکیب کنیم.
:::

**درک محاسبه:**

وقتی زمینه پنهان است، از **قانون احتمال کل** برای ترکیب هر دو سناریو استفاده می‌کنیم و هر کدام را با احتمال وقوعش وزن می‌دهیم (توجه: $P(C) + P(C^c) = 1$):

$$
\begin{align*}
P(H_1\cap H_2) &= P(H_1\cap H_2\mid C)P(C) \\
&\quad + P(H_1\cap H_2\mid C^c)P(C^c)
\end{align*}
$$

**بررسی عددی:**

از تنظیمات می‌دانیم هر سکه با احتمال یکسان انتخاب می‌شود، پس $P(C) = P(C^c) = 0.5$. سکه منصفانه با احتمال 0.5 و سکه نامتقارن با 0.75 شیر می‌دهد. چون هر پرتاب احتمال یکسانی دارد، $P(H_1\mid C) = P(H_2\mid C) = 0.5$ و $P(H_1\mid C^c) = P(H_2\mid C^c) = 0.75$.

اکنون احتمال‌های فردی را محاسبه کنیم:

$$
\begin{align*}
P(H_1) &= P(H_1\mid C)P(C) + P(H_1\mid C^c)P(C^c) \\
&= (0.50)(0.50) + (0.75)(0.50) \\
&= 0.625
\end{align*}
$$

$$
P(H_2) = 0.625 \quad \text{(by the same calculation)}
$$

برای اشتراک، دو ایده را ترکیب می‌کنیم:

1. **قانون احتمال کل** (بالا) ساختار را می‌دهد:

   $$
   \begin{align*}
   P(H_1\cap H_2) &= P(H_1\cap H_2\mid C)P(C) \\
   &\quad + P(H_1\cap H_2\mid C^c)P(C^c)
   \end{align*}
   $$

2. **استقلال شرطی** ([از بخش ۱](#factorization-formula)) اجازه فاکتورسازی در هر زمینه را می‌دهد:

   برای سکه منصفانه:

   $$
   \begin{align*}
   P(H_1\cap H_2\mid C) &= P(H_1\mid C) \times P(H_2\mid C) \\
   &= 0.5 \times 0.5 \\
   &= 0.25
   \end{align*}
   $$

   برای سکه نامتقارن:

   $$
   \begin{align*}
   P(H_1\cap H_2\mid C^c) &= P(H_1\mid C^c) \times P(H_2\mid C^c) \\
   &= 0.75 \times 0.75 \\
   &= 0.5625
   \end{align*}
   $$

3. **جمع‌بندی**:

   $$
   \begin{align*}
   P(H_1\cap H_2) &= P(H_1\cap H_2\mid C)P(C) + P(H_1\cap H_2\mid C^c)P(C^c) \\
   &= (0.25)(0.50) + (0.5625)(0.50) \\
   &= 0.125 + 0.28125 \\
   &= 0.40625
   \end{align*}
   $$

اکنون استقلال را بررسی کنیم:

$$
P(H_1\cap H_2) = 0.40625
$$

$$
\begin{align*}
P(H_1) \times P(H_2) &= 0.625 \times 0.625 \\
&= 0.390625
\end{align*}
$$

چون $0.40625 \neq 0.390625$، احتمال مشترک **برابر حاصل‌ضرب نیست**. یعنی **وقتی زمینه پنهان است واقعه‌ها وابسته‌اند**.

**بررسی به‌روزرسانی (تأیید جایگزین):**

می‌توانیم وابستگی را با بررسی اینکه آیا مشاهده $H_1$ باور ما درباره $H_2$ را به‌روز می‌کند نیز تأیید کنیم:

$$
\begin{align*}
P(H_2\mid H_1) &= \frac{P(H_1\cap H_2)}{P(H_1)} \\
&= \frac{0.40625}{0.625} \\
&= 0.65
\end{align*}
$$

اما $P(H_2) = 0.625$. چون $P(H_2\mid H_1) = 0.65 \neq 0.625 = P(H_2)$، مشاهده $H_1$ باور ما درباره $H_2$ را **به‌روز می‌کند** و وابستگی را تأیید می‌کند.

**بینش کلیدی:** پرتاب‌ها در هر زمینه مستقل‌اند، اما در کل وابسته. چون مشاهده $H_1$ باور ما درباره سکه‌ای که داریم را تغییر می‌دهد و این بدون نوبت بر باور ما درباره $H_2$ اثر می‌گذارد.

:::{admonition} خلاصه هر سه سناریو
:class: tip dropdown

محاسبات بالا نشان داد وقتی زمینه پنهان است (سناریو ۱) چه می‌شود. خلاصه کامل هر سه حالت:

**سناریو ۱: زمینه پنهان (نمی‌دانیم کدام سکه)**

$$
\begin{align*}
P(H_1) &= 0.625 \\
P(H_2) &= 0.625 \\
P(H_1\cap H_2) &= 0.40625 \\
P(H_1)P(H_2) &= 0.390625
\end{align*}
$$

چون $P(H_1\cap H_2) \neq P(H_1)P(H_2)$، واقعه‌ها **مستقل نیستند** (مشاهده $H_1$ باور درباره $H_2$ را به‌روز می‌کند).

**سناریو ۲: می‌دانیم سکه منصفانه انتخاب شده ($C$)**

$$
\begin{align*}
P(H_1\mid C) &= 0.5 \\
P(H_2\mid C) &= 0.5 \\
P(H_1\cap H_2\mid C) &= 0.25 \\
P(H_1\mid C) \times P(H_2\mid C) &= 0.25
\end{align*}
$$

چون $P(H_1\cap H_2\mid C) = P(H_1\mid C) \times P(H_2\mid C)$، واقعه‌ها **در این زمینه مستقل‌اند**.

**سناریو ۳: می‌دانیم سکه نامتقارن انتخاب شده ($C^c$)**

$$
\begin{align*}
P(H_1\mid C^c) &= 0.75 \\
P(H_2\mid C^c) &= 0.75 \\
P(H_1\cap H_2\mid C^c) &= 0.5625 \\
P(H_1\mid C^c) \times P(H_2\mid C^c) &= 0.5625
\end{align*}
$$

چون $P(H_1\cap H_2\mid C^c) = P(H_1\mid C^c) \times P(H_2\mid C^c)$، واقعه‌ها **در این زمینه مستقل‌اند**.

**نتیجه:** $H_1$ و $H_2$ **مستقل شرطی‌اند** با فرض اینکه کدام سکه انتخاب شده ($H_1 \perp H_2 \mid C$)، اما **مستقل نیستند** وقتی سکه نامعلوم است.
:::

---

**بازگشت به اصل کلی:**

مثال سکه ما بینش کلیدی بخش ۵.۱ را به‌خوبی نشان می‌دهد:
- $H_1 \perp H_2 \mid C$ داریم (پرتاب‌ها با فرض سکه مستقل شرطی‌اند)
- اما $H_1 \perp H_2$ **نداریم** (پرتاب‌ها در کل وقتی سکه نامعلوم است وابسته‌اند)

این نشان می‌دهد **استقلال شرطی به معنای استقلال بدون شرط نیست**. وابستگی وقتی زمینه‌ها را مخلوط می‌کنیم (میانگین روی متغیر پنهان $C$) پدید می‌آید. این الگو در همه جای آمار و تحلیل داده دیده می‌شود: روابطی که در زیرگروه‌ها ناپدید می‌شوند اما در داده کلی ظاهر می‌شوند، یا بالعکس.

---

### ۵.۳. نکات کلیدی و کاربردهای واقعی

**بینش اصلی در یک جمله:**

شرط گذاشتن روی $C$ «زمینه را قفل می‌کند» — با فرض $C$، واقعه‌های $A$ و $B$ یکدیگر را به‌روز نمی‌کنند. وقتی $C$ پنهان است، مخلوط کردن زمینه‌ها می‌تواند وابستگی بسازد (یا استقلال را پنهان کند).

**چرا در عمل مهم است:**

استقلال شرطی ایده پشت **کنترل متغیرهای مخدوش‌کننده** در آزمایش‌ها و تحلیل داده واقعی است:

1. **پژوهش پزشکی:** رابطه ظاهری بین درمان و پیامد ممکن است با کنترل سن، جنس یا شدت پایه ضعیف، ناپدید یا حتی معکوس شود.

2. **تحلیل داده:** بسیاری از «کشف‌های کاذب» از نادیده گرفتن متغیرهای گروه‌بندی پنهان می‌آید. مخلوط کردن داده از دسته‌ها، سایت‌ها یا دوره‌های زمانی مختلف می‌تواند همبستگی‌های spurious ایجاد کند که شبیه اثر واقعی به نظر برسند.

3. **یادگیری ماشین:** فهمیدن اینکه ویژگی‌ها با فرض دیگران مستقل شرطی‌اند برای ساخت مدل‌های دقیق و اجتناب از مخدوش‌سازی حیاتی است.

**درس عملی:** همیش بپرسید «در چه زمینه‌ای هستم؟» هنگام تحلیل روابط بین متغیرها، در نظر بگیرید آیا فاکتور پنهان $C$ وجود دارد که پس از لحاظ آن، تصویر کاملاً عوض شود. این یکی از مهم‌ترین مفاهیم برای گذار از نظریه احتمال به استدلال آماری در دنیای واقعی است.

---

+++

## خلاصه فصل


* **قضیه بیز** $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$ قانون بنیادی برای به‌روزرسانی احتمال‌ها (باورها) بر اساس شواهد جدید است.
* آن **احتمال پسین** $P(A|B)$ را به **احتمال پیشین** $P(A)$ و **درست‌نمایی** $P(B|A)$ مرتبط می‌کند.
* جمله $P(B)$ به‌عنوان ثابت نرمال‌سازی عمل می‌کند و اغلب با **قانون احتمال کل** محاسبه می‌شود.
* قضیه بیز در زمینه‌هایی مثل تشخیص پزشکی، یادگیری ماشین (فیلتر هرزنامه، طبقه‌بندی) و استدلال علمی حیاتی است.
* دو واقعه A و B **مستقل**‌اند اگر $P(A \cap B) = P(A)P(B)$، یا به‌طور معادل $P(A|B) = P(A)$ (با فرض $P(B)>0$). وقوع یکی احتمال دیگری را تغییر نمی‌دهد.
* دو واقعه A و B **مستقل شرطی** با فرض C هستند اگر $P(A \cap B | C) = P(A|C)P(B|C)$. پس از معلوم شدن نتیجه C مستقل می‌شوند.
* شبیه‌سازی ابزار ارزشمندی برای ساخت شهود درباره قضیه بیز و استقلال با مشاهده فراوانی‌ها در داده تولیدشده است.

+++

در بخش بعدی کتاب، تمرکز را از واقعه‌ها به **متغیرهای تصادفی** — پیامدهای عددی پدیده‌های تصادفی — منتقل می‌کنیم و توزیع‌هایشان را بررسی می‌کنیم. این به ما اجازه می‌دهد موقعیت‌های احتمالی را ساختاریافته‌تر مدل و تحلیل کنیم.

+++

## تمرین‌ها

1.  **دو urn (بیز):** یک urn را به‌طور تصادفی انتخاب می‌کنید:

    * $U_1$ با احتمال $0.6$ (شامل ۳ قرمز، ۲ آبی)
    * $U_2$ با احتمال $0.4$ (شامل ۱ قرمز، ۴ آبی)

    یک تو می‌کشید و **قرمز** است. $P(U_1\mid R)$ چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    داده شده:

    * $P(U_1)=0.6$, $P(U_2)=0.4$
    * $P(R\mid U_1)=3/5=0.6$
    * $P(R\mid U_2)=1/5=0.2$

    ابتدا $P(R)$ را با احتمال کل محاسبه کنید:

    $$
    \begin{align*}
    P(R) &= P(R\mid U_1)P(U_1)+P(R\mid U_2)P(U_2) \\
    &= (0.6)(0.6)+(0.2)(0.4) \\
    &= 0.44.
    \end{align*}
    $$

    سپس قضیه بیز را به‌کار ببرید:

    $$
    \begin{align*}
    P(U_1\mid R) &= \frac{P(R\mid U_1)P(U_1)}{P(R)} \\
    &= \frac{0.6\cdot 0.6}{0.44} \\
    &= \frac{0.36}{0.44} \\
    &= \frac{9}{11}\approx 0.818.
    \end{align*}
    $$
    ```

2.  **آزمون تشخیصی (احتمال پسین):** بیماری شیوع $P(D)=0.005$ (0.5%) دارد. آزمون:

    * حساسیت $P(\text{Pos}\mid D)=0.98$
    * نرخ مثبت کاذب $P(\text{Pos}\mid D^c)=0.03$

    اگر کسی نتیجه مثبت بگیرد، $P(D\mid \text{Pos})$ چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    ابتدا $P(\text{Pos})$ را بیابید:

    $$
    \begin{align*}
    P(\text{Pos})
      &= P(\text{Pos}\mid D)P(D) + P(\text{Pos}\mid D^c)P(D^c) \\
      &= 0.98\cdot 0.005 + 0.03\cdot (1-0.005) \\
      &= 0.0049 + 0.02985 \\
      &= 0.03475.
    \end{align*}
    $$

    سپس قضیه بیز:

    $$
    \begin{align*}
    P(D\mid \text{Pos})
    &= \frac{P(\text{Pos}\mid D)P(D)}{P(\text{Pos})} \\
    &= \frac{0.98\cdot 0.005}{0.03475} \\
    &\approx 0.141.
    \end{align*}
    $$

    پس حتی با نتیجه مثبت، احتمال واقعی بیماری حدود **14.1%** است (چون بیماری نادر است).
    ```

3.  **فیلتر هرزنامه (بیز):** فرض کنید 20% ایمیل‌ها هرزنامه‌اند:

    * $P(S)=0.20$
    * کلمه «FREE» در 50% ایمیل‌های هرزنامه ظاهر می‌شود: $P(F\mid S)=0.50$
    * کلمه «FREE» در 2% ایمیل‌های غیرهرزنامه ظاهر می‌شود: $P(F\mid S^c)=0.02$

    اگر ایمیلی «FREE» داشته باشد، $P(S\mid F)$ چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    ابتدا $P(F)$ را محاسبه کنید:

    $$
    \begin{align*}
    P(F) &= P(F\mid S)P(S)+P(F\mid S^c)P(S^c) \\
    &= 0.50\cdot 0.20 + 0.02\cdot 0.80 \\
    &= 0.10 + 0.016 \\
    &= 0.116.
    \end{align*}
    $$

    سپس قضیه بیز:

    $$
    \begin{align*}
    P(S\mid F) &= \frac{P(F\mid S)P(S)}{P(F)} \\
    &= \frac{0.50\cdot 0.20}{0.116} \\
    &= \frac{0.10}{0.116} \\
    &= \frac{25}{29}\approx 0.862.
    \end{align*}
    $$

    پس $P(S\mid F)\approx 86.2\%$.
    ```

4.  **آیا این واقعه‌ها مستقل‌اند؟** یک تاس منصفانه شش‌وجهی بینندازید.

    * $A$ = «عدد زوج باشد» = {2, 4, 6}
    * $B$ = «عدد اول باشد» = {2, 3, 5}

    آیا $A$ و $B$ مستقل‌اند؟

    ```{admonition} پاسخ
    :class: dropdown

    محاسبه کنید:

    * $P(A)=3/6=1/2$
    * $P(B)=3/6=1/2$
    * $A\cap B$ = {2}, so $P(A\cap B)=1/6$

    اگر $A$ و $B$ مستقل بودند، باید داشتیم
    $P(A\cap B)=P(A)P(B)=(1/2)(1/2)=1/4$.

    اما $1/6 \ne 1/4$، پس واقعه‌ها **مستقل نیستند**.
    ```

5.  **ناسازگار در برابر مستقل:** یک تاس منصفانه شش‌وجهی بینندازید.

    * $A$ = «عدد 1 باشد»
    * $B$ = «عدد 2 باشد»

    آیا $A$ و $B$ مستقل‌اند؟

    ```{admonition} پاسخ
    :class: dropdown

    آن‌ها **ناسازگار**‌اند: $A\cap B=\emptyset$، پس $P(A\cap B)=0$.

    اما $P(A)=1/6$ و $P(B)=1/6$، پس $P(A)P(B)=1/36$.

    چون $P(A\cap B) \ne P(A)P(B)$، واقعه‌ها **مستقل نیستند**.
    ```

6.  **استقلال شرطی (مخلوط سکه):** یک سکه انتخاب می‌کنید:

    * منصفانه با احتمال $P(C)=0.4$ (پس $P(H\mid C)=0.5$)
    * نامتقارن با احتمال $P(C^c)=0.6$ (پس $P(H\mid C^c)=0.8$)

    سپس دو بار می‌اندازید. $H_1$ «پرتاب اول شیر باشد» و $H_2$ «پرتاب دوم شیر باشد».

    1. $P(H_2)$ و $P(H_2\mid H_1)$ را محاسبه کنید و تصمیم بگیرید آیا $H_1$ و $H_2$ در کل مستقل‌اند.
    2. نشان دهید $H_1 \perp H_2 \mid C$.

    ```{admonition} پاسخ
    :class: dropdown

    **1) در کل (زمینه پنهان).**

    با احتمال کل:

    $$
    \begin{align*}
    P(H_2) &= P(H\mid C)P(C)+P(H\mid C^c)P(C^c) \\
    &= 0.5\cdot 0.4 + 0.8\cdot 0.6 \\
    &= 0.68.
    \end{align*}
    $$

    همچنین،

    $$
    \begin{align*}
    P(H_1\cap H_2) &= P(HH\mid C)P(C) \\
    &\quad +P(HH\mid C^c)P(C^c) \\
    &= (0.5^2)\cdot 0.4 + (0.8^2)\cdot 0.6 \\
    &= 0.25\cdot 0.4 + 0.64\cdot 0.6 \\
    &= 0.484.
    \end{align*}
    $$

    پس

    $$
    \begin{align*}
    P(H_2\mid H_1) &= \frac{P(H_1\cap H_2)}{P(H_1)} \\
    &= \frac{0.484}{0.68} \\
    &\approx 0.712.
    \end{align*}
    $$

    چون $P(H_2\mid H_1)\approx 0.712 \ne P(H_2)=0.68$، پرتاب‌ها **در کل مستقل نیستند**.

    **2) در یک زمینه ثابت.**

    اگر بر اینکه کدام سکه انتخاب کرده‌اید شرط بگذارید:

    * با فرض $C$ (سکه منصفانه)، پرتاب‌ها مستقل‌اند، پس
      $$
      P(H_2\mid H_1, C)=P(H_2\mid C)=0.5.
      $$
    * با فرض $C^c$ (سکه نامتقارن)، به‌طور مشابه،
      $$
      P(H_2\mid H_1, C^c)=P(H_2\mid C^c)=0.8.
      $$

    این دقیقاً شرط «بدون به‌روزرسانی اضافی» است، پس

    $$
    H_1 \perp H_2 \mid C.
    $$
    ```
