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
                for i in range(len(row)):
                    var.append(row[i])
            else:
                row_vals = [isT(v) for v in row]
                table.append(row_vals)
            line_count += 1
        
        return table, var

def solver(f = TEST_FILE):
    table, var = make_truth_table(f)    
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

def create_tester(f = TEST_FILE):    
    template = """
import csv

TEST_FILE = REPLACE_FILE

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
        VARIABLES
        result = FORMULA
                
        if result == f:
            passed = passed + 1
        else:
            print(f"Expected:\t{row}")
            print("-------------------------------------------")
        
    
    print(f"{passed}/{total} cases passed.")

tester()
    """
    table, var = make_truth_table(f)    
    v = ""
    for i in range(len(var)):
        if i == 0:
            v += f"{var[i]} = row[{i}]\n"
        else:
            v += f"        {var[i]} = row[{i}]\n"

    formula = solver(f)
    template = template.replace("VARIABLES", v)
    template = template.replace("FORMULA", formula)
    template = template.replace("REPLACE_FILE", f'"{f}"')
    with open(f"{f}.py", "w") as py_file:
        py_file.write(template)
    
def get_symbols(formula):
    sym_form = formula.replace("and", "&&")
    sym_form = sym_form.replace("or", "||")
    sym_form = sym_form.replace("not ", "~")
    return sym_form


if __name__ == "__main__":
    
    formula = solver()
    create_tester()
    print(get_symbols(formula))

    pass 

