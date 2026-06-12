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
  - file: notebooks/chapter_17.ipynb
---

# فصل ۱۷: مقدمه‌ای بر زنجیره مارکوف

+++

به فصل ۱۷ خوش آمدید! در این فصل با کاوش **زنجیره مارکوف** وارد دنیای فرایندهای تصادفی می‌شویم. زنجیره مارکوف مفهومی بنیادین برای مدل‌سازی سامانه‌هایی است که در طول زمان بین حالت‌های مختلف گذار می‌کنند، جایی که حالت آینده *فقط* به حالت فعلی بستگی دارد، نه به دنبالهٔ واقعه‌های پیشین. این ویژگی «بی‌حافظگی» آن‌ها را برای مدل‌سازی پدیده‌های دنیای واقعی — از الگوهای آب‌وهوا و حرکت بازار سهام تا رفتار مشتری و پیمایش وب‌سایت — فوق‌العاده مفید می‌سازد.

+++

**اهداف یادگیری:**
* تعریف زنجیره مارکوف، اجزای آن (حالت‌ها، گذارها) و ویژگی حیاتی مارکوف را درک کنید.
* نحوهٔ نمایش زنجیره مارکوف با ماتریس‌های گذار را بیاموزید.
* رفتار یک زنجیره مارکوف در طول زمان را با پایتون شبیه‌سازی کنید.
* احتمالات گذار چندمرحله‌ای را با توان ماتریس محاسبه کنید.
* درکی مقدماتی از طبقه‌بندی حالت‌ها (مثلاً حالت‌های جذب‌کننده) به‌دست آورید.
* توزیع‌های پایدار و نحوهٔ یافتن آن‌ها را بیاموزید که رفتار بلندمدت زنجیره را نشان می‌دهند.
* این مفاهیم را در مثال‌های عملی با NumPy به‌کار ببرید.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# Configure plots for better readability
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
```

## ۱۷.۱ زنجیره مارکوف چیست؟

+++

**زنجیره مارکوف** مدل ریاضی است که دنباله‌ای از واقعه‌های (یا حالت‌های) ممکن را توصیف می‌کند، جایی که احتمال گذار به حالت بعدی *فقط* به حالت فعلی بستگی دارد و نه به دنبالهٔ حالت‌های پیشین. این **ویژگی مارکوف** (یا بی‌حافظگی) نامیده می‌شود.

اجزای کلیدی:
* **حالت‌ها:** مجموعهٔ متناهی یا شمارا از شرایط یا موقعیت‌های ممکن سامانه. مجموعهٔ حالت‌ها $S = \{s_1, s_2, ..., s_k\}$ باشد.
* **گذارها:** جابه‌جایی بین حالت‌ها.
* **احتمالات گذار:** احتمال حرکت از یک حالت به حالت دیگر در یک گام زمانی. احتمال گذار از حالت $s_i$ به حالت $s_j$ با $P_{ij} = P(X_{t+1} = s_j | X_t = s_i)$ نمایش داده می‌شود، که $X_t$ حالت در زمان $t$ است.
* **توزیع اولیه:** توزیع احتمالی که حالت آغازین سامانه را در زمان $t=0$ توصیف می‌کند.

**مثال: مدل اشتراک مشتری**

شرکتی طرح‌های اشتراک Free، Basic و Premium ارائه می‌دهد. مشتریان می‌توانند ماه‌به‌ماه طرح عوض کنند یا لغو (churn) کنند. این را می‌توان زنجیره مارکوف مدل کرد:
* **حالت‌ها:** $S = \{\text{'Free', 'Basic', 'Premium', 'Churned'}\}$ 
* **گام زمانی:** یک ماه.
* **فرض ویژگی مارکوف:** احتمال اینکه مشتری ماه بعد به طرح جدید برود *فقط* به طرح فعلی بستگی دارد، نه کل تاریخ (مثلاً اینکه دو ماه پیش Premium بود اگر الان Basic است مستقیماً بر گام بعد تأثیر نمی‌گذارد).

+++

## ۱۷.۲ ماتریس گذار

+++

احتمالات گذار زنجیره مارکوف با $k$ حالت را می‌توان به‌صورت منظم در ماتریس $k \times k$ به نام **ماتریس گذار**، که اغلب با $P$ نمایش داده می‌شود، سازمان داد.

$$ 
P = \begin{pmatrix}
 P_{11} & P_{12} & \cdots & P_{1k} \\
 P_{21} & P_{22} & \cdots & P_{2k} \\
 \vdots & \vdots & \ddots & \vdots \\
 P_{k1} & P_{k2} & \cdots & P_{kk}
 \end{pmatrix}
 $$ 

که در آن $P_{ij}$ احتمال گذار *از* حالت $i$ *به* حالت $j$ در یک گام است.

**ویژگی‌های ماتریس گذار:**
1.  همهٔ درایه‌ها باید نامنفی باشند: $P_{ij} \ge 0$ برای همهٔ $i, j$.
2.  مجموع احتمالات در هر سطر باید برابر ۱ باشد: $\sum_{j=1}^{k} P_{ij} = 1$ برای همهٔ $i$. (از هر حالت $i$، سامانه در گام بعد باید به *برخی* حالت $j$ گذار کند).

+++

**مثال: ماتریس گذار مدل اشتراک**

ماتریس گذار معقولی برای مدل اشتراک تعریف می‌کنیم. ترتیب حالت‌ها: ۰: Free، ۱: Basic، ۲: Premium، ۳: Churned.

| From \\ To | Free | Basic | Premium | Churned |
|-----------|------|-------|---------|---------|
| Free      | 0.60 | 0.20  | 0.10    | 0.10    |
| Basic     | 0.10 | 0.60  | 0.20    | 0.10    |
| Premium   | 0.05 | 0.10  | 0.70    | 0.15    |
| Churned   | 0.00 | 0.00  | 0.00    | 1.00    |  <- Absorbing State

```{code-cell} ipython3
# Define the states
states = ['Free', 'Basic', 'Premium', 'Churned']
state_map = {state: i for i, state in enumerate(states)} # Map state names to indices

