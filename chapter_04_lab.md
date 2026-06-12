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
  - file: notebooks/chapter_04_lab.ipynb
---


# فصل ۴: احتمال شرطی

بیایید با پایتون مفاهیم احتمال شرطی را کاوش کنیم. به کتابخانه‌هایی مانند `numpy` برای عملیات عددی و نمونه‌گیری تصادفی و احتمالاً `pandas` برای کار با داده نیاز داریم.

```{code-cell} ipython3
import numpy as np
import pandas as pd
import random
```

### شبیه‌سازی رویدادهای شرطی: کشیدن کارت

بیایید کشیدن دو کارت از یک دست ۵۲ کارتی استاندارد *بدون جایگزینی* را شبیه‌سازی کنیم و احتمال شرطی $P(\text{2nd is King} | \text{1st is King})$ را تأیید کنیم. انتظار داریم $3/51$ باشد.

```{admonition} توضیح
:class: dropdown
**احتمال شرطی: $P(\text{2nd is King} | \text{1st is King}) = 3/51$**

تصور کنید یک کارت کشیده‌اید و شاه است. چون *بدون جایگزینی* می‌کشیم، آن شاه دیگر در دست نیست.

* **کارت‌های باقی‌مانده:** پس از کشیدن یک شاه، اکنون $52 - 1 = 51$ کارت در دست باقی مانده است.
* **شاه‌های باقی‌مانده:** چون یک شاه برداشته شده، اکنون $4 - 1 = 3$ شاه باقی مانده است.

بنابراین احتمال اینکه کارت دوم شاه باشد، *با فرض* اینکه کارت اول شاه بود، تعداد شاه‌های باقی‌مانده تقسیم بر کل کارت‌های باقی‌مانده است، یعنی $\frac{3}{51}$.
```

همچنین می‌توانیم احتمال کل $P(\text{2nd is King})$ را برآورد کنیم. با تقارن یا قانون احتمال کل، این باید $4/52$ باشد.

```{admonition} توضیح
:class: dropdown
**احتمال کل: $P(\text{2nd is King}) = 4/52$**

اکنون به احتمال شاه بودن کارت دوم بدون دانستن چیزی دربارهٔ کارت اول فکر کنیم. چند راه برای دیدن اینکه چرا $4/52$ است وجود دارد:

1.  **تقارن:** هر یک از ۵۲ کارت دست را در نظر بگیرید. هر کارت شانس برابر دارد در موقعیت دوم قرار گیرد. چون ۴ شاه در دست هست، احتمال شاه بودن کارت در موقعیت دوم باید با احتمال شاه بودن کارت در موقعیت اول، یعنی $\frac{4}{52}$، یکسان باشد.

2.  **قانون احتمال کل (ضمنی):** می‌توانیم دو حالت ممکن برای کارت اول را در نظر بگیریم:

    * **حالت ۱: کارت اول شاه است.** احتمال این $P(\text{1st is King}) = \frac{4}{52}$ است. در این حالت، احتمال شاه بودن کارت دوم $P(\text{2nd is King} | \text{1st is King}) = \frac{3}{51}$ است.
    * **حالت ۲: کارت اول شاه نیست.** احتمال این $P(\text{1st is not King}) = \frac{48}{52}$ است. در این حالت، هنوز ۴ شاه در ۵۱ کارت باقی‌مانده هست، پس احتمال شاه بودن کارت دوم $P(\text{2nd is King} | \text{1st is not King}) = \frac{4}{51}$ است.

    با استفاده از قانون احتمال کل:


    $$
    \begin{aligned}
    P(\text{2nd King}) &= P(\text{2nd King} | \text{1st King})P(\text{1st King}) \\
    &\quad + P(\text{2nd King} | \text{1st Not King})P(\text{1st Not King})
    \end{aligned}
    $$

    $$
    \begin{aligned}
    P(\text{2nd King}) &= \left(\frac{3}{51}\right)\left(\frac{4}{52}\right) + \left(\frac{4}{51}\right)\left(\frac{48}{52}\right) \\
    &= \frac{12 + 192}{51 \times 52} \\
    &= \frac{204}{2652} \\
    &= \frac{4}{52}
    \end{aligned}
    $$
```

