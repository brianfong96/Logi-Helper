import chromedriver as cd
import time
import common

def solver(f = common.TEST_FILE):
    table, var = common.make_truth_table(f)    
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

def get_cnf(formula):
    url = "https://www.dcode.fr/boolean-expressions-calculator"
    driver = cd.CreateDriver()
    driver.get(url)
    time.sleep(2)

    driver.find_element_by_css_selector('#label_bool_calculator_format_cnf').click()
    driver.find_element_by_css_selector('#bool_calculator > table > tbody > tr > td:nth-child(2) > label:nth-child(7)').click()
    input_element = driver.find_element_by_css_selector("#bool_calculator_input")
    input_element.clear()
    input_element.send_keys(formula)
    input_element.send_keys(cd.enter_key)
    time.sleep(5)
    result = driver.find_element_by_css_selector('#results > div.result').text
    driver.quit() 
    
    cnf = result.lower()
    if formula == "true":
        cnf = "True"
    elif formula == "false":
        cnf = "False"
    return cnf

def create_tester(formula, f = common.TEST_FILE):    
    template = """
import common

TEST_FILE = REPLACE_FILE

def tester():
    table, var = common.make_truth_table()
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
        
    print("Using the following formula:")    
    print("FORMULA")
    print(f"{passed}/{total} cases passed.")

tester()
    """
    table, var = common.make_truth_table(f)    
    v = ""
    for i in range(len(var)):
        if i == 0:
            v += f"{var[i]} = row[{i}]\n"
        else:
            v += f"        {var[i]} = row[{i}]\n"

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

def create_truth_table(formula):
    table = list()
    
    return table

if __name__ == "__main__":
    
    f = common.TEST_FILE
    formula = get_cnf(solver(f))    
    create_tester(formula, f)

    pass 

