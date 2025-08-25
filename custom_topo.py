#!/usr/bin/python

"""
This script defines a simple SDN network topology as a reusable class.

The topology consists of:
- A central SDN controller.
- Two OpenFlow switches (s1 and s2).
- Four hosts (h1, h2, h3, h4).

The connections are:
- h1 and h2 are connected to s1.
- h3 and h4 are connected to s2.
- The two switches, s1 and s2, are also connected to each other.
"""

# Import necessary Mininet classes for topology definition and network creation
from mininet.topo import Topo


class SdnNetworkTopo(Topo):
    """
    Custom topology with two switches and four hosts.
    """

    def build(self):
        """
        Create the topology.
        """

        # Add two OpenFlow switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')


        # Add four hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add the links between hosts and switches
        self.addLink(s1, h1,bw =100, delay='2ms')
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)

        # Add the link between the two switches
        self.addLink(s1, s2)


# This dictionary is required by Mininet to load the custom topology from a file.
topos = {'sdnnetwork': (lambda: SdnNetworkTopo())}


