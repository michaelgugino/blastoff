'''Warmup our cache by prepopulating popular pages'''
import blastoff.cache_helper as cache_helper
import os,glob
import redis
import sample_data

redpool = redis.ConnectionPool(
    host='localhost', db=0)
redcon = redis.Redis(connection_pool=redpool)

ch = cache_helper.CacheHelper(redcon=redcon)

filenames = glob.glob(os.path.join('blastoff', 'templates','*.html'))
kd = {}
for name in filenames:
    basename, ext = os.path.splitext(os.path.basename(name))
    with open (name, 'r') as myfile:
        data=myfile.read()
    kd['templates:'+basename] = data

ch.put_in_cache(kd)
ch.put_in_cache(sample_data.sample_dict)
