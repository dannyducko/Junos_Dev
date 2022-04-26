from importlib.resources import path
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

srx1 = Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD').open()

with Config(srx1, mode='exclusive') as cu:
    cu.load(path='Configuration\compare.conf', overwrite=True)
    cu.pdiff()
    cu.rollback(rb_id=0)

srx1.close()