from datetime import date

from django.test import TestCase

from ..models import Post, Author, Tag, Tech, Project, Job


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author_ = 'Igor Kuivjogi Fernandes'

        cls.author = Author.objects.create(name=cls.author_)
        cls.tag_1 = Tag.objects.create(name='test')
        cls.tag_2 = Tag.objects.create(name='develop')

        cls.post = Post.objects.create(
            title='A test', author=cls.author, content='This is a test.', date=date(2021, 6, 16))
        cls.post.tags.set([cls.tag_1, cls.tag_2])

    def test_if_post_has_required_author(self):
        self.assertEqual(self.post.author.name, self.author_)

    def test_if_post_has_many_tags(self):
        self.assertEqual(self.post.tags.count(), 2)

    def test_if_string_representation_is_the_title(self):
        title = self.post.title
        self.assertEqual(str(self.post), title)


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Igor Kuivjogi Fernandes')

    def test_if_string_representation_is_the_author_name(self):
        name = self.author.name
        self.assertEqual(str(self.author), name)


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='test')

    def test_if_string_representation_is_the_tag_name(self):
        name = self.tag.name
        self.assertEqual(str(self.tag), name)


class TechModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tech = Tech.objects.create(name='Python')

    def test_if_string_representation_is_the_tech_name(self):
        name = self.tech.name
        self.assertEqual(str(self.tech), name)


class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tech_1 = Tech.objects.create(name='Python')
        cls.tech_2 = Tech.objects.create(name='Django')

        cls.project = Project.objects.create(
            title='Django blog', content='This was made...', date=date(2021, 7, 16))
        cls.project.techs.set([cls.tech_1, cls.tech_2])

    def test_if_string_representation_is_the_title(self):
        title = self.project.title
        self.assertEqual(str(self.project), title)


class JobModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tech_1 = Tech.objects.create(name='Python')
        cls.tech_2 = Tech.objects.create(name='Flask')
        cls.tech_3 = Tech.objects.create(name='SQL')

        cls.job = Job.objects.create(position='Python Developer', company='ABC', date=date(
            2021, 6, 16))
        cls.job.techs.set([cls.tech_1, cls.tech_2, cls.tech_3])

    def test_if_job_has_many_techs(self):
        self.assertEqual(self.job.techs.count(), 3)

    def test_if_string_representation_is_the_position_with_the_company(self):
        position = self.job.position
        company = self.job.company
        self.assertEqual(str(self.job), f'{position} ({company})')