# Define the transition matrix P
P = np.array([
    [0.60, 0.20, 0.10, 0.10],  # Transitions from Free
    [0.10, 0.60, 0.20, 0.10],  # Transitions from Basic
    [0.05, 0.10, 0.70, 0.15],  # Transitions from Premium
    [0.00, 0.00, 0.00, 1.00]   # Transitions from Churned (Absorbing)
])

# Verify rows sum to 1
print("Transition Matrix P:")
print(P)
print("\nRow sums:", P.sum(axis=1))
```

## ۱۷.۳ شبیه‌سازی مسیرهای زنجیره مارکوف

+++

می‌توانیم پیشرفت سامانه در حالت‌ها در طول زمان را با ماتریس گذار شبیه‌سازی کنیم. با داشتن حالت فعلی، سطر متناظر در ماتریس گذار را به‌عنوان احتمالات برای انتخاب تصادفی حالت بعدی استفاده می‌کنیم.

برای این کار از `numpy.random.choice` استفاده می‌کنیم.

```{code-cell} ipython3
def simulate_path(transition_matrix, state_names, start_state_name, num_steps):
    """Simulates a path through the Markov chain."""
    state_indices = list(range(len(state_names)))
    current_state_index = state_names.index(start_state_name)
    path_indices = [current_state_index]

    for _ in range(num_steps):
        # Get the transition probabilities from the current state
        probabilities = transition_matrix[current_state_index, :]
        
        # Choose the next state based on these probabilities
        next_state_index = np.random.choice(state_indices, p=probabilities)
        path_indices.append(next_state_index)
        
        # Update the current state
        current_state_index = next_state_index
        
        # Optional: Stop if an absorbing state (like Churned) is reached
        if probabilities[current_state_index] == 1.0 and np.sum(probabilities) == 1.0:
           # Check if it's an absorbing state (only loops back to itself)
           if transition_matrix[current_state_index, current_state_index] == 1.0:
              # Fill remaining steps if needed, or break
              # For simplicity here, we just let it stay in the absorbing state
              pass 

    # Convert indices back to state names
    path_names = [state_names[i] for i in path_indices]
    return path_names

