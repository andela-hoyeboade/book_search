from books.models import Book, Category
from django.test import TestCase


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Health')

    def test_category_object_representation(self):
        self.assertEqual(str(self.category), self.category.name)


class TestBook(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Wellness')
        self.book = Book.objects.create(
            title='Living a healthy lifestyle', category=self.category)

    def test_book_object_representation(self):
        self.assertEqual(str(self.book), self.book.title)
