import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if 'src' in s and'<iframe' in s:
        youtub_url = re.findall(r'src="(\S+)"', s)[0]
        if re.search(r'https?://(www\.)?youtube\.com/embed/', youtub_url):
            youtub_id = re.findall(r'embed/(\S+)', youtub_url)[0]
            return f'https://youtu.be/{youtub_id}'
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()
