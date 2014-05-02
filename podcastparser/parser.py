from lxml import etree
from .models import Podcast, PodcastItem, ITunesData, ItemITunesData

ATTRIBUTE_MAPPING = {
    'pubDate': 'pub_date',
    'isCloseCaptioned': 'is_close_captioned',
    'new-feed-url': 'new_feed_url',
}


def get_podcast(feed_url):
    parsed = etree.parse(feed_url)
    channel = parsed.find('channel')

    podcast = Podcast()
    itunes_data = ITunesData()
    items = []

    for element in channel:
        tag = element.tag.split('}')[-1]
        attr = ATTRIBUTE_MAPPING.get(tag, tag)

        prefix = element.prefix
        text = element.text
        attributes = element.attrib

        if prefix == 'itunes':

            if attr in ITunesData.__attrs__:

                if text:
                    setattr(itunes_data, attr, text)
                elif attributes:
                    setattr(itunes_data, attr, attributes)

        if attr == 'item':
            podcast_item = PodcastItem()
            item_itunes_data = ItemITunesData()

            for elem in element:
                etag = elem.tag.split('}')[-1]
                eattr = ATTRIBUTE_MAPPING.get(etag, etag)

                eprefix = elem.prefix
                etext = elem.text
                eattributes = elem.attrib

                if eprefix == 'itunes':

                    if eattr in ItemITunesData.__attrs__:

                        if etext:
                            setattr(item_itunes_data, eattr, etext)
                        elif eattributes:
                            setattr(item_itunes_data, eattr, eattributes)

                if eattr in PodcastItem.__attrs__:

                    if etext:
                        setattr(podcast_item, eattr, etext)
                    elif eattributes:
                        setattr(podcast_item, eattr, eattributes)

            podcast_item.itunes_data = item_itunes_data
            items.append(podcast_item)

        if attr in Podcast.__attrs__:

            if text:
                setattr(podcast, attr, text)
            elif attributes:
                setattr(podcast, attr, attributes)

    podcast.itunes_data = itunes_data
    podcast.items = items

    return podcast


def get_podcasts_from_opml(opml_file):
    podcasts = []

    parsed = etree.parse(opml_file)
    body = parsed.find('body')
    feeds = body.find('outline')

    for feed in feeds:
        podcasts.append(feed.attrib)

    return podcasts
