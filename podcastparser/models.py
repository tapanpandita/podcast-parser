class Podcast(object):
    '''
    Contains attributes of a podcast feed

    '''

    __attrs__ = [
        'title',
        'link',
        'copyright',
        'description',
        'language',
        'itunes_data',
        'items',
    ]

    def __init__(
        self,
        title=None,
        link=None,
        copyright=None,
        description=None,
        language=None,
        itunes_data=None,
        items=None,
    ):
        self.title = title
        self.link = link
        self.copyright = copyright
        self.description = description
        self.language = language
        self.itunes_data = itunes_data
        self.items = items


class ITunesData(object):
    '''
    Contains the itunes attributes of a podcast

    '''

    __attrs__ = [
        'author',
        'block',
        'category',
        'image',
        'explicit',
        'complete',
        'new_feed_url',
        'owner',
        'subtitle',
        'summary',
    ]

    def __init__(
        self,
        author=None,
        block=None,
        category=None,
        image=None,
        explicit=None,
        complete=None,
        new_feed_url=None,
        owner=None,
        subtitle=None,
        summary=None,
    ):
        self.author = author
        self.block = block
        self.category = category
        self.image = image
        self.explicit = explicit
        self.complete = complete
        self.new_feed_url = new_feed_url
        self.owner = owner
        self.subtitle = subtitle
        self.summary = summary


class PodcastItem(object):
    '''
    Contains the attributes of a podcast episode

    '''

    __attrs__ = [
        'guid',
        'title',
        'pub_date',
        'description',
        'enclosure',
        'author',
        'itunes_data',
    ]

    def __init__(
        self,
        guid=None,
        title=None,
        pub_date=None,
        description=None,
        enclosure=None,
        author=None,
        itunes_data=None,
    ):
        self.guid = guid
        self.title = title
        self.pub_date = pub_date
        self.description = description
        self.enclosure = enclosure
        self.author = author
        self.itunes_data = itunes_data


class ItemITunesData(object):
    '''
    Contains the itunes attributes of a podcast episode

    '''

    __attrs__ = [
        'author',
        'block',
        'image',
        'duration',
        'explicit',
        'is_close_captioned',
        'order',
        'subtitle',
        'summary',
        'keywords',
    ]

    def __init__(
        self,
        author=None,
        block=None,
        image=None,
        duration=None,
        explicit=None,
        is_close_captioned=None,
        order=None,
        subtitle=None,
        summary=None,
        keywords=None,
    ):
        self.author = author
        self.block = block
        self.image = image
        self.duration = duration
        self.explicit = explicit
        self.is_close_captioned = is_close_captioned
        self.order = order
        self.subtitle = subtitle
        self.summary = summary
        self.keywords = keywords
