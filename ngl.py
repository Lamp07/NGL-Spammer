import requests

acc = input("Username: ")
text = input("Message: ")
cnt = int(input("Count: "))

headers = {
	"Host": "ngl.link",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/x-www-form-urlencoded",
	"Content-Length": "61",
	"Origin": "https://ngl.link",
	"Connection": "keep-alive",
	"Referer": f"https://ngl.link/{acc}",
	"Cookie": "_ga_5DV1ZR5ZHG=GS1.1.1668874226.1.1.1668874250.0.0.0; _ga=GA1.1.848991674.1668874227; __gads=ID=608441b2a9a1cb27-223ad61974d80078:T=1668874229:RT=1668874229:S=ALNI_MYkiqiUkzXQ8_A5BjMee-7brTst_A; __gpi=UID=00000b7f1d19d4d9:T=1668874229:RT=1668874229:S=ALNI_Mb7ZijbgqFGyGJ77GdLYHDyHYebUQ",
	"Upgrade-Insecure-Requests": "1",
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-User": "?1",
	"TE": "trailers"
}

for _ in range(cnt):
  requests.post(f"https://ngl.link/{acc}", headers=headers, data=f"question={text}&deviceId=8f43878a-d38c-4513-a584-9f700b4a5456")
