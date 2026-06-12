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
  - file: notebooks/chapter_04.ipynb
---

# فصل ۴: احتمال شرطی

در فصول پیشین، مبانی احتمال را گذاشتیم و فضای نمونه، واقعه‌ها و روش‌های شمارش را بررسی کردیم. اکنون به یکی از بنیادی‌ترین و قدرتمندترین مفاهیم نظریه احتمال وارد می‌شویم: **احتمال شرطی**.

اغلب به احتمال وقوع یک واقعه *با فرض اینکه* واقعه دیگری از قبل رخ داده است علاقه‌مندیم. دانش یا فرضیات ما درباره یک واقعه می‌تواند ارزیابی احتمال واقعه دیگر را تغییر دهد. این همان جوهر احتمال شرطی است. این مفهوم به ما اجازه می‌دهد با دریافت اطلاعات جدید، باورهای خود را به‌روز کنیم.


## ۱. تعریف و شهود

**احتمال شرطی** احتمال وقوع واقعه $A$ را با فرض اینکه واقعه دیگر $B$ از قبل رخ داده است (یا معلوم است که رخ داده) می‌سنجد. آن را با $P(A|B)$ نمایش می‌دهیم و «احتمال $A$ با فرض $B$» می‌خوانیم.

**شهود:** کل فضای نمونه $S$ را در نظر بگیرید. وقتی می‌دانیم واقعه $B$ رخ داده است، تمرکز ما عملاً از کل فضای نمونه $S$ به فقط پیامدهای داخل $B$ محدود می‌شود. اکنون به احتمال وقوع $A$ *در این فضای نمونه جدید و کوچک‌شده* $B$ علاقه‌مندیم. پیامدهای مطلوب برای «$A$ با فرض $B$» پیامدهایی هستند که هم به $A$ و هم به $B$ تعلق دارند، یعنی $A \cap B$.

**تعریف رسمی:**
برای هر دو واقعه $A$ و $B$ از فضای نمونه $S$، به‌شرط $P(B) > 0$، احتمال شرطی $A$ با فرض $B$ به‌صورت زیر تعریف می‌شود:

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$

که در آن:
* $P(A \cap B)$ احتمال وقوع هم‌زمان هر دو واقعه $A$ و $B$ است.
* $P(B)$ احتمال وقوع واقعه $B$ است.

+++

### ۱.۱. نمایش بصری

نمودار ون زیر ساختار کلی احتمال شرطی را نشان می‌دهد. وقتی بر وقوع واقعه $B$ شرط می‌گذاریم، توجه خود را به دایره $B$ محدود می‌کنیم. درون آن دایره، $P(A|B)$ سهم $B$ را که با $A$ هم‌پوشانی دارد نشان می‌دهد.

```{code-cell} ipython3
:tags: [remove-input, remove-output]

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

# Generic Venn diagram
fig = plt.figure(figsize=(7, 4.5))
v = venn2(subsets=(3, 1, 1), set_labels=('A', 'B'))
venn2_circles(subsets=(3, 1, 1), linestyle='solid', linewidth=2)

lab = v.get_label_by_id('11')
if lab is not None:
    lab.set_text('A ∩ B')
    lab.set_fontsize(14)
    lab.set_fontweight('bold')

lab = v.get_label_by_id('01')
if lab is not None:
    lab.set_text('B only')
    lab.set_fontsize(12)

lab = v.get_label_by_id('10')
if lab is not None:
    lab.set_text('A only')
    lab.set_fontsize(12)

plt.title('Conditional Probability: Given B occurred, what is P(A|B)?', fontsize=14, fontweight='bold')
plt.annotate(
    'When B happens, restrict to circle B.\nP(A|B) = P(A ∩ B) / P(B)',
    xy=(0.67, 0.5), xycoords='axes fraction',
    xytext=(0.95, 0.85), textcoords='axes fraction',
    arrowprops=dict(arrowstyle='->', lw=2, color='darkblue'),
    ha='left', va='top',
    fontsize=12,
    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='darkblue', linewidth=1.5)
)
plt.tight_layout()
fig.savefig("venn-conditional-generic.svg", format="svg", bbox_inches="tight")
```

```{figure} venn-conditional-generic.svg
---
width: 80%
---
نمودار ون کلی: $P(A|B)$ نسبت هم‌پوشانی به $B$ است.
```

%
% Example code
%

```{code-cell} ipython3
:tags: [remove-input, remove-output]

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

fig = plt.figure(figsize=(7, 4.5))
v = venn2(subsets=(9, 2, 2), set_labels=('A: at least one 3', 'B: sum = 9'))
venn2_circles(subsets=(9, 2, 2), linestyle='solid', linewidth=1)

lab = v.get_label_by_id('11')
if lab is not None:
    lab.set_text('A ∩ B\n(3,6)\n(6,3)\n\n(A|B)')

lab = v.get_label_by_id('01')
if lab is not None:
    lab.set_text('B only\n(4,5)\n(5,4)')

lab = v.get_label_by_id('10')
if lab is not None:
    lab.set_text('A only\n(…9 outcomes…)')

plt.title('Given B, restrict to circle B; A|B is the overlap')
plt.annotate(
    'We already know B happened\n→ restrict attention to circle B\n\u2234 P(A|B) is a ratio of P(A n B) to P(B)',
    xy=(0.75, .75), xycoords='axes fraction',
    xytext=(1, 0.95), textcoords='axes fraction',
    arrowprops=dict(arrowstyle='->', lw=1),
    ha='left', va='top'
)
plt.tight_layout()

fig.savefig("venn-dice-a-given-b.svg", format="svg", bbox_inches="tight")

# plt.show()
# plt.close(fig)
```

%
% Example
% 


:::{admonition} مثال
:class: tip dropdown

**دو تاس — «حداقل یک ۳» با فرض «مجموع برابر ۹»**

دو تاس منصفانه شش‌وجهی بیندازید.

