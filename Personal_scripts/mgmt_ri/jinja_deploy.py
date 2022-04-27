from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
import creds

# Below are DNS entries for my lab.
junos_hosts = ['lab.srx1', 'lab.srx2']

for host in junos_hosts:
    filename = host + '.yml'
    with open(filename, 'r') as fh:
        data = yaml.safe_load(fh)
        with Device(host, user=creds.username, passwd=creds.password) as dev:
            with Config(dev, mode="exclusive") as conf:
                conf.load(template_path="mgmt_ri.j2", template_vars=data, format="text")
                conf.pdiff()
                conf.commit()
            print("Configuration loaded successfully.")
