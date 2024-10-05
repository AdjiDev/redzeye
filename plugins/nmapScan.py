import nmap
import json

def NmapScan(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(target)
        json_result = NmapResult(nm)
        return json_result
    except Exception as e:
        return json.dumps({"error": f"Failed to run Nmap: {str(e)}"})

def NmapResult(nm):
    scan_data = {}
    for host in nm.all_hosts():
        scan_data['host'] = host
        scan_data['state'] = nm[host].state()
        ports = []
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                port_info = {
                    'port': port,
                    'state': nm[host][proto][port]['state'],
                    'name': nm[host][proto][port]['name']
                }
                ports.append(port_info)
        scan_data['ports'] = ports
    return json.dumps(scan_data, indent=4)