- **A** را واقعه *«حداقل یکی از تاس‌ها ۳ نشان دهد»* در نظر بگیرید.
- **B** را واقعه *«مجموع دو تاس برابر ۹ باشد»* در نظر بگیرید.

احتمال شرطی $P(A\mid B)$ را می‌خواهیم.

**گام ۱ — فهرست کردن پیامدهای $B$**
پیامدهای (جفت‌های مرتب) که مجموعشان ۹ می‌شود:
$$B = \{(3,6),(4,5),(5,4),(6,3)\}.$$
پس $|B|=4$ و بنابراین $P(B)=4/36$.

**گام ۲ — یافتن پیامدهایی که هم در $A$ هستند**
درون $B$، پیامدهایی که شامل ۳ هستند:
$$A\cap B = \{(3,6),(6,3)\}.$$
پس $|A\cap B|=2$ و بنابراین $P(A\cap B)=2/36$.

**گام ۳ — به‌کارگیری تعریف**
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)} = \frac{2/36}{4/36}=\frac12.$$

**شهود:** وقتی به ما گفته می‌شود $B$ رخ داده است، «فضای نمونه جدید» فقط همان ۴ پیامد در $B$ است. در این فضای محدودشده، ۲ پیامد از ۴ پیامد $A$ را برآورده می‌کنند، پس $P(A\mid B)=2/4=1/2$.


```{figure} venn-dice-a-given-b.svg
```

:::

+++

## ۲. قانون ضرب برای احتمال شرطی

بازآرایی تعریف احتمال شرطی **قانون ضرب عمومی** را به ما می‌دهد که برای محاسبه احتمال اشتراک دو واقعه مفید است:

$$ P(A \cap B) = P(A|B) P(B) $$

به‌طور مشابه، اگر $P(A) > 0$ باشد، می‌توانیم بنویسیم:

$$ P(A \cap B) = P(B|A) P(A) $$

این قانون به‌ویژه وقتی مفید است که با واقعه‌های پیاپی سر و کار داریم؛ جایی که پیامد واقعه اول بر احتمال واقعه دوم اثر می‌گذارد.


:::{admonition} مثال
:class: tip dropdown
**احتمال کشیدن دو شاه**

احتمال کشیدن دو شاه از یک دسته استاندارد ۵۲ کارتی بدون بازگرداندن.
$A$ را واقعه «کارت اول کشیده‌شده شاه باشد» و $B$ را واقعه «کارت دوم کشیده‌شده شاه باشد» در نظر بگیرید.
می‌خواهیم $P(A \cap B)$ را بیابیم.
با استفاده از قانون ضرب: $P(A \cap B) = P(B|A) P(A)$.
* $P(A)$: ۴ شاه در ۵۲ کارت وجود دارد، پس $P(A) = \frac{4}{52}$.
* $P(B|A)$: *با فرض* اینکه کارت اول شاه بوده است، اکنون ۳ شاه در ۵۱ کارت باقی‌مانده وجود دارد. پس $P(B|A) = \frac{3}{51}$.

بنابراین،

$$
\begin{align*}
P(\text{Draw 2 Kings}) &= P(A \cap B) \\
&= P(B|A) P(A) \\
&= \frac{3}{51} \times \frac{4}{52} \\
&= \frac{12}{2652} \\
&\approx 0.0045
\end{align*}
$$

:::

قانون ضرب را می‌توان به بیش از دو واقعه تعمیم داد. برای سه واقعه $A, B, C$:

$$ P(A \cap B \cap C) = P(C | A \cap B) P(B | A) P(A) $$

:::{admonition} اثبات: قانون زنجیره‌ای برای سه واقعه
:class: tip dropdown

برای یافتن $P(A \cap B \cap C)$، قانون ضرب را در دو مرحله به‌کار می‌بریم:

**گام ۱: $(A \cap B)$ را به‌عنوان یک واقعه واحد در نظر بگیرید** دو واقعه اول را یک بلوک فرض کنید. طبق قانون ضرب استاندارد:
$$P((A \cap B) \cap C) = P(A \cap B) \cdot P(C | A \cap B)$$
*(منطق: برای وقوع هر سه، دو واقعه اول باید رخ دهند و سپس $C$ باید با فرض وقوع $A$ و $B$ رخ دهد.)*

**گام ۲: بلوک اول $P(A \cap B)$ را تجزیه کنید** اکنون قانون ضرب را دوباره فقط برای بخش $A$ و $B$ به‌کار می‌بریم:
$$P(A \cap B) = P(A) \cdot P(B | A)$$

**گام ۳: بخش‌ها را ترکیب کنید** عبارت گام ۲ را در معادله گام ۱ جایگذاری کنید:
$$P(A \cap B \cap C) = \underbrace{P(A) \cdot P(B | A)}_{P(A \cap B)} \cdot P(C | A \cap B)$$

**نتیجه نهایی:**
$$P(A \cap B \cap C) = P(A) \cdot P(B | A) \cdot P(C | A \cap B)$$
:::

+++

## ۳. قانون احتمال کل

گاهی محاسبه مستقیم احتمال واقعه $A$ دشوار است. با این حال، ممکن است احتمال‌های شرطی $A$ را در سناریوهای **دو به دو ناسازگار** و **فراگیر** مختلف بدانیم. **قانون احتمال کل** به ما اجازه می‌دهد آن احتمال‌های مبتنی بر سناریو را در یک احتمال کلی ترکیب کنیم.

### ۳.۱ تعریف

$B_1, B_2, \ldots, B_n$ را **پارتیشن** فضای نمونه $S$ در نظر بگیرید. یعنی:

1. $B_i \cap B_j = \emptyset$ برای همه $i \neq j$ (واقعه‌ها دو به دو ناسازگارند)،
2. $B_1 \cup B_2 \cup \cdots \cup B_n = S$ (کل فضای نمونه را می‌پوشانند)،
3. $P(B_i) > 0$ برای همه $i$ (تا احتمال‌های شرطی به‌درستی تعریف شوند).

