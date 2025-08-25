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
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info


class SdnNetworkTopo(Topo):
    """
    Custom topology with two switches and four hosts.
    """

    def build(self):
        """
        Create the topology.
        """
        info('*** Adding switches\n')
        # Add two OpenFlow switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        info('*** Adding hosts\n')
        # Add four hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        info('*** Creating links\n')
        # Add the links between hosts and switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        # Add the link between the two switches
        self.addLink(s1, s2)


# This dictionary is required by Mininet to load the custom topology from a file.
topos = {'sdnnetwork': (lambda: SdnNetworkTopo())}


def run_network():
    """
    Initializes and runs the network with the custom topology.
    """
    # Set the logging level to 'info' for useful output
    setLogLevel('info')

    # Create a Mininet object with the custom topology
    net = Mininet(
        topo=SdnNetworkTopo(),
        controller=None,
        switch=OVSSwitch
    )


if __name__ == '__main__':
    # Call the main function to run the network
    run_network()
