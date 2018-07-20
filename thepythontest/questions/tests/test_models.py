from django.contrib.auth.models import AbstractUser
from django.db import models
from django.test import TestCase
from questions.models import User, Question, Answer


class QuestionModelTest(TestCase):

    def test_fields(self):
        expected_fields = {
            'text': models.CharField,
            'verified': models.BooleanField,
            'creator': models.ForeignKey
        }

        for field in expected_fields:
            self.assertTrue(hasattr(Question, field))
            self.assertTrue(isinstance(
                Question._meta.get_field(field),
                expected_fields[field]
            ))

        self.assertEqual(Question._meta.get_field('text').max_length, 600)
        self.assertEqual(Question._meta.get_field('text').unique, True)

        self.assertEqual(Question._meta.get_field('verified').default, False)

        self.assertEqual(
            Question._meta.get_field('creator').related_model, User
        )
        self.assertEqual(
            Question._meta.get_field('creator').remote_field.on_delete,
            models.SET_NULL
        )
        self.assertEqual(Question._meta.get_field('creator').null, True)


class AnswerModelTest(TestCase):

    def test_fields(self):

        expected_fields = {
            'text': models.CharField,
            'correct': models.BooleanField,
            'question': models.ForeignKey,
        }

        for field in expected_fields:
            self.assertTrue(hasattr(Answer, field))
            self.assertTrue(isinstance(
                Answer._meta.get_field(field),
                expected_fields[field]
            ))

        self.assertEqual(Answer._meta.get_field('text').max_length, 400)

        self.assertEqual(Answer._meta.get_field('correct').default, False)

        self.assertEqual(
            Answer._meta.get_field('question').related_model, Question
        )
        self.assertEqual(
            Answer._meta.get_field('question').remote_field.on_delete,
            models.CASCADE
        )


class UserModelTest(TestCase):

    def test_superclass(self):
        self.assertTrue(issubclass(User, AbstractUser))

    def test_fields(self):

        expected_fields = {
            'score': models.IntegerField
        }

        for field in expected_fields:
            self.assertTrue(hasattr(User, field))
            self.assertTrue(isinstance(
                User._meta.get_field(field),
                expected_fields[field]
            ))

        self.assertEqual(User._meta.get_field('score').default, 0)