آنگاه برای هر واقعه $A$ در $S$، قانون احتمال کل می‌گوید:

$$
P(A) = \sum_{i=1}^{n} P(A \mid B_i)\,P(B_i).
$$

به‌صورت معادل، به‌صورت مجموع بازشده:

$$
\begin{align*}
P(A) ={}& P(A\mid B_1)P(B_1) \\
& + P(A\mid B_2)P(B_2) \\
& + \ldots \\
& + P(A\mid B_n)P(B_n).
\end{align*}
$$

### ۳.۲ چرا درست است

ایده کلیدی این است که پارتیشن، $A$ را به **قطعات ناسازگار** می‌شکند:

$$
A = (A\cap B_1)\ \cup\ (A\cap B_2)\ \cup\ \cdots\ \cup\ (A\cap B_n),
$$

و این قطعات هم‌پوشانی ندارند چون $B_i$ها هم‌پوشانی ندارند.

پس می‌توانیم احتمال‌هایشان را جمع کنیم:

$$
P(A) = \sum_{i=1}^n P(A\cap B_i).
$$

در پایان، قانون ضرب $P(A\cap B_i)=P(A\mid B_i)P(B_i)$ را برای هر جمله به‌کار ببرید:

$$
P(A) = \sum_{i=1}^n P(A\mid B_i)P(B_i).
$$

### ۳.۳ شهود

$B_i$ها را «سناریویی که در آن هستیم» در نظر بگیرید. ابتدا یک سناریو $B_i$ رخ می‌دهد (با احتمال $P(B_i)$). سپس درون آن سناریو، $A$ با احتمال $P(A\mid B_i)$ رخ می‌دهد. احتمال کلی $P(A)$ یک **میانگین وزنی** از احتمال‌های شرطی $P(A\mid B_i)$ است که وزن‌ها برابر با احتمال هر سناریو هستند.

### ۳.۴ شهود بصری: مدل مساحتی

**نحوه خواندن نمودار**

- فضای نمونه $S$ به نوارهای ناسازگار $B_1,\dots,B_n$ (یک پارتیشن) تقسیم شده است؛ پس دقیقاً یک $B_i$ رخ می‌دهد.
- **عرض** هر نوار نشان‌دهنده $P(B_i)$ است.
- قطعه سایه‌دار داخل نوار $i$ بخشی از $A$ را که در آن نوار قرار دارد نشان می‌دهد، یعنی $A\cap B_i$.
- مساحت (واقعی) آن قطعه برابر است با $P(A\cap B_i)=P(A\mid B_i)P(B_i)$.
- جمع قطعات سایه‌دار ناسازگار، $P(A)$ را می‌دهد.

