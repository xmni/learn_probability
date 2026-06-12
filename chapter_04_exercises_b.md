---

# تمرین‌های فصل ۴ (بخش ب).

```{note}
تمایز میان $P(A \cap B) $ و $ P(A | B) $ فقط از روی عبارت‌بندی مسئله می‌تواند دشوار باشد! بیایید ببینیم هر کدام را چگونه تشخیص دهیم.

** $ P(A \cap B) $ (احتمال A و B)**

این احتمال وقوع **همزمان** رویداد A **و** رویداد B را نشان می‌دهد. واژگان و عباراتی که اغلب $ P(A \cap B) $ را نشان می‌دهند:

* «احتمال اینکه کسی [ویژگی A] **و** [ویژگی B] باشد»
* «نسبت اقلامی که [نوع A] **و** [خاصیت B] دارند»
* «شانس [رویداد A] **و در عین حال** [رویداد B]»
* جملاتی که مستقیماً تعداد یا نسبت همپوشانی دو دسته را می‌دهند.

**مثال:** «احتمال اینکه دانشجویی مهندسی بخواند **و** زن باشد ۰٫۰۵ است.» این مستقیماً $ P(\text{Engineering} \cap \text{Female}) = 0.05 $ را می‌دهد.

** $ P(A | B) $ (احتمال A به شرط B)**

این احتمال وقوع رویداد A **به شرط اینکه** رویداد B رخ داده باشد را نشان می‌دهد؛ یعنی *احتمال شرطی*. واژگان و عباراتی که اغلب $ P(A | B) $ را نشان می‌دهند:

* «احتمال اینکه کسی [ویژگی A] باشد **به شرط اینکه** [ویژگی B] باشد»
* «نسبت اقلام [نوع B] که **همچنین** [نوع A] هستند»
* «اگر [ویژگی B] انتخاب شود، احتمال [ویژگی A] چقدر است؟»
* جملاتی که اطلاعات دربارهٔ زیرمجموعه‌ای از جمعیت می‌دهند.

**مثال:** «از دانشجویان مهندسی، ۲۰٪ زن هستند.» این $ P(\text{Female} | \text{Engineering}) = 0.20 $ را می‌دهد. توجه کنید تمرکز روی زیرمجموعهٔ دانشجویان مهندسی است.

**نکتهٔ کلیدی:**

به عبارت‌هایی که شرط یا محدودیت به گروه خاص را نشان می‌دهند دقت کنید. «از کسانی که...»، «به شرط اینکه...»، و «در میان...» نشانه‌های قوی احتمال شرطی $ P(A | B) $ هستند. عبارات با «و» یا توصیف همپوشانی دو ویژگی اغلب به احتمال اشتراک $ P(A \cap B) $ اشاره دارند.
```

1. **پرتاب تاس — واریانس ساده:** یک تاس منصفانهٔ شش‌وجهی می‌اندازید.

      * احتمال چرخاندن عدد زوج چقدر است؟
      * احتمال چرخاندن عددی بزرگتر از 4 چقدر است؟
      * احتمال چرخاندن عدد اول چقدر است؟ (1 را به عنوان اول در نظر بگیرید)

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید S فضای نمونه برای انداختن تاس منصفانهٔ شش‌وجهی باشد: $ S = \{1, 2, 3, 4, 5, 6\} $. تعداد کل نتایج برابر |S| = 6 $.

    **بخش 1: احتمال چرخاندن عدد زوج.**
    فرض کنید E رویداد چرخاندن یک عدد زوج باشد. نتایج برای E عبارت‌اند از \{2, 4, 6\} $.
    تعداد پیامدهای E برابر |E| = 3 $.

    $ $
    \begin{align*}
    P(E) &= \frac{|E|}{|S|} \\
    &= \frac{3}{6} \\
    &= \frac{1}{2}
    \end{align*}
    $$

    **بخش 2: احتمال چرخش عددی بزرگتر از 4.**
    فرض کنید G رویداد چرخاندن عددی بزرگتر از 4 باشد. نتایج G عبارتند از $ \{5, 6\} $.
    تعداد پیامدهای G برابر |G| = 2 $.
    
    $ $
    \begin{align*}
    P(G) &= \frac{|G|}{|S|} \\
    &= \frac{2}{6} \\
    &= \frac{1}{3}
    \end{align*}
    $$

    **بخش 3: احتمال چرخش عدد اول.**
    فرض کنید P رویداد چرخاندن یک عدد اول باشد. اعداد اول در S عبارت‌اند از \{2, 3, 5\} $. (1 طبق قرارداد اول نیست).
    تعداد پیامدهای P برابر |P| = 3 $.
    
    $ $
    \begin{align*}
    P(P) &= \frac{|P|}{|S|} \\
    &= \frac{3}{6} \\
    &= \frac{1}{2}
    \end{align*}
    $$
    ```

2. **دستهٔ کارت — ویژگی‌های مشخص:** شما یک کارت را از یک دسته استاندارد 52 کارتی می‌کشید.

      * احتمال کشیدن کارت تصویری (سرباز، بیبی، شاه) چقدر است؟
      * احتمال کشیدن کارتی که پیک نباشد چقدر است؟
      * احتمال کشیدن آس قرمز (آس دل یا آس خشت) چقدر است؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    یک دستهٔ استاندارد ۵۲ کارت دارد.

    **بخش ۱: احتمال کشیدن کارت تصویری.**
    در هر یک از ۴ خال، ۳ کارت تصویری (سرباز، بیبی، شاه) وجود دارد.
    تعداد کارت‌های تصویری = $ 3 \times 4 = 12 $.
    
    $ $
    \begin{align*}
    P(\text{Face Card}) &= \frac{12}{52} \\
    &= \frac{3}{13}
    \end{align*}
    $$

    **بخش ۲: احتمال کشیدن کارتی که پیک نباشد.**
    در دسته ۱۳ کارت پیک وجود دارد.
    تعداد کارت‌های غیرپیک = $ 52 - 13 = 39 $.
    
    $ $
    \begin{align*}
    P(\text{Not a Spade}) &= \frac{39}{52} \\
    &= \frac{3}{4}
    \end{align*}
    $$

    در غیر این صورت، $ P(\text{Spade}) = \frac{13}{52} = \frac{1}{4} $.
    
    $ $
    \begin{align*}
    P(\text{Not a Spade}) &= 1 - P(\text{Spade}) \\
    &= 1 - \frac{1}{4} \\
    &= \frac{3}{4}
    \end{align*}
    $$

    **بخش ۳: احتمال کشیدن آس قرمز.**
    دو آس قرمز وجود دارد: آس دل و آس خشت.
    تعداد آس‌های قرمز = ۲.
    
    $ $
    \begin{align*}
    P(\text{Red Ace}) &= \frac{2}{52} \\
    &= \frac{1}{26}
    \end{align*}
    $$
    ```

3. **دو تلنگر سکه منصفانه:** دو سکه منصفانه را برمیگردانید.

      * فضای نمونه برای این آزمایش چقدر است؟
      * احتمال گرفتن حداقل یک دم (T) چقدر است؟
      * احتمال گرفتن دو سر (HH) چقدر است؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    H را شیر و T را خط در نظر بگیرید.

    **بخش 1: فضای نمونه.**
    پیامدهای ممکن هنگام پرتاب دو سکهٔ منصفانه:
    $ S = \{\text{HH, HT, TH, TT}\} $
    وجود دارد $ 2 \times 2 = 4 $ نتایج احتمالی

    **بخش 2: احتمال به دست آوردن حداقل یک دم.**
    اجازه دهید A رویداد بدست آوردن حداقل یک دم باشد. نتایج برای A عبارت‌اند از \{\text{HT, TH, TT}\} $.
    ۳ پیامد از این نوع وجود دارد.
    $ P(A) = \frac{3}{4} $.
    در غیر این صورت، این متمم «هیچ خطی نیاید» (یعنی HH) است.
    $ P(\text{No Tails}) = P(\text{HH}) = \frac{1}{4} $.
    
    $ $
    \begin{align*}
    P(\text{At least one Tail}) &= 1 - P(\text{No Tails}) \\
    &= 1 - \frac{1}{4} \\
    &= \frac{3}{4}
    \end{align*}
    $$

    **بخش سوم: احتمال به دست آوردن دو سر.**
    فرض کنید B رویداد بدست آوردن دو هد باشد. تنها نتیجه برای B این برابر \{\text{HH}\} $.
    ۱ پیامد از این نوع وجود دارد.
    $ P(B) = \frac{1}{4} $.
    ```

4. **احتمال روزهای بارانی:** احتمال بارندگی در هر روز در یک شهر 0.3 است. فرض کنید آب و هوا در هر روز مستقل از آب و هوای روزهای دیگر است.

      * احتمال اینکه در یک روز باران نبارد چقدر است؟
      * احتمال بارندگی در روزهای دوشنبه و سه شنبه چقدر است؟
      * احتمال اینکه دوشنبه یا سه شنبه (یا هر دو) باران ببارد چقدر است؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    بگذارید R رویدادی باشد که در یک روز معین باران می بارد. به ما داده شده برابر P(R) = 0.3 $.
    رویدادها مستقل هستند.

    **بخش ۱: احتمال اینکه در یک روز معین باران نبارد.**
    فرض کنید $ \neg R $ رویداد «باران نبارد» باشد. این متمم R است.
    
    $ $
    \begin{align*}
    P(\neg R) &= 1 - P(R) \\
    &= 1 - 0.3 \\
    &= 0.7
    \end{align*}
    $$

    **بخش 2: احتمال بارندگی در روزهای دوشنبه و سه شنبه.**
    فرض کنید $ R_M $ باران در دوشنبه و $ R_T $ باران در سه‌شنبه باشد
    از آنجایی که رویدادها مستقل هستند، $ P(R_M \text{ and } R_T) = P(R_M) \times P(R_T) $.
    
    $ $
    \begin{align*}
    P(R_M \text{ and } R_T) &= 0.3 \times 0.3 \\
    &= 0.09
    \end{align*}
    $$

    **بخش ۳: احتمال اینکه دوشنبه یا سه شنبه (یا هر دو) باران ببارد.**
    
    ما از فرمول استفاده می کنیم:

    $ $P(R_M \text{ or } R_T) = P(R_M) + P(R_T) - P(R_M \text{ and } R_T)$$
    
    محاسبه:
    
    $ $
    \شروع{تراز*}
    P(R_M \text{ یا } R_T) &= 0.3 + 0.3 - 0.09 \\
    &= 0.6 - 0.09 \\
    &= 0.51
    \پایان{تراز کردن*}
    $$
    
    در غیر این صورت، این $ 1 - P(\text{no rain on Monday AND no rain on Tuesday}) $ است.
    
    $ $
    \شروع{تراز*}
    P(\neg R_M \text{ و } \neg R_T) &= P(\neg R_M) \times P(\neg R_T) \\
    &= 0.7 \ بار 0.7 \\
    &= 0.49
    \پایان{تراز کردن*}
    $$

    پس، $ P(R_M \text{ or } R_T) = 1 - 0.49 = 0.51 $.
    ```

