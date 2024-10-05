import requests
import json

def WhoisIp(ip):
    try:
        url = f"http://ipwho.is/{ip}"
        
        aji = requests.get(url)
        
        if aji.status_code == 200:
            data = aji.json()
            
            if data.get("success"):
                return json.dumps(data, indent=4)  
            else:
                return json.dumps({"error": "Invalid IP address"}, indent=4)
        else:
            return json.dumps({"error": f"HTTP Error: {aji.status_code}"}, indent=4)
    
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)