```{code-cell} ipython3
:tags: [remove-input, remove-output]
# create and save visualisation total-probability-area.svg

from pathlib import Path
import random

def save_total_probability_svg(
    filename="total-probability-area.svg",
    n=6,
    p_B=None,
    p_A_given_B=None,
    magnify=8.0,
    font_scale=2.0,
    line_gap=2.0,
    jitter=True,
    jitter_seed=7,
):
    if p_B is None:
        p_B = [1/n] * n
    if p_A_given_B is None:
        p_A_given_B = [0.10, 0.35, 0.18, 0.06, 0.28, 0.12][:n]

    if len(p_B) != n or len(p_A_given_B) != n:
        raise ValueError("p_B and p_A_given_B must have length n.")

    # normalise widths
    s = sum(p_B)
    p_B = [x / s for x in p_B]

    def fmt(x):
        return f"{x:.3f}".rstrip("0").rstrip(".")

    pA = sum(pb * pab for pb, pab in zip(p_B, p_A_given_B))

    # ---------- sizing ----------
    W = 1600
    L = 60
    box_w, box_h = 1320, 330

    outline = "#111827"
    strip_fill = "#f8fafc"
    shade_fill = "#ef4444"
    shade_stroke = "#b91c1c"

    # fonts
    title_sz = int(22 * font_scale)
    note_sz  = int(15 * font_scale)
    B_sz     = int(14 * font_scale)
    num_sz   = int(14 * font_scale)   # "smallest" numbers
    inside_sz = int(15 * font_scale)
    center1  = int(20 * font_scale)
    center2  = int(15 * font_scale)

    # helper: line spacing in px (baseline-to-baseline)
    def dy(px): 
        return int(px * line_gap)

    # ---------- top-down layout (prevents overlaps) ----------
    title_y = 60
    note1_y = title_y + dy(title_sz)
    note2_y = note1_y + dy(note_sz)

    header_bottom = note2_y + int(note_sz * 0.9)

    # Put B-label band BELOW header
    y_B  = header_bottom + dy(B_sz)        # B_i
    y_PB = y_B + dy(num_sz)                # P(B_i)

    # Put box BELOW B-label band
    y0 = y_PB + int(num_sz * 1.8)
    x0 = L
    y1 = y0 + box_h

    # Bottom labels below box
    y_bottom1 = y1 + int(num_sz * 1.8)
    y_bottom2 = y_bottom1 + dy(num_sz)

    # Total height
    H = y_bottom2 + int(num_sz * 4.0)

    # ---------- SVG ----------
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>')

    # Header as separate text lines (cleaner than giant tspans at huge spacing)
    parts.append(f'''
<text x="{L}" y="{title_y}"
      font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial"
      font-size="{title_sz}" font-weight="700" fill="{outline}">
  Law of Total Probability — area model
</text>
<text x="{L}" y="{note1_y}"
      font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial"
      font-size="{note_sz}" fill="{outline}">
  Widths are to scale (P(Bᵢ)). Shaded height is ×{magnify:g} for visibility (not to scale).
</text>
<text x="{L}" y="{note2_y}"
      font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial"
      font-size="{note_sz}" fill="{outline}">
  P(A)=Σᵢ P(A|Bᵢ)P(Bᵢ) (example numbers here give P(A)={fmt(pA)})
</text>
'''.strip())

    # Box
    parts.append(f'<rect x="{x0}" y="{y0}" width="{box_w}" height="{box_h}" fill="none" stroke="{outline}" stroke-width="2"/>')

    # Inside label
    parts.append(f'''
<text x="{x0+14}" y="{y0+int(inside_sz*1.2)}" text-anchor="start"
      font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial"
      font-size="{inside_sz}" font-weight="800" fill="{outline}">S</text>
<text x="{x0+34}" y="{y0+int(inside_sz*1.2)}" text-anchor="start"
      font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial"
      font-size="{inside_sz-1}" font-weight="600" fill="{outline}">partitioned into Bᵢ</text>
'''.strip())

    rng = random.Random(jitter_seed)

    x = x0
    for i, (pb, pab) in enumerate(zip(p_B, p_A_given_B), start=1):
        w = box_w * pb
        h_mag = min(box_h, box_h * pab * magnify)
        contrib = pb * pab
        cx = x + w/2

        if i == 1:
            lab = "B₁"
        elif i == n:
            lab = "Bₙ"
        else:
            lab = f"B{i}"

        # strip
        parts.append(
            f'<rect x="{x:.2f}" y="{y0}" width="{w:.2f}" height="{box_h}" '
            f'fill="{strip_fill}" stroke="{outline}" stroke-width="1"/>'
        )

        # shaded piece y-position (jittered)
        if jitter:
            max_top = y0
            max_bottom = y1 - h_mag
            y_shade = rng.uniform(max_top, max_bottom) if max_bottom > max_top else (y1 - h_mag)
        else:
            y_shade = y1 - h_mag

        parts.append(
            f'<rect x="{x:.2f}" y="{y_shade:.2f}" width="{w:.2f}" height="{h_mag:.2f}" '
            f'fill="{shade_fill}" fill-opacity="0.18" stroke="{shade_stroke}" stroke-width="1"/>'
        )

        # top labels (now safely below header)
        parts.append(
            f'<text x="{cx:.2f}" y="{y_B}" text-anchor="middle" '
            f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
            f'font-size="{B_sz}" font-weight="800" fill="{outline}">{lab}</text>'
        )
        parts.append(
            f'<text x="{cx:.2f}" y="{y_PB}" text-anchor="middle" '
            f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
            f'font-size="{num_sz}" fill="{outline}">P({lab})={fmt(pb)}</text>'
        )

        # bottom two lines with your requested bigger spacing
        parts.append(
            f'<text x="{cx:.2f}" y="{y_bottom1}" text-anchor="middle" '
            f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
            f'font-size="{num_sz}" fill="{shade_stroke}">P(A|{lab})={fmt(pab)}</text>'
        )
        parts.append(
            f'<text x="{cx:.2f}" y="{y_bottom2}" text-anchor="middle" '
            f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
            f'font-size="{num_sz}" fill="{outline}">P(A∩{lab})={fmt(contrib)}</text>'
        )

        x += w

    # Center red explanation
    center_x = x0 + box_w/2
    center_y = y0 + box_h/2
    parts.append(
        f'<text x="{center_x:.2f}" y="{center_y-10:.2f}" text-anchor="middle" '
        f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
        f'font-size="{center1}" font-weight="900" fill="{shade_stroke}">P(A) = total shaded area</text>'
    )
    parts.append(
        f'<text x="{center_x:.2f}" y="{center_y + dy(center2):.2f}" text-anchor="middle" '
        f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
        f'font-size="{center2}" font-weight="800" fill="{shade_stroke}">= Σᵢ P(A|Bᵢ)P(Bᵢ)</text>'
    )

    # Note for jitter placement (inside box, bottom-left)
    if jitter:
        parts.append(
            f'<text x="{x0+12}" y="{y1-12}" text-anchor="start" '
            f'font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial" '
            f'font-size="{num_sz}" fill="{outline}">'
            f'Note: vertical placement of shaded pieces is arbitrary — only the areas matter.</text>'
        )

    parts.append("</svg>")
    Path(filename).write_text("\n".join(parts), encoding="utf-8")
    return filename

# Your call (works now without overlaps even at huge spacing):
save_total_probability_svg(
    "total-probability-area.svg",
    n=6,
    magnify=8.0,
    jitter=True,
    line_gap=2.0,
    font_scale=2.0
)
```

```{figure} total-probability-area.svg
---
width: 100%
figclass: full-width
---
مدل مساحتی: $P(A)$ مجموع قطعات ناسازگار $A\cap B_i$ است.
````

### ۳.۵ شهود بصری: درخت احتمال (همان ایده، نمای دیگر)

نمودار درختی همان منطق را نشان می‌دهد: ابتدا مشخص می‌کنیم کدام سناریو $B_i$ رخ می‌دهد، سپس (درون آن سناریو) آیا $A$ رخ می‌دهد یا نه. (برای جزئیات بیشتر درباره نمودارهای درختی به [بخش ۴](tree-diagrams) مراجعه کنید.)

```{mermaid}
graph TD
    S((Start))
    
    S --> B1["B1: P_B1"]
    S --> Bd["... (B2..B(n-1))"]
    S --> Bn["Bn: P_Bn"]
    
    B1 --> A1["A: P_A_given_B1"]
    B1 --> NA1["not A: 1 - P_A_given_B1"]
    
    Bn --> An["A: P_A_given_Bn"]
    Bn --> NAn["not A: 1 - P_A_given_Bn"]
