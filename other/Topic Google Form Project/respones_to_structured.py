import csv

def read_document(file_path):
    responses = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            responses.append(line)
    return responses

def manipulate(file):
    n = 1
    for line in file:
        line[0] = f'Group #{n}'

        n += 1
        studentDict = {}
        if ',' in line[2]:
            studentList = line[2].split(',')
        else:
            studentList = line[2].split('\n')
        for student in studentList:
            name = ''
            roll_number = ''
            for letter in student:
                if letter.isdigit():
                    roll_number += letter
                elif letter.isalpha() or letter == " " :
                    name += letter
            studentDict[roll_number.strip()] = name.strip()
            line[2] = studentDict
        line[1],line[3] = line[3],line[1]
        
    with open('Final Responses BA PROGRAM Data Analysis Research Project Topics.csv','w',newline='') as final_responses:
        fieldsname = ['Group_Number','Research_Topic','Member_Rno','Member_Name']
        writer = csv.writer(final_responses)
        writer.writerow(fieldsname)
        for group in file:
            i = 0
            for k,v in group[2].items():
                first_kv = [k,v]
                i+=1
                if i == 1:
                    break
            writer.writerow([group[0],group[1],first_kv[0],first_kv[1]])
            i = 0
            for k,v in group[2].items():
                i += 1
                if i == 1:
                    continue
                else:
                    writer.writerow([group[0],group[1],k,v])

responses = read_document('Data Analysis Project Details.csv')
print(responses)
manipulate(responses)