def functionvars(v1, v2, *args, v3=None):
    print(f"this works and the args passed are- var1:{v1} and var2: {v2}")
    print("now working through variable args")

    """ the below text is a generator expression and NOT a comprehension on the lines of list/dict comprehensions
    the evaluation is lazy and this is more memory efficient for large dataset than list/dict comprehension
    """
    tupl = (i for i in args)
    print(tuple(tupl))
    if v3 is not None:
        print(v3)


if __name__ == "__main__":
    var_a = 1
    var_b = "text"
    var_c = [1, 2, 3]
    var_d = {"key1": 100, "key2": 101}
    var_e = "eos"
    functionvars(var_a, var_b, var_c, var_d, v3=var_e)
