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

# class LinearTopo( Topo ):
#     "Linear Topology Mininet"

#     def __init__( self ):

#         # Initialize topology
#         Topo.__init__( self )

#         hosts = []
#         switches = []

#         for x in range(0, 2):

#             # Add hosts and switches
#             hosts.append(self.addHost( 'h%s' % (x+1) ))
#             switches.append(self.addSwitch( 's%s' % (x+1) ))

#             # Add links in linear topology

#             # Connecting hosts to switches
#             self.addLink(hosts[x], switches[x])
#             # Connecting switches in linear order
#             if(x > 0):
#                 self.addLink(switches[x-1], switches[x]) 

# topos = { 
#  'linear': ( lambda: LinearTopo() ),
#  'ring': ( lambda: RingTopo() ) ,
#  'mesh': ( lambda: MeshTopo() ) ,
#  'star': ( lambda: StarTopo()) 
#   }


#!/usr/bin/python

class SingleSwitchTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self, n=2 ):
    switch = self.addSwitch( 's1' )
    for h in range(n):
        # Each host gets 50%/n of system CPU
        host = self.addHost( 'h%s' % (h + 1),
                         cpu=.5/n )
        # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
        self.addLink( host, switch, bw=10, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True )

def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=4 )
    net = Mininet( topo=topo,
               host=CPULimitedHost, link=TCLink )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get( 'h1', 'h4' )
    net.iperf( (h1, h4) )
    net.stop()

if _name_ == '_main_':
    setLogLevel( 'info' )
    perfTest()



    