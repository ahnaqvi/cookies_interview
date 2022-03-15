import sys
import subprocess

def matchCookies(lines, targetDay):
    '''given contents of a file and target dat, 
    find most active cookies that match'''

    matchStart = False
    cookies = {}
    for index, line in enumerate(lines):
        if len(line.split(",")) != 2:
            # print corrupt line but continue
            print(F'Log file corrupted at line {index+1}')
            continue
        cookie, date = line.split(",")
        day = date.split("T")[0]


        if matchStart == False:
            # find a matching date
            if day == targetDay:
                # found first match
                matchStart = True
                if cookie not in cookies:
                    cookies[cookie] = 0
                cookies[cookie] += 1
                continue

        if matchStart == True:
            # if stops matching
            if day != targetDay:
            # exhausted all matches. No need to continue since log is sorted
                break
            # else, update cookie count
            if cookie not in cookies:
                cookies[cookie] = 0
            cookies[cookie] += 1

    maxCount = max(cookies.values())
    mostActiveCookies = [cookie for cookie in cookies if cookies[cookie] == maxCount]
    return mostActiveCookies

def main():
    filename = sys.argv[1]

    if sys.argv[2] != '-d':
        print("Date not specified in proper format. Use '-d date' option to use date.")
        return -1 # error

    if len(sys.argv[3]) != 10 or sys.argv[3].count('-') != 2 or sys.argv[3][-3] != '-' or sys.argv[3][-6] != '-':
        print('Format of date is wrong. Use following format: 20YY-MM-DD')
        return -1 # error

    targetDay = sys.argv[3] # read target day

    with open(filename, 'r') as fd:
        lines = fd.readlines()
    lines = lines[1:] # eliminate csv header
    mostActiveCookies = matchCookies(lines, targetDay)
    for cookie in mostActiveCookies:
        print(cookie)
    return 1

if __name__ == '__main__':
    sys.exit(main())