```


در شاخه $S \to B_i \to A$، احتمال حاصل‌ضرب $P(B_i),P(A\mid B_i)$ است. جمع برگ‌های «$A$» روی همه سناریوها، $P(A)$ را می‌دهد.

:::{admonition} مثال
:class: tip dropdown

**دو خط تولید**

یک کارخانه قطعات را روی دو خط تولید می‌سازد:

- $A$ را واقعه *«قطعه معیوب باشد»* در نظر بگیرید.
- $B_1$ را واقعه *«قطعه از خط ۱ آمده باشد»* در نظر بگیرید.
- $B_2$ را واقعه *«قطعه از خط ۲ آمده باشد»* در نظر بگیرید.

فرض کنید:

* $P(B_1)=0.6$، $P(B_2)=0.4$
* $P(A\mid B_1)=0.02$ (۲٪ معیوب در خط ۱)
* $P(A\mid B_2)=0.05$ (۵٪ معیوب در خط ۲)

آنگاه:

$$
\begin{align*}
P(A) &= P(A\mid B_1)P(B_1)+P(A\mid B_2)P(B_2) \\
     &= 0.02\cdot 0.6 + 0.05\cdot 0.4 \\
     &= 0.012 + 0.020 \\
     &= 0.032.
\end{align*}
$$

پس در مجموع حدود **۳.۲٪** از همه قطعات معیوبند.

:::

+++

## ۴. نمودارهای درختی

نمودارهای درختی ابزار بصری مفیدی برای مسائل شامل دنباله‌ای از واقعه‌ها هستند، به‌ویژه وقتی احتمال‌های شرطی در میان باشند.

* هر شاخه یک واقعه را نشان می‌دهد.
* احتمال هر واقعه روی شاخه نوشته می‌شود.
* شاخه‌هایی که از یک نقطه منشأ می‌گیرند، پیامدهای ناسازگار یک مرحله را نشان می‌دهند و احتمال‌هایشان باید جمعشان ۱ شود.
* احتمال رسیدن به یک نقطه پایانی مشخص (یک دنباله از واقعه‌ها) با ضرب احتمال‌ها در امتداد مسیر منتهی به آن نقطه پایانی (با استفاده از قانون ضرب) به‌دست می‌آید.
* احتمال واقعه‌ای که می‌تواند از چند مسیر رخ دهد، با جمع احتمال آن مسیرها به‌دست می‌آید (مرتبط با قانون احتمال کل).

### ۴.۱. ساختار کلی درخت

قبل از دیدن یک مثال خاص، الگوی کلی را ببینیم. فرض کنید پارتیشن $B_1, B_2, \ldots, B_n$ از فضای نمونه داریم و می‌خواهیم بدانیم آیا واقعه $A$ رخ می‌دهد یا نه. نمودار درختی زیر نشان می‌دهد چگونه ابتدا «انتخاب» می‌کنیم کدام سناریو $B_i$ رخ دهد، سپس (درون آن سناریو) آیا $A$ رخ می‌دهد یا نه.

```{mermaid}
graph TD
    Start((Start))

    Start -- "P(B₁)" --> B1["B₁"]
    Start -- "P(B₂)" --> B2["B₂"]
    Start -- "..." --> Bd["..."]
    Start -- "P(Bₙ)" --> Bn["Bₙ"]

    B1 -- "P(A|B₁)" --> A1["A"]
    B1 -- "P(A̅|B₁)" --> NA1["A̅ (not A)"]

    B2 -- "P(A|B₂)" --> A2["A"]
    B2 -- "P(A̅|B₂)" --> NA2["A̅"]

    Bn -- "P(A|Bₙ)" --> An["A"]
    Bn -- "P(A̅|Bₙ)" --> NAn["A̅"]
```

**خواندن درخت:**
* سطح اول پارتیشن را نشان می‌دهد: دقیقاً یکی از $B_1, B_2, \ldots, B_n$ رخ می‌دهد.
* هر شاخه سطح دوم نشان می‌دهد آیا $A$ (یا عدم $A$) با فرض آن سناریوی خاص رخ می‌دهد یا نه.
* احتمال هر مسیر کامل حاصل‌ضرب احتمال‌ها در امتداد آن مسیر است. مثلاً مسیر Start → $B_1$ → $A$ احتمال $P(B_1) \times P(A|B_1) = P(A \cap B_1)$ دارد.
* برای یافتن $P(A)$، احتمال همه مسیرهایی که به $A$ ختم می‌شوند را جمع می‌کنیم:

$$
P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \cdots + P(A|B_n)P(B_n)
$$

این دقیقاً همان **قانون احتمال کل** بخش ۳ است، فقط به‌صورت درخت به‌جای مدل مساحتی.

:::{admonition} مثال
:class: tip dropdown
مصورسازی احتمال پیامدها در دنباله‌ای از دو پرتاب احتمالاً نامتقارن سکه.
فرض کنید سکه‌ای داریم که $P(\text{Heads}) = 0.6$ و $P(\text{Tails}) = 0.4$. آن را دو بار می‌اندازیم. پیامدها مستقلند.

```{mermaid}
graph TD
    Start((Start))
    
    Start -- 0.6 --> H1(H)
    Start -- 0.4 --> T1(T)
    
    H1 -- 0.6 --> H2(H)
    H1 -- 0.4 --> T2(T)
    
    T1 -- 0.6 --> H3(H)
    T1 -- 0.4 --> T3(T)
    
    subgraph Flip 1
    H1
    T1
    end
    
    subgraph Flip 2
    H2
    T2
    H3
    T3
    end
