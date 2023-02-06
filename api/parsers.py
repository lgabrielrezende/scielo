from rest_framework.parsers import BaseParser
from bs4 import BeautifulSoup

JOURNAL_TAGS = ['journal-id', 'journal-title-group']


class PlainTextParser(BaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read().decode()


class ArticleXmlParser(BaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        parse_constant = {}
        data_decoded = stream.read().decode()
        soup = BeautifulSoup(data_decoded, 'lxml')
        journal_id = soup.find('front').find('journal-meta').find('journal-id').get_text()
        journal_title = soup.find('front').find('journal-meta').find('journal-title-group').find(
            'journal-title').get_text()
        return parse_constant