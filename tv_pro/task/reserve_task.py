import os,sys, time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'tv_pro.settings'
sys.path.append(BASE_DIR)
django.setup()
from django.core.mail import send_mail
from django.conf import settings
from tv_backend.models import Reviews
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import json

urlpart = 'https://yandex.ru/maps/api/business/fetchReviews?ajax=1&businessId=182308908187&csrfToken='
urlpart2 = '&page=1&pageSize=50&ranking=by_relevance_org&reqId=1582326767841727-513550703-sas1-6045-sas-addrs-nmeta-new-8031&sessionId=1582326767812_796524'
opts = Options()
#opts.set_headless()
#assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts)
browser.get(urlpart+urlpart2)
time.sleep(5)
search_csrf = browser.find_element_by_class_name("objectBox-string").text
browser.get(urlpart + search_csrf[1:-1]+urlpart2)
respons = json.loads(browser.find_element_by_tag_name('body').text)
detect_tv = [("смартфон"), ("ноутбук"), ("ноутбуком"), ("компьютер"), ("компьютером"), ("телефон"), ("пк"),
             ("принтер"), ("мфу"), ("ноут"), ("комп"), ("iphone"), ("ipad"), ("айфон"),  ("айпад"), ("ноутбука")]
try:
    for i in respons["data"]["reviews"]:
        if len(i["author"]["avatarUrl"])>5 :
            print('Длина', len(i["author"]["avatarUrl"]))
            user_photo_link = i["author"]["avatarUrl"]
            user_photo_link = user_photo_link.replace('{size}', 'islands-75')
        else:
            user_photo_link = 'https://yapic.yandex.ru/get/88085623/islands-75'
        testing = []
        [testing.append((x)) for x in i["text"].replace(',', ' ').replace('.', ' ').split()]
        if not any(m in testing for m in detect_tv):
            respons_reviews_wr = Reviews.objects.update_or_create(
                            name_user=i["author"]["name"],
                            user_photo_link=user_photo_link,
                            review=i["text"],
                            review_rate=i["rating"],
                        )
            if respons_reviews_wr:
                send_mail(u'На сайте ТВ СЕРВИСА появился новый отзыв' , i["text"],
                        settings.EMAIL_HOST_USER, ['skret002@mail.ru'])
except Exception as e:
    send_mail(u'КРИТИЧНО! На сайте ТВ СЕРВИСА выявлена критическая ошибка получения данных', e,
              settings.EMAIL_HOST_USER, ['skret002@mail.ru'])
browser.close()