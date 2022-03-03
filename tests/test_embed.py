from bs4 import BeautifulSoup

from wagtailaudioembed.embed import AudioEmbedFinder

from django.test import SimpleTestCase


class AudioEmbedFinderTest(SimpleTestCase):

    context = {"title": "TestTitle", "url": "https://audio.org/file.ogg"}

    def setUp(self):
        self.finder = AudioEmbedFinder()

    def test_accept_invalid_urls(self):
        invalid_urls = [
            "",
            "http://foo.de/test.mp4",
            "https://www.youtube.com/watch?v=abcdefg",
            "ftp://ftpserv.com/datei.ogg" "datei.ogg",
        ]
        for url in invalid_urls:
            self.assertFalse(self.finder.accept(url), msg=f"{url} should be invalid.")

    def _get_soup(self):
        return BeautifulSoup(self.finder._get_html(self.context), features="html5lib")

    def test_get_html_audio(self):
        self.assertEqual(1, len(self._get_soup().findAll("audio")))
        self.assertEqual(self._get_soup().find("audio").get("src"), self.context["url"])

    def test_get_html_caption(self):
        title = self._get_soup().find("figcaption")
        self.assertIsNotNone(title)
        self.assertEqual(title.text, self.context["title"])

    def test_get_html_missing_caption(self):
        del self.context["title"]
        figcaption = self._get_soup().find("figcaption")
        self.assertIsNone(figcaption)
        figure = self._get_soup().find("figure")
        self.assertIsNone(figure)

    def test_accept(self):
        valid_urls = [
            "http://www.oekolog.at/test.ogg",
            "https://www.oekolog.at/test.ogg",
            "https://othersite.de/test.ogg",
            "https://somesite.de/bar.ogg?extra_params=should_not_matter",
            "noscheme.com/bar.ogg",
            "www.subdomain.com/foo.ogg",
            "http://spacesinurl.com/spacey%20filename.ogg",
        ]
        for url in valid_urls:
            self.assertTrue(self.finder.accept(url), msg=f"{url} should be valid.")
