#IMPORTS
import os # For directory creation
import sys # Command line things

class WrongParameterNumber(Exception):
    pass

class LackNameParameter(Exception):
    pass

def print_instructions():
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

def create_root_dir_and_return_its_path(current_working_directory, name):
    root_dir = f"{current_working_directory}/{name}"
    os.mkdir(root_dir)
    return root_dir

def create_build_directory(root_dir):
    build_dir = f"{root_dir}/build"
    os.mkdir(build_dir)

def create_deploy_directory(root_dir):
    deploy_dir = f"{root_dir}/deploy"
    os.mkdir(deploy_dir)

try:
    parameter_dict = get_params_or_raise_error()
    current_working_directory = os.getcwd()
    root_dir = create_root_dir_and_return_its_path(os.getcwd(), parameter_dict['-n'])
    create_build_directory(root_dir)
    create_deploy_directory(root_dir)

except WrongParameterNumber:
    print("create_directories error: Wrong number of parameters.")
    print_instructions();
except LackNameParameter:
    print("create_directories error: name not informed (-n)")
    print_instructions();
except OSError as err:
    pass
