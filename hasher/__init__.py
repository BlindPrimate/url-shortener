import hashids

def generate_hash_id(url):
    """Convert string to hash."""
    hasher = hashids.Hashids()
    return hasher.decode(url)


