from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

h1 = net.get('h1')
# h2 = net.get('h2')

results=h1.cmd('ifconfig')
print results