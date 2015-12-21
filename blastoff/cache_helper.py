'''This module loads items from the cache so we can use them locally'''


class CacheHelper(object):

    def __init__(self, redcon):
        '''store the connection and create an empty dict to hold keys'''
        self.redcon = redcon
        self.cache_dict = {}

    def load_from_cache(self,kl):
        '''load a list of keys from the cache'''
        res = self.redcon.mget(kl)
        for i in range(0,len(kl)):
            self.cache_dict[kl[i]] = res[i]

    def put_in_cache(self,kd):
        self.redcon.mset(kd)
