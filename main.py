import cv2
import numpy as np
import urllib.request
import time

start_time = time.time()
# creating a loop to get 809 pokemon image
for i in range(1, 41):
    try:
        url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+ '{:03d}' .format(i) +'.png'
        # print(url)
        # send https request and returns data
        request = urllib.request.Request(url)
        # open the request get response as a binary string
        response = urllib.request.urlopen(request)
        # convertion of binary string using opencv
        binary_str = response.read()
        # convert binary to byte arra
        byte_array = bytearray(binary_str)
        # convert as numpy array
        numpy_array = np.asarray(byte_array, dtype="uint8")
        # convert as opencv image
        image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("image/" + '{:04d}' .format(i) +'.png',image )
        print("saved" + '{:04d}' .format(i) +'.png')
    except Exception as e:
        print(str(e))
end_time = time.time()
print("Demo")
print("Time taken : "+ str(end_time - start_time) + "sec")