import urllib.request

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

try:
    # Open the URL and read its contents
    with urllib.request.urlopen(url) as response:
        # Read the content of the response
        data = response.read().decode('utf-8')
        
        # Display the body of the response
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        
except urllib.error.URLError as e:
    # Handle URL errors
    print("Error:", e)
