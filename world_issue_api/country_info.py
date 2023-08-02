import func
# [
#   1. 신문사 URL
#   2. 덧붙일 URL
#   3. 제목 경로
#   4. 이미지 경로
#   5. 기사 URL 경로
#   6. 나라이름
#   7. 나라가 대한민국인지 여부
# ]

# #Canada()  Brazil() 추가예정
country_infos=[
    func.news_scraping(
        'https://edition.cnn.com/us',
        'https://edition.cnn.com',
        'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2) > div > div > span',
        'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(1) > div > div > div.image__container.image > picture > img',
        'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2)',
        '미국',
        False
    ),
    func.news_scraping(
        'https://mainichi.jp/',
        'https://mainichi.jp',
        '#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-detail > h3',
        '#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-image.image-mask > picture > img',
        '#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a',
        '일본',
        False
    ),
    func.news_scraping(
        'https://www.thequint.com/international',
        'https://www.thequint.com/international',
        '#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link > div > h1',
        '#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a:nth-child(1) > div > figure > picture > img',
        '#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link',
        '인도',
        False
    ),
    func.news_scraping(
        'https://www.lemonde.fr/',
        'https://www.lemonde.fr/',
        '#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > h1 > p',
        '#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > div.article__media-container > picture > img',
        '#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a',
        '프랑스',
        False
    ),
    # func.news_scraping(
    #     'https://www.thestar.com/news/canada/',
    #     'https://www.thestar.com/news/canada',
    #     '#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a',
    #     '#card-summary-3f9057df-e038-528c-ac9f-cc6f703bbc00 > div > div.card-image > div > figure > div > a > img',
    #     '#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a',
    #     '캐나다',
    #     False
    # ),
    # func.news_scraping(
    #     'https://iz.ru/',
    #     'https://iz.ru/',
    #     '#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top',
    #     '#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top',
    #     '#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top > a',
    #     '러시아',
    #     False
    # ),
    func.news_scraping(
        'https://www.faz.net/aktuell/',
        'https://www.faz.net/aktuell/',
        '#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a > header > h2 > span.tsr-Base_HeadlineText',
        '#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.tsr-Base_MediaWrapper.btn-Wrapper > img',
        '#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a',
        '독일',
        False
    ),
    func.news_scraping(
        'https://www.bbc.com/news/uk',
        'https://www.bbc.com',
        '#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        '#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-image.gs-u-mb.gs-u-mb0\@xs.gel-2\/3\@m.gel-1\/2\@xl > div > div > img',
        '#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        '영국',
        False
    ),
    func.news_scraping(
        'https://www.repubblica.it/',
        'https://www.repubblica.it/',
        '#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        '#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > figure > a > picture > img',
        '#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        '이탈리아',
        False
    ),
    # news_scraping(
    #     'https://www.uol.com.br/',
    #     'https://www.uol.com.br/',
    #     '#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a > h3',
    #     '#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a > figure > picture > img',
    #     '#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a',
    #     '브라질',
    #     False
    # ),
    func.news_scraping(
        'https://www.joongang.co.kr/',
        'https://www.joongang.co.kr/',
        '#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > div > h2 > a',
        '#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > figure > a > img',
        '#container > section > div:nth-child(5) > section > div:nth-child(5) > div > div:nth-child(1) > div > div > h2 > a',
        '대한민국',
        True
    ),
    func.news_scraping(
        'https://thanhnien.vn',
        'https://thanhnien.vn',
        '#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        '#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > a > img',
        '#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        '베트남',
        False
    ),
]