پس هم شهود ما و هم کاربرد رسمی‌تر قواعد احتمال این نتایج را تأیید می‌کنند! اکنون آمادهٔ شبیه‌سازی هستید؟

```{code-cell} ipython3
# Represent the deck
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S'] # Hearts, Diamonds, Clubs, Spades
deck = [rank + suit for rank in ranks for suit in suits]
kings = {'KH', 'KD', 'KC', 'KS'}
```

```{code-cell} ipython3
# Simulation parameters
num_simulations = 100000
```

```{code-cell} ipython3
# Counters
count_first_king = 0
count_second_king = 0
count_both_king = 0
count_second_king_given_first_king = 0
```

```{code-cell} ipython3
# Run simulations
for _ in range(num_simulations):
    # Shuffle the deck implicitly by drawing random samples
    drawn_cards = random.sample(deck, 2)
    card1 = drawn_cards[0]
    card2 = drawn_cards[1]

    # Check conditions
    is_first_king = card1 in kings
    is_second_king = card2 in kings

    if is_first_king:
        count_first_king += 1
        if is_second_king:
            count_second_king_given_first_king += 1

    if is_second_king:
        count_second_king += 1

    if is_first_king and is_second_king:
        count_both_king += 1
```

```{code-cell} ipython3
# Calculate probabilities from simulation
prob_first_king_sim = count_first_king / num_simulations
prob_second_king_sim = count_second_king / num_simulations
prob_both_king_sim = count_both_king / num_simulations
```

```{code-cell} ipython3
# Calculate conditional probability P(B|A) = P(A and B) / P(A)
# We can estimate this directly from the counts:
if count_first_king > 0:
    prob_second_given_first_sim = count_second_king_given_first_king / count_first_king
else:
    prob_second_given_first_sim = 0
```

```{code-cell} ipython3
# Theoretical values
prob_first_king_theory = 4/52
prob_second_king_theory = 4/52 # By symmetry
prob_both_king_theory = (4/52) * (3/51)
prob_second_given_first_theory = 3/51
```

```{code-cell} ipython3
# Print results
print(f"--- Theoretical Probabilities ---")
print(f"P(1st is King): {prob_first_king_theory:.6f} ({4}/{52})")
print(f"P(2nd is King): {prob_second_king_theory:.6f} ({4}/{52})")
print(f"P(Both Kings): {prob_both_king_theory:.6f}")
print(f"P(2nd is King | 1st is King): {prob_second_given_first_theory:.6f} ({3}/{51})")
print("\n")
print(f"--- Simulation Results ({num_simulations} runs) ---")
print(f"Estimated P(1st is King): {prob_first_king_sim:.6f}")
print(f"Estimated P(2nd is King): {prob_second_king_sim:.6f}")
print(f"Estimated P(Both Kings): {prob_both_king_sim:.6f}")
print(f"Estimated P(2nd is King | 1st is King): {prob_second_given_first_sim:.6f}")
```

نتایج شبیه‌سازی باید به مقادیر نظری بسیار نزدیک باشند و نشان دهند شبیه‌سازی چگونه می‌تواند محاسبات احتمالی را تقریب بزند. هرچه `num_simulations` بزرگ‌تر باشد، برآوردها معمولاً نزدیک‌ترند.

+++

### محاسبهٔ احتمال‌های شرطی از روی داده

تصور کنید داده‌ای دربارهٔ بازدیدکنندگان وب‌سایت داریم، از جمله اینکه خرید کرده‌اند یا نه و آیا ابتدا صفحهٔ محصول خاصی را دیده‌اند. می‌توانیم با Pandas احتمال‌های شرطی را از این داده محاسبه کنیم.

+++

#### دادهٔ نمونه

یک DataFrame با دادهٔ بازدیدکنندگان، شامل اینکه صفحهٔ محصول خاص را دیده‌اند و خرید کرده‌اند، ساخته می‌شود.

