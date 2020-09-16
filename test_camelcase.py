import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelcase.camel_case('Hello World'))

    def test_empty_entry(self):
        self.assertEqual('', camelcase.camel_case(' '))

    def test_one_word_entry(self):
        self.assertEqual('hello', camelcase.camel_case('Hello'))

    def test_spaces(self):
        self.assertEqual('hello', camelcase.camel_case('Hello '))

        self.assertEqual('hello', camelcase.camel_case(' Hello'))

        self.assertEqual('hello', camelcase.camel_case('  Hello'))

    def test_digit_entry(self):
        self.assertEqual('', camelcase.camel_case(1234))

        self.assertEqual('', camelcase.camel_case('🐈'))

    def test_escape(self):
        self.assertEqual('helloWorld', camelcase.camel_case('\nHello World'))

        self.assertEqual('helloWorld', camelcase.camel_case('Hello World\n'))

        self.assertEqual('helloWorld', camelcase.camel_case('Hello\nWorld'))

    def test_capital(self):
        self.assertEqual('helloWorld', camelcase.camel_case('hElLo WoRlD'))

        self.assertEqual('helloWorld', camelcase.camel_case('HELLO WORLD'))

        self.assertEqual('helloWorld', camelcase.camel_case('hello world'))
