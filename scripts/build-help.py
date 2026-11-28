#!/usr/bin/env python3
"""Builds the how-to guides in help/ (English) and help/th/ (Thai).

One language per URL so search engines index each guide in its own language.
Edit the text here, then run:  python3 scripts/build-help.py
Screens are real Simulator screenshots in img/help/ (700 px wide WebP).
Website rules: never mention the free item limit, Pro or its price.
"""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://datebell.github.io'
STORE = 'https://apps.apple.com/app/id6821503223'
APPLE_CANCEL = {'en': 'https://support.apple.com/en-us/118428', 'th': 'https://support.apple.com/th-th/118428'}

def url(lang, slug):
    base = '/help/' if lang == 'en' else '/help/th/'
    return base + (slug + '.html' if slug else '')

UI = {
    'en': {'home': 'Home', 'features': 'Features', 'guides': 'Guides', 'steps': 'Step by step',
           'free': 'Free on iPhone', 'ig': 'Follow <b>@datebell.app</b> on Instagram',
           'more': 'More guides', 'support': 'Support', 'privacy': 'Privacy Policy', 'step': 'Step',
           'badge_alt': 'Download on the App Store', 'now': 'now', 'short': 'Short answer'},
    'th': {'home': 'หน้าแรก', 'features': 'ฟีเจอร์', 'guides': 'คู่มือ', 'steps': 'ทีละขั้น',
           'free': 'ฟรีบน iPhone', 'ig': 'ติดตาม <b>@datebell.app</b> บน Instagram',
           'more': 'คู่มืออื่น', 'support': 'ช่วยเหลือและติดต่อ', 'privacy': 'นโยบายความเป็นส่วนตัว', 'step': 'ขั้นที่',
           'badge_alt': 'ดาวน์โหลดบน App Store', 'now': 'ตอนนี้', 'short': 'คำตอบสั้นๆ'},
}

