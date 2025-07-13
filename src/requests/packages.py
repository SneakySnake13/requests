import requests

url = "https://web.archive.org/web/20250712195426js_/https://static.cdninstagram.com/rsrc.php/v4iZv44/yd/l/en_US/TRDXuNMgym8.js"
response = requests.get(url)
response.raise_for_status()  # Stops if download fails
js_code = response.text      # The JS code as a string
