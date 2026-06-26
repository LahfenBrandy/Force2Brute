import urllib.request
import argparse
import os

def httpFlags():
    parser = argparse.ArgumentParser(description="HTTP brute")
    parser.add_argument('-u', '--url', help="Get url")
    parser.add_argument('-U', '--urls', help="URL file")
    
    parser.add_argument('-t', '--tag', help="Tags")
    parser.add_argument('-T', '--tags', help="Tags file")
    
    args =parser.parse_args()
    
    # URL flag
    urls =[]
    if args.url:
       urls.append(args.url)
    elif args.urls:
        if os.path.exist(args.urls):
            with open(args.urls, 'r', encoding='utf-8', errors='ignore')as f:
                urls = {line.strip for line in f if line.strip()}
        else:
            print(f'[-] File {args.urls} not found')
            return
    
    #Tags flag
    tags = []
    if args.tag:	
        tags.append(args.tag)
    elif args.tags:
        if os.path.exist(args.tags):
            with open(args.tags, 'r', encoding='utf-8', errors='ignore') as f:
                tags = {line.strip for line in f if line.strip()}
        else:
            print(f'[-] File {args.tags} not found')
            return
    
    if not urls or tags:
      print('[!] Missing either urls or tags')
    for URL in urls:
        for TAG in tags:
           Request = urllib.request(URL, TAG)

if __name__ == "__main__":
    httpFlags()
