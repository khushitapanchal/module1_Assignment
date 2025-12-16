import urllib.request

URL = "http://localhost:8000/"

try:
    # Send a GET request to the server
    response = urllib.request.urlopen(URL)

    # Read the response data
    html_content = response.read().decode('utf-8')

    # Print the response
    print("--- Server Response Status ---")
    print(response.status, response.reason)
    print("\n--- Server Response Content ---")
    print(html_content)

except Exception as e:
    print(f"An error occurred: {e}")

