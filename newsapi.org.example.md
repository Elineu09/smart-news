Definition
GET https://newsapi.org/v2/everything?q=Apple&from=2026-05-05&sortBy=popularity&apiKey=API_KEY

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2026-05-05&'
       'sortBy=popularity&'
       'apiKey=8ad1b1d29f90479db5e0da55bf633487')

response = requests.get(url)

print r.json

{
"status": "ok",
"totalResults": 19,
-"articles": [
-{
-"source": {
"id": null,
"name": "GSMArena.com"
},
"author": "Vlad",
"title": "iPhone 18 Pro and iPhone 18 Pro Max to have a smaller Dynamic Island",
"description": "We've essentially been witnessing a game of \"will it / won't it\" for the past few months when it comes to rumors and leaks about whether Apple will make the Dynamic Island punch-hole cutout smaller on the upcoming iPhone 18 Pro and iPhone 18 Pro Max or not.\n\n…",
"url": "https://www.gsmarena.com/iphone_18_pro_and_iphone_18_pro_max_to_have_a_smaller_dynamic_island-news-72665.php",
"urlToImage": "https://fdn.gsmarena.com/imgroot/news/26/05/iphone-18-pro-iphone-18-pro-max-smaller-dynamic-island/-952x498w6/gsmarena_000.jpg",
"publishedAt": "2026-05-05T00:01:02Z",
"content": "We've essentially been witnessing a game of \"will it / won't it\" for the past few months when it comes to rumors and leaks about whether Apple will make the Dynamic Island punch-hole cutout smaller o… [+1029 chars]"
},
-{
-"source": {
"id": null,
"name": "Smartworld.it"
},
"author": "Vincenzo Ronca",
"title": "Il Face ID per Android sotto il display dal 2027: cosa sappiamo su Polar ID",
"description": "Polar ID di Metalenz porta lo sblocco facciale sotto il display OLED degli Android: funziona al buio e arriva nel 2027.\r\nL'articolo Il Face ID per Android sotto il display dal 2027: cosa sappiamo su Polar ID sembra essere il primo su Smartworld.",
"url": "https://www.smartworld.it/news/polar-id-riconoscimento-facciale-sicuro-android-sotto-display.html",
"urlToImage": "https://www.smartworld.it/images/2025/06/16/scuola-studenti-smartphone_1200x675.jpg",
"publishedAt": "2026-05-05T00:07:00Z",
"content": "Lo sblocco facciale sicuro è sempre stato un privilegio di iPhone, grazie al notch e alla selva di sensori che Apple si porta dietro dal 2017. Gli Android hanno provato a recuperare, ma senza hardwar… [+2599 chars]"
},
-{
-"source": {
"id": null,
"name": "Expansion.com"
},
"author": "MONTSE MATEOS, REALIZACIÓN: TAMARA VÁZQUEZ",
"title": "Cómo trabajar con agentes de IA, con Francisco Mateo-Sidrón",
"description": "&quot;El ser humano es el encargado de administrar la información para que la IA aprenda, es quien pone los parámetros, quien tiene que tunearla&quot;. Con esta afirmación,...",
"url": "https://www.expansion.com/podcasts/trabajo-y-mas/2026/05/05/69f87b40468aebf4628b45a3.html",
"urlToImage": "https://e01-phantom-expansion.uecdn.es/18dbdb35ec2d051cd19c297f82ffc1d5/resize/1200/f/webp/assets/multimedia/imagenes/2026/05/04/17779016685129.jpg",
"publishedAt": "2026-05-05T00:56:44Z",
"content": "La inteligencia artificial no existe sin los datos. Cómo alimentar a nuestro agente de IA es fundamental para garantizar su eficacia y cumplir nuestros objetivos. \"El ser humano es el encargado de ad… [+1238 chars]"
},
-{
-"source": {
"id": null,
"name": "Vanity Fair"
},
"author": "Clara Molot",
"title": "The Met Gala has a Heavy, Although Somewhat Invisible Presence at the Met",
"description": "Jeff Bezos and Mark Zuckerberg opted to skip the carpet — but inside, OpenAI, Meta, Snapchat, Shopify, and Amazon all have tables.",
"url": "https://www.vanityfair.com/style/story/the-met-gala/tech",
"urlToImage": "https://media.vanityfair.com/photos/69f9394d0fcf10132a823ea9/16:9/w_1280,c_limit/2274525976",
"publishedAt": "2026-05-05T00:45:32Z",
"content": "The Met Gala has earned the nickname \"Tech Gala\" this spring for Silicon Valley's heavy presence. Jeff and Lauren Sánchez Bezos are the main sponsors of the event, with a reported $10 million donatio… [+1206 chars]"
},
-{
-"source": {
"id": null,
"name": "Technews.tw"
},
"author": "Atkinson",
"title": "英特爾第一季財報超乎預期股價飆升 24%，那將公布財報的 AMD 呢 ?",
"description": "處理器大廠 AMD 將於台北時間 6 日清晨美股盤後公布第一季財報，投資人正密切關注這家晶片大廠是否能從全球 AI 競賽所帶動的中央處理器（CPU）需求激增中受益。在此之前，競爭對手英特爾（Intel）已於 4 月 23 日公布財報，其營收與獲利均優於分析師預期，且資料中心業務前景亮眼，帶動英特爾股...",
"url": "https://finance.technews.tw/2026/05/05/amd-is-about-to-release-its-q1-2026-financial-results/",
"urlToImage": "https://img.technews.tw/wp-content/uploads/2026/01/06115008/CES2026-AMD-1.png",
"publishedAt": "2026-05-05T01:30:21Z",
"content": "AMD 6 AI CPUIntel 4 23 24% AMD \r\nAI AI agents CPU AMD CPU AMD AI GPU\r\nBloombergAMD 98.8 EPS 1.28 2025 74.3 EPS 0.96 AI 56 2025 36.7 52%\r\nAMD Helios rack-scale system GPU CPU Nvidia Vera Rubin NVL72 \r… [+109 chars]"
},
-{
-"source": {
"id": null,
"name": "Newsshooter"
},
"author": "Matthew Allard ACS",
"title": "The New Frontier of Underwater Immersive Content– ACHTEL 3Deep & Apple Vision Pro",
"description": "The Apple Vision Pro has created a demand for high-fidelity 180° stereoscopic immersive video. While capturing this on land is a known challenge, doing so underwater has historically been considered an optical impossibility. Here is where the ACHTEL 3Deep Imm…",
"url": "https://www.newsshooter.com/2026/05/04/the-new-frontier-of-underwater-immersive-content-achtel-3deep-apple-vision-pro/",
"urlToImage": "https://www.newsshooter.com/wp-content/uploads/2026/05/Screenshot-2026-05-05-at-9.26.16.jpeg",
"publishedAt": "2026-05-05T00:31:46Z",
"content": "The Apple Vision Pro has created a demand for high-fidelity 180° stereoscopic immersive video. While capturing this on land is a known challenge, doing so underwater has historically been considered … [+3111 chars]"
},
-{
-"source": {
"id": null,
"name": "Gagadget.com"
},
"author": "gagadget.com",
"title": "Apple добавила сквозное шифрование между iPhone и Android в бета-версии iOS 26.5: как работает новая функция",
"description": "В новой тестовой версии операционной системы iOS 26.5 компания Apple добавила сквозное шифрование для RCS-сообщений между iPhone и Android. Речь идет о бета-функции, которая постепенно станет доступной пользователям в сетях операторов, поддерживающих соответс…",
"url": "https://gagadget.com/ru/708327-apple-dobavila-skvoznoe-shifrovanie-mezhdu-iphone-i-android-v-beta-versii-ios-265-kak-rabotaet-novaya-funktsiya/",
"urlToImage": "https://gagadget.com/media/cache/2a/97/2a97f0ca6bc295a17ea381ac2fa90ad3.webp",
"publishedAt": "2026-05-05T00:10:56Z",
"content": "iOS 26.5 Apple RCS- iPhone Android. -, , .\r\n(E2EE) . RCS iOS 26.5. , .\r\n 9to5Google, Messages iPhone , Android. Android Google Messages RCS- .\r\n RCS iOS 18- , GSMA E2EE 2025 . Apple \" \", . iOS 26.4, … [+13 chars]"
},
-{
-"source": {
"id": null,
"name": "Minatokobe.com"
},
"author": "酔いどれ",
"title": "Screen Studioの$89に悩んでるMacユーザーへ、無料OSSで”あの動き”を再現できる時代が来てた",
"description": "まいど、酔いどれ（@yoidoreo）です。 Macで「おしゃれな画面録画」を作りたい、と思ったことはありませんか？ YouTubeやXで見かける、操作画面がスッと拡大して、カーソルがヌルヌル動くやつ。あれ、大体「Screen Studio」で作られてます。 ただ、Screen Studioは$89（約13,000円）するんですよね。 しかもmacOS専用。「ブログに貼る30秒の操作GIFのために1万円超か……」と思って、私も二の足を踏んでたクチです。 無料で同じことができるOSSが2つある で、2026年に入っ…",
"url": "https://minatokobe.com/wp/os-x/mac/post-105693.html",
"urlToImage": "https://minatokobe.com/wp/wp-content/uploads/2026/05/Mac-OSS_01.jpg",
"publishedAt": "2026-05-05T01:31:16Z",
"content": "1990Mac IIci MacMac Studio M1 MAX + Studio Display,16inch MacBook Pro M1 Pro 2021, iPhone 15 Pro Max, iPhone 13 Pro Max, 12.9inch iPad Pro 2021, iPad Air,  Apple Watch Ultra, 1HomePodApple TV 4KApple… [+43 chars]"
},
-{
-"source": {
"id": null,
"name": "Yahoo Entertainment"
},
"author": "住展房屋網",
"title": "2026泰山買房首選：解析「泰山楓江地區」房價窪地，與塭仔圳 10%價差的置產紅利",
"description": "在新北購屋，大家都在追逐「重劃區」。從早期的板橋江翠、新店央北，到近兩年話題度最高的「新泰塭仔圳」。但隨著房價水漲船高，許多首購族與置產客發現，塭仔圳的入場門檻已非昔日。這時，聰明的資金開始往周邊尋找「價值窪地」，而緊鄰其側的「泰山楓江地區」，正以驚人的高 CP 值與發展潛力，成為 2026 年最受矚目的房市黑馬...",
"url": "https://tw.stock.yahoo.com/news/2026%E6%B3%B0%E5%B1%B1%E8%B2%B7%E6%88%BF%E9%A6%96%E9%81%B8%EF%BC%9A%E8%A7%A3%E6%9E%90%E3%80%8C%E6%B3%B0%E5%B1%B1%E6%A5%93%E6%B1%9F%E5%9C%B0%E5%8D%80%E3%80%8D%E6%88%BF%E5%83%B9%E7%AA%AA%E5%9C%B0%EF%BC%8C%E8%88%87%E5%A1%AD%E4%BB%94%E5%9C%B3-10%E5%83%B9%E5%B7%AE%E7%9A%84%E7%BD%AE%E7%94%A2%E7%B4%85%E5%88%A9-010023260.html",
"urlToImage": "https://s.yimg.com/os/creatr-uploaded-images/2026-05/33891920-4798-11f1-b36f-9c68f50ca4a6",
"publishedAt": "2026-05-05T01:00:23Z",
"content": "(Apple Inc.)(4)104180040730 52,8705252,505180040730 41,4081,4201102,3006 SpaceX IPO"
},
-{
-"source": {
"id": null,
"name": "Yahoo Entertainment"
},
"author": "財訊快報",
"title": "戰火升溫油價飆，美股週一回落道瓊急挫557點，物流與工業股賣壓沉重",
"description": "【財訊快報／陳孟朔】中東緊張局勢週一急速升溫，市場傳出美國軍艦在荷姆茲海峽附近遭伊朗導彈攻擊，雖然美方隨後否認相關說法，但阿聯酋石油工業區遇襲、韓國營運貨船在海峽內側爆炸起火，加上美軍宣稱擊毀伊朗快艇，油價大漲的同時，使投資人避險情緒升溫，美股主要股指週一齊步收黑；道瓊工業指數收盤急挫約557點或1.1%，失守四萬九關口，退回一週低約。道瓊工業指數低開82點後跌幅擴大，最多急挫586點，終場收跌557.37點或1.13%，報48,941.90點為4月29日以來最低。標普、那指和費半皆自歷史高點回落，標準普爾500…",
"url": "https://tw.stock.yahoo.com/news/%E6%88%B0%E7%81%AB%E5%8D%87%E6%BA%AB%E6%B2%B9%E5%83%B9%E9%A3%86-%E7%BE%8E%E8%82%A1%E9%80%B1-%E5%9B%9E%E8%90%BD%E9%81%93%E7%93%8A%E6%80%A5%E6%8C%AB557%E9%BB%9E-%E7%89%A9%E6%B5%81%E8%88%87%E5%B7%A5%E6%A5%AD%E8%82%A1%E8%B3%A3%E5%A3%93%E6%B2%89%E9%87%8D-001316692.html",
"urlToImage": "https://s.yimg.com/cv/apiv2/social/images/yahoo_default_logo-1200x1200.png",
"publishedAt": "2026-05-05T00:13:16Z",
"content": "5571.1%82586557.371.13%48,941.90429\r\n50029.370.41%7,200.75()46.640.19%25,067.8060.680.57%10,534.66ADR0.99%\r\n743136%114\r\n(Amazon)Amazon Supply Chain Services(FedEx)9.1%(UPS)10.5%1.4%\r\n(Home Depot)3.6%… [+301 chars]"
},
-{
-"source": {
"id": null,
"name": "Potaroo.net"
},
"author": null,
"title": "D2D",
"description": "t's a new space race with a number of satellite operators pushing out LEO satellite services that operate directly to hand-held devices, or D2D.",
"url": "https://www.potaroo.net/ispcol/2026-05/d2d.html",
"urlToImage": null,
"publishedAt": "2026-05-05T00:00:00Z",
"content": "D2DMay 2026\r\nWhen Motorola unveiled its Iridium global satellite-based mobile telephony service in the late 1990's everything augured well for a revolution in the satellite communications market, onl… [+7924 chars]"
},
-{
-"source": {
"id": null,
"name": "Livedoor.biz"
},
"author": "vintagecomp",
"title": "Apple Vision Pro 開発中止？",
"description": "Apple Vision Pro の開発チームを解散し、開発を事実上停止したとMacRumors が伝えています。昨年10月にM5モデルを投入したばかりですが、ほとんど話題にも上らず売り上げは低迷。あくまで開発中止の噂情報で、現行モデルは引き続き販売中です。Apple Vision Pro は、大きな...",
"url": "https://vintagecomp.livedoor.biz/archives/52064217.html",
"urlToImage": "https://parts.blog.livedoor.jp/img/usr/cmn/ogp_image/livedoor.png",
"publishedAt": "2026-05-05T00:02:20Z",
"content": "Apple Vision Pro MacRumors10M5Apple Vision Pro Vintage Computer Apple Store iPod, iPhone, iPad, Apple Watch Vision Pro Mac Neo \r\nMetaApple"
},
-{
-"source": {
"id": null,
"name": "Pypi.org"
},
"author": null,
"title": "superdoc-sdk-cli-darwin-arm64 1.8.0.dev45",
"description": "SuperDoc CLI binary for macOS ARM64 (Apple Silicon)",
"url": "https://pypi.org/project/superdoc-sdk-cli-darwin-arm64/1.8.0.dev45/",
"urlToImage": null,
"publishedAt": "2026-05-05T00:10:04Z",
"content": "A required part of this site couldnt load. This may be due to a browser\r\n extension, network issues, or browser settings. Please check your\r\n connection, disable any ad blockers, or try using a diffe… [+12 chars]"
},
-{
-"source": {
"id": null,
"name": "Pypi.org"
},
"author": null,
"title": "superdoc-sdk-cli-darwin-arm64 1.8.0.dev46",
"description": "SuperDoc CLI binary for macOS ARM64 (Apple Silicon)",
"url": "https://pypi.org/project/superdoc-sdk-cli-darwin-arm64/1.8.0.dev46/",
"urlToImage": null,
"publishedAt": "2026-05-05T00:26:54Z",
"content": "A required part of this site couldnt load. This may be due to a browser\r\n extension, network issues, or browser settings. Please check your\r\n connection, disable any ad blockers, or try using a diffe… [+12 chars]"
},
-{
-"source": {
"id": null,
"name": "Pypi.org"
},
"author": null,
"title": "superdoc-sdk-cli-darwin-arm64 1.8.0.dev47",
"description": "SuperDoc CLI binary for macOS ARM64 (Apple Silicon)",
"url": "https://pypi.org/project/superdoc-sdk-cli-darwin-arm64/1.8.0.dev47/",
"urlToImage": null,
"publishedAt": "2026-05-05T00:37:23Z",
"content": "A required part of this site couldnt load. This may be due to a browser\r\n extension, network issues, or browser settings. Please check your\r\n connection, disable any ad blockers, or try using a diffe… [+12 chars]"
},
-{
-"source": {
"id": null,
"name": "Droidsans.com"
},
"author": "madamKiM",
"title": "Apple แจกวอลเปเปอร์ใหม่ และเปิดตัวสาย Sport Loop รุ่น Pride Edition",
"description": "ต้อนรับช่วงเวลา Pride Month ประจำปี 2026 ทาง Apple ร่วมเฉลิมฉลองให้กับชุมชนชาว LGBTQ+ ทั่วโลกด้วยการอัปเดต \"ภาพหน้าจอแบบใหม่\" ให้ผู้ใช้งานทั่วโลกได้ใช้ฟรี ไปจนถึงการเปิดตัวสายแบบ Sport Loop รุ่นใหม่สีสันสดใส",
"url": "https://droidsans.com/apple-launches-new-pride-collection-2026/",
"urlToImage": "https://images.droidsans.com/wp-content/uploads/2026/05/Apple-New-Pride-Collection-2026-Web-Cover.jpg",
"publishedAt": "2026-05-05T00:06:00Z",
"content": "Pride Month 2026 Apple LGBTQ+ “” Sport Loop \r\n Apple “Sport Loop Pride Edition”“ 11 ”\r\nSport Loop “”\r\n Sport Loop Pride Edition 1,800 3 40 ., 42 ., 46 .\r\n“ Pride Luminance” (iPhone iPad)\r\nApple Watch… [+82 chars]"
},
-{
-"source": {
"id": null,
"name": "Livedoor.com"
},
"author": "GIGAZINE（ギガジン）",
"title": "2026第1四半期に世界で最も売れたスマートフォンは「iPhone 17」、上位10機種が全体の25％を占める",
"description": "調査企業のCounterpoint Researchが公開しているスマートフォン市場の調査レポートであるGlobal Handset Model Sales Trackerによると、2026年第1四半期(1～3月)に世界で最も売れたスマートフォンはAppleの「iPhone 17」だったそうです。iPhone 17は同期における全世界のスマートフォン販売台数の6％を占めました。iPhone 17 Global Best-Selling Smartphone in Q1 2026, Top 10 Take 25% …",
"url": "https://news.livedoor.com/article/detail/31181421/",
"urlToImage": "https://image.news.livedoor.com/newsimage/stf/d/8/d8f35_88_8013d5bfa2fde06af4c3df2097473f0b.jpg",
"publishedAt": "2026-05-05T01:31:00Z",
"content": "Counterpoint ResearchGlobal Handset Model Sales Tracker20261(13)AppleiPhone 17iPhone 176\r\niPhone 17 Global Best-Selling Smartphone in Q1 2026, Top 10 Take 25% Sharehttps://counterpointresearch.com/en… [+907 chars]"
},
-{
-"source": {
"id": null,
"name": "Pypi.org"
},
"author": null,
"title": "reinforceclaw added to PyPI",
"description": "Personal RL feedback system — rate AI responses, train local LoRA adapters",
"url": "https://pypi.org/project/reinforceclaw/",
"urlToImage": "https://pypi.org/static/images/twitter.abaf4b19.webp",
"publishedAt": "2026-05-05T01:18:23Z",
"content": "Self-improving reinforcement learning for your AI agents. Set it up once, rate responses as you work, and your local model keeps improving in the background.\r\nSetup\r\nCurrent source checkout:\r\ncdReinf… [+9436 chars]"
},
-{
-"source": {
"id": null,
"name": "Github.com"
},
"author": "chrisallick",
"title": "Show HN: I built a native macOS audio player and it changed my life",
"description": "I've going through a backlog of projects and checking them off with Claude Code. What started out as a quick afternoon of coding with claude has relight my love of making.\n\nComments URL: https://news.ycombinator.com/item?id=48016525\nPoints: 1\n# Comments: 1",
"url": "https://github.com/chrisallick/light-crime-audio-player",
"urlToImage": "https://opengraph.githubassets.com/4293f5349edbfa1e10f1fe659ea324050a0c48833958d84e899fbdb12b0246bd/chrisallick/light-crime-audio-player",
"publishedAt": "2026-05-05T00:06:06Z",
"content": "A Winamp-inspired macOS audio player with a flat, 90s cyber aesthetic.\r\n<ul><li>Plays MP3, FLAC, AAC, M4A, WAV, AIFF, CAF, MP4, MOV (audio extracted automatically)</li><li>Parses M3U, M3U8, PLS, and … [+4294 chars]"
}
]
}