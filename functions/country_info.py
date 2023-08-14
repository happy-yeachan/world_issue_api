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


#멋사로고 이미지 경로(위키피디아)
lion_img='https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png/692px-%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC_%EB%A1%9C%EA%B3%A0.png'

# #Canada()  Brazil() 추가예정
country_infos=[
    {
        'url':'https://edition.cnn.com/us',
        'plus_url':'https://edition.cnn.com',
        'title_path':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2) > div > div > span',
        'img_path':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(1) > div > div > div.image__container.image > picture > img',
        'article_url':'body > div.layout__content-wrapper.layout-no-rail__content-wrapper > section.layout__wrapper.layout-no-rail__wrapper > section.layout__main.layout-no-rail__main > div > section > div > div > div > div:nth-child(1) > div > div.zone__items.layout--wide-left-balanced-2 > div:nth-child(1) > div > div > div > div.container_lead-plus-headlines__cards-wrapper > div > div > div:nth-child(1) > a:nth-child(2)',
        'country_name':'미국',
        'article_path':'body > div.layout__content-wrapper.layout-with-rail__content-wrapper > section.layout__wrapper.layout-with-rail__wrapper > section.layout__main-wrapper.layout-with-rail__main-wrapper > section.layout__main.layout-with-rail__main > article > section > main > div.article__content-container > div.article__content',
        'spcial_picture':'https://i.namu.wiki/i/8h-OcAXbgFdpNVcIkyXYAy7TqJjvGmtd6_8hvV008ssnfZbBaB7Q-uzgOHoN8MWxvz2Zz1_3KOJa6p83cr_hrA.webp',
    },
    {
        'url':'https://mainichi.jp/',
        'plus_url':'https://mainichi.jp',
        'title_path':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-detail > h3',
        'img_path':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a > div > div.toppickup-image.image-mask > picture > img',
        'article_url':'#index-pickup > div.maintab-content-wrapper > section.maintab-content.is-active > div > div.l-half-1 > div.toppickup > a',
        'country_name':'일본',
        'article_path':'#articledetail-body',
        'spcial_picture':'https://i.namu.wiki/i/dlxaRWAGt6oORy7od4B8tffh0taLfslDoMn6q_AGALw4nCvLzT_hIb8_uWE4tcLbz5At61X6CXtDrBpTYJ4rVQ.webp',
    },
    {
        'url':'https://indianexpress.com/',
        'plus_url':'https:',
        'title_path':'#HP_TOP_NEWS > div.left-part > div > div.ie-first-story > h2 > a',
        'img_path':'#HP_TOP_NEWS > div.left-part > div > div.lead-img.m-premium > a > img',
        'article_url':'#HP_TOP_NEWS > div.left-part > div > div.ie-first-story > h2 > a',
        'country_name':'인도',
        'article_path':'#section > div > div:nth-child(2) > div.leftpanel > div > div > div > div',
        'spcial_picture':'https://i.namu.wiki/i/kfqyGLgS2n0X2dq24LAE3SeD-OQN7ahAYYrMLmpD745wdz0TsS1WuxcaLgZoJf_X9HyOyo3nw2j2kqlGAOYSuA.webp',
    },
    {
        'url':'https://www.lemonde.fr/',
        'plus_url':'https://www.lemonde.fr',
        'title_path':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > h1 > p',
        'img_path':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a > div.article__media-container > picture > img',
        'article_url':'#habillagepub > section.zone.zone--homepage > section.area.area--main.old__area-main.old__area > div > a',
        'country_name':'프랑스',
        'article_path':'#habillagepub > section > section.article__wrapper > article',
        'spcial_picture':'https://i.namu.wiki/i/LFRIiqAJzEUKx0dbsftnohx78BLrGv9qznkKtCUTyephVHhu9gYo3pRs_7YyBnDNBo_6ttVnBw1AZ5KZgbH6tw.webp',
    },
    {
        'url':'https://www.thestar.com/news/canada/',
        'plus_url':'https://www.thestar.com/news/canada',
        'title_path':'#card-summary-5823f189-e175-5957-961e-9134c55b3745 > div > div.card-image > div > figure > div > a',
        'img_path':'#card-summary-5823f189-e175-5957-961e-9134c55b3745 > div > div.card-image > div > figure > div > a > img',
        'article_url':'#card-summary-5823f189-e175-5957-961e-9134c55b3745 > div > div.card-image > div > figure > div > a',
        'country_name':'캐나다',
        'article_path':'#article-body',
        'spcial_picture':'https://newsimg-hams.hankookilbo.com/2022/10/19/d55051de-585a-4811-b9f3-e8ab273cfdb0.jpg',
    },
    {
        'url':'https://ria.ru/',
        'plus_url':'https://ria.ru',
        'title_path':'#content > div > div:nth-child(2) > div.section__cell > div.section__content > div:nth-child(1) > div:nth-child(1) > div > div > div > div > div > div.cell-main-photo__text > div.cell-main-photo__desc > div',
        'img_path':'#content > div > div:nth-child(2) > div.section__cell > div.section__content > div:nth-child(1) > div:nth-child(1) > div > div > div > div > div > div.cell-main-photo__image > picture > source:nth-child(1)',
        'article_url':'#content > div > div:nth-child(2) > div.section__cell > div.section__content > div:nth-child(1) > div:nth-child(1) > div > div > div > div > div > a',
        'country_name':'러시아',
        'article_path':'#endless > div.endless__item.m-active > div > div > div > div.layout-article__over > div.layout-article__main > div > div:nth-child(1) > div.article__body.js-mediator-article.mia-analytics',
        'spcial_picture':'https://i.namu.wiki/i/OHAxb5GxvBHEm8hFa5z4w5pJNX968GoLDyJOhUvSy3arxZz8bePTPqiyB-waYxrK9TeISgXlWH2wx853Diqbdw.webp',
    },
    {
        'url':'https://www.faz.net/aktuell/',
        'plus_url':'https://www.faz.net/aktuell',
        'title_path':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a > header > h2 > span.tsr-Base_HeadlineText',
        'img_path':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.tsr-Base_MediaWrapper.btn-Wrapper > img',
        'article_url':'#TOP > div.Home > div.o-ModuleWrapper.o-ModuleWrapper-has-more-bottom-gap.o-ModuleWrapper-is-tsr-top1 > article > div.o-Grid > div > div > div > div.o-Grid_Col.o-Grid_Col-8 > div > div > div > a',
        'country_name':'독일',
        'article_path':'#pageIndex_1',
        'spcial_picture':'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Seodaemun_Monument%2C_Seoul.jpg/640px-Seodaemun_Monument%2C_Seoul.jpg',
    },
    {
        'url':'https://www.bbc.com/news/uk',
        'plus_url':'https://www.bbc.com',
        'title_path':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        'img_path':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-image.gs-u-mb.gs-u-mb0\@xs.gel-2\/3\@m.gel-1\/2\@xl > div > div > img',
        'article_url':'#topos-component > div.mpu-available > div:nth-child(1) > div > div.nw-c-seven-slice.gel-layout__item.gs-u-pb\+\@m.gel-1\/1\@xl.gel-1\/1\@xxl.gs-u-ml0.nw-o-keyline.nw-o-no-keyline\@m.gs-u-display-block\@xs.gs-u-display-block\@l.gs-u-display-block\@xl.gs-u-display-none\@xxl > div > div.gs-c-promo-body.gs-u-mt\@xxs.gs-u-mt\@m.gs-c-promo-body--primary.gs-u-mt\@xs.gs-u-mt\@s.gs-u-mt\@m.gs-u-mt\@xl.gel-1\/3\@m.gel-1\/2\@xl > div:nth-child(1) > a',
        'country_name':'영국',
        'article_path':'#main-content > article',
        'spcial_picture':'https://i.namu.wiki/i/kec1tp2gFubT9DMgeRh3xd9qF82sW6SWmG6bv2SulfNZzYAZrJRl_b9Pu3FQByLsSaNiD6oaHU5WdZFeCtvv0g.webp',
    },
    {
        'url':'https://www.repubblica.it/',
        'plus_url':'https://www.repubblica.it/',
        'title_path':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        'img_path':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > figure > a > picture > img',
        'article_url':'#home > main > div:nth-child(2) > div.gd-column-8 > section:nth-child(1) > div > div > article > div > h2 > a:nth-child(1)',
        'country_name':'이탈리아',
        'article_path':'#article-body > div.story__text',
        'spcial_picture':'https://i.namu.wiki/i/lI83jn5gj17g3OSAw5Rd40APO5pRIEBdOPUWjGWKGz-smrWqBMo74_VK33RkJUj6qsdxqJUE77Jb_8SSfFSzfQ.webp',
    },
    {
        'url':'https://www.estadao.com.br/',
        'plus_url':'https://www.estadao.com.br',    
        'title_path':'#fusion-app > div > div:nth-child(2) > div:nth-child(1) > div > div > div.styles__Tag-sc-1kqcjew-0.styles__TagStyled-sc-1kqcjew-1.jizfvP.fhItmR.col-12.col-xl-8 > div > div.info > a > h2',
        'img_path':'#fusion-app > div > div:nth-child(2) > div:nth-child(1) > div > div > div.styles__Tag-sc-1kqcjew-0.styles__TagStyled-sc-1kqcjew-1.jizfvP.fhItmR.col-12.col-xl-8 > div > div.slick-slider.carrossel-item.slick-initialized > div > div > div.slick-slide.slick-active.slick-current > div > div > a > img',
        'article_url':'#fusion-app > div > div:nth-child(2) > div:nth-child(1) > div > div > div.styles__Tag-sc-1kqcjew-0.styles__TagStyled-sc-1kqcjew-1.jizfvP.fhItmR.col-12.col-xl-8 > div > div.info > a',
        'country_name':'브라질',
        'article_path':'#content > div.styles__ContentWrapperContainerStyled-sc-1ehbu6v-0.klsZKo.content-wrapper.news-body.container.content.template-reportagem',      
        'spcial_picture':'https://i.namu.wiki/i/lvrSfhtYy08Po5120KKUx19r75WLcuO6qiyeG3cy9z0cIJBz4svy3f3jW0FOBbvK4dKUwUGvR0ZEyCDlQ4ouAg.webp',
    },
    {
        'url':'https://www.joongang.co.kr/',
        'plus_url':'https://www.joongang.co.kr/',
        'title_path':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > div > h2 > a',
        'img_path':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > figure > a > img',
        'article_url':'#container > section > div:nth-child(4) > section.chain_wrap.col_lg9.spotlight_wrap > div > div.col_lg8 > div > div > h2 > a',
        'country_name':'대한민국',
        'article_path':'#article_body',
        'spcial_picture':'https://i.namu.wiki/i/hIBbbdByyQmvWd8l6SLuJJS9aCfLJWXl_jSBk3jnodgry6lJV20NM7hAdnlky4324Z89W56IalWypBH3DAMXxg.webp',
    },
    {
        'url':'https://thanhnien.vn',
        'plus_url':'https://thanhnien.vn',
        'title_path':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        'img_path':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > a > img',
        'article_url':'#content > div.section__home-focus > div > div > div.section__hf-main > div > div > div > div.item-first > div > h2 > a',
        'country_name':'베트남',
        'article_path':'#content > div.detail__section > div > div > div.detail__main > div > div.detail__cmain-flex > div.detail__cmain-main > div.detail-cmain > div',
        'spcial_picture':'https://i.namu.wiki/i/RSMkz5MAmcGpcvebyigDhIcaY8QM1RuPVqG9iipI-RfiaISGIlYDqKDB41WxvRNRh09DDzWPu0ZmhmrrhHuaEA.webp',
    },
    {
        'url':'https://www.abc.net.au/news/australia',
        'plus_url':'https://www.abc.net.au',
        'title_path':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.CardLayout_content__bev76 > h3 > span > a',
        'img_path':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.GenericCard_cardImage__f3Olr.undefined.CardLayout_imageContainer__89V4v.CardLayout_mobileImageTop__eskhD.CardLayout_tabletImageTop__ROit7.CardLayout_desktopImageTop__bXR3h > div > div > img',
        'article_url':'#anchor-8078842 > div > div > div > div > div:nth-child(1) > div > div > div.CardLayout_content__bev76 > h3 > span > a',
        'country_name':'호주',
        'article_path':'#body > div > div:nth-child(1) > div',                       
        'spcial_picture':'https://i.namu.wiki/i/LE-4kyzbxeeYGE2gc4Fnewr9jhBvkBgQDyeND1gQOPwRKGvXKhzcH_q5g_k_ew_lhg7XGnr9tevydzXEdc1tCw.webp',
    },
    {
        'url':'https://mexiconewsdaily.com/',
        'plus_url':'https://mexiconewsdaily.com',
        'title_path':'#tdi_115 > div > div:nth-child(1) > div > div.item-details > h3 > a',
        'img_path':'#tdi_115 > div > div:nth-child(1) > div > div.td-module-image > div > a > img',
        'article_url':'#tdi_115 > div > div:nth-child(1) > div > div.item-details > h3 > a',
        'country_name':'멕시코',
        'article_path':'#tdi_115 > div > div.vc_column.tdi_118.wpb_column.vc_column_container.tdc-column.td-pb-span8 > div > div.td_block_wrap.tdb_single_content.tdi_130.td-pb-border-top.td_block_template_1.td-post-content.tagdiv-type > div',
        'spcial_picture':'https://heritage.unesco.or.kr/wp-content/uploads/2019/03/site_0412_0001-500-333-20091001123325.jpg',
    },
    {
        'url':'https://cincodias.elpais.com/',
        'plus_url':'https://cincodias.elpais.com',
        'title_path':'#fusion-app > main > div.z.z-hi > section._g._g-md._g-o.b.b-d > div.b-d_b.b_op._g._g-md.b_op-1-2 > article > header > h2 > a',
        'img_path':'#fusion-app > main > div.z.z-hi > section._g._g-md._g-o.b.b-d > div.b-d_b.b_op._g._g-md.b_op-1-2 > article > figure > a > img',
        'article_url':'#fusion-app > main > div.z.z-hi > section._g._g-md._g-o.b.b-d > div.b-d_b.b_op._g._g-md.b_op-1-2 > article > header > h2 > a',
        'country_name':'스페인',
        'article_path':'#fusion-app > article > div.a_c.clearfix',                   
        'spcial_picture':'https://i.namu.wiki/i/FSR4n3YCckQir4wvbDkbDrUj6i_P3_5tA9ct53KCPGyWqf_0CDd4J1IWg5G94rV_6j9niudW4hO_b3ck46PiLg.webp',
    },
    {
        'url':'https://www.kompas.com/',
        'plus_url':'https://www.kompas.com',
        'title_path':'#general-container > div:nth-child(6) > div.col-bs10-7 > div.headline.ga--headline.clearfix > div.headline__big.clearfix > ul > div > div > li.headline__big__item.slick-slide.slick-current.slick-active > a > div.headline__big__box > h1',
        'img_path':'#general-container > div:nth-child(6) > div.col-bs10-7 > div.headline.ga--headline.clearfix > div.headline__big.clearfix > ul > div > div > li.headline__big__item.slick-slide.slick-current.slick-active > a > div.headline__big__img > img',
        'article_url':'#general-container > div:nth-child(6) > div.col-bs10-7 > div.headline.ga--headline.clearfix > div.headline__big.clearfix > ul > div > div > li.headline__big__item.slick-slide.slick-current.slick-active > a',
        'country_name':'인도네시아',
        'article_path':'body > div.wrap > div.container.clearfix > div.row.col-offset-fluid.clearfix.js-giant-wp-sticky-parent > div.col-bs10-7.js-read-article > div.read__article.mt2.clearfix.js-tower-sticky-parent > div.col-bs9-7 > div.read__content > div',
        'spcial_picture':'https://ozimg.flyasiana.com/temp/image/20190718/093e4176-764f-46ff-86f2-05bc31929386.jpeg',
    },
    {
        'url':'https://www.nrc.nl/',
        'plus_url':'https://www.nrc.nl',
        'title_path':'#item176594 > div > a > header > h3',
        'img_path':'#item176594 > div > a > div > figure > picture > img',
        'article_url':'#item176594 > div > a',
        'country_name':'네덜란드',
        'article_path':'#main > article > main',
        'spcial_picture':'https://ozimg.flyasiana.com/temp/image/20190718/093e4176-764f-46ff-86f2-05bc31929386.jpeg',
    },
    {
        'url':'https://www.philstar.com/',
        'plus_url':'https://www.philstar.com',
        'title_path':'#carousel_light > div > div > div.carousel__item.carousel__item-0 > div.carousel__item__title > h2 > a',
        'img_path':'#carousel_light > div > div > div.carousel__item.carousel__item-0 > div.carousel__item__image > a > picture > img',
        'article_url':'#carousel_light > div > div > div.carousel__item.carousel__item-0 > div.carousel__item__title > h2 > a',
        'country_name':'필리핀',
        'article_path':'#sports_article_writeup',
        'spcial_picture':'https://admin.itsmorefuninthephilippines.co.kr//uploads/Destination_Images/manila_main2019522_17031.jpg',
    }    
]