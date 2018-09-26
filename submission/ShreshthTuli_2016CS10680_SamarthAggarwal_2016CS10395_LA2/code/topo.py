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

class LinearTopo( Topo ):
    "Linear Topology Mininet"

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

topos = { 
 'linear': ( lambda: LinearTopo() ),
 'ring': ( lambda: RingTopo() ) ,
 'mesh': ( lambda: MeshTopo() ) ,
 'star': ( lambda: StarTopo()) 
  }