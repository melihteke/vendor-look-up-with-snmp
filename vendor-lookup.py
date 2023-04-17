
from pysnmp.hlapi import *
import re



class SNMPQuery:
    
    '''
    SNMPv2
    snmp = SNMPQuery(ip='192.168.178.1', community='MyCommunity')
    snmp.get_vendor()
    'Cisco'
    >>> 
    
    SNMPv3
    snmp = SNMPQuery(ip='NEXCOURX39', user='V3User',  auth_key='XXXXXXX', priv_key='XXXXXXX')
    snmp.get_vendor()
    'Cisco'
    
    '''
    
    def __init__(self, ip, community=None, user=None, auth_key=None, priv_key=None):
        self.ip = ip
        self.community = community
        self.user = user
        self.auth_key = auth_key
        self.priv_key = priv_key

    def get_vendor(self):
        if self.community:
            snmp_query = getCmd(
                SnmpEngine(),
                CommunityData(self.community),
                UdpTransportTarget((self.ip, 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
            )
        else:
            snmp_query = getCmd(
                SnmpEngine(),
                UsmUserData(self.user, self.auth_key, self.priv_key, authProtocol=usmHMACSHAAuthProtocol, privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((self.ip, 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
            )

        errorIndication, errorStatus, errorIndex, varBinds = next(snmp_query)

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print(f"Error: {errorStatus}")
        else:
            response = str(varBinds[0])
            vendor = re.search(r'Cisco|Juniper', response, re.IGNORECASE)

            if vendor:
                return vendor.group()
            else:
                return "unknown"
