#!/usr/bin/env python3
"""
Update Sukoon landing page with real product info.
"""

import re

with open('/home/z/my-project/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Meta description
html = html.replace(
    'وسادة سُكون - نوم أعمق وجودة أفضل. وسادة بتقنية الفوم المجزأ وميموري فوم مصممة لتخفيف الضغط ودعم العمود الفقري. توصيل لجميع أنحاء سلطنة عُمان.',
    'مخدة ميموري فوم بخاصية الفوم المجزأ من سُكون - دعم العمود الفقري وتصحيح أوضاع النوم. توصيل لجميع أنحاء سلطنة عُمان. 14 ر.ع للواحدة و 24 ر.ع للاثنتين.'
)

# 2. Keywords
html = html.replace(
    'وسادة سكون, مخدة, ميموري فوم, فوم مجزأ, نوم مريح, سلطنة عمان, وسادة طبية, وسادة عنق, مخدة عمانية',
    'مخدة سكون, ميموري فوم, فوم مجزأ, مخدة عمانية, وسادة نوم, دعم العمود الفقري, مخدة طبية, سلطنة عمان'
)

# 3. Hero badge
html = html.replace(
    '<span class="hero-badge">تقنية الفوم المجزأ وميموري فوم</span>',
    '<span class="hero-badge">مخدة ميموري فوم بخاصية الفوم المجزأ</span>'
)

# 4. Hero description
html = html.replace(
    'وسادة سُكون مصممة بعناية فائقة لتخفيف الضغط على الرقبة والكتفين، مزودة بتقنية الفوم المجزأ وميموري فوم لتمنحك راحة لا مثيل لها طوال الليل.',
    'مخدة سُكون بتقنية ميموري فوم والفوم المجزأ تدعم العمود الفقري وتصحح أوضاع النوم، مع حشو إضافي قابل للتعديل لتناسب راحتك.'
)

# 5. Hero stats
html = html.replace(
    '''<div class="stat">
                        <span class="stat-number">60\u00d743</span>
                        <span class="stat-label">سنتيمتر</span>
                    </div>
                    <div class="stat-divider"></div>
                    <div class="stat">
                        <span class="stat-number">3</span>
                        <span class="stat-label">أنواع متاحة</span>
                    </div>
                    <div class="stat-divider"></div>
                    <div class="stat">
                        <span class="stat-number">14</span>
                        <span class="stat-label">ميزة حصرية</span>
                    </div>''',
    '''<div class="stat">
                        <span class="stat-number">14</span>
                        <span class="stat-label">ر.ع</span>
                    </div>
                    <div class="stat-divider"></div>
                    <div class="stat">
                        <span class="stat-number">24</span>
                        <span class="stat-label">ر.ع للاثنتين</span>
                    </div>
                    <div class="stat-divider"></div>
                    <div class="stat">
                        <span class="stat-number">7</span>
                        <span class="stat-label">أيام ضمان</span>
                    </div>'''
)

# 6. Features section header
html = html.replace(
    '<span class="section-badge">لماذا سُكون؟</span>',
    '<span class="section-badge">مميزات المخدة</span>'
)
html = html.replace(
    'مميزات تجعل النوم <span class="highlight">تجربةً استثنائية</span>',
    'مميزات تجعل النوم <span class="highlight">أكثر راحة</span>'
)
html = html.replace(
    'صُممت وسادة سُكون بأحدث التقنيات لتمنحك أفضل تجربة نوم ممكنة، مع مراعاة كل التفاصيل التي تهم صحتك وراحتك',
    'مخدة ميموري فوم بخاصية الفوم المجزأ مصممة لتدعم العمود الفقري وتصحح أوضاع النوم والرقبة'
)

# 7. Feature cards - verified info
html = html.replace(
    '<h3>راحة فائقة</h3>\n                    <p>تقنية الفوم المجزأ وميموري فوم تتكيف مع شكل جسمك لتوفير راحة لا مثيل لها طوال ساعات النوم</p>',
    '<h3>دعم العمود الفقري</h3>\n                    <p>تدعم فقرات الظهر والرقبة والكتفين وتساعد على تصحيح أوضاع النوم لتستيقظ بدون ألم</p>'
)
html = html.replace(
    '<h3>تهوية متقدمة</h3>\n                    <p>تصميم يسمح بمرور الهواء بشكل فعّال للحفاظ على برودة الوسادة ومنع تراكم الحرارة أثناء النوم</p>',
    '<h3>تهوية فعّالة</h3>\n                    <p>ميزة التهوية الجيدة تحافظ على برودة المخدة وتمنع تراكم الحرارة أثناء النوم</p>'
)
html = html.replace(
    '<h3>تخفيف نقاط الضغط</h3>\n                    <p>توزيع متوازن للضغط على الرقبة والكتفين والرأس مما يقلل من التيبس والألم عند الاستيقاظ</p>',
    '<h3>حشو قابل للتعديل</h3>\n                    <p>تعبيئة إضافية تتيح لك تعديل ارتفاع وصلابة المخدة حسب راحتك الشخصية</p>'
)
html = html.replace(
    '<h3>مرونة استثنائية</h3>\n                    <p>مواد عالية المرونة تستجيب لحركات الجسم وتعود لشكلها الأصلي بسرعة لضمان دعم مستمر</p>',
    '<h3>ميموري فوم متقدم</h3>\n                    <p>تقنية ميموري فوم تتكيف مع شكل جسمك وتوزع الضغط بشكل متوازن لراحة لا مثيل لها</p>'
)
html = html.replace(
    '<h3>مضادة للحساسية</h3>\n                    <p>مواد معالجة خصيصًا لمقاومة مسببات الحساسية وحماية البشرة الحساسة أثناء النوم</p>',
    '<h3>غطاء قطني طبيعي</h3>\n                    <p>مصنوعة من القطن الطبيعي المريح والآمن للبشرة، مع ملمس ناعم يضمن نومًا هادئًا</p>'
)
html = html.replace(
    '<h3>مضادة للبكتيريا</h3>\n                    <p>طبقة حماية متطورة تمنع نمو البكتيريا والفطريات لضمان بيئة نوم صحية ونظيفة</p>',
    '<h3>قابلة للغسيل</h3>\n                    <p>قابلة للغسيل في الغسالة الآلية لضمان نظافة وصحة دائمة دون الحاجة لعناية خاصة</p>'
)
html = html.replace(
    '<h3>متانة طويلة الأمد</h3>\n                    <p>خامات عالية الجودة تضمن بقاء الوسادة بحالتها المثالية لسنوات دون فقدان دعمها أو شكلها</p>',
    '<h3>متانة عالية</h3>\n                    <p>خامات عالية الجودة تحافظ على شكل المخدة ودعمها لفترة طويلة من الاستخدام</p>'
)

# 8. Products section - replace with 2 pricing cards
# Replace section header
html = html.replace(
    '<span class="section-badge">تشكيلة الوسائد</span>',
    '<span class="section-badge">اطلب الآن</span>'
)
html = html.replace(
    'اختر الوسادة <span class="highlight">الأنسب لك</span>',
    'مخدة ميموري فوم <span class="highlight">بخاصية الفوم المجزأ</span>'
)
html = html.replace(
    'ثلاثة أنواع مصممة بعناية لتلبية مختلف الاحتياجات، كل منها يحمل بصمة سُكون في الجودة والراحة',
    'مخدة واحدة تدعم العمود الفقري وتصحح أوضاع النوم، مع حشو إضافي قابل للتعديل'
)

# Replace product 1 (نخبة) with مخدة واحدة
html = html.replace(
    'alt="وسادة نخبة"',
    'alt="مخدة ميموري فوم بخاصية الفوم المجزأ"'
)
html = html.replace(
    'src="assets/images/product-nukhba.jpg"',
    'src="assets/images/product-detail.jpg"'
)
html = html.replace(
    '<h3 class="product-name">وسادة نخبة</h3>',
    '<h3 class="product-name">مخدة واحدة</h3>'
)
html = html.replace(
    '<p class="product-type">بريميوم</p>',
    '<p class="product-type">ميموري فوم بخاصية الفوم المجزأ</p>'
)
html = html.replace(
    '<p class="product-desc">وسادة فاخرة بتقنية ميموري فوم متقدمة، توفر دعمًا مثاليًا للرقبة والكتفين مع ملمس حريري فائق النعومة</p>',
    '<div class="product-price"><span class="price-current">14 ر.ع</span></div>'
)
html = html.replace(
    '''<ul class="product-features">
                            <li>ميموري فوم عالي الكثافة</li>
                            <li>دعم شديد للعمود الفقري</li>
                            <li>غطاء حريري قابل للغسل</li>
                        </ul>''',
    '''<ul class="product-features">
                            <li>دعم العمود الفقري والرقبة</li>
                            <li>حشو إضافي قابل للتعديل</li>
                            <li>غطاء قطني طبيعي</li>
                        </ul>'''
)
html = html.replace(
    '%D9%88%D8%B3%D8%A7%D8%AF%D8%A9%20%D9%86%D8%AE%D8%A8%D8%A9',
    '%D9%85%D8%AE%D8%AF%D8%A9%20%D9%88%D8%A7%D8%AD%D8%AF%D8%A9'
)

# Replace product 2 (منوسة) with مخدتين
html = html.replace(
    'alt="وسادة منوسة"',
    'alt="مخدتين ميموري فوم بخاصية الفوم المجزأ"'
)
html = html.replace(
    'src="assets/images/product-manousa.jpg"',
    'src="assets/images/product-softness.jpg"'
)
html = html.replace(
    '<h3 class="product-name">وسادة منوسة</h3>',
    '<h3 class="product-name">مخدتين</h3>'
)
html = html.replace(
    '<p class="product-type">ناعمة</p>',
    '<p class="product-type">ميموري فوم بخاصية الفوم المجزأ</p>'
)
html = html.replace(
    '<p class="product-desc">وسادة ذات نعومة استثنائية بتقنية الفوم المجزأ، مثالية لمن يفضلون الملمس الناعم والانغماس في الراحة</p>',
    '<div class="product-price"><span class="price-current">24 ر.ع</span> <span class="price-was">28 ر.ع</span></div>'
)
html = html.replace(
    '''<ul class="product-features">
                            <li>فوم مجزأ فائق النعومة</li>
                            <li>ملمس قطني طبيعي</li>
                            <li>تهوية محسّنة</li>
                        </ul>''',
    '''<ul class="product-features">
                            <li>دعم العمود الفقري والرقبة</li>
                            <li>حشو إضافي قابل للتعديل</li>
                            <li>وفر 4 ر.ع عند طلب الاثنتين</li>
                        </ul>'''
)
html = html.replace(
    '%D9%88%D8%B3%D8%A7%D8%AF%D8%A9%20%D9%85%D9%86%D9%88%D8%B3%D8%A9',
    '%D9%85%D8%AE%D8%AF%D8%AA%D9%8A%D9%86'
)

# Remove product 3 (عريضة) entirely
p3_pattern = r'\s*<!-- Product 3: عريضة -->.*?</div>\s*</div>\s*</div>'
html = re.sub(p3_pattern, '', html, flags=re.DOTALL)

# 9. CTA section
html = html.replace(
    'جاهز لتجربة <span class="highlight">نومٍ مختلف؟</span>',
    'جاهز لتجربة <span class="highlight">نومٍ مريح؟</span>'
)
html = html.replace(
    'اطلب وسادة سُكون الآن واستمتع بنوم أعمق وجودة أفضل مع ضمان رضاك التام',
    'اطلب مخدة سُكون الآن واستمتع بدعم العمود الفقري وراحة لا مثيل لها'
)

# 10. Footer social links
html = html.replace(
    'href="https://instagram.com/sukoon"',
    'href="https://instagram.com/Sokoun_om"'
)
html = html.replace(
    'href="https://tiktok.com/@sukoon"',
    'href="https://tiktok.com/@Sokoun_om"'
)

# 11. JSON-LD
html = html.replace(
    '"name": "وسادة سُكون"',
    '"name": "مخدة ميموري فوم بخاصية الفوم المجزأ"'
)
html = html.replace(
    '"description": "وسادة بتقنية الفوم المجزأ وميموري فوم مصممة لتخفيف الضغط ودعم العمود الفقري"',
    '"description": "مخدة ميموري فوم بخاصية الفوم المجزأ تدعم العمود الفقري وتصحح أوضاع النوم مع حشو إضافي قابل للتعديل"'
)
html = html.replace(
    '"priceCurrency": "OMR",\n            "seller"',
    '"priceCurrency": "OMR",\n            "price": "14.00",\n            "seller"'
)

# 12. OG/Twitter
html = html.replace(
    'نوم أعمق وجودة أفضل مع وسادة سُكون بتقنية الفوم المجزأ وميموري فوم. توصيل لجميع أنحاء سلطنة عُمان.',
    'مخدة ميموري فوم بخاصية الفوم المجزأ من سُكون - دعم العمود الفقري وتصحيح أوضاع النوم. 14 ر.ع للواحدة و 24 ر.ع للاثنتين.'
)
html = html.replace(
    'نوم أعمق وجودة أفضل مع وسادة سُكون بتقنية الفوم المجزأ وميموري فوم',
    'مخدة ميموري فوم بخاصية الفوم المجزأ من سُكون - دعم العمود الفقري وتصحيح أوضاع النوم'
)

# 13. Hero image alt
html = html.replace(
    'alt="وسادة سكون"',
    'alt="مخدة ميموري فوم بخاصية الفوم المجزأ من سُكون"'
)

# 14. FAQ
html = html.replace(
    'مقاس المخدة 60×43 سنتيمتر',
    'مخدة ميموري فوم بخاصية الفوم المجزأ بحشو إضافي قابل للتعديل'
)
html = html.replace(
    '7 أيام ضمان على جميع المنتجات',
    '7 أيام ضمان - إذا لم تعجبك المخدة يمكنك استرجاعها خلال 7 أيام'
)

# Write the file
with open('/home/z/my-project/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
