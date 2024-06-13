import requests
import json

def get_ip_report(ip):
    url = f'https://ci-www.threatcrowd.org/searchApi/v2/ip/report/?ip={ip}'
    response = requests.get(url, verify=False)
    return response.json()

def get_file_report(file_hash):
    url = f'https://ci-www.threatcrowd.org/searchApi/v2/file/report/?resource={file_hash}'
    response = requests.get(url, verify=False)
    return response.json()

def get_email_report(email):
    url = f'https://ci-www.threatcrowd.org/searchApi/v2/email/report/?email={email}'
    response = requests.get(url, verify=False)
    return response.json()

def get_domain_report(domain):
    url = f'https://ci-www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}'
    response = requests.get(url, verify=False)
    return response.json()

ip_report = get_ip_report('216.58.208.46')
file_report = get_file_report('44d88612fea8a8f36de82e1278abb02f')
email_report = get_email_report('william19770319@yahoo.com')
domain_report = get_domain_report('google.com')

print("IP Report:")
print(json.dumps(ip_report, indent=4))

print("\nFile Report:")
print(json.dumps(file_report, indent=4))

print("\nEmail Report:")
print(json.dumps(email_report, indent=4))

print("\nDomain Report:")
print(json.dumps(domain_report, indent=4))
