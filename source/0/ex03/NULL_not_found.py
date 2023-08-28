def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
    elif isinstance(object, bool) and object == False:
        print("Fake: False", type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero: 0", type(object))
    elif isinstance(object, str) and object == "":
        print("Empty: ", type(object))
    else:
        print("Type not found")
        return 1
    return 0