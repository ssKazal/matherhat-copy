from hashids import Hashids
from datetime import datetime
import random


def generate_hashids(obj_name, obj_id):
	hashids = Hashids(salt='{}{}'.format(obj_name, obj_id))
	ids = hashids.encode(5, 5, 5, obj_id)
	return ids


def generate_uids():
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	n1 = random.randint(10000, 1000000)
	hashids = Hashids(salt='{}{}'.format(n1, timestamp))
	n2 = random.randint(1, 9999)
	ids = hashids.encode(5, 5, 5, n2)
	return ids