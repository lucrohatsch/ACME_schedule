from person import Person


def strHour2float(strHour :str) -> float:
    """
    Convert str time to float base 10
    input: str HH-MM
    output: float H.M base 10
    example 10-15 -> 10.25
    """
    h,m=strHour.split(':')
    floatHour = (int(h) + (float(m)/60))
    return floatHour

def getData(file_path :str) -> list:
    """
    Get data\n
    Steps:
        1 - Open file\n
        2 - Returns a list with all lines 
    """
    # Step 1
    with open(file_path, 'r', encoding='utf8') as file:
        lines = file.readlines()
    return lines

def tranformData(lines :list) -> list:
    """
    transformData\n
    Read line by line and create the "Person" objects with structured data.
    """
# Step 2 and 3
    persons=[]
    days=[]    
    for line in lines:
        line=line.replace(" ","").split('=')
        person=Person(line[0])
        line[1]=line[1].strip().split(',')
        for x in line[1]:
            day , hours = x[:2], x[2:].split('-')
            line[1][line[1].index(x)]=[day, [strHour2float(hours[0]),strHour2float(hours[1])]]
            person.works(day, hours)
            if day not in days:
                days.append(day)
        persons.append(person)
    return persons, days

def processData(persons :list, days :list):
    """
    Process data\n 
    Steps: 
        1 - Generate all possible combinations of persons.\n
        2 - Verify time range.\n
        3 - Count coincident shifts for persons in peers.
    """
    # Step 1
    peers = []
    for i in range(0, len(persons)):
        for j in range(i,len(persons)):
            if (i!=j):
                together=0
    # Step 2 and 3
                for day in days:
                    rangeA=persons[i].schedule.get(day)
                    rangeB=persons[j].schedule.get(day)
                    if rangeA and rangeB:
                        if  rangeA[0] <= rangeB[0] <= rangeA[1]:
                            together+=1
                        elif rangeB[0] <= rangeA[0] <= rangeB[1]:
                            together+=1
                if together != 0:
                       peers.append((persons[i].name,persons[j].name, together))
    return peers