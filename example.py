from functools import reduce


def Filter():

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    odd_filter = list(filter(lambda x: x % 2 != 0, my_list))
    odd = [i for i in my_list if i % 3 != 0]

    print(odd_filter)


def Map():
    my_list = [1, 2, 3, 4, 5]
    pwd = [i**2 for i in my_list]
    pwd_map = list(map(lambda x: x**2, my_list))

    print(pwd_map)


def reduce_example():
    my_list = [2, 2, 2, 2, 2]
    #multiplied = 1
    # for i in my_list:
    #     multiplied = multiplied * i

    multiplied_reduce = reduce(lambda a, b: a*b, my_list)
    print(multiplied_reduce)


# def example():
#      orders = [
#         {"product": 'Pizza al carbon', "total": 3, "date": '2019-08-12'},
#         {"product": 'Pizza de queso', "total": 10, "date": '2019-08-12'},
#         {"product": 'Pizza de 3 ingredientes', "total": 5, "date": '2019-08-12'},
#         {"product": 'Especial del chef', "total": 30, "date": '2019-08-12'},
#         {"product": 'Especial del chef', "total": 3, "date": '2019-08-13'},
#         {"product": 'Pizza al carbon', "total": 10, "date": '2019-08-14'},
#     ]
#      totals = orders.reduce((previous, order) => Object.assign({}, previous, {
#             [order.product]: (previous[order.product] | | 0) + order.total,
#         }),{})

if __name__ == "__main__":
    # Map()
    # Filter()
    # reduce_example()

    # i for i in my_list if i%2!=0