# Simulate a path for 12 months starting from 'Free'
start_state = 'Free'
steps = 12
simulated_journey = simulate_path(P, states, start_state, steps)

print(f"Simulated {steps}-month journey starting from {start_state}:")
print(" -> ".join(simulated_journey))
```

سلول شبیه‌سازی را چند بار اجرا کنید تا مسیرهای مختلفی که مشتری ممکن است طی کند ببینید.

+++

## ۱۷.۴ احتمالات گذار $n$ مرحله‌ای

+++

ماتریس گذار $P$ احتمالات گذار بین حالت‌ها در *یک* گام را می‌دهد. اگر بخواهیم احتمال گذار از حالت $i$ به حالت $j$ در *$n$* گام را بدانیم چه؟

این با درایه $(i, j)$ توان ماتریس $P^n$ داده می‌شود.

$P^{(n)}_{ij} = P(X_{t+n} = s_j | X_t = s_i) = (P^n)_{ij}$

توان ماتریس را با `numpy.linalg.matrix_power` محاسبه می‌کنیم.

```{code-cell} ipython3
# Calculate the transition matrix after 3 steps (months)
n_steps = 3
P_n = np.linalg.matrix_power(P, n_steps)

print(f"Transition Matrix after {n_steps} steps (P^{n_steps}):")
print(np.round(P_n, 3)) # Round for readability

# Example: Probability of being in 'Premium' after 3 months, starting from 'Free'
start_idx = state_map['Free']
end_idx = state_map['Premium']
prob_free_to_premium_3_steps = P_n[start_idx, end_idx]

print(f"\nProbability(State=Premium at month 3 | State=Free at month 0): {prob_free_to_premium_3_steps:.3f}")

# Example: Probability of being 'Churned' after 6 months, starting from 'Basic'
n_steps_long = 6
P_n_long = np.linalg.matrix_power(P, n_steps_long)
start_idx_basic = state_map['Basic']
end_idx_churned = state_map['Churned']
prob_basic_to_churned_6_steps = P_n_long[start_idx_basic, end_idx_churned]