```{code-cell} ipython3
import pandas as pd

# Create sample data
data = {
    'visited_product_page': [True, False, True, True, False, False, True, True, False, True],
    'made_purchase':        [True, False, False, True, False, True, False, True, False, False]
}
df = pd.DataFrame(data)

print("Sample Visitor Data:")
display(df)
print("\n")
```

#### رویکرد ۱: احتمال شرطی محاسبه‌شده

+++

ابتدا احتمال‌های پایه را محاسبه کنید:

- **احتمال‌های پایه**: تعداد کل بازدیدکنندگان، کسانی که صفحهٔ محصول را دیده‌اند، کسانی که خرید کرده‌اند، و کسانی که هر دو را انجام داده‌اند محاسبه می‌شود. از این‌ها برای محاسبهٔ احتمال‌های پایه استفاده می‌شود:
  - $ P(\text{Visited Page}) $
  - $ P(\text{Purchased}) $
  - $ P(\text{Visited and Purchased}) $

```{code-cell} ipython3
# Calculate basic probabilities
n_total = len(df)
n_visited_page = df['visited_product_page'].sum()
n_purchased = df['made_purchase'].sum()
n_visited_and_purchased = len(df[(df['visited_product_page'] == True) & (df['made_purchase'] == True)])

P_visited = n_visited_page / n_total
P_purchased = n_purchased / n_total
P_visited_and_purchased = n_visited_and_purchased / n_total

print(f"P(Visited Page) = {P_visited:.2f}")
print(f"P(Purchased) = {P_purchased:.2f}")
print(f"P(Visited and Purchased) = {P_visited_and_purchased:.2f}")
print("\n")
```

سپس احتمال‌های شرطی را محاسبه کنید:

- **تعریف**: این رویکرد از قواعد بنیادین احتمال برای استخراج احتمال‌های شرطی استفاده می‌کند.
- **محاسبات**:
  - **$ P(\text{Purchased} \mid \text{Visited Page}) $**: با فرمول $ P(A \mid B) = \frac{P(A \cap B)}{P(B)} $ محاسبه می‌شود، که $ A $ «خرید کرده» و $ B $ «صفحه را دیده» است.
  - **$ P(\text{Visited Page} \mid \text{Purchased}) $**: به‌طور مشابه با همان قاعده محاسبه می‌شود.
- **مزیت**: وقتی $ P(A \cap B) $ و $ P(B) $ را دارید و می‌خواهید احتمال شرطی را بیابید مفید است. برای درک بنیادهای نظری احتمال شرطی نیز کمک‌کننده است.

```{code-cell} ipython3
# Calculate Conditional Probability: P(Purchase | Visited Page)
if P_visited > 0:
    P_purchased_given_visited = P_visited_and_purchased / P_visited
    print(f"Calculated P(Purchased | Visited Page) = {P_purchased_given_visited:.2f}")
else:
    print("Cannot calculate P(Purchased | Visited Page) as P(Visited Page) is 0.")

# Calculate Conditional Probability: P(Visited Page | Purchased)
if P_purchased > 0:
    P_visited_given_purchased = P_visited_and_purchased / P_purchased
    print(f"Calculated P(Visited Page | Purchased) = {P_visited_given_purchased:.2f}")
else:
    print("Cannot calculate P(Visited Page | Purchased) as P(Purchased) is 0.")
```

