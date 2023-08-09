# [
#   1. 신문사 URL
#   2. 덧붙일 URL
#   3. 제목 경로
#   4. 이미지 경로
#   5. 기사 URL 경로
#   6. 나라이름
#   7. 나라가 대한민국인지 여부
#   8. 아티클 경로
# ]

# #Canada()  Brazil() 추가예정
country_infos=[
    {
        'url':'https://edition.cnn.com/us',
        'plus_url':'https://edition.cnn.com',
        'title_path':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2) > div > div > span',
        'img_path':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(1) > div > div > div.image__container.image > picture > img',
        'article_url':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2)',
        'country_name':'미국',
        'is_korea':False,
        'article_path':'body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content',
    },
    {
        'url':'https://mainichi.jp/',
        'plus_url':'https://mainichi.jp',
        'title_path':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-detail > h3',
        'img_path':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-image.image-mask > picture > img',
        'article_url':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a',
        'country_name':'일본',
        'is_korea':False,
        'article_path':'#articledetail-body',
    },
    {
        'url':'https://www.thequint.com/international',
        'plus_url':'https://www.thequint.com/international',
        'title_path':'#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link > div > h1',
        'img_path':'#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a:nth-child(1) > div > figure > picture > img',
        'article_url':'#qw-top-story-home > div._1I_6Y > div.custom-story-card-1 > div > a.headline-link',
        'country_name':'인도',
        'is_korea':False,
        'article_path':'#container > div > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1)',
    },
    {
        'url':'https://www.lemonde.fr/',
        'plus_url':'https://www.lemonde.fr/',
        'title_path':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > h1 > p',
        'img_path':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > div.article__media-container > picture > img',
        'article_url':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a',
        'country_name':'프랑스',
        'is_korea':False,
        'article_path':'#id-1070203 > div.content--live'
    },
    {
        'url':'https://www.thestar.com/news/canada/',
        'plus_url':'https://www.thestar.com/news/canada',
        'title_path':'#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a',
        'img_path':'#card-summary-3f9057df-e038-528c-ac9f-cc6f703bbc00 > div > div.card-image > div > figure > div > a > img',
        'article_url':'#card-summary-6aea2cdf-7874-526b-80c9-bd5aa5db79d8 > div > div.card-body > div.card-headline > h3 > a',
        'country_name':'캐나다',
        'is_korea':False,
        'article_path':0,
    },
    {
        'url':'https://iz.ru/',
        'plus_url':'https://iz.ru/',
        'title_path':'#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top',
        'img_path':'#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top',
        'article_url':'#block-front-bt-a > div > div.main-events-table__inside__left.article-box > div > div > div.main-news-big-img__inside__top > a',
        'country_name':'러시아',
        'is_korea':False,
        'article_path':0
    },
    {
        'url':'https://www.faz.net/aktuell/',
        'plus_url':'https://www.faz.net/aktuell/',
        'title_path':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a > header > h2 > span.tsr-Base_HeadlineText',
        'img_path':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.tsr-Base_MediaWrapper.btn-Wrapper > img',
        'article_url':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a',
        'country_name':'독일',
        'is_korea':False,
        'article_path':'#pageIndex_1',
    },
    {
        'url':'https://www.bbc.com/news/uk',
        'plus_url':'https://www.bbc.com',
        'title_path':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        'img_path':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-image.gs-u-mb.gs-u-mb0\@xs.gel-2\/3\@m.gel-1\/2\@xl > div > div > img',
        'article_url':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        'country_name':'영국',
        'is_korea':False,
        'article_path':'#main-content > article',
    },
    {
        'url':'https://www.repubblica.it/',
        'plus_url':'https://www.repubblica.it/',
        'title_path':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        'img_path':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > figure > a > picture > img',
        'article_url':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        'country_name':'이탈리아',
        'is_korea':False,
        'article_path':'#article-body > div.story__text',
    },
    {
        'url':'https://www.uol.com.br/',
        'plus_url':'https://www.uol.com.br/',
        'title_path':'#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a > h3',
        'img_path':'#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a > figure > picture > img',
        'article_url':'#app > div > div:nth-child(7) > section:nth-child(2) > div > div > div:nth-child(2) > div > div.col-24.col-lg-15 > article > a',
        'country_name':'브라질',
        'is_korea':False,  
        'article_path':0,      
    },
    {
        'url':'https://www.joongang.co.kr/',
        'plus_url':'https://www.joongang.co.kr/',
        'title_path':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > div > h2 > a',
        'img_path':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > figure > a > img',
        'article_url':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > div > h2 > a',
        'country_name':'대한민국',
        'is_korea':True,
        'article_path':'#article_body',
    },
    {
        'url':'https://thanhnien.vn',
        'plus_url':'https://thanhnien.vn',
        'title_path':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        'img_path':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > a > img',
        'article_url':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        'country_name':'베트남',
        'is_korea':False,
        'article_path':'#content > div.detail__section > div > div > div.detail__main > div > div.detail__cmain-flex > div.detail__cmain-main > div.detail-cmain > div',
    },
    {
        'url':'https://www.abc.net.au/news/australia',
        'plus_url':'https://www.abc.net.au',
        'title_path':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.CardLayout_content__bev76 > h3 > span > a',
        'img_path':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.GenericCard_cardImage__f3Olr.undefined.CardLayout_imageContainer__89V4v.CardLayout_mobileImageTop__eskhD.CardLayout_tabletImageTop__ROit7.CardLayout_desktopImageTop__bXR3h > div > div > img',
        'article_url':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.CardLayout_content__bev76 > h3 > span > a',
        'country_name':'호주',
        'is_korea':False,
        'article_path':'#body > div > div:nth-child(1) > div',                       
    },
    {
        'url':'https://mexiconewsdaily.com/',
        'plus_url':'https://mexiconewsdaily.com',
        'title_path':'#tdi_114 > div > div.meta-info-container > div.td-module-meta-info > div > h3 > a',
        'img_path':'#tdi_114 > div > div.meta-info-container > div.td-module-thumb > a > img',
        'article_url':'#tdi_114 > div > div.meta-info-container > div.td-module-meta-info > div > h3 > a',
        'country_name':'멕시코',
        'is_korea':False,
        'article_path':'#tdi_115 > div > div.vc_column.tdi_118.wpb_column.vc_column_container.tdc-column.td-pb-span8 > div > div.td_block_wrap.tdb_single_content.tdi_130.td-pb-border-top.td_block_template_1.td-post-content.tagdiv-type > div',
    },
    {
        'url':'https://www.thelocal.es/',
        'plus_url':'https://www.thelocal.es/',
        'title_path':'#main > div > div > div:nth-child(1) > div > div.hp-new__article.hp-new__article--1.hp-new__article--mobileRight > article > div > h3 > a',
        'img_path':'#main > div > div > div:nth-child(1) > div > div.hp-new__article.hp-new__article--1.hp-new__article--mobileRight > article > a > img',
        'article_url':'#main > div > div > div:nth-child(1) > div > div.hp-new__article.hp-new__article--1.hp-new__article--mobileRight > article > div > h3 > a',
        'country_name':'스페인',
        'is_korea':False,
        'article_path':'#main > div.article-single.article-single--regular > div.container-md > div > div.col-xl-8.mobile-full-width > main > div.article-single__content.cXenseParse',                   
    },
    {
        'url':'https://www.thejakartapost.com/',
        'plus_url':'https://www.thejakartapost.com',
        'title_path':'body > div.col-xs-12.tjpcontainer > div.container.borderGrid > div:nth-child(2) > div > div > div.col-xs-12.columns.mainChannel.wdsk.wtbl > div.jpRow.mainNews.lineSection.sectionHeadLine > div.bigHeadline > div > div.descNews.col-md-4 > a:nth-child(2) > h2',
        'img_path':'body > div.col-xs-12.tjpcontainer > div.container.borderGrid > div:nth-child(2) > div > div > div.col-xs-12.columns.mainChannel.wdsk.wtbl > div.jpRow.mainNews.lineSection.sectionHeadLine > div.bigHeadline > div > div.col-md-8 > a > div > img',
        'article_url':'body > div.col-xs-12.tjpcontainer > div.container.borderGrid > div:nth-child(2) > div > div > div.col-xs-12.columns.mainChannel.wdsk.wtbl > div.jpRow.mainNews.lineSection.sectionHeadLine > div.bigHeadline > div > div.descNews.col-md-4 > a:nth-child(2)',
        'country_name':'인도네시아',
        'is_korea':False,
        'article_path':'body > div.col-xs-12.tjpcontainer.channelSingle > div.container.single-page > div.row.loop > div:nth-child(1) > div > div.col-xs-12.columns.main-single-page.multiSingle > div > div.col-xs-12.main-single > div > div.col-xs-12.stop > div > div.col-md-10.col-xs-12.detailNews',
    },
    {
        'url':'https://www.dutchnews.nl/',
        'plus_url':'https://www.dutchnews.nl',
        'title_path':'#main > div:nth-child(1) > div > div.col-12.col-md-6.col-xl-7.px-0.px-md-4.mb-6.mb-md-0.pb-xl-8 > div.px-4.px-md-0.pt-5.pb-6.py-md-4.pt-lg-3.pb-lg-0 > h2 > a',
        'img_path':'#main > div:nth-child(1) > div > div.col-12.col-md-6.col-xl-7.px-0.px-md-4.mb-6.mb-md-0.pb-xl-8 > a > div > img',
        'article_url':'#main > div:nth-child(1) > div > div.col-12.col-md-6.col-xl-7.px-0.px-md-4.mb-6.mb-md-0.pb-xl-8 > a',
        'country_name':'네덜란드',
        'is_korea':False,
        'article_path':'#main > article > main',
    },
    {
        'url':'https://www.arabnews.com/',
        'plus_url':'https://www.arabnews.com',
        'title_path':'#main-wrap > div:nth-child(3) > div > main > div.grid-container.small-grid-collapse > div:nth-child(1) > div > div > div > div > div > div.article-item > div.article-item-overbox.grid-x.align-bottom > div > div.article-item-title.bottom-spacer--s > h1 > a',
        'img_path':'#main-wrap > div:nth-child(3) > div > main > div.grid-container.small-grid-collapse > div:nth-child(1) > div > div > div > div > div > div.article-item > div.article-item-img > img',
        'article_url':'#main-wrap > div:nth-child(3) > div > main > div.grid-container.small-grid-collapse > div:nth-child(1) > div > div > div > div > div > div.article-item > div.article-item-overbox.grid-x.align-bottom > div > div.article-item-title.bottom-spacer--s > h1 > a',
        'country_name':'사우디아라비아',
        'is_korea':False,
        'article_path':'#content-articles > div.pageWrapper.active > article > div.grid-x.entry-article-inner.align-center > div.cell.large-auto > div.printable-area.shareable > div.entry-content > div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div > div',
    }    
]