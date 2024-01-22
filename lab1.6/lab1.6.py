import ipaddress
import re
def main(f1 = open("10.31.71.65_AR-1.log" ,"r"),
         f2 = open("10.31.172.7_DEMO_SW_4.log","r"), f3 = open("10.31.70.209_csr-api.log", "r"),
         f4 = open("10.31.69.201_demo01-615a.csr.jet.msk.su.log", "r"), f5 = open("10.31.69.202_demo02-615a.csr.jet.msk.su.log", "r"),
         f6 = open("10.31.69.203_demo03-615a.csr.jet.msk.su.log", "r")):
    for line in f1.readlines():
       pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'  ### Ищет IP адреса в строке с маской
       searcher = re.search(pattern, line)
       if searcher:
           matcher = searcher.group(0)
           if ipaddress.IPv4Interface(matcher):
             print("ip address " + matcher)

    for line in f2.readlines():
        pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'
        searcher = re.search(pattern, line)
        if searcher:
            matcher = searcher.group(0)
            if ipaddress.IPv4Interface(matcher):
                print("ip address " + matcher)
    for line in f3.readlines():
        pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'
        searcher = re.search(pattern, line)
        if searcher:
            matcher = searcher.group(0)
            if ipaddress.IPv4Interface(matcher):
                print("ip address " + matcher)
    for line in f4.readlines():
        pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'
        searcher = re.search(pattern, line)
        if searcher:
            matcher = searcher.group(0)
            if ipaddress.IPv4Interface(matcher):
                print("ip address " + matcher)
    for line in f5.readlines():
        pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'
        searcher = re.search(pattern, line)
        if searcher:
            matcher = searcher.group(0)
            if ipaddress.IPv4Interface(matcher):
                print("ip address " + matcher)
    for line in f6.readlines():
        pattern = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b)'
        searcher = re.search(pattern, line)
        if searcher:
            matcher = searcher.group(0)
            if ipaddress.IPv4Interface(matcher):
                print("ip address " + matcher)
    return "END OF PROGRAM"





print(main())