```{code-cell} ipython3
:tags: [remove-input]

# Visualization for Approach 1: Venn Diagram
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

plt.figure(figsize=(4, 3))

# Sizes: (Size of V only, Size of P only, Size of V & P)
venn_diagram = venn2(subsets=(round(P_visited - P_visited_and_purchased, 2),
                              round(P_purchased - P_visited_and_purchased, 2),
                              round(P_visited_and_purchased, 2)),
                     set_labels=('Visited Page (V)', 'Purchased (P)'))

if venn_diagram: # Check if venn_diagram was successfully created
    # Color coding the areas
    if venn_diagram.get_patch_by_id('10'): # V only
        venn_diagram.get_patch_by_id('10').set_alpha(0.5)
        venn_diagram.get_patch_by_id('10').set_color('skyblue')
    if venn_diagram.get_patch_by_id('01'): # P only
        venn_diagram.get_patch_by_id('01').set_alpha(0.5)
        venn_diagram.get_patch_by_id('01').set_color('lightgreen')
    if venn_diagram.get_patch_by_id('11'): # V and P
        venn_diagram.get_patch_by_id('11').set_alpha(0.8)
        venn_diagram.get_patch_by_id('11').set_color('dodgerblue')

    # Setting text and adjusting positions for each area
    label_10 = venn_diagram.get_label_by_id('10') # V only area
    if label_10:
      label_10.set_text(f'$P(V \\cap \\neg P) = {P_visited - P_visited_and_purchased:.2f}$')
      # Move label '10' to the left
      current_position_10 = label_10.get_position()
      x_offset_10 = -0.25 # Negative value to move left
      label_10.set_position((current_position_10[0] + x_offset_10, current_position_10[1]))

    label_01 = venn_diagram.get_label_by_id('01') # P only area
    if label_01:
      label_01.set_text(f'$P(\\neg V \\cap P) = {P_purchased - P_visited_and_purchased:.2f}$')
      current_position_01 = label_01.get_position()
      x_offset_01 = 0.25 # Positive value to move right
      label_01.set_position((current_position_01[0] + x_offset_01, current_position_01[1]))

    label_intersection = venn_diagram.get_label_by_id('11') # V and P intersection
    if label_intersection:
      label_intersection.set_text(f'$P(V \\cap P) = {P_visited_and_purchased:.2f}$')
      current_position_intersection = label_intersection.get_position()
      y_offset_intersection = 0.0 # Adjust this value to move the label higher
      label_intersection.set_position((current_position_intersection[0], current_position_intersection[1] + y_offset_intersection))

plt.suptitle('Approach 1: Venn Diagram of Probabilities')
plt.title(
          f'$P(Purchased | Visited Page) = P(V \\cap P) / P(V) = {P_visited_and_purchased:.2f} / {P_visited:.2f} = {P_purchased_given_visited:.2f}$\n'
          f'$P(Visited Page | Purchased) = P(V \\cap P) / P(P) = {P_visited_and_purchased:.2f} / {P_purchased:.2f} = {P_visited_given_purchased:.2f}$',
          fontsize=8, y=-0.45)
plt.show()
```

این نمودار ون به‌صورت بصری نشان می‌دهد احتمال‌های مختلف چگونه مرتبط‌اند:

* **پیامدهای مشخص:** مقادیر داخل هر بخش مجزای نمودار احتمال وقوع آن سناریوی خاص را نشان می‌دهند. مثلاً:
    * $P(V \cap \neg P)$ احتمال بازدیدکننده‌ای که «صفحه را دیده اما خرید نکرده» را نشان می‌دهد.
    * $P(V \cap P)$ احتمال بازدیدکننده‌ای که «صفحه را دیده *و* خرید کرده» را نشان می‌دهد.

* **احتمال کل رویداد:** احتمال کل یک رویداد (مثل «صفحه دیده شده»، نماد $P(V)$) با جمع احتمال همهٔ بخش‌های تشکیل‌دهندهٔ آن به‌دست می‌آید.
    * مثلاً $P(V) = P(V \cap \neg P) + P(V \cap P)$.

* **مؤلفه‌های احتمال شرطی:** این احتمال کل (مثلاً $P(V)$) همراه احتمال اشتراک (مثلاً $P(V \cap P)$) مقادیر ضروری فرمول احتمال شرطی‌اند.
    * مثلاً $P(\text{Purchased} | \text{Visited Page}) = P(V \cap P) / P(V)$.

* **مصورسازی فضای نمونه:** نمودار به‌خوبی نشان می‌دهد چگونه کل دایرهٔ رویداد شرط (مثلاً دایرهٔ «صفحه دیده شده»، نمایانگر $P(V)$) هنگام محاسبهٔ احتمال شرطی فضای نمونهٔ جدید و کوچک‌شده می‌شود.

+++

#### رویکرد ۲: احتمال شرطی مستقیم

