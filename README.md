# SNMPQuery
SNMPQuery is a Python class that provides a simple interface for querying SNMP-enabled devices and retrieving information about their vendor.

## Requirements
The following packages are required to use SNMPQuery:

- pysnmp

## Usage
```sh
Create an instance of SNMPQuery with SNMPv2
snmp_v2 = SNMPQuery(ip='192.168.178.1', community='mycommunity')
vendor_v2 = snmp_v2.get_vendor()
print(vendor_v2) # Cisco

Create an instance of SNMPQuery with SNMPv3
snmp_v3 = SNMPQuery(ip='10.62.19.132', user='SNMP_V3USER', auth_key='234asda@^%ads', priv_key='234sdf$#re')
vendor_v3 = snmp_v3.get_vendor()
print(vendor_v3) # Cisco
```

## Constructor
The constructor takes the following parameters:

- ip: The IP address of the device to query.
- community: The SNMP community string to use for SNMPv2 queries. If this parameter is omitted, SNMPv3 will be used.
- user: The SNMPv3 username to use.
- auth_key: The SNMPv3 authentication key to use.
- priv_key: The SNMPv3 privacy key to use.
