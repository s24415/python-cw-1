import webbrowser
import requests


def is_time_stamp(data):
    data = str(data)
    return len(data) == 14 and data.isnumeric()


websiteUrl = input("Insert website URL: ")

exists = len(requests.get(f"https://archive.org/wayback/available?url={websiteUrl}").json()["archived_snapshots"]) > 0
if not exists:
    print("Website don't exist in archive")
else:
    test = "http://web.archive.org/cdx/search/cdx?url=https://pl.wikipedia.org/wiki/Wikipedia"
    split_snapshots_data = requests.get(test).text.split(" ")
    snapshots_timestamps = filter(is_time_stamp, split_snapshots_data)

    print("Available timestamps:")
    for timestamp in snapshots_timestamps:
        print(timestamp)

    for i in range(3):
        user_timestamp = input("Insert timestamp (YYYYMMDDhhmmss):")
        url = f"http://archive.org/wayback/available?url={str(websiteUrl)}&timestamp={str(user_timestamp)}"
        page = requests.get(url).json()["archived_snapshots"]["closest"]["url"]
        webbrowser.open(page)
        print()