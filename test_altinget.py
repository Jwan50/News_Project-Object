import unittest

import firebase_admin
from firebase_admin import credentials
from news_builder import altinget_building
from firebase_admin import firestore
from news_builder.altinget_building import alt_news_building


class test_Altinget(unittest.TestCase):

    def test_getNews_altinget(self):
        global headline, content, date, data_list, category, provider
        try:
            alt_news_building(2).getNews_altinget()
            category = altinget_building.alt_news_building(2).news.category
            headline = altinget_building.alt_news_building(2).news.headline
            content = altinget_building.alt_news_building(2).news.content
            date = altinget_building.alt_news_building(2).news.date
            provider = altinget_building.alt_news_building(2).news.provider
            firebase_admin.initialize_app(credentials.Certificate(r"C:\Users\gwan1\PycharmProjects\News_Project\serviceAccountKey.json"))

        except Exception as e:
            print(e)
        db = firestore.client()

        news_list = str(headline)
        docs = db.collection('altinget').where('headline', '==', headline).stream()
        for doc in docs:
            a = u'{} => {}'.format(doc.id, doc.to_dict())
            a = a.split("=>")
            a = a[1]
            a = a.split("headline': ")
            a = a[1]
            if 'content' in a:
                a = a.split(", 'content':")
                a = a[0]
            if 'provider' in a:
                a = a.split(", 'provider':")
                a = a[0]
            if 'category' in a:
                a = a.split(", 'category':")
                a = a[0]

            if 'date' in a:
                a = a.split(", 'date':")
                a = a[0]
            if '\xa0' in a:
                a = a.replace('\xa0', '')
            a = a.replace(u"'", u"")
            print(news_list, '----', a)

            self.assertEqual(news_list, a)