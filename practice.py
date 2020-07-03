import collections
def countReqFromIP(ipAddress, logs):
    count = 0
    for line in logs:
        if line.startswith(ipAddress):
            count += 1
    return count
def getCounter(logs):
    counter = collections.Counter()
    for line in logs:
        words = line.split('- -')
        if words[0]:
            word = words[0].strip()
            counter[word] += 1
    return counter

def countMaxReqClient(logs):
    counter = getCounter(logs)
    countMaxReq = counter.most_common(1)[0][1]
    maxReqClient = counter.most_common(1)[0][0]
    return countMaxReq, maxReqClient 

def countMinReq(logs):
    counter = getCounter(logs)
    countMinReq = counter.most_common()[:-2:-1][0][1]
    return countMinReq
def averReq(logs):
    counter = getCounter(logs)
    countAverReq = round(sum(counter.values())/len(counter))
    return countAverReq

def main(filename):
    dummyAccessObj = open(filename, encoding="utf-8")
    dummyAccessLogs = dummyAccessObj.readlines()
    dummyAccessObj.close()
    ipAddress = '79.136.245.135'
    # ipAddress = '127.0.0.1'
    print('С Ip-адреса {} было совершено {} запросов'.format(ipAddress,countReqFromIP(ipAddress, dummyAccessLogs)))
    countMaxReq, maxReqClient = countMaxReqClient(dummyAccessLogs)
    print('Наибольшее число запросов - {} с IP-адреса {}'.format(countMaxReq, maxReqClient))
    print('Минимальное число запросов - {}'.format(countMinReq(dummyAccessLogs)))
    print('Среднее число запросов - {}'.format(averReq(dummyAccessLogs)))

if __name__ == "__main__":
    filePath = "dummy-access.log"
    main(filePath)
