from setuptools import setup

setup(
    name = "podcast-parser", # pip install podcast-parser
    description = "fast podcast feed parser",
    #long_description=open('README.md', 'rt').read(),

    # version
    # third part for minor release
    # second when api changes
    # first when it becomes stable someday
    version = "0.0.2",
    author = 'Tapan Pandita',
    author_email = "tapan.pandita@gmail.com",

    url = 'http://github.com/tapanpandita/podcast-parser/',
    license = 'BSD',

    # as a practice no need to hard code version unless you know program wont
    # work unless the specific versions are used
    install_requires = ["lxml", ],

    py_modules = ["podcastparser"],

    zip_safe = True,
)

# TODO: Do all this and delete these lines
# register: Create an accnt on pypi, store your credentials in ~/.pypirc:
#
# [pypirc]
# servers =
#     pypi
#
# [server-login]
# username:<username>
# password:<pass>
#
# $ python setup.py register # one time only, will create pypi page for
# podcast-parser
# $ python setup.py sdist --formats=gztar,zip upload # create a new release
#
