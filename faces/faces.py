def convert(str):
    text = str.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    ask = input()
    txt = convert(ask)
    print(txt)




main()