print(f"Probability(State=Churned at month 6 | State=Basic at month 0): {prob_basic_to_churned_6_steps:.3f}")
```

## ۱۷.۵ طبقه‌بندی حالت‌ها (مقدمهٔ مختصر)

+++

حالت‌های یک زنجیره مارکوف را می‌توان بر اساس رفتار بلندمدت طبقه‌بندی کرد:

* **دسترس‌پذیر:** حالت $j$ از حالت $i$ دسترس‌پذیر است اگر احتمال غیرصفر رسیدن در نهایت به $j$ با شروع از $i$ وجود داشته باشد (یعنی $P^{(n)}_{ij} > 0$ برای برخی $n \ge 0$).
* **ارتباطی:** حالت‌های $i$ و $j$ ارتباطی‌اند اگر از یکدیگر دسترس‌پذیر باشند.
* **زنجیره تقلیل‌ناپذیر:** زنجیره مارکوف تقلیل‌ناپذیر است اگر همهٔ حالت‌ها با یکدیگر ارتباط داشته باشند (از هر حالتی بتوان به هر حالت دیگر رسید).
* **حالت بازگشت‌پذیر:** اگر با شروع از حالت $i$، احتمال بازگشت در نهایت به $i$ برابر ۱ باشد.
* **حالت گذرا:** اگر با شروع از حالت $i$، احتمال *هرگز* بازنگشتن به $i$ غیرصفر باشد.
* **حالت جذب‌کننده:** حالت $i$ جذب‌کننده است اگر پس از ورود، نتوان آن را ترک کرد ($P_{ii} = 1$). در مثال ما، 'Churned' حالت جذب‌کننده است.

در مدل اشتراک ما:
* 'Churned' حالت جذب‌کننده است.
* 'Free'، 'Basic' و 'Premium' احتمالاً حالت‌های گذرا هستند چون از هر کدام مسیری به 'Churned' وجود دارد و پس از ورود به 'Churned' نمی‌توان بازگشت.
* زنجیره تقلیل‌ناپذیر *نیست* چون نمی‌توان حالت 'Churned' را ترک کرد.

+++

## ۱۷.۶ توزیع‌های پایدار

+++

برای انواع خاصی از زنجیره مارکوف (به‌ویژه تقلیل‌ناپذیر و بدون دوره‌ای)، توزیع احتمالات روی حالت‌ها صرف‌نظر از حالت اولیه به یک **توزیع پایدار** (یا توزیع حالت پایدار) یکتا همگرا می‌شود. $\pi = [\pi_1, \pi_2, ..., \pi_k]$ بردار سطری این توزیع باشد، که $\pi_j$ احتمال بلندمدت بودن در حالت $j$ است.

توزیع پایدار $\pi$ معادلهٔ زیر را برآورده می‌کند:

$$ \pi P = \pi $$ 

با قید $\sum_{j=1}^{k} \pi_j = 1$.

این یعنی اگر توزیع حالت‌ها $\pi$ باشد، پس از یک گام دیگر نیز $\pi$ می‌ماند. $\pi$ بردار ویژهٔ چپ ماتریس گذار $P$ متناظر با مقدار ویژه $\lambda = 1$ است.

**نکتهٔ مهم:** مدل اشتراک ما حالت جذب‌کننده دارد. در چنین مواردی، احتمال بلندمدت در نهایت کاملاً در حالت(های) جذب‌کننده متمرکز می‌شود. برای هر حالت آغازین غیر از 'Churned'، احتمال بودن در 'Churned' با $n \to \infty$ به ۱ نزدیک می‌شود. مفهوم توزیع پایدار یکتا روی *همه* حالت‌ها مستقیماً‌تر برای زنجیره‌هایی اعمال می‌شود که همیشه بتوان بین حالت‌ها جابه‌جا شد (زنجیره‌های تقلیل‌ناپذیر).

+++

**مثال: یافتن توزیع پایدار برای مدل آب‌وهوا**

مدل آب‌وهوای ساده‌تر و تقلیل‌ناپذیری (آفتابی، ابری، بارانی) را برای نمایش یافتن توزیع پایدار در نظر می‌گیریم.

حالت‌های آب‌وهوا: `['Sunny', 'Cloudy', 'Rainy']`
ماتریس آب‌وهوا `W`:
```
   Sunny Cloudy Rainy
Sunny  [0.7,  0.2,   0.1]
Cloudy [0.3,  0.5,   0.2]
Rainy  [0.2,  0.4,   0.4]
```
باید $\pi = [\pi_S, \pi_C, \pi_R]$ را بیابیم که $\pi W = \pi$ و $\pi_S + \pi_C + \pi_R = 1$. این معادل یافتن بردار ویژهٔ چپ برای مقدار ویژه ۱ است.

```{code-cell} ipython3
# Weather example
W_states = ['Sunny', 'Cloudy', 'Rainy']
W = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.5, 0.2],
    [0.2, 0.4, 0.4]
])

# Find eigenvalues and eigenvectors
# We need the *left* eigenvector (v P = lambda v), numpy finds *right* (P u = lambda u).
# The left eigenvector of P for eigenvalue lambda is the right eigenvector of P.T for eigenvalue lambda.
eigenvalues, eigenvectors = np.linalg.eig(W.T)

# Find the eigenvector corresponding to eigenvalue 1
# Due to floating point precision, check for eigenvalues close to 1
idx = np.isclose(eigenvalues, 1)

if not np.any(idx):
    print("No eigenvalue close to 1 found. Check matrix.")
else:
    # Get the eigenvector corresponding to eigenvalue 1
    # Ensure we select only one eigenvector if multiple eigenvalues are close to 1
    # and take the real part as the eigenvector should be real for a stochastic matrix
    stationary_vector_raw = eigenvectors[:, np.where(idx)[0][0]].flatten().real
    
    # Normalize the eigenvector so its components sum to 1
    stationary_distribution = stationary_vector_raw / np.sum(stationary_vector_raw)

    print("Stationary Distribution (Long-run probabilities):")
    for state, prob in zip(W_states, stationary_distribution):
        print(f"  {state}: {prob:.4f}")

    # Verification: pi * W should be equal to pi
    print("\nVerification (pi * W):", np.dot(stationary_distribution, W))
