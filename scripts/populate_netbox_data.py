import pynetbox
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


p2p_range = '172.16.'
lo0_range = '192.168.255.'

num_ios = 1
num_os10 = 1

# Connect to NetBox
nb = pynetbox.api(
    'http://localhost',
    token='3cae8e837546ef3105bb8ff64309025cc37216a4'
)
# Create new Site
new_site = nb.dcim.sites.get(slug='2_node_demo_topo')
if not new_site:
    new_site = nb.dcim.sites.create(
        name='2-node-demo-topo',
        slug='2_node_demo_topo',
    )
# Create Device Role  for IOS 
nb.dcim.device_roles.create(
    name='ios_device',
    slug='ios_Device',
    color='2196f3'
)
# Create Device Role for OS10
nb.dcim.device_roles.create(
    name='os10_device',
    slug='os10_device',
    color='3f51b5'
)

for a in range(num_ios):
    nb.ipam.prefixes.create(
        prefix=f'{p2p_range}{a+1}.0/24',
        description=f'ios-{a+1} P2P'
    )
    n = 0
    for h in range(num_os10):
        nb.ipam.prefixes.create(
            prefix=f'{p2p_range}{a+1}.{n}/31',
            description=f'ios-{a+1}-os10-{h+1} P2P'
        )  
        n+=2

nb.ipam.prefixes.create(
        prefix=f'{lo0_range}0/24',
        description=f'Switch Loopbacks'
    )

ios_dev = ["ios_7200_1"]
os10_dev = ["os10_5224_1"]








all_devices = os10_dev + ios_dev

