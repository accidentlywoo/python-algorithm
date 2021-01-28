import json
import csv


# json = json.loads(array)
data = []

# f = open('health_14_35_days.csv', 'r', encoding='utf-8')
with open('health_14_35_days.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data.append(row)

def amen_making_json(data):
    array = '{}'
    for row in data:
        for item in row:
            print()

    print()


def lambda_handler(event, context):
    i = 0
    for list in context:
        print(list)
        print(list[0])
        # if(list[4] == 1):
        #     print(list.index())

        for item in list:
            # print(item)
            print()

lambda_handler({
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "ap-northeast-2",
            "eventTime": "2021-01-22T09:01:58.474Z",
            "eventName": "ObjectCreated:CompleteMultipartUpload",
            "userIdentity": {
                "principalId": "AWS:AIDAY5YVQCRY23UTDBPCO"
            },
            "requestParameters": {
                "sourceIPAddress": "54.243.203.218"
            },
            "responseElements": {
                "x-amz-request-id": "669DD1B09BF2CF81",
                "x-amz-id-2": "oXVRajzMH4gfksfNomCAVxtSiH/miIBt0gZ4KkdYioAyKzkHow7ZryD+JwUENfpqdvmHqhpN+1zgJdU9WEaAAZBAXKTorj1EJAyudCDZwEA="
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "health_infant_14_35_trigger",
                "bucket": {
                    "name": "stg-recv3-public",
                    "ownerIdentity": {
                        "principalId": "A3SKQPC5ZYRLDC"
                    },
                    "arn": "arn:aws:s3:::stg-recv3-public"
                },
                "object": {
                    "key": "infant/health_14_35_days.csv",
                    "size": 24466,
                    "eTag": "37097e3dd4b7353d3a5d63dbc6d3a8a3-1",
                    "sequencer": "00600A9486F6F4FC13"
                }
            }
        }
    ]
}, data)
