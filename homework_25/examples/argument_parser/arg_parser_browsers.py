from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--browser", help="browser name", default="chrome")

browser = parser.parse_args()

if browser == "chrome":
    print("Chrome")
elif browser == "firefox":
    print("Firefox")
else:
    print("No such browser")