```

این توزیع پایدار می‌گوید در بلندمدت، صرف‌نظر از اینکه امروز آفتابی، ابری یا بارانی باشد، احتمال روز آیندهٔ آفتابی حدود ۴۴٫۷٪، ابری حدود ۳۶٫۸٪ و بارانی حدود ۱۸٫۴٪ است.

+++

## ۱۷.۷ عملی: تحلیل بلندمدت مدل اشتراک

+++

از شبیه‌سازی و احتمالات گذار $n$ مرحله‌ای برای دیدن آنچه در بلندمدت برای مشترکین در مدل اصلی با حالت 'Churned' رخ می‌دهد استفاده می‌کنیم.

```{code-cell} ipython3
# Simulate many paths to see the distribution of final states
num_simulations = 5000
simulation_length = 24 # Simulate for 2 years
final_states = []

initial_state = 'Basic' # Example starting state

for _ in range(num_simulations):
    path = simulate_path(P, states, initial_state, simulation_length)
    final_states.append(path[-1]) # Get the state after 'simulation_length' months

# Calculate the proportion of simulations ending in each state
from collections import Counter # Efficient way to count
final_state_counts = Counter(final_states)
# Ensure all states are present in the counts, even if 0
for state in states:
    if state not in final_state_counts:
        final_state_counts[state] = 0

final_state_proportions = {state: final_state_counts[state] / num_simulations for state in states}

print(f"Distribution of states after {simulation_length} months starting from '{initial_state}' (based on {num_simulations} simulations):")
for state in states: # Print in consistent order
    print(f"  {state}: {final_state_proportions[state]:.4f}")

# Compare with n-step transition probability calculation
P_long_term = np.linalg.matrix_power(P, simulation_length)
start_idx = state_map[initial_state]
theoretical_probs = P_long_term[start_idx, :]

print(f"\nTheoretical probabilities after {simulation_length} months starting from '{initial_state}':")
for i, state in enumerate(states):
    print(f"  {state}: {theoretical_probs[i]:.4f}")
```

توجه کنید نتایج شبیه‌سازی به‌خوبی با احتمالات نظری محاسبه‌شده با توان ماتریس $P^n$ هم‌خوان است. همچنین مشاهده کنید با افزایش تعداد گام‌ها (`simulation_length`)، جرم احتمال به‌طور قابل‌توجهی به سمت حالت 'Churned' جابه‌جا می‌شود، همان‌طور که برای مدلی با حالت جذب‌کننده انتظار می‌رود.

+++

## ۱۷.۸ خلاصه

+++

در این فصل زنجیره مارکوف را معرفی کردیم؛ ابزاری قدرتمند برای مدل‌سازی سامانه‌هایی که بر اساس حالت فعلی بین حالت‌ها گذار می‌کنند.

آموختیم:
* تعریف حالت‌ها، گذارها و ویژگی مارکوف.
* استفاده از ماتریس‌های گذار ($P$) برای نمایش احتمالات یک‌گامی.
* شبیه‌سازی مسیرهای زنجیره مارکوف با پایتون و `np.random.choice`.
* اینکه توان ماتریس ($P^n$) احتمالات گذار $n$ مرحله‌ای را می‌دهد.
* طبقه‌بندی پایهٔ حالت‌ها، از جمله حالت‌های جذب‌کننده.
* مفهوم توزیع پایدار ($\pi P = \pi$) برای زنجیره‌های تقلیل‌ناپذیر و بدون دوره‌ای که رفتار بلندمدت را نشان می‌دهد و نحوهٔ یافتن آن با بردارهای ویژه.

زنجیره مارکوف پایهٔ بسیاری از مدل‌ها و الگوریتم‌های پیشرفته‌تر در حوزه‌هایی مانند یادگیری تقویتی، مالی، ژنتیک و تحقیق در عملیات است.

+++

## تمرین‌ها

+++

1.  **مدل آب‌وهوای ساده:** مدل آب‌وهوا (آفتابی، ابری، بارانی) با ماتریس گذار `W` را در نظر بگیرید. اگر امروز آفتابی باشد، احتمال بارانی بودن پس‌فردا (در ۲ گام) چقدر است؟ با ضرب ماتریس محاسبه کنید.
2.  **ورشکستگی قمارباز (شبیه‌سازی):** قماربازی با \$3 شروع می‌کند. \$1 روی پرتاب سکهٔ منصفانه شرط‌بندی می‌کند (۵۰٪ برد، ۵۰٪ باخت). اگر به \$0 (ورشکستگی) یا \$5 (برد) برسد متوقف می‌شود.
    الف. حالت‌ها را تعریف کنید (مقدار پول: ۰، ۱، ۲، ۳، ۴، ۵).
    ب. ماتریس گذار را تعریف کنید. حالت‌های جذب‌کننده ۰ و ۵ را در نظر بگیرید.
    ج. ۱۰۰۰۰ بازی با شروع از \$3 شبیه‌سازی کنید. چه نسبتی به ورشکستگی (\$0) و چه نسبتی به برد (\$5) ختم می‌شود؟
3.  **تأیید توزیع پایدار:** برای مدل آب‌وهوا، به‌صورت دستی تأیید کنید توزیع پایدار محاسبه‌شده $\pi$ رابطه $\pi W = \pi$ را برآورده می‌کند.
4.  **تغییر مدل اشتراک:** حالت 'Churned' در مدل اشتراک `P` را طوری تغییر دهید که احتمال کوچکی (مثلاً ۰٫۰۵) برای بازاشتراک مشتری لغوشده در طرح 'Free' هر ماه وجود داشته باشد (احتمال $P_{33}$ را متناسب تنظیم کنید تا مجموع سطر همچنان ۱ باشد). آیا زنجیره هنوز جذب‌کننده است؟ با روش بردار ویژه توزیع پایدار جدید را بیابید. اکنون چه چیزی را نشان می‌دهد؟

```{code-cell} ipython3
# فضای کد/محاسبهٔ تمرین ۱
W_states = ['Sunny', 'Cloudy', 'Rainy']
W = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.5, 0.2],
    [0.2, 0.4, 0.4]
])

# Calculate W^2
W_2 = np.linalg.matrix_power(W, 2)

# Probability Sunny -> Rainy in 2 steps
sunny_idx = W_states.index('Sunny')
rainy_idx = W_states.index('Rainy')
prob_sunny_to_rainy_2_steps = W_2[sunny_idx, rainy_idx]
print(f"(Exercise 1) Probability Sunny -> Rainy in 2 steps: {prob_sunny_to_rainy_2_steps:.4f}")
```

```{code-cell} ipython3
# فضای کد/محاسبهٔ تمرین ۲
# Gambler's Ruin
gambler_states = [0, 1, 2, 3, 4, 5] # Amount of money
P_gambler = np.array([
    [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], # From 0 (Ruin)
    [0.5, 0.0, 0.5, 0.0, 0.0, 0.0], # From 1
    [0.0, 0.5, 0.0, 0.5, 0.0, 0.0], # From 2
    [0.0, 0.0, 0.5, 0.0, 0.5, 0.0], # From 3
    [0.0, 0.0, 0.0, 0.5, 0.0, 0.5], # From 4
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]  # From 5 (Win)
])

def simulate_gambler(transition_matrix, states, start_state_val, max_steps=200): # Increased max_steps slightly
    """Simulates one game until an absorbing state is reached."""
    state_indices = list(range(len(states)))
    current_state_index = states.index(start_state_val)
    #path_indices = [current_state_index] # Path not needed for final state only

    steps = 0
    while steps < max_steps:
        current_state_val = states[current_state_index]
        # Check if in absorbing state
        if current_state_val == 0 or current_state_val == 5:
            return current_state_val # Return final state
            
        probabilities = transition_matrix[current_state_index, :]
        next_state_index = np.random.choice(state_indices, p=probabilities)
        #path_indices.append(next_state_index)
        current_state_index = next_state_index
        steps += 1
        
    # If max_steps reached without hitting absorbing state (unlikely here but good practice)
    return states[current_state_index] 

num_games = 10000 # Increased simulations for better accuracy
start_money = 3
end_results = []
for _ in range(num_games):
    end_results.append(simulate_gambler(P_gambler, gambler_states, start_money))

from collections import Counter
end_counts = Counter(end_results)

ruin_count = end_counts.get(0, 0) # Use .get for safety
win_count = end_counts.get(5, 0)

print(f"\n(Exercise 2) Gambler's Ruin Simulation ({num_games} games starting at ${start_money}):")
print(f"  Proportion ending in Ruin ($0): {ruin_count / num_games:.4f}") # Should be 0.4
print(f"  Proportion ending in Win ($5): {win_count / num_games:.4f}")  # Should be 0.6
```

```{code-cell} ipython3
# فضای کد/محاسبهٔ تمرین ۳
# Verification: pi * W = pi

# From previous calculation (ensure these are accurate)
# Recalculate just in case
eigenvalues, eigenvectors = np.linalg.eig(W.T)
idx = np.isclose(eigenvalues, 1)
stationary_vector_raw = eigenvectors[:, np.where(idx)[0][0]].flatten().real
pi_weather = stationary_vector_raw / np.sum(stationary_vector_raw)

result_vector = np.dot(pi_weather, W)

print("\n(Exercise 3) Stationary Distribution Verification:")
print(f"  Calculated pi: {pi_weather}")
print(f"  Result pi * W: {result_vector}")
# Use np.allclose for robust floating point comparison
print(f"  Are they close? {np.allclose(pi_weather, result_vector)}")
```

```{code-cell} ipython3
# فضای کد/محاسبهٔ تمرین ۴

# Reload original P and states just in case they were modified
states = ['Free', 'Basic', 'Premium', 'Churned']
state_map = {state: i for i, state in enumerate(states)}
P = np.array([
    [0.60, 0.20, 0.10, 0.10],  # Transitions from Free
    [0.10, 0.60, 0.20, 0.10],  # Transitions from Basic
    [0.05, 0.10, 0.70, 0.15],  # Transitions from Premium
    [0.00, 0.00, 0.00, 1.00]   # Transitions from Churned (Absorbing)
])

P_modified = P.copy() # Start with original subscription matrix

# Modify the 'Churned' row (index 3)
prob_churn_to_free = 0.05
P_modified[3, state_map['Free']] = prob_churn_to_free
P_modified[3, state_map['Churned']] = 1.0 - prob_churn_to_free # Adjust P_33

print("\n(Exercise 4) Modified Transition Matrix:")
print(P_modified)
print("\nIs 'Churned' still absorbing?", P_modified[3, 3] == 1.0) # Should be False
print("The chain is no longer absorbing, as state 'Churned' can transition to 'Free'.")
print("The chain should now be irreducible if all other states can eventually reach Churned and Churned can reach Free.")

# Try finding the stationary distribution for the modified matrix
eigenvalues_mod, eigenvectors_mod = np.linalg.eig(P_modified.T)
idx_mod = np.isclose(eigenvalues_mod, 1)

if not np.any(idx_mod):
    print("\nNo eigenvalue close to 1 found for modified matrix.")
else:
    stationary_vector_raw_mod = eigenvectors_mod[:, np.where(idx_mod)[0][0]].flatten().real
    stationary_distribution_mod = stationary_vector_raw_mod / np.sum(stationary_vector_raw_mod)
    
    print("\nStationary Distribution for Modified Matrix:")
    for state, prob in zip(states, stationary_distribution_mod):
        print(f"  {state}: {prob:.4f}")
    
    print("\nThis represents the long-run proportion of time the system spends in each state.")
    print("Even though customers churn, the small chance of returning means there's a non-zero steady state for all plans.")
    # Verification
    print("\nVerification (pi_mod * P_mod):", np.dot(stationary_distribution_mod, P_modified))
```