# ring = (x%, y%, w%, h%) on the 700x1522 screen; ntf = (title, body) notification card drawn on top
GUIDES = [
  {
    'slug': 'free-trial-reminder-iphone',
    'en': {
      'title': 'How to get reminded before a free trial ends on iPhone',
      'meta': 'Free trials turn into paid plans on the day they end. Here’s how to get a reminder on your iPhone 2 days before, so there’s time to cancel.',
      'card': 'Get a reminder 2 days before any free trial turns into a paid plan.',
      'h1': 'How to get reminded before a <em>free trial ends</em> on iPhone',
      'short': 'Add the trial to Datebell with the date it ends. Datebell reminds you 2 days before, so there’s time to cancel. Apple suggests cancelling <a href="{apple}" rel="noopener">at least 24 hours before a trial ends</a>, and many other services charge on that day too.',
      'steps': [
        ('Tap + and pick the service',
         'Open Datebell and tap <b>+</b> on Home. Under <b>Subscriptions</b>, search for the service or pick it from the list. Over 1,200 services come with their name and logo. Not there? Tap <b>Add your own</b>.',
         'add-list', [(3, 23, 94, 6.4), (3, 48.6, 94, 14.2)], None),
        ('Turn on Free trial and set the end date',
         'Set the price you’ll pay after the trial, turn on <b>Free trial</b> and choose the day it ends. The reminder then tells you what you’d pay.',
         'trial-form', [(3, 65.4, 94, 13.2)], None),
        ('Save. Datebell rings 2 days before',
         'The reminder comes 2 days before the trial ends, at your reminder time (9:00 AM unless you change it in Settings). On Home, the trial is marked Free trial with the days left.',
         'trial-home', [(4, 63, 92, 12.6)], ('Free trial ends in 2 days', 'Your Disney+ free trial ends in 2 days. Cancel at least a day before if you don’t want to pay.')),
        ('Cancel it, or keep it',
         'Open the trial to see when it ends and what it will cost. Tap <b>Cancel it</b> to see how to cancel that service, and <b>How to cancel</b> for its steps. If you keep it, Datebell carries on as a normal subscription and reminds you before each payment.',
         'trial-item', [(19, 42.6, 62, 6.2), (3, 81.4, 94, 7.6)], None),
      ],
      'extra': [
        ('Where to find the date a trial ends',
         '<p>For trials billed by Apple, open <b>Settings</b>, tap your name, then <b>Subscriptions</b> (<a href="{apple}" rel="noopener">Apple’s guide</a>). For trials you started on a website, check the welcome email or the account page on that site.</p>'),
        ('Can I do it without an app?',
         '<p>Yes. In the Reminders app, add a reminder for 2 days before the trial ends. Datebell does the counting for you, keeps the price and the way to cancel with it, and keeps reminding you before each payment if you stay.</p>'),
      ],
    },
    'th': {
      'title': 'วิธีตั้งเตือนก่อนทดลองใช้ฟรีหมด บน iPhone',
      'meta': 'ทดลองใช้ฟรีหลายแอปเริ่มตัดเงินในวันที่หมด วิธีตั้งให้ iPhone เตือนก่อนหมด 2 วัน จะได้มีเวลายกเลิกทันก่อนโดนตัดเงิน',
      'card': 'ให้ iPhone เตือนก่อนทดลองใช้ฟรีหมด 2 วัน ยกเลิกทันก่อนโดนตัดเงิน',
      'h1': 'วิธีตั้งเตือนก่อน<em>ทดลองใช้ฟรีหมด</em> บน iPhone',
      'short': 'เพิ่มทดลองใช้ฟรีไว้ใน Datebell พร้อมวันที่หมด แล้ว Datebell จะเตือนก่อนหมด 2 วัน มีเวลายกเลิกทันก่อนตัดเงิน Apple แนะนำให้<a href="{apple}" rel="noopener">ยกเลิกก่อนหมดอย่างน้อย 24 ชั่วโมง</a> และบริการอื่นหลายเจ้าก็เริ่มตัดเงินในวันที่หมดเช่นกัน',
      'steps': [
        ('แตะ + แล้วเลือกบริการ',
         'เปิด Datebell แล้วแตะ <b>+</b> ที่หน้าแรก ในหมวด<b>ค่าสมาชิก</b> ค้นชื่อหรือเลือกจากรายการ มีกว่า 1,200 บริการพร้อมชื่อและโลโก้ ถ้าไม่เจอ แตะ<b>เพิ่มชื่อเอง</b>',
         'add-list', [(3, 23, 94, 6.4), (3, 48.6, 94, 14.2)], None),
        ('เปิดทดลองใช้ฟรี แล้วใส่วันที่หมด',
         'ใส่ราคาที่ต้องจ่ายหลังหมดทดลอง เปิดสวิตช์<b>ทดลองใช้ฟรี</b> แล้วเลือกวันที่หมด การแจ้งเตือนจะบอกว่าถ้าไม่ยกเลิกจะเสียเท่าไหร่',
         'trial-form', [(3, 65.4, 94, 13.2)], None),
        ('บันทึก แล้ว Datebell จะเตือนก่อน 2 วัน',
         'การแจ้งเตือนมาก่อนทดลองฟรีหมด 2 วัน ตามเวลาเตือนของคุณ (9:00 น. ถ้าไม่ได้เปลี่ยนในตั้งค่า) หน้าแรกมีป้ายทดลองฟรี พร้อมบอกว่าเหลืออีกกี่วัน',
         'trial-home', [(4, 63, 92, 12.6)], ('ทดลองใช้ฟรีหมดในอีก 2 วัน', 'ทดลองใช้ฟรี Disney+ จะหมดในอีก 2 วัน ถ้าไม่ใช้ต่อ ยกเลิกล่วงหน้าอย่างน้อย 1 วัน')),
        ('ยกเลิก หรือใช้ต่อ',
         'เปิดรายการเพื่อดูว่าหมดวันไหน และจะต้องจ่ายเท่าไหร่ แตะ<b>ไปยกเลิก</b> เพื่อดูว่ายกเลิกบริการนั้นได้อย่างไร หรือแตะ<b>วิธียกเลิก</b> เพื่อดูขั้นตอน ถ้าใช้ต่อ Datebell จะติดตามเป็นค่าสมาชิกปกติ และเตือนก่อนตัดเงินทุกรอบ',
         'trial-item', [(19, 42.6, 62, 6.2), (3, 81.4, 94, 7.6)], None),
      ],
      'extra': [
        ('ดูวันที่ทดลองใช้ฟรีหมดได้ที่ไหน',
         '<p>ถ้าสมัครผ่าน Apple เปิด<b>การตั้งค่า</b> แตะชื่อของคุณ แล้วแตะ<b>การสมัครรับ</b> (<a href="{apple}" rel="noopener">คู่มือของ Apple</a>) ถ้าสมัครผ่านเว็บไซต์ ดูในอีเมลต้อนรับ หรือหน้าบัญชีบนเว็บนั้น</p>'),
        ('ไม่ใช้แอปได้ไหม',
         '<p>ได้ ตั้งเตือนในแอปเตือนความจำ ให้ตรงกับ 2 วันก่อนหมด ส่วน Datebell นับวันให้เอง เก็บราคาและวิธียกเลิกไว้ในรายการเดียวกัน และเตือนก่อนตัดเงินทุกรอบถ้าคุณใช้ต่อ</p>'),
      ],
    },
  },
  {
    'slug': 'track-subscription-renewals-iphone',
    'en': {
      'title': 'How to track subscription renewals on iPhone',
      'meta': 'Keep every subscription in one list on your iPhone, get a reminder before each renewal, and see what you spend in a month and a year.',
      'card': 'One list for every subscription, a reminder before each renewal, and the total.',
      'h1': 'How to track <em>subscription renewals</em> on iPhone',
      'short': 'Add each subscription to Datebell with its price, how often you pay and the billing date. Datebell reminds you 7 days and 1 day before each charge and on the day, and adds up what’s due in the next 30 days and in a year.',
      'steps': [
        ('Tap + and pick the service',
         'Tap <b>+</b> on Home, keep <b>Subscriptions</b> selected and search for the service. The name and logo fill in for you.',
         'add-list', [(3, 23, 94, 6.4)], None),
        ('Add the price, how often and the billing date',
         'Type the price per charge, or tap <b>Choose a plan</b> for many popular services. Pick Monthly, Yearly, Weekly or Other, then the billing date. A past date is fine: future charges follow the same day. 15 currencies are supported.',
         'sub-form', [(3, 45.8, 94, 18.8), (3, 70.8, 94, 6.4), (3, 82.6, 94, 6.4)], None),
        ('Save, and see your totals',
         'Home shows what’s due in the next 30 days and what it all costs in a year, with the next charge at the top.',
         'trial-home', [(3, 32.6, 94, 12.2)], None),
        ('Get a reminder before every charge',
         'Datebell reminds you 7 days and 1 day before each payment, and on the day, at your reminder time. If a plan you picked from the list goes up in price, the reminder tells you.',
         'sub-detail', [(3, 59, 94, 11.4)], None),
      ],
      'extra': [
        ('Why not just use the iPhone Subscriptions list?',
         '<p>The list in <b>Settings</b> › your name › <b>Subscriptions</b> only shows subscriptions billed by Apple. Plans you pay on a website, through your phone provider or with a card each month don’t appear there (<a href="{apple}" rel="noopener">Apple</a>). Datebell keeps them all in one list.</p>'),
        ('Once a month: is it still worth it?',
         '<p>Datebell asks once a month about what you pay for. Keep what you use, and spot what you don’t.</p>'),
      ],
    },
    'th': {
      'title': 'วิธีติดตามวันต่ออายุค่าสมาชิก บน iPhone',
      'meta': 'รวมค่าสมาชิกทุกอย่างไว้ในรายการเดียวบน iPhone เตือนก่อนตัดเงินทุกรอบ และเห็นยอดที่ต้องจ่ายต่อเดือนและต่อปี',
      'card': 'รวมค่าสมาชิกไว้ที่เดียว เตือนก่อนตัดเงินทุกรอบ พร้อมยอดรวม',
      'h1': 'วิธีติดตาม<em>วันต่ออายุค่าสมาชิก</em> บน iPhone',
      'short': 'เพิ่มค่าสมาชิกแต่ละรายการไว้ใน Datebell พร้อมราคา รอบการจ่าย และวันที่ตัดเงิน Datebell จะเตือนก่อนตัดเงิน 7 วัน 1 วัน และในวันจริง พร้อมรวมยอดที่ต้องจ่ายใน 30 วันข้างหน้าและทั้งปี',
      'steps': [
        ('แตะ + แล้วเลือกบริการ',
         'แตะ <b>+</b> ที่หน้าแรก เลือกหมวด<b>ค่าสมาชิก</b> แล้วค้นชื่อบริการ ชื่อและโลโก้มาให้เอง',
         'add-list', [(3, 23, 94, 6.4)], None),
        ('ใส่ราคา รอบการจ่าย และวันที่ตัดเงิน',
         'พิมพ์ราคาต่อรอบ หรือแตะ<b>เลือกแพ็กเกจ</b> สำหรับบริการยอดนิยม เลือกรายเดือน รายปี รายสัปดาห์ หรืออื่นๆ แล้วใส่วันที่ตัดเงิน ใส่วันที่ผ่านมาแล้วก็ได้ รอบถัดไปจะยึดวันเดียวกัน รองรับ 15 สกุลเงิน',
         'sub-form', [(3, 45.8, 94, 18.8), (3, 70.8, 94, 6.4), (3, 82.6, 94, 6.4)], None),
        ('บันทึก แล้วดูยอดรวม',
         'หน้าแรกบอกยอดที่ต้องจ่ายใน 30 วันข้างหน้า และรวมทั้งปีเท่าไหร่ รายการที่จะตัดเงินถัดไปอยู่บนสุด',
         'trial-home', [(3, 32.6, 94, 12.2)], None),
        ('เตือนก่อนตัดเงินทุกรอบ',
         'Datebell เตือนก่อนตัดเงิน 7 วัน 1 วัน และในวันจริง ตามเวลาเตือนของคุณ ถ้าแพ็กเกจที่เลือกจากรายการขึ้นราคา การแจ้งเตือนจะบอกด้วย',
         'sub-detail', [(3, 59, 94, 11.4)], None),
      ],
      'extra': [
        ('ทำไมไม่ใช้รายการการสมัครรับใน iPhone',
         '<p>รายการใน<b>การตั้งค่า</b> › ชื่อของคุณ › <b>การสมัครรับ</b> แสดงเฉพาะที่เรียกเก็บเงินผ่าน Apple ส่วนที่จ่ายผ่านเว็บไซต์ ค่ายมือถือ หรือตัดบัตรรายเดือน จะไม่อยู่ในนั้น (<a href="{apple}" rel="noopener">Apple</a>) Datebell รวมทั้งหมดไว้ในรายการเดียว</p>'),
        ('เดือนละครั้ง ยังคุ้มอยู่ไหม',
         '<p>Datebell ชวนเช็กสิ่งที่จ่ายอยู่เดือนละครั้ง อันไหนใช้ก็เก็บไว้ อันไหนไม่ได้ใช้ก็รู้ทันที</p>'),
      ],
    },
  },
]

