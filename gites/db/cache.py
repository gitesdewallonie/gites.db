# -*- coding: utf-8 -*-
import md5
import os
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
memcached_server = os.environ.get('MEMCACHE_SERVER', '127.0.0.1:11211')
regions['gdw'] = make_region(key_mangler=md5_key_mangler).configure(
    'dogpile.cache.memcached',
    expiration_time=21600,
    arguments={
        'url': memcached_server,
        'distributed_lock': True,
    }
)
