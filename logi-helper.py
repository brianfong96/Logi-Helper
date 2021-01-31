import csv

def isT(s):    
    return s == 'T'

def make_truth_table(f = "test.csv"):
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

def solver():
    table, var = make_truth_table()    
    formula = ""

    for row in table:                    
        if row[-1]:            
            sub_formula = ""
            for i in range(len(row)-1):
                if sub_formula != "":
                    sub_formula += " and "
                if row[i]:
                    sub_formula += var[i]
                else:
                    sub_formula += f"not {var[i]}"
            if formula != "":
                formula += " or "
            formula += f"({sub_formula})"
    return formula

if __name__ == "__main__":
    print(solver())
    pass 

