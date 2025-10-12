#  Цифровой ассистент для планирования питания**

  

## **1) Рынок и сегментация (TAM / SAM / SOM)**

  

**Контекст и опоры для расчётов**

- Онлайн-заказы продуктов в РФ в 2023 г.: **917,5 млрд ₽** (+47% г/г), доля e-grocery близка к 4,7% в IV кв. 2023. 
    
- Интернет-проникновение: **~88,9% населения** (данные Росстата/РИА, 2024). 
    
- Доля городского населения: **~75%** (109–110 млн чел). 
    
- Регулярно/периодически заказывают продукты онлайн: **~35% россиян** (опрос ЮKassa, 2025). 
    

  

**TAM (адресуемый рынок)**

- Пользовательский TAM (чел.): городское население с доступом к e-grocery и смартфону. Консервативно **30–50 млн** потенциальных пользователей (фильтры: урбанизация × интернет × интерес к онлайн-заказам).
    
- Денежный TAM (₽/год): ориентиром служит масштаб e-grocery. Даже **2% комиссия** от 917,5 млрд ₽ ≈ **~18 млрд ₽/год** как верхняя граница «посреднической» модели; при подписке **500 ₽/мес** и 30 млн плательщиков — **~180 млрд ₽/год** (теоретический потолок). Реалистичный диапазон «достижимого TAM на старте» — **~15–20 млрд ₽/год** (неполный охват и смешанная монетизация). 
    

  

**SAM (сервисируемый рынок)**

- Фокус: активные онлайн-покупатели в крупных агломерациях (25–45, занятые профи и семьи среднего дохода).
    
- Оценка: **~10–15 млн** пользователей, которых реально обслужить в ближайшие годы (география + привычки + готовность планировать меню).
    
- Денежно: при **10% платящих** с ARPU≈**6000 ₽/год** + комиссии с остальной базы — **~3–5 млрд ₽/год**.
    

  

**SOM (доля, достижимая за 24 мес.)**

- Цель: **~0,1–0,3 млн MAU** (≈1–2% от SAM) за 24 месяца.
    
- Выручка: при **5% конверсии в подписку**, **ARPPU 500 ₽/мес**, плюс комиссия с бесплатных пользователей — **~50–100 млн ₽/год** порядка величины.
    
- Конкурентная среда: «последняя миля» (Самокат, Яндекс Лавка, СберМаркет, X5), meal kits (Шефмаркет, Elementaree; в 2021 HelloFresh инвестировал в Шефмаркет), доставка готовой еды (Яндекс Еда и др.). 
    

  

**Ключевые допущения (прозрачно)**

- Смешанная монетизация: подписка + комиссия с заказов.
    
- Средняя частота планирования — **неделя**; средний чек заказа продуктов — **пара тысяч ₽** (для масштаба, не для точных расчётов).
    
- Драйверы спроса: экономия времени и снижение стресса выбора; барьеры — привычка к офлайн-покупкам и доверие к качеству доставки (в расчётах учтено через консервативный SAM/SOM).
    

---

## **2) Критическая метрика активации (магическое число)**

  

**Гипотеза активации**

- Порог **X+Y** в первые 7 дней:
    
    - **X = ≥5 блюд** добавлено в план (будни одной недели),
        
    - **Y = ≥1 оформленный заказ продуктов**.
        
    
- Альтернатива: **2 полных недельных плана** + заказ(ы) в первый месяц.
  

**Почему может сработать -  Пользователь проживает полный цикл ценности (план → список → заказ → готовка), что резко повышает субъективную полезность и вероятность возврата.


---

## **3) Циклы роста (Growth Loops)**

  

**Value Loop (ценность ↔ данные)**

- Больше планирования ⇒ больше поведенческих данных ⇒ **лучше персонализация** (рецепты, списки, остатки) ⇒ выше полезность ⇒ выше удержание ⇒ ещё больше планирования. Усиливает LTV.


**Viral Loop (рефералы и шаринг)**

