import hashids

SALT = 'kavaqizuqnqwfuzhqjuxcuis'

class Hasher:
    def __init__(self, length=8):
        self._hasher = hashids.Hashids(SALT, length)

    def generate_hash_id(self, url):
        """Convert string to hash."""
        return self._hasher.encode(url)

    def retrieve_url_id_from_hash(self, url_hash):
        return self._hasher.decode(url_hash)