HUB = {
  'en': {'title': 'Datebell guides: reminders for trials and subscriptions on iPhone',
         'meta': 'Short how-to guides for iPhone: get reminded before a free trial ends, and keep track of subscription renewals.',
         'h1': 'Datebell <em>guides</em>', 'lede': 'Short how-tos with real screens from the app.'},
  'th': {'title': 'คู่มือ Datebell: เตือนทดลองใช้ฟรีและค่าสมาชิกบน iPhone',
         'meta': 'คู่มือสั้นๆ สำหรับ iPhone ตั้งเตือนก่อนทดลองใช้ฟรีหมด และติดตามวันต่ออายุค่าสมาชิก',
         'h1': 'คู่มือ <em>Datebell</em>', 'lede': 'วิธีใช้สั้นๆ พร้อมหน้าจอจริงจากแอป'},
}

LOGO = open(os.path.join(ROOT, 'scripts', 'logo.svg.txt')).read().strip()
DEFS = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><clipPath id="dbBc"><path d="M512 270 C392 270 322 360 322 480 L322 610 L262 690 Q250 712 276 712 L748 712 Q774 712 762 690 L702 610 L702 480 C702 360 632 270 512 270 Z"/></clipPath><linearGradient id="dbG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD27A"/><stop offset="1" stop-color="#F7A21F"/></linearGradient></defs></svg>'