- Шеринг недельных меню/списков и UGC (фото блюд, отзывы) + **реферальные бонусы**. Цель — K-factor > 1 в ключевых когортах. Классический реферальный приём (аналогичный логике Dropbox) валидирован рынком.
  

**Commerce/Revenue Loop (самофинансирование)**

- Заказ → комиссия (например, **~2–3%** от партнёрских доставок) → реинвест в перфоманс, рефералы и продукт → рост заказов/базы → рост комиссий. KPI: **LTV:CAC ≥ 3:1** как нижний здоровый порог; таргет **4:1**. 

---

## **4) Целевые метрики на горизонте 24 месяцев**

  

**Приоритет: удержание ядра и окупаемость привлечения.**

- **CAC**: $20–40 на масштабе; целевой коридор **~$20–30** (2000–3000 ₽) по мере роста органики и рефералов. Валидируем через LTV:CAC. (Бенчмарк LTV:CAC ≥3:1.) 
    
- **ARPPU / ARPU**: ARPPU ≈ **500–600 ₽/мес** (цена подписки). Совокупный **ARPU базы ~40–50 ₽/мес** при ~5% платящих + комиссионный доход.
    
- **Retention**:
    
    - **Weekly** целевой **50–60%** (привычка еженедельного планирования).
        
    - **Monthly (D30)** ориентир **20–30%** (выше среднего для шоппинг-приложений; рынок в среднем заметно ниже). 
        
    
- **Churn (платные)**: старт **8–10%/мес**, к 24-му месяцу **5–7%/мес** (в «зелёной зоне» по B2C-бенчмаркам). Допуски: лучшие практики для B2C — 3–5%/мес, <2% — выдающийся уровень. 
    
- **LTV : CAC**: целевой **~4:1** (минимум 3:1). Рычаги: снижение churn, рост частоты заказов (комиссии), рост доли платящих. 
    
- **Конверсия в подписку**: **~5%** (2–3% на раннем этапе; 7–10% в зрелых когортах с высокой активацией). Отслеживаем uplift у «активированных» когорт.


  

**Ключевые триггеры достижения плана**

- «Магическое число» закрыто у **≥50–60%** новичков (разгоняет weekly retention и конверсию).
    
- Контент-/UGC-механики и партнёрские акции снижают CAC.
    
- Commerce-loop поддерживает **самофинансирование** роста на базе комиссий.
    
- Контрольные пороги: LTV:CAC < 2:1 или churn платных >15%/мес — **красный флаг**, при котором приоритетно улучшаем удержание/ценность, а не масштабируемся.

  

**Риски и смягчение**

- **Поведенческие барьеры** (привычка к офлайн-покупкам, доверие к качеству доставки): адресуем через гарантии качества партнёров, прозрачные замены и SLA, а также экономику «меньше импульсных трат → экономия».
    
- **Конкуренция экосистем**: фокус на кросс-платформенных интеграциях и нейтральности к ритейлу (лучшие цены/акции вне одной экосистемы).
    
- **Сезонность**: прогноз и анти-чёрн кампании на «провальные» недели; годовые планы/семейные тарифы для «зашивки» сезонности.
    

---

### **Источники**


Рынок e-grocery в России, объёмы и игроки

- https://infoline.spb.ru/news/?news=302423
    
- https://www.retail.ru/news/infoline-po-itogam-iv-kvartala-2024-goda-samokat-ustupil-kh5-group-liderstvo-na–27-fevralya-2025-261493/
    
- https://russretail.ru/mnenia/26805-infoline-po-itogam-2024-goda-segment-e-grocery-vyrastet-na-57-do-145-trln-rublej.html
    
- https://logistics.ru/internet-torgovlya-i-fulfilment-produkty-pitaniya-i-fresh/e-grocery-2025-rynok-rastet-lider
    
- https://datainsight.ru/all-egrocery-2024
    
- https://tadviser.com/index.php/Article%3AOnline_food_sales_in_Russia
    
- https://www.x5.ru/en/news/x5-becomes-market-leader-in-online-sales/
    
