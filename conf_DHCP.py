#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

def install_Xinit():
	os.system("sudo apt-get install xinit flwm");
	os.system(startx);


def install_DHCP():
	os.system("sudo apt-get install isc-dhcp-server");


def conf_DHCP():
	ipServer = raw_input('Insira o IP do servidor Principal:')
	mask = raw_input('Insira a Mascara de Rede:')
	range1 = raw_input('Insira o range(1) de IPs da Rede:')
	range2 = raw_input('Insira o range(2) de IPs da Rede:')
	broadcast = raw_input('Insira o endereço de broadcast:')
	with open('/etc/dhcp/dhcpd.conf','a') as arq:
		arq.write("subnet " + ipServer +" netmask " + mask + " {" + "\n"
				+ "range " + range1 + " " + range2 + ";\n" +
				"option broadcast-address " + broadcast + ";\n}")
	arq.close()


if __name__ == '__main__':
	i = raw_input('Deseja instalar o Xinit: (y/n)')
	if (i == "y"):
		install_DHCP()

	v0 = raw_input('Deseja instalar o DHCP Server: (y/n)')
	if (v0 == "y"):
		install_DHCP()

	v1 = raw_input('Deseja configurar o DHCP: (y/n)')
	if (v1 == "y"):
		conf_DHCP()