- **تعریف**: این رویکرد داده را فیلتر می‌کند تا احتمال شرطی مستقیماً از زیرمجموعهٔ مرتبط محاسبه شود.
- **محاسبات**:
  - **$ P(\text{Purchased} \mid \text{Visited Page}) $**: DataFrame فقط به بازدیدکنندگانی که صفحه را دیده‌اند فیلتر می‌شود. سپس تعداد خریداران تقسیم بر کل کسانی که صفحه را دیده‌اند می‌شود.
  - **$ P(\text{Visited Page} \mid \text{Purchased}) $**: DataFrame فقط به خریداران فیلتر می‌شود. سپس تعداد کسانی که صفحه را دیده‌اند تقسیم بر کل خریداران می‌شود.
- **مزیت**: این روش مستقیم و شهودی است چون مستقیماً از زیرمجموعهٔ مرتبط داده استفاده می‌کند.

```{code-cell} ipython3
# Direct calculation from counts: P(Purchase | Visited Page)
df_visited = df[df['visited_product_page'] == True]
n_purchased_in_visited = df_visited['made_purchase'].sum()
n_visited = len(df_visited)

if n_visited > 0:
    P_purchased_given_visited_direct = n_purchased_in_visited / n_visited
    print(f"Direct P(Purchased | Visited Page) = {P_purchased_given_visited_direct:.2f} ({n_purchased_in_visited}/{n_visited})")
else:
    print("Cannot calculate P(Purchased | Visited Page) directly as no one visited the page.")

# Direct calculation from counts: P(Visited Page | Purchased)
df_purchased = df[df['made_purchase'] == True]
n_visited_in_purchased = df_purchased['visited_product_page'].sum()
n_purchased_total = len(df_purchased)

if n_purchased_total > 0:
    P_visited_given_purchased_direct = n_visited_in_purchased / n_purchased_total
    print(f"Direct P(Visited Page | Purchased) = {P_visited_given_purchased_direct:.2f} ({n_visited_in_purchased}/{n_purchased_total})")
else:
    print("Cannot calculate P(Visited Page | Purchased) directly as no one made a purchase.")
```