5.  **قید مجموع تاس:** You roll two fair six-sided dice.

      * احتمال اینکه مجموع تاس‌ها ۶ باشد چقدر است؟
      * با فرض اینکه تاس اول ۲ باشد، احتمال اینکه مجموع ۶ باشد چقدر است؟
      * آیا رویدادهای «مجموع ۶ است» و «تاس اول ۲ نشان می‌دهد» مستقل‌اند؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    کل پیامدهای ممکن = $ 6 \times 6 = 36 $. هر پیامد به‌طور یکسان محتمل است.

    **بخش ۱: احتمال اینکه مجموع تاس‌ها ۶ باشد.**
    فرض کنید S6 رویداد «مجموع برابر ۶» باشد.
    پیامدهای S6: {(1,5), (2,4), (3,3), (4,2), (5,1)}. ۵ پیامد از این نوع وجود دارد.
    $ P(S6) = \frac{5}{36} $.

    **بخش ۲: با فرض اینکه تاس اول ۲ باشد، احتمال اینکه مجموع ۶ باشد چقدر است؟**

    فرض کنید D1_2 رویداد «تاس اول ۲ نشان دهد» باشد.

    پیامدهای D1_2: {(2,1), (2,2), (2,3), (2,4), (2,5), (2,6)}. ۶ پیامد از این نوع وجود دارد.

    می‌خواهیم بیابیم $ P(S6 | D1\_2) $.

    اگر تاس اول ۲ باشد، برای اینکه مجموع ۶ شود، تاس دوم باید $ 6 - 2 = 4 $ باشد.

    پیامد (2,4) تنها پیامدی است که هر دو شرط را برآورده می‌کند.

    در فضای نمونهٔ کاهش‌یافته که تاس اول ۲ است، ۱ پیامد وجود دارد که مجموع ۶ شود.

    $ P(S6 | D1\_2) = \frac{1}{6} $.

    در غیر این صورت، با استفاده از فرمول

    $ $P(S6 | D1\_2) = \frac{P(S6 \cap D1\_2)}{P(D1\_2)}$$

    $ P(D1\_2) = \frac{6}{36} = \frac{1}{6} $.
    $ P(S6 \cap D1\_2) $ (مجموع 6 و تاس اول 2 است) نتیجه (2،4) است، ، پس $ P(S6 \cap D1\_2) = \frac{1}{36} $.
    
    $ $
    \begin{align*}
    P(S6 | D1\_2) &= \frac{1/36}{6/36} \\
    &= \frac{1}{6}
    \end{align*}
    $$

    **بخش 3: آیا رویدادهای "جمع 6 است" و "اولین تاس نشان می دهد 2" مستقل هستند؟**

    دو رویداد A و B مستقل هستند اگر $ P(A \cap B) = P(A) \times P(B) $.

    اینجا، $ A = S6 $ و $ B = D1\_2 $.
    $ P(S6) = \frac{5}{36} $.
    $ P(D1\_2) = \frac{1}{6} $.

    $ $P(S6) \times P(D1\_2) = \frac{5}{36} \times \frac{1}{6} = \frac{5}{216}$$

    یافتیم $ P(S6 \cap D1\_2) = \frac{1}{36} $.
    از آنجا که $ \frac{1}{36} \neq \frac{5}{216} $، رویدادها مستقل نیستند.

    در غیر این صورت، رویدادها مستقل‌اند اگر $P(A|B)=P(A)$. اینجا، $ P(S6 | D1\_2) = \frac{1}{6} $ and $ P(S6) = \frac{5}{36} $. از آنجا که $\frac{1}{6} \neq \frac{5}{36}$، رویدادها مستقل نیستند.
    ```

6.  **کشیدن دو کارت پیاپی:** دو کارت از یک دستهٔ استاندارد ۵۲ کارتی بدون بازگرداندن می‌کشید.

      * احتمال کشیدن شاه اول و سپس بیبی دوم چقدر است؟
      * احتمال کشیدن یک شاه و یک بیبی به هر ترتیبی چقدر است؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    **بخش ۱: احتمال کشیدن شاه اول و سپس بیبی دوم (K سپس Q).**
    احتمال کشیدن شاه اول: $ P(K1) = \frac{4}{52} $.
    با فرض کشیدن شاه اول، ۵۱ کارت باقی می‌ماند. هنوز ۴ بیبی وجود دارد.
    احتمال کشیدن بیبی دوم، با فرض شاه اول: $ P(Q2 | K1) = \frac{4}{51} $.
    
    $ $
    \شروع{تراز*}
    P(K1 \text{ سپس } Q2) &= P(K1) \times P(Q2 | K1) \\
    &= \frac{4}{52} \times \frac{4}{51} \\
    &= \frac{1}{13} \times \frac{4}{51} \\
    &= \frac{4}{663}
    \پایان{تراز کردن*}
    $$

    **بخش ۲: احتمال کشیدن یک شاه و یک بیبی به هر ترتیب.**
    این می‌تواند به دو روش رخ دهد:
    1.  شاه اول، سپس بیبی (K سپس Q): $ P(K1 \text{ then } Q2) = \frac{4}{663} $ (calculated above).
    2.  بیبی اول، سپس شاه (Q سپس K):
        $ P(Q1) = \frac{4}{52} $.
        $ P(K2 | Q1) = \frac{4}{51} $.

        $ $
        \شروع{تراز*}
        P(Q1 \text{ سپس } K2) &= P(Q1) \times P(K2 | Q1) \\
        &= \frac{4}{52} \times \frac{4}{51} \\
        &= \frac{4}{663}
        \پایان{تراز کردن*}
        $$

    احتمال کشیدن یک شاه و یک بیبی به هر ترتیبی، مجموع این احتمال‌هاست:

    $ $
    \شروع{تراز*}
    P(\text{King and Queen}) &= P(K1 \text{ سپس } Q2) + P(Q1 \text{ سپس } K2) \\
    &= \frac{4}{663} + \frac{4}{663} \\
    &= \frac{8}{663}
    \پایان{تراز کردن*}
    $$
    ```

