
import csv

TEST_FILE = "test.csv"

def isT(s):    
    return s == 'T'

def make_truth_table(f = TEST_FILE):
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        table = list()
        var = list()
        line_count = 0
        for row in csv_reader:
            if line_count == 0:                
                for i in range(len(row)-1):
                    var.append(row[i])
            else:
                row_vals = [isT(v) for v in row]
                table.append(row_vals)
            line_count += 1
        
        return table, var

def tester():
    table, var = make_truth_table()
    total = len(table)
    passed = 0

    for row in table:                    
        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]
        f = row[4]

        result = (not a or not d) and (a or c) and (not b or not c or d)
                
        if result == f:
            passed = passed + 1
        else:
            print(f"Expected:	{row}")
            print("-------------------------------------------")
        
    print("Using the following formula:")    
    print("(not a or not d) and (a or c) and (not b or not c or d)")
    print(f"{passed}/{total} cases passed.")

tester()
    