```

* **مسیر ۱ (HH):** 

$$
\begin{align*}
P(H_1 \cap H_2) &= P(H_1) \times P(H_2 | H_1) \\
&= 0.6 \times 0.6 \\
&= 0.36
\end{align*}
$$
$$
\text{(Since flips are independent, } P(H_2|H_1) = P(H_2) = 0.6 \text{)}
$$

* **مسیر ۲ (HT):** $P(\text{H on 1st} \cap \text{T on 2nd}) = 0.6 \times 0.4 = 0.24$.
* **مسیر ۳ (TH):** $P(\text{T on 1st} \cap \text{H on 2nd}) = 0.4 \times 0.6 = 0.24$.
* **مسیر ۴ (TT):** $P(\text{T on 1st} \cap \text{T on 2nd}) = 0.4 \times 0.4 = 0.16$.

توجه کنید احتمال همه پیامدهای ممکن جمعشان ۱ می‌شود: $0.36 + 0.24 + 0.24 + 0.16 = 1.0$.

می‌توانیم از این برای یافتن احتمال واقعه‌های ترکیبی استفاده کنیم، مثلاً

$$
\begin{align*}
P(\text{Exactly one Head}) &= P(HT) + P(TH) \\
&= 0.24 + 0.24 \\
&= 0.48
\end{align*}
$$

:::

+++

## ۵. نکاتی برای تمایز $P(A \cap B)$ و $P(A | B)$

تمایز $P(A \cap B)$ و $P(A | B)$ در مسائل احتمال می‌تواند دشوار باشد.

**$P(A \cap B)$** **احتمال وقوع هم‌زمان واقعه A و واقعه B** را نشان می‌دهد. به کلیدواژه‌هایی مثل «**و**»، «**هر دو**» یا عباراتی که هم‌پوشانی مستقیم دو ویژگی را نشان می‌دهند توجه کنید. مثلاً «احتمال اینکه یک دانشجو هم رشته مهندسی باشد **و** هم زن باشد».

**$P(A | B)$** **احتمال وقوع واقعه A با فرض اینکه واقعه B از قبل رخ داده است** را نشان می‌دهد. این یک **احتمال شرطی** است که روی زیرمجموعه‌ای از جامعه تمرکز می‌کند. عباراتی مثل «**با فرض اینکه**»، «**از میان کسانی که**» یا «**اگر یک [ویژگی B] انتخاب شود**» نشانه‌های قوی هستند. مثلاً «از دانشجویانی که مهندسی می‌خوانند، ۲۰٪ زن هستند» نمونه‌ای از $P(\text{Female} | \text{Engineering})$ است.

تمایز کلیدی در این است که آیا مسئله احتمال وقوع هم‌زمان دو واقعه (اشتراک) را توصیف می‌کند یا احتمال وقوع یک واقعه *تحت شرط* رخ دادن واقعه دیگر (شرطی).

+++

## خلاصه فصل

### نکات کلیدی

**بینش اصلی:** احتمال شرطی $P(A|B)$ باور به‌روزشده ما درباره واقعه $A$ را با فرض اینکه واقعه $B$ رخ داده است نشان می‌دهد. فضای نمونه را فقط به پیامدهایی که $B$ در آن‌ها درست است محدود می‌کند.

**مفاهیم بنیادی:**

1. **احتمال شرطی** $P(A|B) = \frac{P(A \cap B)}{P(B)}$، به‌شرط $P(B) > 0$
   - احتمال $A$ را **با فرض** وقوع $B$ نشان می‌دهد
   - فضای نمونه را از $S$ به فقط پیامدهای $B$ محدود می‌کند
   - **تمایز کلیدی:** $P(A|B) \neq P(A \cap B)$ — شرطی‌سازی در برابر اشتراک!

2. **قانون ضرب:** $P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$
   - بنیادی برای محاسبه احتمال‌های مشترک
   - برای چند واقعه زنجیره‌ای می‌شود: $P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)$

3. **قانون احتمال کل:** اگر $B_1, B_2, \ldots, B_n$ فضای نمونه را پارتیشن کنند، آنگاه:
   $$P(A) = \sum_{i=1}^n P(A|B_i) \cdot P(B_i)$$
   - احتمال پیچیده را به قطعات شرطی ساده‌تر می‌شکند
   - برای سناریوها با مسیرها یا مراحل متعدد ضروری است
   - پایه قضیه بیز (فصل بعد)

4. **نمودارهای درختی:** ابزار بصری برای سازمان‌دهی احتمال‌های پیاپی یا مرحله‌ای
   - شاخه‌ها احتمال‌های شرطی را نشان می‌دهند
   - احتمال مسیرها در امتداد شاخه‌ها ضرب می‌شود
   - احتمال پیامد نهایی با جمع مسیرهای مربوط به‌دست می‌آید

### چرا این مهم است

احتمال شرطی بنیادی است برای:

- **تشخیص پزشکی:** $P(\text{disease}|\text{positive test})$ در برابر $P(\text{positive test}|\text{disease})$
- **یادگیری ماشین:** آموزش مدل‌ها با یادگیری $P(\text{label}|\text{features})$
- **ارزیابی ریسک:** به‌روزرسانی احتمال‌ها بر اساس اطلاعات یا شواهد جدید
- **تصمیم‌گیری:** چگونه داده‌های جدید باید باورها و اقدامات ما را تغییر دهند
- **استدلال علمی:** آزمون فرضیه و استنتاج بیزی

### خطاهای رایج که باید از آن‌ها پرهیز کرد

1. **اشتباه گرفتن $P(A|B)$ با $P(A \cap B)$:**
   - $P(A|B)$ یک نسبت است: «از دفعاتی که B رخ می‌دهد، چند بار A هم رخ می‌دهد؟»
   - $P(A \cap B)$ مطلق است: «چند بار هر دو A و B رخ می‌دهند؟»
   - بررسی بصری: $P(A|B)$ از $B$ به‌عنوان «کل» استفاده می‌کند، $P(A \cap B)$ از کل فضای نمونه $S$

2. **معکوس کردن شرط (مغالطه دادستان):**
   - $P(A|B) \neq P(B|A)$ به‌طور کلی!
   - مثال: $P(\text{positive test}|\text{disease}) \neq P(\text{disease}|\text{positive test})$
   - برای معکوس کردن شرط به قضیه بیز نیاز داریم (فصل ۵)

3. **فراموش کردن پارتیشن کامل:**
   - برای قانون احتمال کل، واقعه‌های $B_i$ باید دو به دو ناسازگار و فراگیر باشند
   - از دست دادن یک عنصر پارتیشن به مجموع‌های نادرست منجر می‌شود

4. **برداشت نادرست نمودارهای درختی:**
   - شاخه‌ها احتمال‌های شرطی را نشان می‌دهند، نه احتمال‌های مشترک
   - در امتداد مسیر ضرب کنید، روی مسیرها جمع کنید

### یادگیرهای بصری

**احتمال شرطی:** روی ناحیه $B$ بزرگ‌نمایی کنید، ببینید چه کسری از آن در $A$ هم هست

**قانون ضرب:** احتمال مسیر = حاصل‌ضرب گام‌های شرطی در امتداد مسیر

**قانون احتمال کل:** میانگین وزنی روی همه «مسیرهای» ممکن به $A$

### گام‌های بعدی

در فصل ۵، بر احتمال شرطی بنا می‌گذاریم و این موارد را بررسی می‌کنیم:
- **قضیه بیز:** معکوس کردن احتمال‌های شرطی
- **استقلال:** وقتی شرطی‌سازی احتمال‌ها را تغییر نمی‌دهد
- **استقلال شرطی:** استقلال درون زمینه‌ها

+++

## تمرین‌ها

1.  **دو تاس:** اگر دو تاس منصفانه شش‌وجهی بینندازید، احتمال شرطی اینکه مجموع ۸ باشد با فرض اینکه تاس اول ۳ نشان دهد چقدر است؟ احتمال شرطی اینکه تاس اول ۳ نشان دهد با فرض اینکه مجموع ۸ باشد چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    D1 را نتیجه تاس اول و D2 را نتیجه تاس دوم در نظر بگیرید. تعداد کل پیامدهای ممکن هنگام انداختن دو تاس منصفانه شش‌وجهی $6 \times 6 = 36$ است. هر پیامد (D1, D2) به‌طور یکسان محتمل است.

    **بخش ۱: احتمال شرطی اینکه مجموع ۸ باشد با فرض اینکه تاس اول ۳ نشان دهد.**
    A را واقعه «مجموع ۸ باشد» و B را واقعه «تاس اول ۳ نشان دهد» در نظر بگیرید.
    می‌خواهیم $P(A | B)$ را بیابیم.

    پیامدهای واقعه B (تاس اول ۳ است):
    {(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)}. ۶ پیامد از این نوع وجود دارد.
    با فرض اینکه تاس اول ۳ است، برای اینکه مجموع ۸ شود، تاس دوم (D2) باید $8 - 3 = 5$ باشد.
    پس تنها پیامدی که تاس اول ۳ و مجموع ۸ است، (3,5) است.
    بنابراین در فضای نمونه کاهش‌یافته‌ای که تاس اول ۳ است، ۱ پیامد وجود دارد که مجموع ۸ می‌شود.
    پس $P(\text{Sum}=8 | \text{First die}=3) = 1/6$.

    به‌طور جایگزین، با استفاده از فرمول $P(A | B) = P(A \cap B) / P(B)$:
    $P(B) = 6/36 = 1/6$.
    $P(A \cap B)$ (مجموع ۸ و تاس اول ۳) متناظر با پیامد (3,5) است، پس $P(A \cap B) = 1/36$.
    $P(A | B) = (1/36) / (6/36) = 1/6$.

    **بخش ۲: احتمال شرطی اینکه تاس اول ۳ نشان دهد با فرض اینکه مجموع ۸ باشد.**
    A را واقعه «مجموع ۸ باشد» و B را واقعه «تاس اول ۳ نشان دهد» در نظر بگیرید.
    می‌خواهیم $P(B | A)$ را بیابیم.

    پیامدهای واقعه A (مجموع ۸):
    {(2,6), (3,5), (4,4), (5,3), (6,2)}. ۵ پیامد از این نوع وجود دارد.
    با فرض اینکه مجموع ۸ است، به دنبال پیامدهایی می‌گردیم که تاس اول ۳ باشد. تنها پیامد (3,5) است.
    بنابراین در فضای نمونه کاهش‌یافته‌ای که مجموع ۸ است، ۱ پیامد وجود دارد که تاس اول ۳ است.
    پس $P(\text{First die}=3 | \text{Sum}=8) = 1/5$.

    به‌طور جایگزین، با استفاده از فرمول $P(B | A) = P(B \cap A) / P(A)$:
    $P(A) = 5/36$.
    $P(B \cap A)$ (تاس اول ۳ و مجموع ۸) متناظر با پیامد (3,5) است، پس $P(B \cap A) = 1/36$.
    $P(B | A) = (1/36) / (5/36) = 1/5$.
    ```