def esc(s):
    return html.escape(s, quote=True)

def strip_tags(s):
    import re
    return re.sub('<[^>]+>', '', s)

def head(lang, title, meta, path, alt_path):
    other = 'th' if lang == 'en' else 'en'
    en_path, th_path = (path, alt_path) if lang == 'en' else (alt_path, path)
    return f'''<!doctype html>
<html lang="{lang}" data-fixed>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" hreflang="en" href="{SITE}{en_path}">
<link rel="alternate" hreflang="th" href="{SITE}{th_path}">
<link rel="alternate" hreflang="x-default" href="{SITE}{en_path}">
<meta name="theme-color" content="#0B5E45">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Datebell">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'th_TH'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/icon.png">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600&family=Prompt:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>'''

def bar(lang, alt_path):
    u = UI[lang]
    q = '?lang=' + lang
    langs = ''.join(
        f'<a href="{alt_path}" lang="{l}" hreflang="{l}">{n}</a>' if l != lang else f'<a aria-current="true" lang="{l}">{n}</a>'
        for l, n in (('th', 'ไทย'), ('en', 'EN')))
    return f'''<header class="wrap">
  <div class="bar">
    <a class="mark" href="/{q}">{LOGO}<span>Datebell</span></a>
    <nav class="tabs" aria-label="Pages"><a href="/{q}">{u['home']}</a><a href="/features.html{q}">{u['features']}</a></nav>
    <div class="lang" role="group" aria-label="Language">{langs}</div>
  </div>
</header>'''

