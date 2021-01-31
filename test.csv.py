
import common

TEST_FILE = "test.csv"

def tester():
    table, var = common.make_truth_table()
    total = len(table)
    passed = 0

    for row in table:                    
        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]
        f = row[4]

        result = not a or b or not c or d
                
        if result == f:
            passed = passed + 1
        else:
            print(f"Expected:	{row}")
            print("-------------------------------------------")
        
    print("Using the following formula:")    
    print("not a or b or not c or d")
    print(f"{passed}/{total} cases passed.")

tester()
    