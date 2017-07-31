from django.test import TestCase, Client, tag


class TestIndexView(TestCase):
    @tag('obsolete')
    def test_index_site(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)
