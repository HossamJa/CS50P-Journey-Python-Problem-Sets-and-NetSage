import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_parts = ip.split('.')
    valid_ip = r'^([0-9][0-9]?[0-9]?\.)([0-9][0-9]?[0-9]?\.)([0-9][0-9]?[0-9]?\.)([0-9][0-9]?[0-9]?)$'
    valid = re.search(valid_ip, ip)

    if valid:
        for part in ip_parts:
            if int(part)<0 or int(part)>255:
                return False

        return True
    
    else:
        return False


if __name__ == "__main__":
    main()
