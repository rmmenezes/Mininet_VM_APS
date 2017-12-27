#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

net = Mininet()                                                                                                       
h1 = net.addHost( 'h1' )                                                                                              
h2 = net.addHost( 'h2' )
h3 = net.addHost( 'h3' )
h4 = net.addHost( 'h4' )                                                                                               

s1 = net.addSwitch( 's1' )

router= net.addHost( 'router')

s2 = net.addSwitch( 's2' )

c0 = net.addController( 'c0' ) 
                                                                                         
net.addLink( h1, s1 )                                                                                                 
net.addLink( h2, s1 )      
net.addLink( h3, s2 )     
net.addLink( h4, s2 )

net.addLink( s1, router)
net.addLink( s2, router)
                                                                                       
net.start()

router.cmd( 'ifconfig router-eth0 192.168.100.1/24')
router.cmd( 'ifconfig router-eth1 192.168.200.1/24')
router.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

h1.cmd( 'ifconfig h1-eth0 192.168.100.2')#ip locais
h1.cmd( 'route add default gw 192.168.100.1')
h2.cmd( 'ifconfig h2-eth0 192.168.100.3') 
h2.cmd( 'route add default gw 192.168.100.1')
h3.cmd( 'ifconfig h3-eth0 192.168.200.2')
h3.cmd( 'route add default gw 192.168.200.1')
h4.cmd( 'ifconfig h4-eth0 192.168.200.3')                                                                               
h4.cmd( 'route add default gw 192.168.200.1')
CLI( net )                                                                                                            
net.stop()  