2.  **آزمون پزشکی:** بیماری ۱ از هر ۱۰۰۰ نفر را تحت تأثیر قرار می‌دهد. آزمونی برای بیماری ۹۹٪ دقیق است (یعنی P(Positive | Disease) = 0.99) و نرخ مثبت کاذب ۲٪ دارد (یعنی P(Positive | No Disease) = 0.02). از قانون احتمال کل برای محاسبه احتمال کلی اینکه یک فرد تصادفی نتیجه مثبت بگیرد استفاده کنید. (در فصل قضیه بیز دوباره به این موضوع برمی‌گردیم).

    ```{admonition} پاسخ
    :class: dropdown

    D را واقعه «فرد بیمار باشد» و $\neg D$ را واقعه «فرد بیمار نباشد» در نظر بگیرید.
    + را واقعه «فرد نتیجه مثبت بگیرد» در نظر بگیرید.

    داده شده:
    * $P(D) = 1/1000 = 0.001$
    * $P(\text{Positive} | D) = P(+|D) = 0.99$ (دقت آزمون برای بیماران)
    * $P(\text{Positive} | \neg D) = P(+|\neg D) = 0.02$ (نرخ مثبت کاذب)

    از $P(D)$ می‌توانیم $P(\neg D)$ را بیابیم:
    * $P(\neg D) = 1 - P(D) = 1 - 0.001 = 0.999$

    باید احتمال کلی اینکه یک فرد تصادفی نتیجه مثبت بگیرد، یعنی $P(+)$ را محاسبه کنیم. از قانون احتمال کل استفاده می‌کنیم:
    $P(+) = P(+|D) \cdot P(D) + P(+|\neg D) \cdot P(\neg D)$
    $P(+) = (0.99 \cdot 0.001) + (0.02 \cdot 0.999)$
    $P(+) = 0.00099 + 0.01998$
    $P(+) = 0.02097$

    پس احتمال کلی اینکه یک فرد تصادفی نتیجه مثبت بگیرد 0.02097 است، یعنی حدود 2.097٪.
    ```

