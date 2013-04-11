# -*- coding: utf-8 -*-
import md5
from dogpile.cache.region import make_region


def md5_key_mangler(key):
    """Receive cache keys as long concatenated strings;
    distill them into an md5 hash.

    """
    try:
        return md5.md5(key).hexdigest()
    except UnicodeEncodeError:
        return md5.md5(key.encode('utf-8')).hexdigest()

regions = {}
regions['gdw'] = make_region(key_mangler=md5_key_mangler).configure(
    'dogpile.cache.memcached',
    expiration_time=21600,
    arguments={
        'url': '127.0.0.1:11211',
        'distributed_lock': True,
    }
)
