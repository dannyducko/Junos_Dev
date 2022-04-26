from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml

# Below are DNS entries for my lab.
junos_hosts = ['lab.srx1', 'lab.srx2']

for host in junos_hosts:
    filename = 'Config_using_jinja2/' + host + '.yml'
    with open(filename, 'r') as fh:
        data = yaml.safe_load(fh)
        with Device(host, user='USERNAME', passwd='PASSWORD') as dev:
            with Config(dev, mode="exclusive") as conf:
                conf.load(template_path="Config_using_jinja2/example.j2", template_vars=data, format="text")
                conf.pdiff()
                conf.commit()
            print("Configuration loaded succesfully.")