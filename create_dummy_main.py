#IMPORTS
import os # For directory creation
import sys # Command line things
import shutil

class WrongParameterNumber(Exception):
    pass

class LackNameParameter(Exception):
    pass

def print_instructions():
    print("create_dummy_main creates a minimal c++ main file so that the project has something to compile")
    print("Parameters are :")
    print("-n <name> : name of the project, equal to name of the root directory")

def test_amount(number_of_arguments):
    if number_of_arguments % 2 == 0 or number_of_arguments == 1:
        raise WrongParameterNumber()

def create_parameter_dict():
    parameters_keys = list(filter(lambda v:v[0]!=0 and v[0]%2==1, enumerate(sys.argv)))
    parameter_dict = dict()
    for k in parameters_keys:
        param_idx = k[0]
        param_key = k[1]
        value = sys.argv[param_idx+1]
        parameter_dict[param_key] = value
    return parameter_dict

def test_name_parameter_presence(parameter_dict):
    if '-n' not in parameter_dict:
        raise LackNameParameter();

def get_params_or_raise_error():
    number_of_arguments = len(sys.argv)
    test_amount(number_of_arguments)
    parameter_dict = create_parameter_dict()
    test_name_parameter_presence(parameter_dict)
    return parameter_dict

try:
    parameter_dict = get_params_or_raise_error()
    current_working_directory = os.getcwd()
    project_name =  parameter_dict['-n']
    ## TODO: goto the src directory
    src_directory = f"{current_working_directory}/{project_name}/src"
    where_is_the_script = os.path.dirname(os.path.realpath(__file__))
    print(f"where is the script {where_is_the_script}")
    print(f"where working dir {current_working_directory}")
    ## TODO: Write the main there
    shutil.copyfile(
        f"{where_is_the_script}/dummy_main.cpp",
        f"{src_directory}/main.cpp"
    )
    pass
except WrongParameterNumber:
    print("create_dummy_main error: Wrong number of parameters.")
    print_instructions();
except LackNameParameter:
    print("create_dummy_main error: name not informed (-n)")
    print_instructions();
except OSError as err:
    pass