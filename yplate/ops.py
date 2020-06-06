import os

""" Functions imported in commands  """

## Load path to model config ##
def load_model():

    dirname = os.path.dirname(__file__)
    cfg = os.path.join(dirname, 'input/cfg/plate.cfg')
    weights = os.path.join(dirname, 'input/weights/plate.weights')
    label = ['Plate']
    return cfg,weights,label

## Command line Display UI ##
def display_top():
    print("\n#################################################")
    print("                   Plate-Scan                     ")
    print("#################################################\n")

def display_input(file_name):
    print("\n-------------------------------------------------")
    print("                     Input                    ")
    print("-------------------------------------------------\n")
    print("Input image: "+file_name)


def display_error():
    print("-------------------------------------------------")
    print("                     Error                      ")
    print("-------------------------------------------------\n")

def display_output():
    print("\n\n-------------------------------------------------")
    print("                     Output                      ")
    print("-------------------------------------------------\n")


## Show Model Config ##
def model_config():
    print("#################################################")
    print("               Model Configuration               ")
    print("#################################################\n")
    print("model: YOLO v3")
    print("Model cfg: plate.cfg")
    print("Model weights: plate.weights")
    print("Last training Iteration: 4234")
    print("\n################################################\n")
