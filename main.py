import re
import requests

r = requests.get("https://docs.python.org/3/library/index.html").content
r = r.decode("utf-8")

term = input("Package: ")
search_pat = re.compile(re.escape(term), re.IGNORECASE)

if search_pat.search(r):
	print("Package mentioned:", search_pat.search(r).group())
else:
	print("Package not mentioned")
