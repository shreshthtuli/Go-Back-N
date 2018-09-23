"""

Mininet Topologies with 2 nodes 
Author : Shreshth Tuli

Usage:
    - sudo mn --custom topo.py --topo linear --controller=remote,ip=127.0.0.1

To specify parameters use: --link tc,bw=10,delay=3,loss=2,max_queue_size=3

Example : for ring topology with bandwidth limited to 2:
	- sudo mn --custom topo.py --topo linear --controller=remote,ip=127.0.0.1 --link tc,bw=10

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class LinearTopo( Topo ):
    "Linear Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        hosts = []
        switches = []

        for x in range(0, 2):

            # Add hosts and switches
            hosts.append(self.addHost( 'h%s' % (x+1) ))
            switches.append(self.addSwitch( 's%s' % (x+1) ))

            # Add links in linear topology

            # Connecting hosts to switches
            self.addLink(hosts[x], switches[x])
            # Connecting switches in linear order
            if(x > 0):
                self.addLink(switches[x-1], switches[x]) 

topos = { 
 'linear': ( lambda: LinearTopo() ),
 'ring': ( lambda: RingTopo() ) ,
 'mesh': ( lambda: MeshTopo() ) ,
 'star': ( lambda: StarTopo()) 
  }