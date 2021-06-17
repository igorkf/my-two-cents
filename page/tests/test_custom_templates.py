from django.test import TestCase

from ..templatetags import markdown_extras


class MarkdownExtrasTest(TestCase):
    def test_markdown_header(self):
        content = 'This is a header'
        html = f'<h1>{content}</h1>'
        result = markdown_extras.markdown(f'# {content}')
        self.assertEqual(result, html)

    def test_markdown_fenced_code_block(self):
        content = 'x = [1, 2, 3]'
        html = f'<p><code>{content}</code></p>'
        result = markdown_extras.markdown(f'```{content}```')
        self.assertEqual(result, html)
