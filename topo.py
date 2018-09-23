"""

Mininet Topologies with 2 nodes 
Author : Shreshth Tuli

Usage:
    - sudo mn --custom topo.py --controller=remote,ip=127.0.0.1

To specify parameters use: --link tc,bw=10,delay=3,loss=2,max_queue_size=3

Example : for ring topology with bandwidth limited to 2:
	- sudo mn --custom topo.py --controller=remote,ip=127.0.0.1 --link tc,bw=10

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SimpleTopo( Topo ):
    "Simple Linear Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        h1 = self.addHost('h1', ip='0.0.0.1')
        h2 = self.addHost('h2', ip='0.0.0.2')
        s1 = self.addSwitch('s1')

        self.addLink(h1, s1)
        self.addLink(h2, s1)   

topos = SimpleTopo()