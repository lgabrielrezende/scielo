from rest_framework import serializers
from .models import Article, Journal
from functools import reduce
import operator
from typing import List, Dict


class CommonSerializer:

    @staticmethod
    def get_from_dict(data, keys):
        return reduce(operator.getitem, keys, data)

    def extract_values(self, data: Dict, keys: List):
        try:
            value_from_keys = self.get_from_dict(data, keys)
            return value_from_keys

        except KeyError:
            raise serializers.ValidationError({
                f'Error while serialization {keys}'
            })


class JournalSerializer(CommonSerializer, serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

    def to_internal_value(self, data):
        journal_id = self.extract_values(data=data, keys=['journal-id'])
        title = self.extract_values(data=data, keys=['journal-title-group', 'journal-title'])

        return {
            'journal_id': journal_id,
            'title': title
        }


class ArticleSerializer(CommonSerializer, serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

    def to_internal_value(self, data):
        article_id = self.extract_values(data=data, keys=['front', 'article-meta', 'article-id'])
        title = self.extract_values(data=data, keys=['front', 'article-meta', 'title-group',
                                                     'trans-title-group', 'trans-title'])
        volume = self.extract_values(data=data, keys=['front', 'article-meta', 'volume'])
        publication_year_date = self.extract_values(data=data, keys=['front', 'article-meta', 'pub-date', 'year'])
        journal = self.extract_values(data=data, keys=['front', 'journal-meta'])

        return {
            'article_id': article_id,
            'title': title,
            'volume': volume,
            'publication_year_date': publication_year_date,
            'journal': journal
        }

    def create(self, validated_data):
        journal_validated_data = validated_data.pop('journal')
        journal_serializer = JournalSerializer(data=journal_validated_data)
        journal_serializer.is_valid(raise_exception=True)
        journal = journal_serializer.save()
        return Article.objects.create(journal=journal, **validated_data)