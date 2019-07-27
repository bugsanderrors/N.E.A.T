import sys
import requests
url = "http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat"


#r = requests.get(url, stream = True)

with open("imagenet-vgg-verydeep-19.mat", 'wb') as f:
	print("Downloading {0}".format("imagenet-vgg-verydeep-19.mat"))
	response = requests.get(url, stream = True)
	total_length = response.headers.get('content-length')

	if total_length is None:
		f.write(response.content)
	else:
		dl = 0
		total_length = int(total_length)
		for data in response.iter_content(chunk_size = 4096):
			dl+=len(data)
			f.write(data)
			done = int(50* dl / total_length)
			sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
			sys.stdout.flush()
