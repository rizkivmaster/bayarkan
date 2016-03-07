__author__ = 'rizkivmaster'

from datetime import datetime

# <user_id, amount>
cache = dict()


def topup(*args, **kwargs):
    """
    add money to account
    :param args:
    :param kwargs:
    :return:
    """

    user_id = kwargs['user_id']
    topup_amount = kwargs['topup_amount']
    cache[user_id] = cache[user_id] + topup_amount if cache.has_key(user_id) else topup_amount

def retrieve_amount(*args, **kwargs):
    """
    retrieve amount
    :param args:
    :param kwargs:
    :return:
    """
    user_id = kwargs['user_id']
    return cache[user_id] if user_id in cache else 0


def send(*args,**kwargs):
    """
    send money from one to another
    :param arg:
    :param args:
    :return:
    """
    destination_user_id = kwargs['destination_user_id']
    source_user_id = kwargs['source_user_id']
    send_amount = kwargs['send_amount']
    check_amount = cache[source_user_id] if source_user_id in cache else 0
    if check_amount - send_amount < 0:
        raise NoMoreFundException()
    cache[source_user_id] = check_amount - send_amount
    cache[destination_user_id] = cache[destination_user_id] + send_amount if destination_user_id in cache else send_amount


def reimburse(*args, **kwargs):
    """
    return money from people
    :param args:
    :param kwargs:
    :return:
    """
    user_id = kwargs['user_id']
    reimburse_amount = kwargs['reimburse_amount']
    check_amount = cache[user_id] if user_id in cache else 0
    if check_amount - reimburse_amount < 0:
        raise NoMoreFundException()
    cache[user_id] = check_amount - reimburse_amount


def print_stats(*agrs,**kwargs):
    print(datetime.now())
    for key, value in cache.iteritems():
        print(key, value)




class NoMoreFundException(Exception):
    pass