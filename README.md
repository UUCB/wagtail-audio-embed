# Wagtail-Audio-Embed

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/peterjochum/wagtail-audio-embed?sort=semver)
[![Coverage Status](https://coveralls.io/repos/github/peterjochum/wagtail-audio-embed/badge.svg?branch=main)](https://coveralls.io/github/peterjochum/wagtail-audio-embed?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Wagtail-Audio-Embed allows you to use links to sound files using the embed
feature of the [Draftail editor](https://www.draftail.org).

It uses the default audio tag to play the audio file:

![Rendering in Firefox](https://github.com/peterjochum/wagtail-audio-embed/raw/main/img/screenshot.png)

See [Wagtail-Audio-Embed on PyPi](https://pypi.org/project/wagtail-audio-embed/)
for binaries and additional information.

## Quick start

Install using pip:

```bash
pip install wagtail-audio-embed
```

Add "wagtailaudioembed" to your INSTALLED_APPS setting:

```python
INSTALLED_APPS = [
    ...
    'wagtailaudioembed',
]
```

Register the embed finder class in your settings:

```python
WAGTAILEMBEDS_FINDERS = [
    {
        "class": "wagtailaudioembed.embed.AudioEmbedFinder",
    }
]
```

Restart your application and start embedding links to Vorbis files.

## Known limitations

- `.ogg` has to be in the URL for the finder to accept. The finder is not
  allowed to make requests in the URL acceptance decision.
- Only Vorbis files are supported which excludes Safari Users
  [according to Caniuse](https://caniuse.com/?search=audio%20format).

## References

- [Advanced tutorial: How to write reusable apps](https://docs.djangoproject.com/en/4.0/intro/reusable-apps/)
- [Wagtail docs - Embedded content](https://docs.wagtail.org/en/stable/advanced_topics/embeds.html)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Mozilla Developer Network : The Embed Audio element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
