"""

Mininet Topologies with 2 nodes 
Author : Shreshth Tuli

Usage:
    - sudo mn --custom topo.py --topo linear --controller=remote,ip=127.0.0.1

To specify parameters use: --link tc,bw=10,delay=3,loss=2,max_queue_size=3

Example : for ring topology with bandwidth limited to 2:
	- sudo mn --custom topo.py --topo linear --controller=remote,ip=127.0.0.1 --link tc,bw=1,delay=3,loss=1

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SimpleTopo( Topo ):
    "Linear Topology Mininet"

    def __init__( self , b=1, d='0ms', l=0):

        # Initialize topology
        Topo.__init__( self )

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s2, s2, bw = b, delay = d, loss = l)


if __name__ == '__main__':
    topo = SimpleTopo(1, '0ms', 0)
    net = Mininet( topo=topo,
               host=CPULimitedHost, link=TCLink )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    h1 = net.get('h1')
    h2 = net.get('h2')
    h1.cmd('tmux pyhton3 host.py 0 README.md a.txt')