#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

net = Mininet()                                                                                                       
          
# Adiciona os hosts
servidor = net.addHost( 'servidor' )                                                                              
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
h3 = net.addHost( 'h3' )
h4 = net.addHost( 'h4' )                                                                                               
s1 = net.addSwitch( 's1' )
c0 = net.addController( 'c0' )  
                                                                                    
# Adiciona os links
net.addLink( servidor, s1 )                                                                                        
net.addLink( h1, s1 )      
net.addLink( h2, s1 )     
net.addLink( h3, s1 ) 
net.addLink( h4, s1 )                                                                                      
net.start()


servidor.cmd( 'ifconfig servidor-eth0 192.168.100.1/24')
servidor.cmd( 'dhcpd -cf /etc/dhcp/dhcpd.conf') 

h3.cmd( 'ifconfig h3-eth0 192.168.100.16' )						#IP FIXO
h3.cmd( 'route add default gw 192.168.100.1')					#ROTA
h3.cmd( 'echo “nameserver 8.8.8.8” >> /etc/resolv.conf' )		#DNS

h4.cmd( 'ifconfig h4-eth0 192.168.100.17' )						#IP FIXO        
h4.cmd( 'route add default gw 192.168.100.1')					#rota
h3.cmd( 'echo “nameserver 189.38.95.95” >> /etc/resolv.conf' )	#DNS

h1.cmd( 'dhclient')												#IP dado pelo DHCP  
h2.cmd( 'dhclient')  											#IP dado pelo DHCP
                                                                       
CLI( net )                                                      #Start CLI                                                      
net.stop()  															