```{code-cell} ipython3
:tags: [remove-input]

import matplotlib.pyplot as plt
import pandas as pd # Added for completeness if you run this standalone with the sample data

# Conceptual Tree Diagram for Approach 2
fig_tree, ax_tree = plt.subplots(figsize=(14, 9)) # Increased size for better readability
ax_tree.set_xlim(0, 10)
ax_tree.set_ylim(0, 10)
ax_tree.axis('off')
ax_tree.text(5, 9.5, "Approach 2: Conceptual Tree Diagram Illustrating Filtering", ha='center', va='center', fontsize=14, weight='bold')

# --- Branch for P(Purchased | Visited Page) ---
ax_tree.text(2.5, 8.5, "$P(Purchased \ | \ Visited \ Page)$", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightblue', alpha=0.5))
# Root: All Visitors
ax_tree.text(2.5, 7.5, f"All Visitors\n(N={n_total})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="whitesmoke", ec="black"))
# Branch to Visited Page / Not Visited Page
ax_tree.plot([2.5, 1.5], [7.0, 6.0], 'k-')
ax_tree.plot([2.5, 3.5], [7.0, 6.0], 'k-')
ax_tree.text(1.5, 5.5, f"Visited Page (V)\n(N={n_visited_page})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen", ec="black", linewidth=2)) # Conditioned on this group
ax_tree.text(3.5, 5.5, f"Not Visited Page (¬V)\n(N={n_total - n_visited_page})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightcoral", ec="black"))

# From "Visited Page" (this is the group of size n_visited), branch to Purchased / Not Purchased
ax_tree.text(1.5, 4.8, f"Focus on this group (N={n_visited})", ha='center', va='center', fontsize=9, style='italic', color='darkgreen')
ax_tree.plot([1.5, 0.75], [5.0, 4.0], 'k-') # Line to Purchased
ax_tree.plot([1.5, 2.25], [5.0, 4.0], 'k-') # Line to Not Purchased
ax_tree.text(0.75, 3.5, f"Purchased (P)\n(N={n_purchased_in_visited})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="palegreen", ec="black"))
# Corrected variable: n_visited (length of df_visited)
ax_tree.text(2.25, 3.5, f"Not Purchased (¬P)\n(N={n_visited - n_purchased_in_visited})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightpink", ec="black"))
# Corrected variable: n_visited
ax_tree.text(1.5, 2.5, f"$P(P | V) = \\frac{{{n_purchased_in_visited}}}{{{n_visited}}} = {P_purchased_given_visited_direct:.2f}$", ha='center', va='center', fontsize=10, weight='bold', color='darkgreen')


# --- Branch for P(Visited Page | Purchased) ---
ax_tree.text(7.5, 8.5, "$P(Visited \ Page \ | \ Purchased)$", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightpink', alpha=0.5))
# Root: All Visitors
ax_tree.text(7.5, 7.5, f"All Visitors\n(N={n_total})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="whitesmoke", ec="black"))
# Branch to Purchased / Not Purchased
ax_tree.plot([7.5, 6.5], [7.0, 6.0], 'k-')
ax_tree.plot([7.5, 8.5], [7.0, 6.0], 'k-')
ax_tree.text(6.5, 5.5, f"Purchased (P)\n(N={n_purchased})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightgoldenrodyellow", ec="black", linewidth=2)) # Conditioned on this group
ax_tree.text(8.5, 5.5, f"Not Purchased (¬P)\n(N={n_total - n_purchased})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightgrey", ec="black"))

# From "Purchased" (this is the group of size n_purchased_total), branch to Visited Page / Not Visited Page
ax_tree.text(6.5, 4.8, f"Focus on this group (N={n_purchased_total})", ha='center', va='center', fontsize=9, style='italic', color='darkred')
ax_tree.plot([6.5, 5.75], [5.0, 4.0], 'k-') # Line to Visited Page
ax_tree.plot([6.5, 7.25], [5.0, 4.0], 'k-') # Line to Not Visited Page
ax_tree.text(5.75, 3.5, f"Visited Page (V)\n(N={n_visited_in_purchased})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="khaki", ec="black"))
# Corrected variable: n_purchased_total (length of df_purchased)
ax_tree.text(7.25, 3.5, f"Not Visited Page (¬V)\n(N={n_purchased_total - n_visited_in_purchased})", ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightgray", ec="black"))
# Corrected variable: n_purchased_total
ax_tree.text(6.5, 2.5, f"$P(V | P) = \\frac{{{n_visited_in_purchased}}}{{{n_purchased_total}}} = {P_visited_given_purchased_direct:.2f}$", ha='center', va='center', fontsize=10, weight='bold', color='darkred')

plt.tight_layout()
plt.show()
```

این نمودار درختی رویکرد مستقیم احتمال شرطی را با تقسیم‌بندی بصری جمعیت بازدیدکنندگان بر اساس توالی رویدادها یا شرایط نشان می‌دهد. برای یافتن $P(\text{Purchased} | \text{Visited Page})$، مثلاً ابتدا شاخهٔ «صفحه دیده شده» را دنبال می‌کنید و داده را فیلتر می‌کنید، سپس سهم کسانی که بعداً «خرید کرده‌اند» را می‌بینید. نمودار به‌وضوح نشان می‌دهد شرط اولیه چگونه تمرکز را به زیرگروه مشخص محدود می‌کند.

+++

#### خلاصه

- **رویکرد محاسباتی**: از قواعد احتمال برای استخراج احتمال شرطی از احتمال‌های شناخته‌شده استفاده می‌کند.
- **رویکرد مستقیم**: داده را به شرط فیلتر کرده و محاسبه را روی دادهٔ فیلترشده انجام می‌دهد.

هر دو رویکرد در صورت درست انجام شدن باید نتیجهٔ یکسان بدهند و انتخاب بین آن‌ها به زمینه و داده یا احتمال‌های در دسترس بستگی دارد.

+++

این مثال نشان می‌دهد چگونه احتمال شرطی را مستقیماً از دادهٔ مشاهده‌شده — کار رایج در تحلیل داده — محاسبه کنیم. $P(\text{Purchased} | \text{Visited Page})$ احتمال خرید *در میان کسانی که آن صفحه را دیده‌اند* را می‌گوید، در حالی که $P(\text{Visited Page} | \text{Purchased})$ احتمال اینکه کسی که *خرید کرده* قبلاً آن صفحه را دیده باشد. این‌ها می‌توانند بسیار متفاوت باشند!