7.  **بررسی استقلال رویدادها:** فرض کنید A و B دو رویداد باشند و $P(A)=0.4$، $P(B)=0.5$، $P(A \cup B)=0.7$.

      * $ P(A \cap B) $ را بیابید.
      * آیا رویدادهای A و B مستقل‌اند؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    **بخش ۱: $ P(A \cap B) $ را بیابید.**
    از فرمول احتمال اجتماع دو رویداد استفاده می‌کنیم:
    $ $P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
    به ما داده می شود:
    $ P(A) = 0.4 $
    $ P(B) = 0.5 $
    $ P(A \\cup B) = 0.7 $
    پس،

    $ $
    \begin{align*}
    0.7 &= 0.4 + 0.5 - P(A \cap B) \\
    0.7 &= 0.9 - P(A \cap B) \\
    P(A \cap B) &= 0.9 - 0.7 \\
    P(A \cap B) &= 0.2
    \end{align*}
    $$

    **بخش 2: آیا رویدادهای A و B مستقل هستند؟**
    دو رویداد A و B مستقل هستند اگر $ P(A \cap B) = P(A) \times P(B) $.
    محاسبه کردیم $ P(A \cap B) = 0.2 $.
    بیایید محاسبه کنیم $ P(A) \times P(B) $:
    $ P(A) \times P(B) = 0.4 \times 0.5 = 0.2 $.
    از آنجایی که $ P(A \cap B) = P(A) \times P(B) $ (هر دو 0.2 هستند)، رویدادهای A و B مستقل هستند.
    ```

8. **خانواده با دو فرزند:** یک خانواده دارای دو فرزند است. فرض کنید احتمال پسر (B) یا دختر (G) برابر (0.5) و مستقل برای هر کودک است.

      * احتمال پسر بودن هر دو فرزند چقدر است؟
      * با توجه به اینکه حداقل یک فرزند پسر است، احتمال پسر بودن هر دو فرزند چقدر است؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    ترکیبات جنسی ممکن برای دو کودک (بزرگترین تا کوچکترین) عبارتند از:
    $ S = \{\text{BB, BG, GB, GG}\} $. هر پیامد احتمال $0.5 \times 0.5 = 0.25$ دارد.

    **بخش 1: احتمال اینکه هر دو فرزند پسر باشند.**
    
    اجازه دهید E رویدادی باشد که هر دو فرزند پسر هستند. نتیجه {BB} است.
    $ P(E) = P(\text{BB}) = 0.25 $.

    **بخش 2: با توجه به اینکه حداقل یک فرزند پسر است، احتمال پسر بودن هر دو فرزند چقدر است؟**
    
    اجازه دهید A رویدادی باشد که حداقل یک کودک پسر باشد.
    
    پیامدهای A عبارت‌اند از $ \{\text{BB, BG, GB}\} $. So $ P(A) = \frac{3}{4} = 0.75 $.
    
    فرض کنید B رویدادی باشد که هر دو فرزند پسر هستند. نتیجه برای B این برابر \{\text{BB}\} $. So $ P(B) = \frac{1}{4} = 0.25 $.
    
    ما می خواهیم پیدا کنیم $ P(B | A) = P(\text{both boys } | \text{ at least one boy}) $.
    
    رویداد "B و A" (هر دو پسر و حداقل یک پسر) صرفاً رویداد "هر دو پسر" است که $ \{\text{BB}\} $.
    
    پس، $ P(B \cap A) = P(\text{BB}) = 0.25 $.

    با استفاده از فرمول احتمال شرطی:
    $ $P(B | A) = \frac{P(B \cap A)}{P(A)}$$

    $ $
    \شروع{تراز*}
    P(B | A) &= \frac{0.25}{0.75} \\
    &= \frac{1}{3}
    \پایان{تراز کردن*}
    $$

    در غیر این صورت، با استفاده از فضای نمونهٔ کاهش‌یافته:
    
    رویداد «حداقل یک فرزند پسر است» یعنی پیامدهای ممکن $ \{\text{BB, BG, GB}\} $.

    این فضای نمونهٔ جدید ماست، با ۳ پیامد به‌طور یکسان محتمل.
    
    از این ۳ پیامد، فقط ۱ پیامد «هر دو فرزند پسر» (BB) است.
    پس، احتمال شرطی برابر $ \frac{1}{3} $.
    ```

9.  **دادهٔ نظرسنجی: قهوه و بهره‌وری:** در نظرسنجی ۱۰۰ کارمند اداری:

      * ۶۰ نفر قهوه می‌نوشند.
      * ۴۰ نفر از نوشندگان قهوه گزارش بهره‌وری صبحگاهی دادند.
      * ۳۰ نفر از غیرنوشندگان قهوه گزارش بهره‌وری صبحگاهی دادند.
        فرض کنید C رویداد «کارمند قهوه می‌نوشد» و P رویداد «کارمند productive است».
      * $P(C)$ را بیابید.
      * $P(P | C)$ را بیابید.
      * $P(P | \\neg C)$ را بیابید.

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    کل کارکنان = ۱۰۰.
    تعداد نوشندگان قهوه = ۶۰.
    تعداد غیرنوشندگان قهوه = $ 100 - 60 = 40 $.
    تعداد نوشندگان قهوه که productive feel = 40.
    تعداد غیرنوشندگان قهوه که productive هستند = ۳۰.

    **بخش ۱: بیابید $ P(C) $.**
    C is the event a worker drinks coffee.

    $ $
    \شروع{تراز*}
    P(C) &= \frac{\text{تعداد مصرف کنندگان قهوه}}{\text{کل کارگر}} \\
    &= \frac{100} \\
    &= 0.6
    \پایان{تراز کردن*}
    $$

    **بخش ۲: بیابید $ P(P | C) $.**
    این احتمال productive بودن کارمند، به شرط نوشیدن قهوه است.

    $ $
    \شروع{تراز*}
    P(P | C) &= \frac{\text{تعداد قهوه‌نوشانی که احساس بهره‌وری می‌کنند}}{\text{تعداد قهوه‌خوران}} \\
    &= \frac{40}{60} \\
    &= \frac{2}{3} \\
    &\حدود 0.667
    \پایان{تراز کردن*}
    $$

    **بخش ۳: $P(P | \neg C)$ را بیابید.**
    این احتمال productive بودن کارمند، به شرط نوشیدن نکردن قهوه است.
    $ \neg C $ is the event a worker does not drink coffee.

    $ $
    \شروع{تراز*}
    P(P | \neg C) &= \frac{\text{تعداد افرادی که قهوه نمی‌نوشند و احساس بهره‌وری می‌کنند}}{\text{تعداد افرادی که قهوه نمی‌نوشند}} \\
    &= \frac{30}{40} \\
    &= \frac{3}{4} \\
    &= 0.75
    \پایان{تراز کردن*}
    $$
    ```

10. **قطعات معیوب از ماشین‌ها:** A factory has two machines, A and B.

      * Machine A produces 60% of the daily output, and 5% of its products are defective.
      * Machine B produces 40% of the daily output, and 3% of its products are defective.
      * احتمال اینکه قطعهٔ تصادفی از ماشین A ساخته شده و معیوب باشد چقدر است؟
      * احتمال اینکه قطعهٔ تصادفی از ماشین B ساخته شده و معیوب نباشد چقدر است؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید A رویداد «قطعه توسط ماشین A ساخته شده» و B رویداد «قطعه توسط ماشین B ساخته شده» باشد.
    فرض کنید D رویداد «قطعه معیوب باشد» و $ \neg D $ رویداد «قطعه معیوب نباشد» باشد.

    داده شده:
    $ P(A) = 0.60 $
    $ P(B) = 0.40 $
    $ P(D | A) = 0.05 $ (defect rate for Machine A)
    $ P(D | B) = 0.03 $ (defect rate for Machine B)

    از این، می‌توانیم بیابیم:

    $ $
    \شروع{تراز*}
    P(\neg D | A) &= 1 - P(D | A) \\
    &= 1 - 0.05 \\
    &= 0.95
    \پایان{تراز کردن*}
    $$

    $ $
    \شروع{تراز*}
    P(\neg D | B) &= 1 - P(D | B) \\
    &= 1 - 0.03 \\
    &= 0.97
    \پایان{تراز کردن*}
    $$

    **بخش ۱: احتمال a part was made by Machine A AND is defective.**
    می‌خواهیم بیابیم $ P(A \cap D) $.
    با استفاده از قانون ضرب: $ P(A \cap D) = P(D | A) \times P(A) $
    $ P(A \cap D) = 0.05 \times 0.60 = 0.03 $.

    **بخش ۲: احتمال a part was made by Machine B AND is NOT defective.**
    می‌خواهیم بیابیم $ P(B \cap \neg D) $.
    با استفاده از قانون ضرب: $ P(B \cap \neg D) = P(\neg D | B) \times P(B) $
    $ P(B \cap \neg D) = 0.97 \times 0.40 = 0.388 $.
    ```

11. **توپ‌ها در یک ظرف (دو بار کشیدن):** An urn contains 5 red balls and 3 blue balls. You draw two balls from the urn *without* replacement.

      * احتمال اینکه هر دو توپ کشیده‌شده قرمز باشند چقدر است؟
      * احتمال اینکه توپ اول قرمز و دوم آبی باشد چقدر است؟
      * احتمال اینکه یک توپ قرمز و یک آبی باشد (به هر ترتیب) چقدر است؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    کل توپ‌ها در ابتدا = $ 5 \text{ Red} + 3 \text{ Blue} = 8 $ balls.

    **بخش ۱: احتمال both balls drawn are red (R1 and R2).**
    $ P(R1) = \text{Probability first ball is red} = \frac{5}{8} $.
    با فرض قرمز بودن اول، ۴ توپ قرمز و ۷ توپ در کل باقی می‌ماند.
    $ P(R2 | R1) = \text{Probability second ball is red, given first was red} = \frac{4}{7} $.

    $ $
    \شروع{تراز*}
    P(R1 \text{ و } R2) &= P(R1) \times P(R2 | R1) \\
    &= \frac{5}{8} \times \frac{4}{7} \\
    &= \frac{20}{56} \\
    &= \frac{5}{14}
    \پایان{تراز کردن*}
    $$

    **بخش ۲: احتمال the first ball is red and the second ball is blue (R1 and B2).**
    $ P(R1) = \frac{5}{8} $.
    با فرض قرمز بودن اول، ۳ توپ آبی و ۷ توپ در کل باقی می‌ماند.
    $ P(B2 | R1) = \text{Probability second ball is blue, given first was red} = \frac{3}{7} $.

    $ $
    \شروع{تراز*}
    P(R1 \text{ و } B2) &= P(R1) \times P(B2 | R1) \\
    &= \frac{5}{8} \times \frac{3}{7} \\
    &= \frac{15}{56}
    \پایان{تراز کردن*}
    $$

    **بخش ۳: احتمال one ball is red and one ball is blue (any order).**
    این می‌تواند به دو روش رخ دهد:
    1.  Red first, then Blue (R1 and B2): $ P(R1 \text{ and } B2) = \frac{15}{56} $ (from Part 2).
    2.  Blue first, then Red (B1 and R2):
        $ P(B1) = \text{Probability first ball is blue} = \frac{3}{8} $.
        Given the first was blue, there are 5 red balls left and 7 total balls.
        $ P(R2 | B1) = \text{Probability second ball is red, given first was blue} = \frac{5}{7} $.

        $ $
        \شروع{تراز*}
        P(B1 \text{ و } R2) &= P(B1) \times P(R2 | B1) \\
        &= \frac{3}{8} \times \frac{5}{7} \\
        &= \frac{15}{56}
        \پایان{تراز کردن*}
        $$

    احتمال کل، مجموع این دو رویداد ناسازگار است:

    $ $
    \شروع{تراز*}
    P(\text{یک قرمز، یک آبی}) &= P(R1 \text{ و } B2) + P(B1 \text{ و } R2) \\
    &= \frac{15}{56} + \frac{15}{56} \\
    &= \frac{30}{56} \\
    &= \frac{15}{28}
    \پایان{تراز کردن*}
    $$
    ```

12. **پیش‌نیاز درس و قبولی:** To take Course B, a student must first pass Course A.

      * The probability a student passes Course A is $ P(A\_p) = 0.7 $.
      * If a student passes Course A, the probability they also pass Course B is $ P(B\_p | A\_p) = 0.8 $.
      * احتمال قبولی دانشجو در هر دو درس A و B چقدر است؟
      * احتمال قبولی در A و مردودی در B چقدر است؟ (فرض کنید $P(B\_f | A\_p) = 1 - P(B\_p | A\_p)$)

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید $ A_p $ رویداد «دانشجو درس A را pass کند» باشد.
    فرض کنید $ B_p $ رویداد «دانشجو درس B را pass کند» باشد.
    فرض کنید $ B_f $ رویداد «دانشجو درس B را fail کند» باشد.

    داده شده:
    $ P(A_p) = 0.7 $
    $ P(B_p | A_p) = 0.8 $

    **بخش ۱: Probability a student passes both Course A and Course B.**
    می‌خواهیم بیابیم $ P(A_p \cap B_p) $.
    با استفاده از قانون ضرب برای احتمال شرطی:
    $ P(A_p \cap B_p) = P(B_p | A_p) \times P(A_p) $
    $ P(A_p \cap B_p) = 0.8 \times 0.7 = 0.56 $.

    **بخش ۲: Probability a student passes Course A but fails Course B.**
    به دنبال $ P(A_p \cap B_f) $ هستیم.
    اگر دانشجو درس A را pass کند، یا B را pass می‌کند یا fail.
    پس،

    $ $
    \شروع{تراز*}
    P(B_f | A_p) &= 1 - P(B_p | A_p) \\
    &= 1 - 0.8 \\
    &= 0.2
    \پایان{تراز کردن*}
    $$

    سپس، با استفاده از قانون ضرب:
    $ P(A_p \cap B_f) = P(B_f | A_p) \times P(A_p) $
    $ P(A_p \cap B_f) = 0.2 \times 0.7 = 0.14 $.
    ```

13. **سناریوی جایگزین آزمون پزشکی (قانون احتمال کل):** بیماری دیگری ۲٪ جمعیت را تحت تأثیر قرار می‌دهد. آزمون جدید ۹۵٪ احتمال شناسایی درست فرد آلوده (حساسیت) و ۱۰٪ احتمال مثبت کاذب برای فرد سالم دارد. احتمال کل تست مثبت برای فرد تصادفی چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید D رویداد «فرد بیماری دارد» و $ \neg D $ رویداد «فرد بیماری ندارد» باشد.
    فرض کنید + رویداد «فرد تست مثبت دهد» باشد.

    داده شده:
    * $ P(D) = 0.02 $ (prevalence of the disease)
    * $ P(+ | D) = 0.95 $ (sensitivity: test is positive given disease)
    * $ P(+ | \neg D) = 0.10 $ (false positive rate: test is positive given no disease)

    از $ P(D) $، می‌توانیم $ P(\neg D) $ را بیابیم:
    \begin{align*}
    P(\neg D) &= 1 - P(D) \\
    &= 1 - 0.02 \\
    &= 0.98
    \end{align*}

    باید احتمال کل اینکه فرد تصادفی تست مثبت دهد، $ P(+) $ را محاسبه کنیم. از قانون احتمال کل استفاده می‌کنیم:

    $ $
    \شروع{تراز*}
    P(+) &= P(+|D) \cdot P(D) + P(+|\neg D) \cdot P(\neg D) \\
    &= (0.95 \cdot 0.02) + (0.10 \cdot 0.98) \\
    &= 0.019 + 0.098 \\
    &= 0.117
    \پایان{تراز کردن*}
    $$

    پس، احتمال کل تست مثبت ۰٫۱۱۷ یا ۱۱٫۷٪ است.
    ```

14. **کاربرد قضیهٔ بیز:** Using the information from the "Alternative Medical Test Scenario" (Exercise 13): اگر فرد تصادفی تست مثبت دهد، احتمال بیمار بودن واقعی چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    از تمرین ۱۳، داریم:
    * $ P(D) = 0.02 $
    * $ P(\neg D) = 0.98 $
    * $ P(+ | D) = 0.95 $
    * $ P(+ | \neg D) = 0.10 $
    * $ P(+) = 0.117 $ (overall probability of testing positive)

    می‌خواهیم بیابیم $ P(D | +) $, the probability that a person has the disease given they tested positive.
    با استفاده از قضیهٔ بیز:
    $ $P(D | +) = \frac{P(+ | D) \cdot P(D)}{P(+)}$$
    محاسبه مقدار:

    $ $
    \begin{align*}
    P(D | +) &= \frac{0.95 \cdot 0.02}{0.117} \\
    &= \frac{0.019}{0.117} \\
    &\approx 0.16239
    \end{align*}
    $$

    بنابراین، اگر آزمایش فردی مثبت باشد، احتمال ابتلای او به این بیماری تقریباً 0.1624 یا حدود 16.24٪ است.
    توجه داشته باشید که حتی با یک آزمایش مثبت، به دلیل شیوع کم بیماری و میزان مثبت کاذب، احتمال ابتلا به این بیماری هنوز نسبتاً کم است.
    ```

15. **نرخ خطای سه چاپگر:** یک شرکت دارای سه چاپگر P1، P2 و P3 است که به ترتیب 30، 50 و 20 درصد از کل اسناد را چاپ می کنند. میزان خطای این چاپگرها به ترتیب 1%، 2% و 3% است. اگر سندی که به طور تصادفی انتخاب شده دارای خطا باشد، احتمال اینکه از P1 آمده باشد چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    اجازه دهید P1، P2، P3 رویدادهایی باشند که یک سند توسط چاپگر 1، 2 یا 3 چاپ شده است.
    فرض کنید E رویدادی باشد که یک سند دارای خطا است.

    به ما داده می شود:
    $ P(P1) = 0.30 $
    $ P(P2) = 0.50 $
    $ P(P3) = 0.20 $

    و احتمالات مشروط خطا با توجه به چاپگر:
    $ P(E | P1) = 0.01 $
    $ P(E | P2) = 0.02 $
    $ P(E | P3) = 0.03 $

    ابتدا احتمال کلی خطا را محاسبه می کنیم، $ P(E) $با استفاده از قانون احتمال کل:

    $ $
    \begin{align*}
    P(E) &= P(E | P1)P(P1) + P(E | P2)P(P2) + P(E | P3)P(P3) \\
    &= (0.01 \cdot 0.30) + (0.02 \cdot 0.50) + (0.03 \cdot 0.20) \\
    &= 0.003 + 0.010 + 0.006 \\
    &= 0.019
    \end{align*}
    $$

    حال، می‌خواهیم احتمال این را پیدا کنیم که سند از P1 آمده است، با توجه به اینکه خطا دارد: $ P(P1 | E) $.
    با استفاده از قضیه بیز:
    $ $P(P1 | E) = \frac{P(E | P1) \cdot P(P1)}{P(E)}$$
    محاسبهٔ مقدار:

    $ $
    \شروع{تراز*}
    P(P1 | E) &= \frac{0.01 \cdot 0.30}{0.019} \\
    &= \frac{0.003}{0.019} \\
    &\حدود 0.15789
    \پایان{تراز کردن*}
    $$

    پس اگر سند خطا داشته باشد، احتمال چاپ از Printer 1 حدود ۰٫۱۵۷۹ یا ۱۵٫۷۹٪ است.
    ```

16. **فیلتر سادهٔ هرزنامهٔ ایمیل:** Suppose 70% of emails are legitimate (ham) and 30% are spam.

      * The word "free" appears in 10% of spam emails.
      * The word "free" appears in 1% of ham emails.
        اگر ایمیل شامل کلمه free باشد، احتمال spam بودن چقدر است؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید S رویداد «ایمیل spam باشد» و H رویداد «ایمیل ham (معتبر) باشد».
    فرض کنید F رویداد «ایمیل شامل کلمه free باشد».

    داده شده:
    $ P(S) = 0.30 $
    $ P(H) = 0.70 $ (since $ P(H) = 1 - P(S) $)
    $ P(F | S) = 0.10 $ (probability "free" appears given spam)
    $ P(F | H) = 0.01 $ (probability "free" appears given ham)

    می‌خواهیم بیابیم $ P(S | F) $, the probability an email is spam given it contains "free".
    ابتدا به $ P(F) $، احتمال کل شامل بودن free، نیاز داریم. از قانون احتمال کل:

    $ $
    \شروع{تراز*}
    P(F) &= P(F | S)P(S) + P(F | H)P(H) \\
    &= (0.10 \cdot 0.30) + (0.01 \cdot 0.70) \\
    &= 0.030 + 0.007 \\
    &= 0.037
    \پایان{تراز کردن*}
    $$

    حالا، با استفاده از قضیهٔ بیز:
    $ $P(S | F) = \frac{P(F | S) \cdot P(S)}{P(F)}$$
    محاسبه مقدار:

    $ $
    \begin{align*}
    P(S | F) &= \frac{0.10 \cdot 0.30}{0.037} \\
    &= \frac{0.030}{0.037} \\
    &\approx 0.8108
    \end{align*}
    $$

    بنابراین، اگر یک ایمیل حاوی کلمه "رایگان" باشد، احتمال اسپم بودن آن تقریباً 0.8108 یا حدود 81.08٪ است.
    ```

17. **احتمال قرعه کشی ساده:** در یک مینی قرعه کشی، شما 2 عدد مجزا از مجموعه انتخاب می کنید. $ {1, 2, ..., 10} $. قرعه کشی همچنین 2 عدد متمایز را از این مجموعه انتخاب می کند. احتمال اینکه دو عدد انتخابی شما دقیقاً با دو عدد قرعه کشی مطابقت داشته باشند چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    ابتدا، بیایید تعداد کل روش‌هایی را که قرعه‌کشی می‌تواند 2 عدد متمایز از 10 را انتخاب کند، تعیین کنیم. ترتیبی که بخت‌آزمایی آنها را انتخاب می‌کند برای مسابقه مهم نیست، بنابراین از ترکیب‌ها استفاده می‌کنیم.

    $ $
    \begin{align*}
    \text{Total possible pairs} &= C(10, 2) = \binom{10}{2} \\
    &= \frac{10!}{2!(10-2)!} \\
    &= \frac{10 \times 9}{2 \times 1} \\
    &= 45
    \end{align*}
    $$

    45 جفت اعداد منحصر به فرد ممکن وجود دارد که قرعه کشی می تواند قرعه کشی کند.

    شما یک جفت عدد مشخص را انتخاب می کنید.
    تنها یک راه وجود دارد که جفت انتخابی شما دقیقاً جفت قرعه کشی شده باشد.

    بنابراین، احتمال تطابق دو عدد شما با دو عدد قرعه کشی این است:

    $ $
    \begin{align*}
    P(\text{match}) &= \frac{\text{Number of your successful pairs}}{\text{Total possible lottery pairs}} \\
    &= \frac{1}{45}
    \end{align*}
    $$
    ```

18. **انتخاب کمیته با نقش‌های مشخص:** کمیته 3 نفره از بین 5 مرد و 4 زن انتخاب می‌شود.

      * مجموع راه های تشکیل کمیته چقدر است؟
      * احتمال اینکه کمیته دقیقاً 2 مرد و 1 زن باشد چقدر است؟
      * اگر کمیته باید دارای رئیس، منشی و خزانه‌دار باشد و این نقش‌ها پس از انتخاب 3 نفر تعیین شود، از چند طریق می‌توان نقش‌ها را به یک کمیته 3 نفره اختصاص داد؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    کل افراد = $ 5 \text{ men} + 4 \text{ women} = 9 $ مردم

    **بخش 1: تعداد کل راه های تشکیل کمیته 3.**
    ترتیب انتخاب برای کمیته مهم نیست، بنابراین ما از ترکیب استفاده می کنیم.

    $ $
    \begin{align*}
    \text{Total ways} &= C(9, 3) = \binom{9}{3} \\
    &= \frac{9!}{3!(9-3)!} \\
    &= \frac{9 \times 8 \times 7}{3 \times 2 \times 1} \\
    &= 3 \times 4 \times 7 = 84
    \end{align*}
    $$

    84 کمیته احتمالی وجود دارد.

    **بخش 2: احتمال اینکه کمیته دقیقاً از 2 مرد و 1 زن تشکیل شده باشد.**
    تعداد روش های انتخاب 2 مرد از 5:
    $ $C(5, 2) = \binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10$$
    تعداد روش‌های انتخاب ۱ زن از ۴:
    $ $C(4, 1) = \binom{4}{1} = \frac{4}{1} = 4$$
    تعداد راه های تشکیل کمیته با 2 مرد و 1 زن = $ C(5, 2) \times C(4, 1) = 10 \times 4 = 40 $.

    $ $
    \begin{align*}
    P(\text{2 men, 1 woman}) &= \frac{\text{Ways to choose 2 men and 1 woman}}{\text{Total ways to choose 3 people}} \\
    &= \frac{40}{84} \\
    &= \frac{10}{21}
    \end{align*}
    $$

    **بخش 3: اگر کمیته باید دارای رئیس، منشی و خزانه‌دار باشد، از چند طریق می‌توان نقش‌ها را به یک کمیته 3 نفره اختصاص داد؟**
    هنگامی که یک کمیته خاص متشکل از 3 نفر (مثلاً شخص A، شخص B، شخص C) انتخاب شد، باید 3 نقش متمایز را به این 3 نفر اختصاص دهیم. این یک مشکل جایگشت است.
    تعداد روش های اختصاص نقش = $ P(3, 3) = 3! = 3 \times 2 \times 1 = 6 $.
    (صندلی می تواند هر یک از 3 نفر، منشی هر 2 نفر باقیمانده، خزانه دار آخرین نفر باشد).
    ```

19. **احتمال انتخاب سنگ مرمر:** یک کوزه دارای 4 تیله قرمز، 3 سبز و 2 تیله آبی است. شما به طور تصادفی 3 تیله را بدون جایگزینی انتخاب می کنید. احتمال اینکه از هر رنگ دقیقاً 1 رنگ (1 قرمز، 1 سبز، 1 آبی) انتخاب کنید چقدر است؟

    ```{admonition} پاسخ
    :class: dropdown

    کل تیله = $ 4 (\text{R}) + 3 (\text{G}) + 2 (\text{B}) = 9 $ سنگ مرمر
    ما در حال انتخاب 3 تیله هستیم.

    ابتدا تعداد کل راه‌های انتخاب 3 تیله از 9 مورد را پیدا کنید:
    
    $ $
    \begin{align*}
    \text{Total combinations} &= C(9, 3) = \binom{9}{3} \\
    &= \frac{9 \times 8 \times 7}{3 \times 2 \times 1} \\
    &= 3 \times 4 \times 7 = 84
    \end{align*}
    $$

    در مرحله بعد، تعداد راه هایی را برای انتخاب دقیقاً 1 سنگ مرمر قرمز، 1 سبز و 1 آبی پیدا کنید:
    * راه های انتخاب 1 سنگ مرمر قرمز از 4 = $ C(4, 1) = 4 $.
    * راه های انتخاب 1 سنگ مرمر سبز از 3 = $ C(3, 1) = 3 $.
    * راه های انتخاب 1 سنگ مرمر آبی از 2 = $ C(2, 1) = 2 $.

    تعداد روش های انتخاب 1 از هر رنگ حاصل این موارد است:
    راه ها (1R، 1G، 1B) = $ C(4, 1) \times C(3, 1) \times C(2, 1) = 4 \times 3 \times 2 = 24 $.

    احتمال انتخاب 1 رنگ از هر رنگ:

    $ $
    \begin{align*}
    P(\text{1R, 1G, 1B}) &= \frac{\text{Ways (1R, 1G, 1B)}}{\text{Total combinations}} \\
    &= \frac{24}{84} \\
    &= \frac{2}{7}
    \end{align*}
    $$
    ```

20. **امید ریاضی بازی سادهٔ تاس:** شما یک بازی انجام می دهید که در آن یک قالب شش وجهی منصفانه می اندازید.

      * اگر 6 رول کنید، 10 دلار برنده می شوید.
      * اگر 1 رول کنید، 4 دلار از دست می دهید.
      * اگر هر عدد دیگری (2، 3، 4، 5) رول کنید، 0 دلار برنده خواهید شد.
        ارزش مورد انتظار یک بار انجام این بازی چقدر است؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    اجازه دهید X متغیر تصادفی باشد که نشان دهنده برنده شدن بازی است.
    نتایج ممکن برای X عبارتند از $ 10, - $4, and $ 0.
    ما به احتمالات هر نتیجه نیاز داریم:
    * $P(X = 10) $ (غلت یک 6) = $ 1/6 $.
    * $ P(X = -4) $ (غلتان یک 1) = $ 1/6 $.
    * $ P(X = 0) $ (غلتان 2، 3، 4 یا 5) = $ 4/6 = 2/3 $.

    مقدار مورد انتظار $ E(X) $ به صورت زیر محاسبه می شود:
    $ $E(X) = \sum [x \cdot P(X=x)]$$

    $ $
    \شروع{تراز*}
    E(X) &= (10 \cdot P(X=10)) + (-4 \cdot P(X=-4)) + (0 \cdot P(X=0)) \\
    &= \left(10 \cdot \frac{1}{6}\right) + \left(-4 \cdot \frac{1}{6}\right) + \left(0 \cdot \frac{4}{6}\right) \\
    &= \frac{10}{6} - \frac{4}{6} + 0 \\
    &= \frac{6}{6} \\
    &= 1
    \پایان{تراز کردن*}
    $$

    امید ریاضی بازی ۱ دلار است. یعنی به‌طور میانگین، در بازی‌های زیاد انتظار برد ۱ دلار در هر بازی دارید.
    ```

21. **امید ریاضی بلیط قرعه‌کشی:** A charity sells 500 raffle tickets for $ 2 each. There is one grand prize of $300 and two second prizes of $ 50 each.

      * امید ریاضی خرید یک بلیط از دید خریدار چقدر است؟
      * آیا این بازی برای خریدار «منصفانه» است؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    هزینهٔ یک بلیط = \ $2.
    کل بلیط‌های فروخته‌شده = ۵۰۰.

    جوایز:
    * 1 grand prize of \ $ 300.
    * 2 second prizes of \ $50 each (total \ $ 100 in second prizes).

    فرض کنید X سود خالص از خرید یک بلیط باشد. The possible values for X are:
    
    * Win grand prize: Gain = \ $300 (prize) - \ $ 2 (cost) = \ $298.
        Probability = $ \frac{1}{500} $.
    * Win second prize: Gain = \ $ 50 (prize) - \ $2 (cost) = \ $ 48.
        Probability = $\frac{2}{500} $.
    * Win nothing: Gain = \ $ 0 (prize) - \ $2 (cost) = -\ $ 2.
        Number of losing tickets = $500 - 1 - 2 = 497 $.
        Probability = $ \frac{497}{500} $.

    **بخش ۱: Expected value of buying one ticket.**

    $ $
    \شروع{تراز*}
    E(X) &= \left(298 \cdot \frac{1}{500}\right) + \left(48 \cdot \frac{2}{500}\right) + \left(-2 \cdot \frac{497}{500}\right) \\
    &= \frac{298}{500} + \frac{96}{500} - \frac{994}{500} \\
    &= \frac{298 + 96 - 994}{500} \\
    &= \frac{394 - 994}{500} \\
    &= \frac{-600}{500} \\
    &= -\frac{6}{5} = -\ $1.20
    \پایان{تراز کردن*}
    $ $

    امید ریاضی خرید یک بلیط −\ $1.20 است. یعنی به‌طور میانگین، خریدار انتظار باخت \ $ 1.20 در هر بلیط دارد.

    **بخش ۲: Is this a "fair" game for the buyer?**
    A "fair" game is one where the expected value is 0. Since the expected value is -\ $1.20 (which is negative), this is not a fair game for the buyer. It is favorable to the seller (the charity). This is typical for raffles and lotteries, as they are designed to raise money.
    ```

22. **امید ریاضی تصمیم سرمایه‌گذاری:** You have $ 1000 to invest.

      * Investment A: 70% chance to return \ $1200 (profit \ $ 200), 30% chance to return \ $800 (loss \ $ 200).
      * Investment B: 40% chance to return \ $1500 (profit \ $ 500), 60% chance to return \ $900 (loss \ $ 100).
        امید ریاضی *سود* هر سرمایه‌گذاری را محاسبه کنید. کدام امید ریاضی سود بالاتری دارد؟

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    فرض کنید $X_A $ سود سرمایه‌گذاری A و $ X_B $ سود سرمایه‌گذاری B باشد.

    **Investment A:**
    * Profit if success: \ $ 1200 - \ $1000 = \ $ 200. Probability = 0.70.
    * Profit if failure (loss): \ $800 - \ $ 1000 = -\ $200. Probability = 0.30.
    امید ریاضی سود سرمایه‌گذاری A، $ E(X_A) $:

    $ $
    \شروع{تراز*}
    E(X_A) &= (200 \cdot 0.70) + (200- \cdot 0.30) \\
    &= 140 - 60 \\
    &= \ $80
    \پایان{تراز کردن*}
    $ $

    **Investment B:**
    * Profit if success: \ $1500 - \ $ 1000 = \ $500. Probability = 0.40.
    * Profit if failure (loss): \ $ 900 - \ $1000 = -\ $ 100. Probability = 0.60.
    امید ریاضی سود سرمایه‌گذاری B، $E(X_B) $ :

    $$
    \شروع{تراز*}
    E(X_B) &= (500 \cdot 0.40) + (-100 \cdot 0.60) \\
    &= 200 - 60 \\
    &= \ $ 140
    \پایان{تراز کردن*}
    $$

    **مقایسه:**
    امید ریاضی سود سرمایه‌گذاری A = \$80.
    امید ریاضی سود سرمایه‌گذاری B = \$140.

    سرمایه‌گذاری B امید ریاضی سود بالاتری دارد (\ $ 140) compared to Investment A (\ $80). Based solely on expected profit, Investment B would be the preferred choice.
    ```

23. **شبیه‌سازی پرتاب سکهٔ نامنصفانه:** A coin is biased such that it lands on Heads (H) with a probability of 0.6 and Tails (T) with a probability of 0.4.

      * Describe how you would simulate flipping this coin 1000 times.
      * After the simulation, how would you verify if the observed frequencies of Heads and Tails are close to their theoretical probabilities?

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    **بخش ۱: Describing the simulation.**
    برای شبیه‌سازی پرتاب این سکهٔ نامنصفانه ۱۰۰۰ بار:
    1.  **Initialize Counters:** Set a counter for Heads ( `count_H` ) to 0 and a counter for Tails ( `count_T` ) to 0.
    2.  **Loop for Trials:** Repeat the following steps 1000 times (for each flip):
        a.  **Generate Random Number:** Generate a random number `r` uniformly distributed between 0 and 1.
        b.  **Determine Outcome:**
            * If `r < 0.6`, consider the outcome to be Heads. Increment `count_H`.
            * Else (if `r >= 0.6`), consider the outcome to be Tails. Increment `count_T`.
    3.  **Record Results:** After 1000 flips, `count_H` will hold the total number of Heads observed, and `count_T` will hold the total number of Tails observed.

    **بخش ۲: Verifying observed frequencies.**
    پس از شبیه‌سازی:
    1.  **محاسبهٔ فراوانی‌های مشاهده‌شده (نسبت‌ها):**
        * $ $\text{Observed frequency of Heads} = \frac{\text{count\_H}}{1000}$$
        * $ $\text{Observed frequency of Tails} = \frac{\text{count\_T}}{1000}$$
    2.  **مقایسه با احتمال‌های نظری:**
        * Compare the observed frequency of Heads with the theoretical probability $ P(H) = 0.6 $.
        * Compare the observed frequency of Tails with the theoretical probability $ P(T) = 0.4 $.
    3.  **ارزیابی نزدیکی:**
        * The observed frequencies should be "close" to the theoretical probabilities. Due to the randomness of the simulation, they are unlikely to be exactly equal.
        * The Law of Large Numbers suggests that as the number of trials (flips) increases, the observed frequencies will converge towards the theoretical probabilities. For 1000 flips, we would expect the observed proportion of Heads to be around 0.6 (e.g., between 0.57 and 0.63 might be typical).
        * You can calculate the absolute difference: $ | \text{Observed Freq(H)} - 0.6 | $ and $ | \text{Observed Freq(T)} - 0.4 | $. Smaller differences indicate better agreement.
    ```

24. **شبیه‌سازی مسئلهٔ تولد (تقریبی):** The "Birthday Problem" asks for the probability that in a group of N people, at least two share a birthday.

      * Describe how you would simulate this for $ N=23 $ people to estimate this probability. Assume 365 days in a year and equal likelihood for each birthday.
      * How would you calculate the estimated probability from many simulation trials?

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    **بخش ۱: Describing one simulation trial for N=23 people.**
    برای شبیه‌سازی یک آزمایش برای گروه ۲۳ نفره:
    1.  **Generate Birthdays:** Create a list or array to store the birthdays of the 23 people. For each person, randomly assign a birthday, which is an integer from 1 to 365 (inclusive). Each day should have an equal chance of being selected.
    2.  **Check for Duplicates:** Examine the list of 23 birthdays. If there is at least one pair of identical birthdays in the list, then this trial results in a "match" (at least two people share a birthday). Otherwise, it's a "no match."
        * A simple way to check for duplicates is to add the birthdays to a set. If the size of the set is less than 23, it means there was at least one duplicate birthday.

    **بخش ۲: Calculating the estimated probability from many simulation trials.**
    برای برآورد احتمال:
    1.  **Initialize Counters:** Set a counter for the number of trials with a match (`match_count`) to 0. Define the total number of simulation trials to run (e.g., `total_trials = 10000`).
    2.  **Run Simulations:** Repeat the single trial simulation (described in Part 1) for `total_trials` times.
        * For each trial, if it results in a "match," increment `match_count`.
    3.  **Calculate Estimated Probability:** After all trials are complete, the estimated probability of at least two people sharing a birthday in a group of 23 is:
        $ $P(\text{shared birthday}) \approx \frac{\text{match\_count}}{\text{total\_trials}}$$

    برای $N=23$، احتمال نظری کمی بیش از ۵۰٪ است. با افزایش `total_trials`، شبیه‌سازی باید نتیجه‌ای نزدیک به این بدهد.
    ```

25. **شبیه سازی کارت های خاص کشیدن:** شما 3 کارت را از یک دسته استاندارد 52 کارتی بدون تعویض می کشید.

      * توضیح دهید که چگونه می‌توانید یک شبیه‌سازی طراحی کارت را تغییر دهید تا احتمال ترسیم دقیقاً 2 قلب از 3 کارت کشیده شده را برآورد کنید.
      * این احتمال تخمینی را چگونه محاسبه می کنید؟

    <!-- لیست پایانی -->

    ```{admonition} پاسخ
    :class: dropdown

    **بخش 1: اصلاح شبیه سازی طراحی کارت برای یک آزمایش.**
    برای شبیه سازی کشیدن 3 کارت و بررسی دقیق 2 قلب:
    1. **نماینده دسته:** نمایشی از یک دسته استاندارد 52 کارتی ایجاد کنید. هر کارت باید دارای یک کت و شلوار (قلب، الماس، کلوپ، بیل) و یک رتبه باشد. 13 قلب در دسته وجود دارد.
    2. ** به هم زدن و قرعه کشی:**
        الف  دسته را کاملاً به هم بزنید تا ترتیب کارت‌ها تصادفی شود.
        ب  3 کارت بالا را از دسته به هم ریخته بکشید.
    3. **شمار قلب:** 3 کارت کشیده شده را بررسی کنید. شمارش کنید که چند تا از آنها قلب هستند.
    4. **شرایط بررسی:** اگر تعداد قلب ها دقیقا 2 باشد، این آزمایش یک "موفقیت" است. در غیر این صورت، این یک "شکست" است.

    **بخش 2: محاسبه احتمال تخمینی.**
    برای تخمین احتمال کشیدن دقیقا 2 قلب در 3 کارت:
    1. **آغاز کردن شمارنده ها:** شمارنده ای را برای آزمایش های موفق ("تعداد_موفقیت") روی 0 تنظیم کنید. تعداد کل آزمایش های شبیه سازی را برای اجرا تعریف کنید (به عنوان مثال، "مجموع_آزمایش ها = 10000" یا بیشتر برای دقت بهتر).
    2. **اجرای شبیه سازی:** شبیه سازی آزمایشی منفرد (شرح داده شده در قسمت 1) را برای بارهای "کل_آزمایی" تکرار کنید.
        * برای هر آزمایش، اگر منجر به "موفقیت" شود (دقیقاً 2 قلب ترسیم شده است)، "شمار_موفقیت" را افزایش دهید.
    3. **محاسبه احتمال تخمینی:** پس از اتمام تمام آزمایشات، احتمال تخمین زده شده برابر است با:
        $ $P(\text{exactly 2 Hearts in 3 draws}) \approx \frac{\text{success\_count}}{\text{total\_trials}}$$

    **رویکرد نظری (برای مقایسه):**
    احتمال نظری را می‌توان با ترکیب‌ها محاسبه کرد:
    * Ways to choose 2 Hearts from 13: $ C(13, 2) = \binom{13}{2} = \frac{13 \times 12}{2} = 78 $.
    * Ways to choose 1 non-Heart from the remaining 39 non-Heart cards: $ C(39, 1) = \binom{39}{1} = 39 $.
    * Total ways to choose 3 cards from 52:

    $ $
    \شروع{تراز*}
    C(52, 3) &= \binom{52}{3} \\
    &= \frac{52 \times 51 \times 50}{3 \times 2 \times 1} \\
    &= 22100
    \پایان{تراز کردن*}
    $$

    *

    $ $
    \شروع{تراز*}
    P(\text{دقیقاً 2 قلب}) &= \frac{C(13، 2) \times C(39، 1)}{C(52، 3)} \\
    &= \frac{78 \times 39}{22100} \\
    &= \frac{3042}{22100} \\
    &\حدود 0.1376
    \پایان{تراز کردن*}
    $$

    نتیجهٔ شبیه‌سازی باید به این احتمال نظری میل کند.
    ```

26. **مجموعهٔ دادهٔ تایتانیک: بقا بر اساس جنس:** Using the Titanic dataset (commonly available in libraries like Seaborn or as a CSV):

      * Calculate $ P(\text{Survived} | \text{Sex='female'}) $ (the probability of survival given the passenger was female).
      * Calculate $ P(\text{Survived} | \text{Sex='male'}) $ (the probability of survival given the passenger was male).
      * What do these probabilities suggest about survival likelihood based on sex?

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    این تمرین شامل استفاده از مجموعه‌داده‌ای مانند تایتانیک برای محاسبهٔ احتمال‌های شرطی با Pandas است.

    **گام‌ها با Pandas:**
    1.  **Load Data:**
        * Import Pandas: `import pandas as pd`
        * Load the Titanic dataset (e.g., `df = sns.load_dataset('titanic')` if using Seaborn, or from a CSV).
        * The DataFrame (`df`) typically contains a 'survived' column (0 = No, 1 = Yes) and a 'sex' column (e.g., 'male', 'female').

    2.  **Calculate $ P(\text{Survived} | \text{Sex='female'}) $:**
        * **Filter for Females:** Create a subset of the DataFrame for female passengers:
            `df_female = df[df['sex'] == 'female']`
        * **Calculate Survival Rate for Females:** Within this subset, find the proportion who survived. The mean of the 'survived' column (if coded 0/1) gives this probability:
            `P_survived_given_female = df_female['survived'].mean()`

    3.  **Calculate $ P(\text{Survived} | \text{Sex='male'}) $:**
        * **Filter for Males:** Create a subset for male passengers:
            `df_male = df[df['sex'] == 'male']`
        * **Calculate Survival Rate for Males:**
            `P_survived_given_male = df_male['survived'].mean()`

    **این احتمال‌ها چه می‌گویند؟**
    * $ P(\text{Survived} | \text{Sex='female'}) $ indicates the proportion of female passengers who survived the Titanic disaster.
    * $ P(\text{Survived} | \text{Sex='male'}) $ indicates the proportion of male passengers who survived.
    * **مقایسه:** By comparing these two probabilities, we can infer the influence of a passenger's sex on their chance of survival. Historically, and as reflected in the data, $ P(\text{Survived} | \text{Sex='female'}) $ is typically significantly higher than $ P(\text{Survived} | \text{Sex='male'}) $. This reflects the "women and children first" protocol that was often (though not perfectly) followed during the evacuation. These conditional probabilities provide quantitative evidence of differing survival rates between these two groups.
    ```

27. **مجموعهٔ دادهٔ تایتانیک: کودکان بازمانده:** Using the Titanic dataset, define a "child" as someone with an age less than 18.

      * Calculate $ P(\text{Child} | \text{Survived}=1) $ (the probability a survivor was a child).
      * Calculate $ P(\text{Child} | \text{Survived}=0) $ (the probability a non-survivor was a child).
      * What might these probabilities indicate about the survival priority of children?

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    این تمرین از مجموعه‌دادهٔ تایتانیک و Pandas استفاده می‌کند. فرض کنید ستون‌های age و survived موجودند.

    **گام‌ها با Pandas:**
    1.  **Load Data & Define Child:**
        * Load the Titanic dataset as in the previous exercise.
        * Handle missing 'age' values (e.g., by dropping rows with missing age or imputation, though for this exercise, dropping might be simpler for a cleaner calculation on known ages). `df.dropna(subset=['age'], inplace=True)`
        * Create a 'is_child' boolean column: `df['is_child'] = df['age'] < 18`

    2.  **Calculate $ P(\text{Child} | \text{Survived}=1) $:**
        * This is the proportion of children among those who survived.
        * **Filter for Survivors:** Create a subset of the DataFrame for passengers who survived:
            `df_survived = df[df['survived'] == 1]`
        * **Calculate Proportion of Children among Survivors:**
            `P_child_given_survived = df_survived['is_child'].mean()` (The mean of a boolean column (True=1, False=0) gives the proportion of True values).

    3.  **Calculate $ P(\text{Child} | \text{Survived}=0) $:**
        * This is the proportion of children among those who did not survive.
        * **Filter for Non-Survivors:** Create a subset for passengers who did not survive:
            `df_notsurvived = df[df['survived'] == 0]`
        * **Calculate Proportion of Children among Non-Survivors:**
            `P_child_given_notsurvived = df_notsurvived['is_child'].mean()`

    **این احتمال‌ها ممکن است چه نشان دهند؟**
    * $ P(\text{Child} | \text{Survived}=1) $ tells us, of the group of people who survived, what fraction were children.
    * $ P(\text{Child} | \text{Survived}=0) $ tells us, of the group of people who did not survive, what fraction were children.
    * **Interpretation:** If $ P(\text{Child} | \text{Survived}=1) $ is notably higher than the overall proportion of children on board, and potentially higher than $ P(\text{Child} | \text{Survived}=0) $, it might suggest that children were given some priority in evacuation efforts. However, it's important to compare this with $ P(\text{Survived} | \text{Child}) $ as well for a fuller picture. A higher proportion of children among survivors than among non-survivors would lend support to the idea that children had a better chance of surviving relative to adults within the same outcome group.
    ```

28. **مجموعهٔ دادهٔ Iris: پیش‌بینی گونه بر اساس پهنای گلبرگ:** Load the Iris dataset (e.g., via scikit-learn or Seaborn).

      * Choose a threshold $ X $ for 'petal width (cm)' (e.g., $ X=1.5 \text{ cm} $).
      * Calculate $ P(\text{Species='virginica'} | \text{Petal Width} \> X) $.
      * Calculate $ P(\text{Species='setosa'} | \text{Petal Width} \< 0.5 \text{ cm}) $. (Note: Setosa typically has small petal width).
      * What do these conditional probabilities suggest about using petal width to help identify species?

    <!-- end list -->

    ```{admonition} پاسخ
    :class: dropdown

    این تمرین از مجموعه‌دادهٔ Iris، رایج در یادگیری ماشین، استفاده می‌کند.

    **گام‌ها با Pandas (و در صورت نیاز scikit-learn برای بارگذاری داده):**
    1.  **Load Data:**
        * `from sklearn.datasets import load_iris`
        * `import pandas as pd`
        * `iris = load_iris()`
        * `df = pd.DataFrame(data=iris.data, columns=iris.feature_names)`
        * `df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)`
        (The columns would include 'petal width (cm)' and 'species' with values like 'setosa', 'versicolor', 'virginica').

    2.  **Calculate $ P(\text{Species='virginica'} | \text{Petal Width} > 1.5 \text{ cm}) $:**
        * Let $ X = 1.5 $.
        * **Filter for Petal Width > X:** Create a subset of the DataFrame:
            `df_petal_gt_X = df[df['petal width (cm)'] > 1.5]`
        * **Calculate Proportion of Virginica:** Within this subset, find the proportion of 'virginica' species:
            `P_virginica_given_petal_gt_X = (df_petal_gt_X['species'] == 'virginica').mean()`

    3.  **Calculate $ P(\text{Species='setosa'} | \text{Petal Width} < 0.5 \text{ cm}) $:**
        * **Filter for Petal Width < 0.5:** Create a subset:
            `df_petal_lt_0_5 = df[df['petal width (cm)'] < 0.5]`
        * **Calculate Proportion of Setosa:** Within this subset, find the proportion of 'setosa' species:
            `P_setosa_given_petal_lt_0_5 = (df_petal_lt_0_5['species'] == 'setosa').mean()`

    **این احتمال‌های شرطی چه می‌گویند؟**
    * $ P(\text{Species='virginica'} | \text{Petal Width} > 1.5 \text{ cm}) $: If this probability is high (e.g., close to 1), it suggests that if an Iris flower has a petal width greater than 1.5 cm, it is very likely to be of the 'virginica' species. This indicates that large petal width is a strong indicator for 'virginica'.
    * $ P(\text{Species='setosa'} | \text{Petal Width} < 0.5 \text{ cm}) $: If this probability is very high (likely close to 1, as Setosa usually has small petal widths around 0.2-0.3 cm), it suggests that a petal width less than 0.5 cm is a very strong indicator that the species is 'setosa'.
    * **Overall:** These conditional probabilities demonstrate how a specific feature measurement (petal width) can be used to predict or classify the species of an Iris flower. High conditional probabilities indicate a strong relationship between the feature value and the class label, forming the basis of many classification algorithms.
    ```

29. **توضیح مغالطهٔ قمارباز:** مغالطهٔ قمارباز را با مثال پرتاب سکهٔ منصفانه توضیح دهید. اگر ۵ بار HHHHH بیاید، احتمال شیر در پرتاب ششم چقدر است؟ چرا برخی نادرست فکر می‌کنند احتمال تغییر می‌کند؟

    ```{admonition} پاسخ
    :class: dropdown

    **مغالطهٔ قمارباز:**
    مغالطهٔ قمارباز باور نادرستی است که اگر چیزی در یک دوره بیش از حد معمول رخ دهد، در آینده کمتر (یا برعکس) رخ خواهد داد. خطای استدلالی است که فرض می‌کند رویدادهای مستقل گذشته می‌توانند بر پیامدهای مستقل آینده اثر بگذارند.

    **مثال: پرتاب سکهٔ منصفانه**
    فرض کنید سکهٔ منصفانه را ۵ بار پرتاب کنید و هر بار شیر بیاید: HHHHH.
    * **سؤال:** احتمال شیر در پرتاب ششم چقدر است؟
    * **پاسخ درست:** The probability of getting Heads on the 6th flip is still $ \frac{1}{2} $ (or 0.5).

    **چرا احتمال همچنان ۱/۲ است:**
    * **Independence:** Each coin flip is an independent event. The outcome of one flip does not affect the outcome of any other flip. The coin has no "memory" of past results.
    * **Fair Coin:** A fair coin, by definition, has an equal probability of landing on Heads or Tails on any given flip ( $ P(H) = 0.5 $, $ P(T) = 0.5 $).

    **چرا برخی نادرست فکر می‌کنند احتمال تغییر می‌کند:**
    1.  **Misunderstanding of "Law of Averages":** People might think that to "even out" the results or get closer to the expected 50/50 distribution, a Tail is "due." They expect the long-run frequencies to correct themselves in the short term. While it's true that over a very large number of flips the proportion of Heads will tend towards 0.5, this doesn't mean future flips are dependent on past ones to achieve this balance.
    2.  **Pattern Seeking:** Humans are prone to seeing patterns, even in random sequences. A string of HHHHH might seem like a strong pattern that "needs" to be broken by a Tail.
    3.  **Representativeness Heuristic:** People may judge the probability of an event by how representative it is of a typical sequence. A sequence like HHHHHH seems less representative of randomness than, say, HHTHTH, leading them to believe the former is less likely to continue.

    احتمال ۶ شیر پیاپی (HHHHHH) از ابتدا واقعاً کم است ($\left(\frac{1}{2}\right)^6 = \frac{1}{64}$). اما *با فرض اینکه ۵ پرتاب اول уже شیر بوده*، احتمال *پرتاب بعدی* شیر، همان احتمال پایهٔ یک پرتاب یعنی $\frac{1}{2}$ است. پیامدهای قبلی «تاریخ سپری‌شده»اند و بر رویداد مستقل بعدی اثر نمی‌گذارند.
    ```

30. **مسئلهٔ مونتی هال:** مسئلهٔ مونتی هال را بیان کنید. راهبرد بهینه و دلیل کارکرد آن را توضیح دهید؛ در صورت امکان به احتمال‌های شرطی ارجاع دهید.

    ```{admonition} پاسخ
    :class: dropdown

    **بیان مسئلهٔ مونتی هال:**
    فرض کنید در یک مسابقه هستید و انتخاب بین سه در دارید. پشت یکی خودرو و پشت دیگران بز است.
    1.  You pick a door (say, Door #1).
    2.  The host, who knows what's behind the doors, opens another door (say, Door #3), which has a goat. (The host will always open a door with a goat and will never open your chosen door).
    3.  The host then asks you: "Do you want to switch your choice to the remaining closed door (Door #2), or do you want to stay with your original choice (Door #1)?"

    **آیا عوض کردن انتخاب به نفع شماست؟**

    **راهبرد بهینه:** Yes, you should switch. Switching doors doubles your probability of winning the car from $ \frac{1}{3} $ to $ \frac{2}{3} $.

    **توضیح و احتمال‌های شرطی:**

    فرض کنید C1، C2، C3 رویدادهای «خودرو پشت در ۱، ۲ یا ۳» باشند.
    در ابتدا، $P(C1) = P(C2) = P(C3) = \frac{1}{3}$.

    فرض کنید ابتدا در شمارهٔ ۱ را انتخاب می‌کنید.

    **سناریو ۱: با در شمارهٔ ۱ می‌مانید.**
    * You win if the car is actually behind Door #1.
    * The probability of this was $ \frac{1}{3} $ from the start. The host opening another door with a goat doesn't change the fact that your initial $ \frac{1}{3} $ chance was tied to Door #1 having the car.
    * پس، $ P(\text{Win} | \text{Stay}) = \frac{1}{3} $.

    **سناریو ۲: در را عوض می‌کنید.**
    بر اساس محل اولیهٔ خودرو چه می‌شود:
    * **Case A: Car is behind Door #1 (your initial pick).** Probability = $ \frac{1}{3} $.
        If you switch, you will lose (because the host will open either Door #2 or Door #3, both having goats, and you switch to the other goat).
    * **Case B: Car is behind Door #2.** Probability = $ \frac{1}{3} $.
        You initially picked Door #1. The host *must* open Door #3 (the other goat). If you switch, you switch to Door #2 and win.
    * **Case C: Car is behind Door #3.** Probability = $ \frac{1}{3} $.
        You initially picked Door #1. The host *must* open Door #2 (the other goat). If you switch, you switch to Door #3 and win.

    اگر عوض کنید، وقتی برنده می‌شوید که خودرو *پشت* انتخاب اولیه نبود.
    احتمال اینکه خودرو *پشت* انتخاب اولیه (در ۱) نبود

    $ $
    \شروع{تراز*}
    P(\neg C1) &= P(C2) + P(C3) \\
    &= \frac{1}{3} + \frac{1}{3} \\
    &= \frac{2}{3}
    \پایان{تراز کردن*}
    $$

    وقتی خودرو پشت انتخاب اولیه نیست، مجری مجبور است *در دیگر* با بز را باز کند و در خودرو تنها گزینهٔ عوض کردن می‌ماند.
    پس، $ P(\text{Win} | \text{Switch}) = \frac{2}{3} $.

    **دیدگاه احتمال شرطی (ساده‌شده):**
    فرض کنید $D_i$ رویداد «ابتدا در $i$ را انتخاب کنید» و $C_j$ رویداد «خودرو پشت در $j$» باشد. $P(C_j)=\frac{1}{3}$.
    فرض کنید در ۱ را انتخاب می‌کنید. $P(C_1)=\frac{1}{3}$. احتمال پشت در ۲ یا ۳ بودن خودرو $P(C_2 \cup C_3)=\frac{2}{3}$ است.
    عمل مجری در باز کردن در بز از {2, 3} اطلاعات می‌دهد. احتمال اولیه $\frac{2}{3}$ (خودرو پشت در ۲ یا ۳) را عملاً روی تنها در بستهٔ باقی‌مانده متمرکز می‌کند.

    اگر در اولیه درست بود (احتمال ۱/۳)، عوض کردن باخت است.
    اگر در اولیه نادرست بود (احتمال ۲/۳)، عوض کردن برد است.
    بنابراین، عوض کردن راهبرد بهتری است.
    ```
