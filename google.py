from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords": "소녀시대 윤아", "limit":50, "print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the functionp
print(paths)   #printing absolute paths of the downloaded images