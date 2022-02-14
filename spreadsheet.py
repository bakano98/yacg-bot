import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

headers = ["\t\tTopic: ", "\t\tBible Study Leader: ",
           "\t\tWorship Leader: ", "\t\tRemarks: ", "\tBirthday: "]

NO_CG = "No CG this week. Go hang out!"
currentDate = datetime.datetime.now()
currentMonth = currentDate.strftime("%B")
currentDay = datetime.date.today().day
currentWeek = datetime.date.today().isocalendar()[1]

today = datetime.date.today()
endOfWeek = today + datetime.timedelta(days=6 - today.weekday())
endOfWeek = endOfWeek.day

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'rachelle-340511-f69cbb14908c.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Copy of YA CG Planner 2021").sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()


def getMonthItemsRows(fullMonthName):
    rows = []
    cell_list = sheet.findall(fullMonthName)
    for cell in cell_list:
        rows.append(cell.row)
    return rows


def getThisMonthItemsRows():
    return getMonthItemsRows(currentMonth)


def getCertainMonthItemsRows(fullMonthName):
    return getMonthItemsRows(fullMonthName)


def getThisMonthItems():
    items = []
    monthRows = getThisMonthItemsRows()
    for rowValue in monthRows:
        item = sheet.row_values(rowValue)
        item = item[1:]
        if (int(item[1]) < currentDay):
            # then do nothing and skip
            continue
        else:
            items.append(item)
    return items


def getThisWeekItems():
    items = []
    remItems = getThisMonthItems()
    for item in remItems:
        if (int(item[1]) <= endOfWeek):
            items.append(item)
    return items


def getNextItemFormatted():
    items = getThisMonthItems()
    toReturn = items[0]
    date = toReturn[0] + " " + toReturn[1]
    if ("No CG" in toReturn[2]):
        if ("CAP" in toReturn[2]):
            return "CAPing this week on " + date
        return NO_CG
    topic = toReturn[2]
    if (len(toReturn) < 4):
        return date + "\n" + "topic"

    BSL = toReturn[3]
    WSL = toReturn[4]
    isBS = True
    if (("-" in BSL) or ("CG" in BSL) or (BSL == "") or (BSL == " ")):
        isBS = False
    if (isBS):
        date = toReturn[0] + " " + toReturn[1]
        topic = "Topic: " + toReturn[2]
        BSL = "Bible study leader: " + BSL
        WSL = "Worship leader: " + WSL
        hasRemarks = False
        try:
            remarks = toReturn[5]
            hasRemarks = True
        except:
            print("No remarks")
        if (hasRemarks):
            return date + "\n" + topic + "\n" + BSL + "\n" + WSL + "\n" + "Remarks: " + remarks
        return date + "\n" + topic + "\n" + BSL + "\n" + WSL
    else:
        return "No bible study this week! We'll be having " + topic + " instead"


def formatThisMonthItems():
    items = getThisMonthItems()
    twoLength = len(items)
    output = []
    for i in range(twoLength):
        currentItem = items[i]
        length = len(currentItem)
        concatDate = "<b>" + currentItem[0] + " " + currentItem[1] + "</b>"
        strOutput = concatDate
        strOutput += "\n"
        for j in range(2, length):
            strOutput += headers[j-2] + currentItem[j]
            strOutput += "\n"
        output.append(strOutput)
    return output


def formatThisWeekItems():
    items = getThisWeekItems()
    twoLength = len(items)
    output = []
    for i in range(twoLength):
        currentItem = items[i]
        length = len(currentItem)
        concatDate = "<b>" + currentItem[0] + " " + currentItem[1] + "</b>"
        strOutput = concatDate
        strOutput += "\n"
        for j in range(2, length):
            if (currentItem[j] == ""):
                break
            strOutput += headers[j-2] + currentItem[j]
            strOutput += "\n"
        output.append(strOutput)
    return output


def getThisWeekItemsFormatted():
    formatted = formatThisWeekItems()
    output = ""
    for item in formatted:
        output += item + "\n"
    return output


def getThisMonthItemsFormatted():
    formatted = formatThisMonthItems()
    output = ""
    for item in formatted:
        output += item + "\n"
    return output


def getUpcoming():
    output = formatThisWeekItems()[0]
    if ("CAP" in output):
        return output
    if ("No CG" in output):
        date = output.split("\n")[0]
        return date + "\nNo CG this week. Go hang out!"
