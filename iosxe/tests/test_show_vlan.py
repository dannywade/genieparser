import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError

from parser.iosxe.show_vlan import ShowVlan,\
                                              ShowVlanMtu, \
                                              ShowVlanAccessMap, \
                                              ShowVlanRemoteSpan, \
                                              ShowVlanFilter


class test_show_vlan(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'1003': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'token-ring-default', 'stp': '-', 'type': 'tr', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101003', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '500': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0500', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100500', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1005': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'trnet-default', 'stp': 'ibm', 'type': 'trnet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101005', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1004': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'fddinet-default', 'stp': 'ieee', 'type': 'fdnet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101004', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '100': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0100', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100100', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'mtu': '1500', 'BridgeNo': '-'}, 
                             '200': 
                              {'private_secondary_vlan': 'none', 'status': 'active', 'ports': None, 'name': 'VLAN0200', 'private_vlan_type': 'primary', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100200', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '400': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0400', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100400', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'mtu': '1500', 'BridgeNo': '-'}, 
                             '300': 
                              {'private_secondary_vlan': 'none', 'status': 'act/unsup', 'ports': None, 'name': 'VLAN0300', 'private_vlan_type': 'primary', 'stp': '-', 'type': 'fddi', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100300', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '270': 
                              {'private_secondary_vlan': '500', 'status': 'active', 'ports': None, 'name': 'VLAN0270', 'private_vlan_type': 'non-operational', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100270', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1': 
                              {'status': 'active', 'ports': 'Gi1/0/5, Gi1/0/6, Gi1/0/10, Gi1/0/11, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/17, Gi1/0/18, Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22, Gi1/0/23, Gi1/0/24, Gi2/0/1, Gi2/0/2, Gi2/0/3, Gi2/0/4, Gi2/0/5, Gi2/0/6, Gi2/0/7, Gi2/0/8, Gi2/0/9, Gi2/0/10, Gi2/0/11, Gi2/0/12, Gi2/0/13, Gi2/0/14, Gi2/0/15, Gi2/0/16, Gi2/0/17, Gi2/0/18, Gi2/0/19, Gi2/0/20, Gi2/0/21, Gi2/0/22, Gi2/0/23, Gi2/0/24, Gi3/0/1, Gi3/0/2, Gi3/0/3, Gi3/0/4, Gi3/0/5, Gi3/0/6, Gi3/0/7, Gi3/0/8, Gi3/0/9, Gi3/0/10, Gi3/0/11, Gi3/0/12, Gi3/0/13, Gi3/0/14, Gi3/0/15, Gi3/0/16, Gi3/0/17, Gi3/0/18, Gi3/0/19, Gi3/0/20, Gi3/0/21, Gi3/0/22, Gi3/0/23, Gi3/0/24, Gi4/0/1, Gi4/0/2, Gi4/0/3, Gi4/0/4, Gi4/0/5, Gi4/0/6, Gi4/0/7, Gi4/0/8, Gi4/0/9, Gi4/0/10, Gi4/0/11, Gi4/0/12, Gi4/0/13, Gi4/0/14, Gi4/0/15, Gi4/0/16, Gi4/0/17, Gi4/0/18, Gi4/0/19, Gi4/0/20, Gi4/0/21, Gi4/0/22, Gi4/0/23, Gi4/0/24, Gi5/0/1, Gi5/0/2, Gi5/0/3, Gi5/0/4, Gi5/0/5, Gi5/0/6, Gi5/0/7, Gi5/0/8, Gi5/0/9, Gi5/0/10, Gi5/0/11, Gi5/0/12, Gi5/0/13, Gi5/0/14, Gi5/0/15, Gi5/0/16, Gi5/0/17, Gi5/0/18, Gi5/0/19, Gi5/0/20, Gi5/0/21, Gi5/0/22, Gi5/0/23, Gi5/0/24', 'name': 'default', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100001', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '280': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0280', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100280', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1002': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'fddi-default', 'stp': '-', 'type': 'fddi', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101002', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}}}

    missing_mtu_in_parsed_output = {'vlan_id': 
                            {'1003': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'token-ring-default', 'stp': '-', 'type': 'tr', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101003', 'RingNo': '-', 'Trans2': '0', 'BridgeNo': '-'}, 
                             '500': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0500', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100500', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'BridgeNo': '-'}, 
                             '1005': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'trnet-default', 'stp': 'ibm', 'type': 'trnet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101005', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1004': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'fddinet-default', 'stp': 'ieee', 'type': 'fdnet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101004', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '100': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0100', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100100', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'mtu': '1500', 'BridgeNo': '-'}, 
                             '200': 
                              {'private_secondary_vlan': 'none', 'status': 'active', 'ports': None, 'name': 'VLAN0200', 'private_vlan_type': 'primary', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100200', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '400': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0400', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100400', 'RingNo': '-', 'Trans2': '0', 'remote_span_vlan': True, 'mtu': '1500', 'BridgeNo': '-'}, 
                             '300': 
                              {'private_secondary_vlan': 'none', 'status': 'act/unsup', 'ports': None, 'name': 'VLAN0300', 'private_vlan_type': 'primary', 'stp': '-', 'type': 'fddi', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100300', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '270': 
                              {'private_secondary_vlan': '500', 'status': 'active', 'ports': None, 'name': 'VLAN0270', 'private_vlan_type': 'non-operational', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100270', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1': 
                              {'status': 'active', 'ports': 'Gi1/0/5, Gi1/0/6, Gi1/0/10, Gi1/0/11, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/17, Gi1/0/18, Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22, Gi1/0/23, Gi1/0/24, Gi2/0/1, Gi2/0/2, Gi2/0/3, Gi2/0/4, Gi2/0/5, Gi2/0/6, Gi2/0/7, Gi2/0/8, Gi2/0/9, Gi2/0/10, Gi2/0/11, Gi2/0/12, Gi2/0/13, Gi2/0/14, Gi2/0/15, Gi2/0/16, Gi2/0/17, Gi2/0/18, Gi2/0/19, Gi2/0/20, Gi2/0/21, Gi2/0/22, Gi2/0/23, Gi2/0/24, Gi3/0/1, Gi3/0/2, Gi3/0/3, Gi3/0/4, Gi3/0/5, Gi3/0/6, Gi3/0/7, Gi3/0/8, Gi3/0/9, Gi3/0/10, Gi3/0/11, Gi3/0/12, Gi3/0/13, Gi3/0/14, Gi3/0/15, Gi3/0/16, Gi3/0/17, Gi3/0/18, Gi3/0/19, Gi3/0/20, Gi3/0/21, Gi3/0/22, Gi3/0/23, Gi3/0/24, Gi4/0/1, Gi4/0/2, Gi4/0/3, Gi4/0/4, Gi4/0/5, Gi4/0/6, Gi4/0/7, Gi4/0/8, Gi4/0/9, Gi4/0/10, Gi4/0/11, Gi4/0/12, Gi4/0/13, Gi4/0/14, Gi4/0/15, Gi4/0/16, Gi4/0/17, Gi4/0/18, Gi4/0/19, Gi4/0/20, Gi4/0/21, Gi4/0/22, Gi4/0/23, Gi4/0/24, Gi5/0/1, Gi5/0/2, Gi5/0/3, Gi5/0/4, Gi5/0/5, Gi5/0/6, Gi5/0/7, Gi5/0/8, Gi5/0/9, Gi5/0/10, Gi5/0/11, Gi5/0/12, Gi5/0/13, Gi5/0/14, Gi5/0/15, Gi5/0/16, Gi5/0/17, Gi5/0/18, Gi5/0/19, Gi5/0/20, Gi5/0/21, Gi5/0/22, Gi5/0/23, Gi5/0/24', 'name': 'default', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100001', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '280': 
                              {'status': 'active', 'ports': None, 'name': 'VLAN0280', 'stp': '-', 'type': 'enet', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '100280', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}, 
                             '1002': 
                              {'status': 'act/unsup', 'ports': None, 'name': 'fddi-default', 'stp': '-', 'type': 'fddi', 'parent': '-', 'Trans1': '0', 'BrdgMode': '-', 'said': '101002', 'RingNo': '-', 'Trans2': '0', 'mtu': '1500', 'BridgeNo': '-'}}}


    golden_output = {'execute.return_value': '''
 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
 1    default                          active    Gi1/0/5, Gi1/0/6, Gi1/0/10
                                                 Gi1/0/11, Gi1/0/12, Gi1/0/13
                                                 Gi1/0/14, Gi1/0/15, Gi1/0/16
                                                 Gi1/0/17, Gi1/0/18, Gi1/0/19
                                                 Gi1/0/20, Gi1/0/21, Gi1/0/22
                                                 Gi1/0/23, Gi1/0/24, Gi2/0/1
                                                 Gi2/0/2, Gi2/0/3, Gi2/0/4
                                                 Gi2/0/5, Gi2/0/6, Gi2/0/7
                                                 Gi2/0/8, Gi2/0/9, Gi2/0/10
                                                 Gi2/0/11, Gi2/0/12, Gi2/0/13
                                                 Gi2/0/14, Gi2/0/15, Gi2/0/16
                                                 Gi2/0/17, Gi2/0/18, Gi2/0/19
                                                 Gi2/0/20, Gi2/0/21, Gi2/0/22
                                                 Gi2/0/23, Gi2/0/24, Gi3/0/1
                                                 Gi3/0/2, Gi3/0/3, Gi3/0/4
                                                 Gi3/0/5, Gi3/0/6, Gi3/0/7
                                                 Gi3/0/8, Gi3/0/9, Gi3/0/10
                                                 Gi3/0/11, Gi3/0/12, Gi3/0/13
                                                 Gi3/0/14, Gi3/0/15, Gi3/0/16
                                                 Gi3/0/17, Gi3/0/18, Gi3/0/19
          
 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
                                                 Gi3/0/20, Gi3/0/21, Gi3/0/22
                                                 Gi3/0/23, Gi3/0/24, Gi4/0/1
                                                 Gi4/0/2, Gi4/0/3, Gi4/0/4
                                                 Gi4/0/5, Gi4/0/6, Gi4/0/7
                                                 Gi4/0/8, Gi4/0/9, Gi4/0/10
                                                 Gi4/0/11, Gi4/0/12, Gi4/0/13
                                                 Gi4/0/14, Gi4/0/15, Gi4/0/16
                                                 Gi4/0/17, Gi4/0/18, Gi4/0/19
                                                 Gi4/0/20, Gi4/0/21, Gi4/0/22
                                                 Gi4/0/23, Gi4/0/24, Gi5/0/1
                                                 Gi5/0/2, Gi5/0/3, Gi5/0/4
                                                 Gi5/0/5, Gi5/0/6, Gi5/0/7
                                                 Gi5/0/8, Gi5/0/9, Gi5/0/10
                                                 Gi5/0/11, Gi5/0/12, Gi5/0/13
                                                 Gi5/0/14, Gi5/0/15, Gi5/0/16
                                                 Gi5/0/17, Gi5/0/18, Gi5/0/19
                                                 Gi5/0/20, Gi5/0/21, Gi5/0/22
                                                 Gi5/0/23, Gi5/0/24
 100  VLAN0100                         active
 200  VLAN0200                         active
 270  VLAN0270                         active
 280  VLAN0280                         active
 300  VLAN0300                         act/unsup

 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
 400  VLAN0400                         active
 500  VLAN0500                         active
 1002 fddi-default                     act/unsup
 1003 token-ring-default               act/unsup
 1004 fddinet-default                  act/unsup
 1005 trnet-default                    act/unsup

 VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
 ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
 1    enet  100001     1500  -      -      -        -    -        0      0
 100  enet  100100     1500  -      -      -        -    -        0      0
 200  enet  100200     1500  -      -      -        -    -        0      0
 270  enet  100270     1500  -      -      -        -    -        0      0
 280  enet  100280     1500  -      -      -        -    -        0      0
 300  fddi  100300     1500  -      -      -        -    -        0      0
 400  enet  100400     1500  -      -      -        -    -        0      0
 500  enet  100500     1500  -      -      -        -    -        0      0
 1002 fddi  101002     1500  -      -      -        -    -        0      0
 1003 tr    101003     1500  -      -      -        -    -        0      0
 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

 Remote SPAN VLANs
 ------------------------------------------------------------------------------
 100,400,500

 Primary Secondary Type              Ports
 ------- --------- ----------------- ------------------------------------------
 200     none      primary
 270     500       non-operational
 300     none      primary
'''}

    silver_output = {'execute.return_value': '''
 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
 1    default                          active    Gi1/0/5, Gi1/0/6, Gi1/0/10
                                                 Gi1/0/11, Gi1/0/12, Gi1/0/13
                                                 Gi1/0/14, Gi1/0/15, Gi1/0/16
                                                 Gi1/0/17, Gi1/0/18, Gi1/0/19
                                                 Gi1/0/20, Gi1/0/21, Gi1/0/22
                                                 Gi1/0/23, Gi1/0/24, Gi2/0/1
                                                 Gi2/0/2, Gi2/0/3, Gi2/0/4
                                                 Gi2/0/5, Gi2/0/6, Gi2/0/7
                                                 Gi2/0/8, Gi2/0/9, Gi2/0/10
                                                 Gi2/0/11, Gi2/0/12, Gi2/0/13
                                                 Gi2/0/14, Gi2/0/15, Gi2/0/16
                                                 Gi2/0/17, Gi2/0/18, Gi2/0/19
                                                 Gi2/0/20, Gi2/0/21, Gi2/0/22
                                                 Gi2/0/23, Gi2/0/24, Gi3/0/1
                                                 Gi3/0/2, Gi3/0/3, Gi3/0/4
                                                 Gi3/0/5, Gi3/0/6, Gi3/0/7
                                                 Gi3/0/8, Gi3/0/9, Gi3/0/10
                                                 Gi3/0/11, Gi3/0/12, Gi3/0/13
                                                 Gi3/0/14, Gi3/0/15, Gi3/0/16
                                                 Gi3/0/17, Gi3/0/18, Gi3/0/19
          
 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
                                                 Gi3/0/20, Gi3/0/21, Gi3/0/22
                                                 Gi3/0/23, Gi3/0/24, Gi4/0/1
                                                 Gi4/0/2, Gi4/0/3, Gi4/0/4
                                                 Gi4/0/5, Gi4/0/6, Gi4/0/7
                                                 Gi4/0/8, Gi4/0/9, Gi4/0/10
                                                 Gi4/0/11, Gi4/0/12, Gi4/0/13
                                                 Gi4/0/14, Gi4/0/15, Gi4/0/16
                                                 Gi4/0/17, Gi4/0/18, Gi4/0/19
                                                 Gi4/0/20, Gi4/0/21, Gi4/0/22
                                                 Gi4/0/23, Gi4/0/24, Gi5/0/1
                                                 Gi5/0/2, Gi5/0/3, Gi5/0/4
                                                 Gi5/0/5, Gi5/0/6, Gi5/0/7
                                                 Gi5/0/8, Gi5/0/9, Gi5/0/10
                                                 Gi5/0/11, Gi5/0/12, Gi5/0/13
                                                 Gi5/0/14, Gi5/0/15, Gi5/0/16
                                                 Gi5/0/17, Gi5/0/18, Gi5/0/19
                                                 Gi5/0/20, Gi5/0/21, Gi5/0/22
                                                 Gi5/0/23, Gi5/0/24
 100  VLAN0100                         active
 200  VLAN0200                         active
 270  VLAN0270                         active
 280  VLAN0280                         active
 300  VLAN0300                         act/unsup

 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
 400  VLAN0400                         active
 500  VLAN0500                         active
 1002 fddi-default                     act/unsup
 1003 token-ring-default               act/unsup
 1004 fddinet-default                  act/unsup
 1005 trnet-default                    act/unsup

 VLAN Type  SAID       Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
 ---- ----- ---------- ------ ------ -------- ---- -------- ------ ------
 1    enet  100001     -      -      -        -    -        0      0
 100  enet  100100     -      -      -        -    -        0      0
 200  enet  100200     -      -      -        -    -        0      0
 270  enet  100270     -      -      -        -    -        0      0
 280  enet  100280     -      -      -        -    -        0      0
 300  fddi  100300     -      -      -        -    -        0      0
 400  enet  100400     -      -      -        -    -        0      0
 500  enet  100500     -      -      -        -    -        0      0
 1002 fddi  101002     -      -      -        -    -        0      0
 1003 tr    101003     -      -      -        -    -        0      0
 1004 fdnet 101004     -      -      -        ieee -        0      0
 1005 trnet 101005     -      -      -        ibm  -        0      0

 Remote SPAN VLANs
 ------------------------------------------------------------------------------
 100,400,500

 Primary Secondary Type              Ports
 ------- --------- ----------------- ------------------------------------------
 200     none      primary
 270     500       non-operational
 300     none      primary
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlan(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

    def test_missing_parsed_key(self):
        self.device = Mock(**self.silver_output)
        vlan_obj = ShowVlan(device=self.device)
        with self.assertRaises(Exception):
            parsed_output = vlan_obj.parse()

class test_show_vlan_mtu(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'200': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1005': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1003': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '300': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1002': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1004': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '100': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '1500'}, 
                             '1': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '1500'}
                            }
                        }

    golden_output = {'execute.return_value': '''
 VLAN    SVI_MTU    MinMTU(port)      MaxMTU(port)     MTU_Mismatch
 ---- ------------- ----------------  ---------------  ------------
 1    1500          1500              1500              No
 100  1500          1500              1500              No
 200    -           1500              1500              No
 300    -           1500              1500              No
 1002   -           1500              1500              No
 1003   -           1500              1500              No
 1004   -           1500              1500              No
 1005   -           1500              1500              No
'''}

    silver_output = {'execute.return_value': '''
 VLAN    SVI_MTU    MinMTU(port)      MTU_Mismatch
 ---- ------------- ----------------  ------------
 1    1500          1500              No
 100  1500          1500              No
 200    -           1500              No
 300    -           1500              No
 1002   -           1500              No
 1003   -           1500              No
 1004   -           1500              No
 1005   -           1500              No
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanMtu(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanMtu(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

    def test_missing_parsed_key(self):
        self.device = Mock(**self.silver_output)
        vlan_obj = ShowVlan(device=self.device)
        with self.assertRaises(Exception):
            parsed_output = vlan_obj.parse()

class test_show_vlan_remote_span(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'400': 
                                {'vlan_is_remote_span': True}, 
                             '500': 
                                {'vlan_is_remote_span': True}, 
                             '100': 
                                {'vlan_is_remote_span': True}
                            }
                        }

    golden_output = {'execute.return_value': '''
 Remote SPAN VLANs
 ------------------------------------------------------------------------------
 100,400,500
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_access_map(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'access_map_id': 
    {'vlan': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'fg': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'kari3': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'ed': 
        {'access_map_sequence': 
            {'20': {'access_map_action_value': 'drop'}}}, 
     'takashi': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'drop'}}}, 
     'karim': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'mordred': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}
        }
    }
}

    golden_output = {'execute.return_value': '''
Vlan access-map "ed"  20
  Match clauses:
  Action:
    drop
Vlan access-map "fg"  10
  Match clauses:
  Action:
    forward
Vlan access-map "takashi"  10
  Match clauses:
  Action:
    drop
Vlan access-map "mordred"  10
  Match clauses:
  Action:
    forward
Vlan access-map "karim"  10
  Match clauses:
  Action:
    forward
Vlan access-map "vlan"  10
  Match clauses:
  Action:
    forward
Vlan access-map "kari3"  10
  Match clauses:
  Action:
    forward
'''}

    silver_output = {'execute.return_value': '''
Vlan access-map "ed"  20
  Match clauses:
  Action:
    drop
Vlan access-map "fg"  10
  Match clauses:
  Action:
    forward
Vlan access-map "takashi"  10
  Match clauses:
  Action:
    drop
Vlan access-map "mordred"  10
  Match clauses:
  Action:
    forward
Vlan access-map "karim"  10
  Match clauses:
  Action:
    forward
Vlan access-map "vlan"  10
  Match clauses:
  Action:
    forward
Vlan access-map "kari3"  10
  Match clauses:
  Action:
    forward
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanAccessMap(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanAccessMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_filter(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                                {'100': 
                                    {'access_map_tag': 'karim'}, 
                                 '3': 
                                    {'access_map_tag': 'mordred'}, 
                                 '15': 
                                    {'access_map_tag': 'mordred'}, 
                                 '5': 
                                    {'access_map_tag': 'mordred'}
                                }
                            }

    golden_output = {'execute.return_value': '''
 VLAN Map mordred is filtering VLANs:
   3-5,15
 VLAN Map karim is filtering VLANs:
   100
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanFilter(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanFilter(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

if __name__ == '__main__':
    unittest.main()