def foot(lang):
    u = UI[lang]
    q = '?lang=' + lang
    return f'''<footer class="wrap foot">
      <a href="/{q}">{u['home']}</a>
      <a href="/features.html{q}">{u['features']}</a>
      <a href="{url(lang, '')}">{u['guides']}</a>
      <a href="/support.html">{u['support']}</a>
      <a href="/privacy.html">{u['privacy']}</a>
      <a href="https://www.instagram.com/datebell.app/" target="_blank" rel="noopener">Instagram</a>
      <span>© 2026 Datebell</span>
</footer>
<script src="/js/site.js"></script>
</body>
</html>
'''

def end(lang):
    u = UI[lang]
    return f'''  <section class="end">
    <div class="wrap rv">
      <div class="logo">{LOGO}<b>Datebell</b></div>
      <p class="lede" style="margin:0 auto">{u['free']}</p>
      <div class="cta"><a class="badge store" href="{STORE}"><img class="badgeImg" src="/img/badge-en.svg" alt="{u['badge_alt']}" width="162" height="54"></a></div>
      <div class="cta"><a class="igb" href="https://www.instagram.com/datebell.app/" target="_blank" rel="noopener"><img src="/img/instagram-glyph.webp" alt="" width="32" height="32"><span>{u['ig']}</span></a></div>
    </div>
  </section>'''

def crumbs_ld(lang, items):
    data = {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(items)]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'