- https://tass.ru/ekonomika/23194655
    
- https://shoppers.media/news/20844_iandeks-uvelicil-vyrucku-iandeks-marketa-i-servisov-dostavki-edy-na-45-v-2024-g
    
- https://www.comnews.ru/content/231756/2024-02-27/2024-w09/1008/sbermarket-chto-god-2023-y-prines-chto-2024-y-gotovit
    
- https://sber.pro/publication/rossiiskii-rinok-e-grocery-mozhet-virasti-do-2-trln-rublei-v-sleduyuschem-godu/
    

  

Интернет-проникновение и урбанизация

- https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS?locations=RU
    
- https://datareportal.com/reports/digital-2024-russian-federation
    
- https://digital.gov.ru/uploaded/files/internet-v-rossii-v-2022-2023-godah.pdf
    

  

Meal kits и конкуренты

- https://www.rbc.ru/business/15/09/2021/6140c5c59a794756730dc1f3
    
- https://www.forbes.ru/biznes/440023-servis-dostavki-blud-s-receptami-hellofresh-investiroval-v-rossijskij-analog
    
- https://rb.ru/news/hellofresh-became-a-co-owner-chefmarket/
    
- https://logirus.ru/news/e-commerce/kapital_-shefmarket-_stal_bolee_-evropeyskim.html
    
- https://www.annualreports.com/HostedData/AnnualReportArchive/h/hellofresh-se_2021.pdf
    

  

Методология «магического числа» и аналитика

- https://docs.mixpanel.com/docs/reports/apps/signal
    
- https://mixpanel.com/blog/mixpanel-signal-launch/
    
- https://docs.mixpanel.com/docs/reports/retention
    
- https://mixpanel.com/blog/2024-mixpanel-benchmarks-report/
    
- https://mixpanel.com/benchmarks
    
- https://docs.mixpanel.com/changelogs/2024-03-07-benchmark
    

  

Бенчмарки retention, churn, конверсия в подписку

- https://www.businessofapps.com/data/app-retention-rates/
    
- https://onesignal.com/mobile-app-benchmarks-2024
    
- https://www.revenuecat.com/state-of-subscription-apps-2024/
    
- https://www.revenuecat.com/state-of-subscription-apps-2025/
    
- https://recurly.com/research/churn-rate-benchmarks/
    
- https://recurly.com/content/state-of-subscriptions-report/
    
- https://www.lennysnewsletter.com/p/what-is-a-good-free-to-paid-conversion
    

  

Юнит-экономика: LTV, CAC и правила «3×»

- https://www.forentrepreneurs.com/ltv/
    
- https://www.forentrepreneurs.com/ltv-cac/
    
- https://www.forentrepreneurs.com/startup-killer/
    
- https://chartmogul.com/saas-metrics/ltv/
    
- https://chartmogul.com/blog/cac-ltv-waste-money/
    
- https://chartmogul.com/blog/customer-acquisition-cost-cac/
    
- https://www.thesaascfo.com/calculate-customer-lifetime-value-cltv/
    

  

Импульсные покупки и стресс/доверие к доставке (иллюстративные опросы)

- https://adindex.ru/news/researches/2025/07/23/335602.phtml
    
- https://plusworld.ru/articles/67750/
    
- https://e-pepper.ru/news/kak-rossiyane-delayut-impulsivnye-pokupki-v-onlayne.html
    
- https://tass.ru/obschestvo/22123049
    
- https://tass.ru/obschestvo/24081585
    
- https://wciom.ru/analytical-reviews/analiticheskii-obzor/vam-dostavka
    
- https://promo.yookassa.ru/journal/tpost/k1oax7kun1-kazhdii-pyatii-rossiyanin-zakazivaet-pro
    
- https://www.cnews.ru/news/line/2025-05-29_kazhdyj_pyatyj_rossiyanin_zakazyvaet
    
- https://www.malls.ru/rus/news/yukassa-35-rossiyan-zakazyvayut-produkty-cherez-internet.shtml

