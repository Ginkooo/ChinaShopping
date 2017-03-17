import os
import codecs
from django.test import TestCase
from unittest.mock import MagicMock
from apps.provider_lister.providers.alieexpress.alieexpress_crawler import AliexpressCrawler

class AliexpressTest(TestCase):
    def test_can_extract_offers(self):
        html = ''
        with codecs.open(os.path.join(os.path.join(os.path.dirname(__file__), 'resources'), 'alie.html'), 'r', 'utf-8') as f:
            html += f.read()

        connection_response = MagicMock()
        connection_response.get_html = MagicMock(return_value=html)
        connection_service = MagicMock()
        connection_service.execute = MagicMock(return_value=connection_response)
