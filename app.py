import math
from flask import Flask, render_template, request

from helpers import lastBirthday, mergeDigits1122, mergeDigits, piramidBuilder, findNegativeSequences


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kabbalah')
def kabbalah():
    return render_template('kabbalah_index.html')

@app.route('/calculate', methods=["GET", "POST"])
def calculo():
    if request.method == 'POST':

        tmp_namePlainText = request.form.get("name")
        if not tmp_namePlainText:
            return "invalid name"

        tmp_firstName = tmp_namePlainText.split()
        firstName = tmp_firstName[0].upper()

        namePlainText = tmp_namePlainText.replace(" ", "").upper()
        length = len(namePlainText)

        tmp_birthdate = request.form.get("birthdate")
        if not tmp_birthdate:
            tmp_birthdate = "0000-00-00"
            isbirthdate = False
        else:
            isbirthdate = True
        birthdate = tmp_birthdate.split("-")

        year = birthdate[0]
        month = birthdate[1]
        day = birthdate[2]

        age = int(lastBirthday(month, day)) - int(year)


        # Constant KEY for vowels.
        VOWELS_KEY = {"A": "1", "E": "5", "I": "1", "O": "7", "U": "6", "Ä": "2", "Á": "3", "À": "2", "Ë": "1", "É": "7", "È": "1", "Ï": "2", "Í": "3", "Ì": "2", "Ö": "5", "Ó": "9", "Ò": "5", "Ü": "3", "Ú": "8", "Ù": "3", "Â": "8", "Ê": "3", "Î": "8", "Ô": "5", "Û": "4", "Ã": "4", "Õ": "1", "Å" : "8", "Ů" : "4"}

        # Constant KEY for consonants.
        CONSONANTS_KEY = {"B": "2", "C": "3", "D": "4", "F": "8", "G": "3", "H": "5", "J": "1", "K": "2", "L": "3", "M": "4", "N": "5", "P": "8", "Q": "1", "R": "2", "S": "3", "T": "4", "V": "6", "W": "6", "X": "6", "Y": "1", "Z": "7", "Ç": "6"}

        # Constant Key for specials.
        SPECIALS_KEY = {"'": "2" ,"~": "3", "^": "7", "̊ ": "7"}

        # Constant digits list.
        DIGITS_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


        # Declare variables and list.
        generalList = []
        vowelsList = []
        consonantsList = []
        specialsList = []
        birthdateList = []
        lastBdayList = []
        firstNameList = []
        piramidBuilderList = []


        # Expected results.
        motivationNumber = 0
        impressionNumber = 0
        expressionNumber = 0
        destinyNumber = 0 #birthdate
        missionNumber = 0 #birthdate
        karmicDebtsNumbers = []
        karmicLessonsNumbers = []
        hiddenTendenciesNumbers = []
        personalYearNumber = 0 #birthdate
        subconsciousResponse = 0
        firstCycle = []
        secondCycle = []
        thirdCycle = []
        firstDecisive = []
        secondDecisive = []
        thirdDecisive = []
        fourthDecisive = []
        challengesList = []
        intervalueList = []
        soulState = []
        arcane = {}
        piramid = []
        piramidTip = 0
        negativeSequences = []


        # Fills the name chars numbers list, assigning the respective KEY number for each letter in the painText.
        for char in namePlainText:
            if char in VOWELS_KEY:
                strNumber = VOWELS_KEY[char]
                generalList.append(strNumber)
                vowelsList.append(strNumber)
            if char in CONSONANTS_KEY:
                strNumber = CONSONANTS_KEY[char]
                generalList.append(strNumber)
                consonantsList.append(strNumber)
            if char in SPECIALS_KEY:
                strNumber = SPECIALS_KEY[char]
                if char == "'":
                    if generalList[-1] in vowelsList:
                        generalList.append(strNumber)
                        vowelsList.append(strNumber)
                    if generalList[-1] in consonantsList:
                        generalList.append(strNumber)
                        consonantsList.append(strNumber)
                else:
                    generalList.append(strNumber)
                    specialsList.append(strNumber)

        # Fills the first name chars numbers list, assigning the respective KEY number for each letter in the first name.
        for char in firstName:
            if char in VOWELS_KEY:
                strNumber = VOWELS_KEY[char]
                firstNameList.append(strNumber)
            if char in CONSONANTS_KEY:
                strNumber = CONSONANTS_KEY[char]
                firstNameList.append(strNumber)
            if char in SPECIALS_KEY:
                strNumber = SPECIALS_KEY[char]
                firstNameList.append(strNumber)

        # Fill birthdateList and lastBdayList.
        if isbirthdate:
            for char in month:
                birthdateList.append(char)
                lastBdayList.append(char)

            for char in day:
                birthdateList.append(char)
                lastBdayList.append(char)

            for char in year:
                birthdateList.append(char)

            lastBday = lastBirthday(month, day)
            for char in lastBday:
                lastBdayList.append(char)


        # Calculate the Motivation number.
        for number in vowelsList:
            motivationNumber += int(number)
        motivationNumber = mergeDigits1122(motivationNumber)


        # Calculate the Impression number.
        for number in consonantsList:
            impressionNumber += int(number)
        impressionNumber = mergeDigits(impressionNumber)


        # Calculate the Expression number.
        for number in generalList:
            expressionNumber += int(number)
        expressionNumberSum = expressionNumber
        expressionNumber = mergeDigits1122(expressionNumber)


        # Calculate Destiny number.
        if isbirthdate:
            for number in birthdateList:
                destinyNumber += int(number)
            destinyNumber = mergeDigits1122(destinyNumber)


        # Calculate Mission number.
        if isbirthdate:
            missionNumber = expressionNumber + destinyNumber
            missionNumber = mergeDigits1122(missionNumber)


        # Parse karmic Debts number(s).
        if day == "13" or day == "14" or day == "16" or day == "19":
            karmicDebtsNumbers.append(day)

        if expressionNumber == 4 or destinyNumber == 4 or motivationNumber == 4:
            karmicDebt = "13"
            if karmicDebt not in karmicDebtsNumbers:
                karmicDebtsNumbers.append(karmicDebt)

        if expressionNumber == 5 or destinyNumber == 5 or motivationNumber == 5:
            karmicDebt = "14"
            if karmicDebt not in karmicDebtsNumbers:
                karmicDebtsNumbers.append(karmicDebt)
        if expressionNumber == 7 or destinyNumber == 7 or motivationNumber == 7:
            karmicDebt = "16"
            if karmicDebt not in karmicDebtsNumbers:
                karmicDebtsNumbers.append(karmicDebt)
        if expressionNumber == 1 or destinyNumber == 1 or motivationNumber == 1:
            karmicDebt = "19"
            if karmicDebt not in karmicDebtsNumbers:
                karmicDebtsNumbers.append(karmicDebt)


        # Parse karmic Lessons number(s).
        for number in DIGITS_LIST:
            if number not in generalList:
                karmicLessonsNumbers.append(number)


        # Calculate Hidden Tendencies numbers.
        for item in generalList:
            count = 0
            for element in generalList:
                if element == item:
                    count += 1
            if count >= 3:
                if item not in hiddenTendenciesNumbers:
                    hiddenTendenciesNumbers.append(item)


        # Calculate Personal Year number.
        if isbirthdate:
            for number in lastBdayList:
                personalYearNumber += int(number)
            personalYearNumber = mergeDigits(personalYearNumber)


        # Calculate Subconscious Response number.
        subconsciousResponse = (9 - len(karmicLessonsNumbers))


        # Calculate Life Cycles
        if isbirthdate:
            # First Cycle
            gap = 37 - destinyNumber
            firstCycleStart = year
            firstCycleEnd = int(year) + int(gap)
            fisrtCycleFrequency = mergeDigits1122(month)
            firstCycle.extend([fisrtCycleFrequency, firstCycleStart, firstCycleEnd])

            # Second Cycle
            secondCycleStart = firstCycleEnd
            secondCycleEnd = secondCycleStart + 27
            secondCycleFrequency = mergeDigits1122(day)
            secondCycle.extend([secondCycleFrequency, secondCycleStart, secondCycleEnd])

            # Third Cycle
            thirdCycleStart = secondCycleEnd
            thirdCycleFrequency = mergeDigits1122(year)
            thirdCycle.extend([thirdCycleFrequency, thirdCycleStart, "? ? ?"])


        # Calculate Decisive Moments
        if isbirthdate:
            # First Decisive
            firstDecisiveStart = firstCycle[1]
            firstDecisiveEnd = firstCycle[2]
            fisrtDecisiveFrequency = mergeDigits1122((int(month) + int(day)))
            firstDecisive.extend([fisrtDecisiveFrequency, firstDecisiveStart, firstDecisiveEnd])

            # Second Decisive
            secondDecisiveStart = firstDecisiveEnd
            secondDecisiveEnd = secondDecisiveStart + 9
            secondDecisiveFrequency = mergeDigits1122((int(day) + int(year)))
            secondDecisive.extend([secondDecisiveFrequency, secondDecisiveStart, secondDecisiveEnd])

            # Third Decisive
            thirdDecisiveStart = secondDecisiveEnd
            thirdDecisiveEnd = thirdDecisiveStart + 9
            thirdDecisiveFrequency = mergeDigits1122((int(fisrtDecisiveFrequency) + int(secondDecisiveFrequency)))
            thirdDecisive.extend([thirdDecisiveFrequency, thirdDecisiveStart, thirdDecisiveEnd])

            # Fourth Decisive
            fourthDecisiveStart = thirdDecisiveEnd
            fourthDecisiveFrequency = mergeDigits1122((int(month) + int(year)))
            fourthDecisive.extend([fourthDecisiveFrequency, fourthDecisiveStart, "? ? ?"])


        # Calculate Challenges
        if isbirthdate:

            firstChallenge = 0
            fcx = mergeDigits(day)
            fcy = mergeDigits(month)
            if fcx > fcy:
                fcz = fcx - fcy
                firstChallenge = mergeDigits(fcz)
            if fcx < fcy:
                fcz = fcy - fcx
                firstChallenge = mergeDigits(fcz)

            secondChallenge = 0
            scx = mergeDigits(day)
            scy = mergeDigits(year)
            if scx > scy:
                scz = scx - scy
                secondChallenge = mergeDigits(scz)
            if scx < scy:
                scz = scy - scx
                secondChallenge = mergeDigits(scz)

            thirdChallenge = 0
            tcx = firstChallenge
            tcy = secondChallenge
            if tcx > tcy:
                tcz = tcx - tcy
                thirdChallenge = mergeDigits(tcz)
            if tcx < tcy:
                tcz = tcy - tcx
                thirdChallenge = mergeDigits(tcz)

            challengesList.extend([firstChallenge, secondChallenge, thirdChallenge])


        # Calculate Intervalue Ralation
            # Track of how many times each item is repeated in the list
        tmp_dictlist = []
        for item in firstNameList:
            count = 0
            for element in firstNameList:
                if element == item:
                    count += 1
            tmp_dict = {'number': item, 'qty': count}
            tmp_dictlist.append(tmp_dict)
            # Compare dict elements. If element value is twice or bigger than any other, append that element to intervalueList
        for i in range(len(tmp_dictlist)):
            for dictionary in tmp_dictlist:
                if tmp_dictlist[i]['qty'] >= (2 * dictionary['qty']):
                    if tmp_dictlist[i]['number'] not in intervalueList:
                        intervalueList.append(tmp_dictlist[i]['number'])


        # Parse Soul State
        consonantsSum = 0
        vowelsSum = 0
        for item in consonantsList:
            consonantsSum += int(item)
        for item in vowelsList:
            vowelsSum += int(item)
        if consonantsSum > vowelsSum:
            soulState.extend(["Rising",  "⇧"])
        if consonantsSum < vowelsSum:
            soulState.extend(["Decaying", "⇩"])
        if consonantsSum == vowelsSum:
            soulState.extend(["Balanced", "⬄"])


        # Parse Arcanes
        if isbirthdate:
            arcane['quantity'] = length - 1
            arcaneDuration = float(90 / arcane['quantity'])
            arcane['duration'] = "{:.4f}".format(arcaneDuration)
            arcane['influence'] = math.ceil((age * 100) / math.floor(arcaneDuration * 100))


        # Piramid Building.
        for i in generalList:
            piramidBuilderList.append(int(i))
        piramid.append(piramidBuilderList)
        for i in range(len(piramidBuilderList) - 1):
            piramidBuilderList = piramidBuilder(piramidBuilderList, mergeDigits)
            piramid.append(piramidBuilderList)
            i += 1

        # Piramid Tip.
        piramidTip = piramid[len(piramid) - 1][0]

        # Calculate Negative Sequences.
        for lists in piramid:
            sequences = findNegativeSequences(lists)
            for sequence in sequences:
                negativeSequences.append(sequence)

        return render_template("kabbalah_results.html", length=length, namePlainText=namePlainText, generalList=generalList, isbirthdate=isbirthdate, expressionNumber=expressionNumber, motivationNumber=motivationNumber, impressionNumber=impressionNumber, destinyNumber=destinyNumber, missionNumber=missionNumber, personalYearNumber=personalYearNumber, karmicLessonsNumbers=karmicLessonsNumbers, karmicDebtsNumbers=karmicDebtsNumbers, subconsciousResponse=subconsciousResponse, hiddenTendenciesNumbers=hiddenTendenciesNumbers, piramid=piramid, piramidTip=piramidTip, negativeSequences=negativeSequences, day=day, firstCycle=firstCycle, secondCycle=secondCycle, thirdCycle=thirdCycle, firstDecisive=firstDecisive, secondDecisive=secondDecisive, thirdDecisive=thirdDecisive, fourthDecisive=fourthDecisive, challengesList=challengesList, intervalueList=intervalueList, soulState=soulState, arcane=arcane, age=age)
    else:
        return render_template("kabbalah_calculate.html")

@app.route('/tlts')
def tlts_index():
    return render_template('tlts_index.html')

@app.route('/tlts_about')
def tlts_about():
    return render_template('tlts_about.html')

@app.route('/tlts_contact')
def tlts_contact():
    return render_template('tlts_contact.html')

@app.route('/tlts_hours')
def tlts_hours():
    return render_template('tlts_hours.html')

@app.route('/cdt')
def cdt():
    return render_template('cdt.html')

@app.route('/wta')
def wta():
    return render_template('wta.html')
