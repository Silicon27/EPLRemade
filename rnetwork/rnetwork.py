"""
Networking module for the RPi

This module is a collection of functions that are used in the field of networking.
"""


def ping(host: str, count: int = 4) -> str:
    """
    Pings a host and returns the result.

    :arg host: str - The host to ping.
    :arg count: int - The number of packets to send. Default is 4.
    """
    import os

    return os.popen(f"ping -c {count} {host}").read()
