from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from topo import net

h1 = net.get('h1')
# h2 = net.get('h2')

results=h1.cmd('ifconfig')
print results

def perfTest():
    # "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=2 )
    net = Mininet( topo=topo,
               host=CPULimitedHost, link=TCLink )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h2 = net.get( 'h1', 'h2' )
    # net.iperf( (h1, h2) )
    h1.cmd('python3 host.py 0 README.md a.txt')
    h2.cmd('python3 host.py 1 README.md a.txt')
    
    net.stop()

if _name_ == '_main_':
    setLogLevel( 'info' )
    perfTest()



    