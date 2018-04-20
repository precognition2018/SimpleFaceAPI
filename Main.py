########### Python 3.2 #############
import http.client, urllib.error

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '995e68e5c0fb48b0a3b8fc0c0ee10bf6'
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,emotion',
})

try:
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, '{"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Moon_Jae-in_%282017-10-01%29_cropped.jpg/250px-Moon_Jae-in_%282017-10-01%29_cropped.jpg"}', headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################