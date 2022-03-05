import json


def write_in(filename, dependencies):
    with open(filename, 'w') as f:
        for dependencie in dependencies:
            f.write(f"{dependencie}\n")
       
def forge_dependencie_output(dependencie, tag):
     return f"{dependencie}@{tag}"

def forge_dependencie_list(dependencies):
    result = []
    for dependencie in dependencies.keys():
        result.append(forge_dependencie_output(dependencie, dependencies[dependencie]))
    return result

def get_dependencies(data, dependencie_type):
    dependencies = forge_dependencie_list(data[dependencie_type])
    write_in(dependencie_type, dependencies)

def extract(filepath):
    data = {}
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
    get_dependencies(data, "dependencies" )
    get_dependencies(data, "devDependencies" )
