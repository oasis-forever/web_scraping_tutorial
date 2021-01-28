def isfloat(param):
    if not param.isdecimal():
        try:
            float(param)
            return True
        except ValueError:
            return False
    else:
        return False
