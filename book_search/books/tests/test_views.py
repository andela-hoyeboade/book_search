from books.models import Book, Category
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestBookView(TestCase):

    def setUp(self):
        self.health_category = Category.objects.create(name='Health')
        self.sports_category = Category.objects.create(name='Sports')
        self.health_book = Book.objects.create(
            title='Living a Healthy lifestyle', category=self.health_category)
        self.sports_book = Book.objects.create(
            title='The science of sports', category=self.sports_category)

    def test_can_visit_book_page(self):
        # User should be able to visit books page
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_can_search_books_by_title(self):
        # Search should return only books whose title contains query_string
        response = self.client.get(reverse('book_list'), {
                                   'q': 'lifestyle', 'search_type': 'title'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.health_book, response.context_data.get('books'))
        self.assertIn('Living a Healthy lifestyle', response.content)

        self.assertNotIn(self.sports_book, response.context_data.get('books'))
        self.assertNotIn('The science of sports', response.content)

    def test_can_search_books_by_category(self):
        # Search should returns only books matching specified category
        response = self.client.get(reverse('book_list'), {
                                   'q': 'sports', 'search_type': 'category'})
        self.assertEqual(response.status_code, 200)

        self.assertIn(self.sports_book, response.context_data.get('books'))
        self.assertIn('The science of sports', response.content)

        self.assertNotIn(self.health_book, response.context_data.get('books'))
        self.assertNotIn('Living a Healthy lifestyle', response.content)

    def test_can_search_books_by_category_and_title(self):
        # Search should return only books whose category matches or title
        # contains query_string
        response = self.client.get(reverse('book_list'), {
                                   'q': 'he', 'search_type': 'any'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.health_book, response.context_data.get('books'))
        self.assertIn(self.sports_book, response.context_data.get('books'))

        self.assertIn('Living a Healthy lifestyle', response.content)
        self.assertIn('The science of sports', response.content)
