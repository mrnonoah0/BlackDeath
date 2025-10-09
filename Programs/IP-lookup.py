try:
    import requests
    import os
except Exception as e:
    input(e)

try:
    ip = input("Enter the IP address to lookup: ")
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()

    status = "Valid" if data.get('status') == "success" else "Invalid"
    country = data.get('country', 'N/A')
    region = data.get('region', 'N/A')
    city = data.get('city', 'N/A')
    org = data.get('org', 'N/A')
    loc = data.get('loc', 'N/A')
    postal = data.get('postal', 'N/A')
    timezone = data.get('timezone', 'N/A')
    hostname = data.get('hostname', 'N/A')
    isp = data.get('isp', 'N/A')
    as_host = data.get('as', 'N/A')
    latitude = data.get('latitude', 'N/A')
    longitude = data.get('longitude', 'N/A')
    country_code = data.get('country_code', 'N/A')
    asn = data.get('asn', 'N/A')

    Info = f"""
    Status: {status}
    Country: {country}
    Region: {region}
    City: {city}
    Organization: {org}
    Location: {loc}
    Postal: {postal}
    Timezone: {timezone}
    Hostname: {hostname}
    AS Host: {as_host}
    Latitude: {latitude}
    Longitude: {longitude}
    Country Code: {country_code}
    ASN: {asn}
    ISP: {isp}
    """

    print(Info)
    os.system("python Main.py")

except Exception as e:
    input(e)