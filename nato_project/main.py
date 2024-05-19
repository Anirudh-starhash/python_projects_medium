import pandas

data=pandas.read_csv("D:\\nitw\\academics\\demo_py\\nato_project\\nato_phonetic_alphabet.csv")

new_dict={y.letter:y.code for (x,y) in data.iterrows()}
def generate():
    name=input("enter a name :\n")
    try:
        name_list=[new_dict[x.capitalize()] for x in name]
    except KeyError as e:
        print('Sorry! Only numbers should be entered!')
        generate()
    else:
        print(name_list)

generate()