3.  **دو کارت — رتبه یکسان:** دو کارت از یک دسته استاندارد ۵۲ کارتی **بدون بازگرداندن** بکشید. احتمال اینکه دو کارت **رتبه یکسان** داشته باشند (مثلاً دو ۷ یا دو شاه) چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    $M$ را واقعه «دو کارت رتبه یکسان داشته باشند» در نظر بگیرید.

    **رویکرد احتمال شرطی (مطابق راهنما):**
    - کارت اول می‌تواند هر چیزی باشد؛ پس از کشیدن آن، رتبه‌اش ثابت می‌شود.
    - در یک دسته ۵۲ کارتی، از هر رتبه ۴ کارت وجود دارد.
    - پس از کشیدن کارت اول، **۳** کارت از همان رتبه باقی مانده است.
    - در مجموع **۵۱** کارت باقی مانده است.

    پس،

    $$
    P(M)=P(\text{2nd card has same rank as 1st}\mid \text{1st card drawn}).
    $$

    تعریف احتمال شرطی را به‌خاطر بیاورید:

    $$
    P(A\mid B)=\frac{P(A\cap B)}{P(B)} \quad (P(B)>0).
    $$

    برای ملموس‌تر شدن، $B$ را واقعه «کارت اول آس باشد» و $C$ را واقعه «کارت دوم آس باشد» در نظر بگیرید.
    آنگاه $C\cap B$ واقعه «دو کارت اول هر دو آس باشند» است.

    داریم:
    - $P(B)=\frac{4}{52}=\frac{1}{13}$.
    - $P(C\cap B)=\frac{4}{52}\cdot\frac{3}{51}$.

    پس،

    $$
    P(C\mid B)=\frac{P(C\cap B)}{P(B)}
    =\frac{\frac{4}{52}\cdot\frac{3}{51}}{\frac{4}{52}}
    =\frac{3}{51}
    =\frac{1}{17}\approx 0.0588.
    $$

    به‌دلیل تقارن (همان محاسبه برای هر رتبه درست است)، این برابر $P(M)$ است.

    **(بررسی اختیاری با شمارش)**
    - کل دست‌های ۲ کارتی: $\binom{52}{2}$.
    - دست‌های مطلوب: انتخاب رتبه (۱۳ روش)، سپس انتخاب ۲ خال از ۴: $13\binom{4}{2}$.

    $$
    P(M)=\frac{13\binom{4}{2}}{\binom{52}{2}}
    =\frac{13\cdot 6}{1326}
    =\frac{1}{17}.
    $$


    ```

4.  **انتخاب سکه — احتمال کل:** کیفی **دو سکه منصفانه** و **یک سکه نامتقارن** دارد.
    - اگر سکه منصفانه باشد، \(P(H)=0.5\).
    - اگر سکه نامتقارن باشد، \(P(H)=0.8\).
    شما **یک** سکه را به‌طور تصادفی از کیف برمی‌دارید و **دو بار** می‌اندازید. احتمال **دقیقاً یک شیر** چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید:
    - \(A\) واقعه «دقیقاً یک شیر در دو پرتاب» باشد.
    - \(B_1\) «سکه منصفانه انتخاب شده باشد».
    - \(B_2\) «سکه نامتقارن انتخاب شده باشد».

    این‌ها یک پارتیشن می‌سازند: یا سکه منصفانه یا نامتقارن انتخاب می‌شود.

    **گام ۱ — احتمال سناریوها**
    ۳ سکه در مجموع، ۲ تا منصفانه:

    $$
    P(B_1)=\frac{2}{3}, \qquad P(B_2)=\frac{1}{3}.
    $$

    **گام ۲ — محاسبه احتمال‌های شرطی**
    - با فرض سکه منصفانه، دقیقاً یک شیر می‌تواند HT یا TH باشد:

      $$
      P(A\mid B_1)=P(HT)+P(TH)=(0.5)(0.5)+(0.5)(0.5)=0.5.
      $$

    - با فرض سکه نامتقارن، $P(H)=0.8$ و $P(T)=0.2$:

      $$
      P(A\mid B_2)=P(HT)+P(TH)=(0.8)(0.2)+(0.2)(0.8)=0.32.
      $$

    **گام ۳ — به‌کارگیری قانون احتمال کل**

    $$
    P(A)=P(A\mid B_1)P(B_1)+P(A\mid B_2)P(B_2)
        =(0.5)\left(\frac{2}{3}\right)+(0.32)\left(\frac{1}{3}\right).
    $$

    محاسبه:
    $$
    (0.5)\left(\frac{2}{3}\right)=\frac{1}{3}, \qquad
    (0.32)\left(\frac{1}{3}\right)=\frac{0.32}{3}=\frac{8}{75}.
    $$

    پس،

    $$
    P(A)=\frac{1}{3}+\frac{8}{75}=\frac{25}{75}+\frac{8}{75}=\frac{33}{75}=\frac{11}{25}=0.44.
    $$

    **پاسخ:** $P(\text{exactly one Head})=\frac{11}{25}=0.44$.
    ```
