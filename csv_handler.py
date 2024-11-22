import csv

def writeToCSV(data):
    with open("data.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
        for i in data:
            writer.writerow(i)

#def readFromCSV():



def main():
    data = [
    {"name": "Rupert", "age": "20", "grade": "A"},
    {"name": "Emma", "age": "21", "grade": "B"},
    {"name": "Charlie", "age": "19", "grade": "C"}
    ]

    
    writeToCSV(data)

main()