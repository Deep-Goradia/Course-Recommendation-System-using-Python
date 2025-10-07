import pandas as pd

def load_courses(path="data/courses.csv"):
    return pd.read_csv(path, quotechar='"')

def load_materials(path="data/materials.csv"):
    return pd.read_csv(path, quotechar='"')