def guide_page(g, lang):
    c, u = g[lang], UI[lang]
    other = 'th' if lang == 'en' else 'en'
    path, alt = url(lang, g['slug']), url(other, g['slug'])
    apple = APPLE_CANCEL[lang]
    out = [head(lang, c['title'] + ' · Datebell', c['meta'], path, alt)]
    out.append(crumbs_ld(lang, [('Datebell', '/'), (u['guides'], url(lang, '')), (c['title'], path)]))
    out.append('</head>\n<body>\n' + DEFS)
    out.append(bar(lang, alt))
    out.append(f'''<main class="guide">
  <div class="wrap g-head rv">
    <nav class="crumb" aria-label="Breadcrumb"><a href="{url(lang, '')}">{u['guides']}</a></nav>
    <h1>{c['h1']}</h1>
    <div class="answer"><b>{u['short']}</b><p>{c['short'].format(apple=apple)}</p></div>
  </div>
  <section class="sec steps" aria-label="{u['steps']}">
    <div class="wrap"><ol class="g-steps">''')
    for i, (h, p, shot, rings, ntf) in enumerate(c['steps']):
        flip = ' flip' if i % 2 else ''
        rg = ''.join(f'<span class="ring" style="--x:{x}%;--y:{y}%;--w:{w}%;--h:{hh}%;--d:{0.2 + 0.3 * k:.1f}s"></span>' for k, (x, y, w, hh) in enumerate(rings))
        nt = ''
        if ntf:
            nt = f'<div class="ntf2"><img src="/img/icon-180.png" alt="" width="36" height="36"><div><b>Datebell<small>{u["now"]}</small></b><span class="t">{esc(ntf[0])}</span><span class="d">{esc(ntf[1])}</span></div></div>'
        alt_txt = esc(strip_tags(h))
        out.append(f'''      <li class="row{flip} rv">
        <div class="txt"><span class="g-n">{u['step']} {i + 1}</span><h2>{h}</h2><p>{p}</p></div>
        <div class="vis"><div class="phone{' top' if rings and max(y + hh for _, y, _, hh in rings) > 70 else ''}"><div class="scr"><img src="/img/help/{shot}-{lang}.webp" alt="{alt_txt}" width="700" height="1522" loading="{'eager' if i == 0 else 'lazy'}" decoding="async">{rg}</div></div>{nt}</div>
      </li>''')
    out.append('    </ol>')
    for h, body in c['extra']:
        out.append(f'      <div class="g-extra rv"><h2>{h}</h2>{body.format(apple=apple)}</div>')
    others = [o for o in GUIDES if o is not g]
    links = ''.join(f'<li><a href="{url(lang, o["slug"])}"><b>{o[lang]["title"]}</b><span>{o[lang]["card"]}</span></a></li>' for o in others)
    out.append(f'''      <div class="g-more rv"><h3>{u['more']}</h3><ul class="g-cards">{links}<li><a href="/features.html?lang={lang}"><b>{'Everything Datebell does' if lang == 'en' else 'ทุกอย่างที่ Datebell ทำได้'}</b><span>{'All features, with real screens.' if lang == 'en' else 'ฟีเจอร์ทั้งหมด พร้อมหน้าจอจริง'}</span></a></li></ul></div>
    </div>
  </section>''')
    out.append(end(lang))
    out.append('</main>')
    out.append(foot(lang))
    return '\n'.join(out)

def hub_page(lang):
    c, u = HUB[lang], UI[lang]
    other = 'th' if lang == 'en' else 'en'
    path, alt = url(lang, ''), url(other, '')
    out = [head(lang, c['title'], c['meta'], path, alt)]
    out.append(crumbs_ld(lang, [('Datebell', '/'), (u['guides'], path)]))
    out.append('</head>\n<body>\n' + DEFS)
    out.append(bar(lang, alt))
    cards = ''.join(f'<li><a href="{url(lang, g["slug"])}"><b>{g[lang]["title"]}</b><span>{g[lang]["card"]}</span></a></li>' for g in GUIDES)
    out.append(f'''<main class="guide">
  <div class="wrap g-head rv">
    <h1>{c['h1']}</h1>
    <p class="lede">{c['lede']}</p>
  </div>
  <section class="sec"><div class="wrap"><ul class="g-cards big rv">{cards}</ul></div></section>''')
    out.append(end(lang))
    out.append('</main>')
    out.append(foot(lang))
    return '\n'.join(out)

def write(rel, text):
    p = os.path.join(ROOT, rel.lstrip('/'))
    if p.endswith('/'):
        p += 'index.html'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(text)
    print('wrote', os.path.relpath(p, ROOT))

for lang in ('en', 'th'):
    write(url(lang, ''), hub_page(lang))
    for g in GUIDES:
        write(url(lang, g['slug']), guide_page(g, lang))
