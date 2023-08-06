from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import requests

import pandas as pd


def indexURL(urls):
    # print(type(url)); print("URL: {}".format(url));return;

    for u in urls:
        # print("U: {} type: {}".format(u, type(u)))
        ENDPOINT = (
            "https://www.bing.com/indexnow?url="
            + u
            + "&key=a44383dd9b424b37afdf935ede1e3d3b"
        )
        content = {}
        content["url"] = u.strip()
        content["type"] = "URL_UPDATED"
        json_ctn = json.dumps(content)
        # print(json_ctn);return
        response = requests.post(ENDPOINT)
        print(response)
        # response, content = http.request(ENDPOINT, method="POST", body=json_ctn)

        result = json.loads(content.decode())

        # For debug purpose only
        if "error" in result:
            print(
                "Error({} - {}): {}".format(
                    result["error"]["code"],
                    result["error"]["status"],
                    result["error"]["message"],
                )
            )
            break
        else:
            print(
                "urlNotificationMetadata.url: {}".format(
                    result["urlNotificationMetadata"]["url"]
                )
            )
            print(
                "urlNotificationMetadata.latestUpdate.url: {}".format(
                    result["urlNotificationMetadata"]["latestUpdate"]["url"]
                )
            )
            print(
                "urlNotificationMetadata.latestUpdate.type: {}".format(
                    result["urlNotificationMetadata"]["latestUpdate"]["type"]
                )
            )
            print(
                "urlNotificationMetadata.latestUpdate.notifyTime: {}".format(
                    result["urlNotificationMetadata"]["latestUpdate"]["notifyTime"]
                )
            )


"""
data.csv has 2 columns: URL and date.
I just need the URL column.
"""
csv = pd.read_csv("my_data.csv")
csv[["URL"]].apply(lambda x: indexURL(x))