+++

### کاربرد قانون احتمال کل

بیایید قانون احتمال کل را با مثال تولید به کار ببریم. فرض کنید کارخانه‌ای دو ماشین M1 و M2 برای تولید ویجت دارد.
* ماشین M1، ۶۰٪ ویجت‌ها را تولید می‌کند ($P(M1) = 0.6$).
* ماشین M2، ۴۰٪ ویجت‌ها را تولید می‌کند ($P(M2) = 0.4$).
* ۲٪ ویجت‌های M1 معیوب‌اند ($P(D|M1) = 0.02$).
* ۵٪ ویجت‌های M2 معیوب‌اند ($P(D|M2) = 0.05$).

احتمال کل اینکه ویجتی تصادفی معیوب باشد ($P(D)$) چقدر است؟

رویدادهای M1 (ویجت تولید M1) و M2 (ویجت تولید M2) تجزیه‌ای از فضای نمونه (همهٔ ویجت‌ها) می‌سازند. با قانون احتمال کل:

$P(D) = P(D|M1)P(M1) + P(D|M2)P(M2)$

```{code-cell} ipython3
# Define probabilities
P_M1 = 0.60
P_M2 = 0.40
P_D_given_M1 = 0.02
P_D_given_M2 = 0.05
```

```{code-cell} ipython3
# Apply Law of Total Probability
P_D = (P_D_given_M1 * P_M1) + (P_D_given_M2 * P_M2)
```

```{code-cell} ipython3
print(f"P(Defective | M1) = {P_D_given_M1}")
print(f"P(M1) = {P_M1}")
print(f"P(Defective | M2) = {P_D_given_M2}")
print(f"P(M2) = {P_M2}")
print("\n")
print(f"Overall Probability of a Defective Widget P(D) = ({P_D_given_M1} * {P_M1}) + ({P_D_given_M2} * {P_M2}) = {P_D:.4f}")
```

پس احتمال کل یافتن ویجت معیوب ۳٫۲٪ است. این میانگین وزنی نشان می‌دهد M2 سهم معیوب بیشتری دارد اما M1 در کل تولید بیشتری دارد.

می‌توانیم این را هم شبیه‌سازی کنیم:

```{code-cell} ipython3
num_widgets_sim = 100000
defective_count = 0
```

```{code-cell} ipython3
for _ in range(num_widgets_sim):
    # Decide which machine produced the widget
    if random.random() < P_M1: # Simulates P(M1)
        # Widget from M1
        # Check if it's defective
        if random.random() < P_D_given_M1: # Simulates P(D|M1)
            defective_count += 1
    else:
        # Widget from M2
        # Check if it's defective
        if random.random() < P_D_given_M2: # Simulates P(D|M2)
            defective_count += 1
```

```{code-cell} ipython3
# Estimate P(D) from simulation
P_D_sim = defective_count / num_widgets_sim
```

```{code-cell} ipython3
print(f"\n--- Simulation Results ({num_widgets_sim} widgets) ---")
print(f"Estimated overall P(Defective): {P_D_sim:.4f}")
```

باز هم شبیه‌سازی برآوردی بسیار نزدیک به مقدار محاسبه‌شده می‌دهد.

---

این فصل احتمال شرطی، قاعدهٔ ضرب، قانون احتمال کل و نمودارهای درختی را معرفی کرد. این مفاهیم برای استدلال در برابر عدم‌قطعیت حیاتی‌اند و پایهٔ موضوعات پیشرفته‌تر مانند قضیهٔ بیز — که در فصل بعد کاوش می‌کنیم — را می‌سازند. مثال‌های عملی نشان دادند چگونه این احتمال‌ها را با پایتون محاسبه و شبیه‌سازی کنیم.

+++

در اینجا بخش «تمرین‌ها» با سؤالات و توضیحات کشویی مربوط به هر کدام آمده است:

