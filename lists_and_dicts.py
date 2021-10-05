def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname" :"Omar", "lastname": "Hernández"}

    super_list = [
        {"firstname" :"Omar", "lastname": "Hernández"},
        {"firstname" :"Ponny", "lastname": "Garcia"},
        {"firstname" :"Daniel", "lastname": "Vergara"},
        {"firstname" :"Eduardo", "lastname": "Toti"},
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,2.3,4.5,8.5]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

    for item in super_list:
        print(item["firstname"],"- ", item["lastname"])
        

if __name__== '__main__':
    run()