import sys
import ast
import ipaddress

def get_network(interface):
    return ipaddress.ip_interface(interface).network
    
def build_network(d):
    networks = {}
    for host in d:
        for interface in d[host]:
            network = get_network(interface)
            if network in networks:
                networks.append(host)
            else:
                networks = [host]


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    net_dict = ast.literal_eval(test_cases.readline())
    network = build_network(net_dict)
    for test in test_cases.readlines():
        route(test.split(' '))
    test_cases.close()
