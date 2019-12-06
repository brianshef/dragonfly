import wikipediaapi

WIKI_LANG = 'en'
XFORMAT = wikipediaapi.ExtractFormat.WIKI

class Handler():
    def __init__(self, config):
        _client = wikipediaapi.Wikipedia(language=WIKI_LANG, extract_format=XFORMAT)
        self.client = _client
        self.artist = config.artist
        self.wiki = config.wiki
    
    def artist_page_name(self):
        return self.wiki if self.wiki else self.artist.replace(' ', '_')
    
    def get_wiki(self):
        page = self.client.page(self.artist_page_name())
        if not page.exists():
            raise Exception('wiki page {} does not exist'.format(page))
        return page.text.upper()
