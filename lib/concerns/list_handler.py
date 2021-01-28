from decimal_handler import *

def tag_elems_list(items, tag):
    elems_list = []
    for item in items:
        _elems_list = []
        for elem in item.find_elements_by_tag_name(tag):
            _elems_list.append(elem.text)
        elems_list.append(_elems_list)
    return elems_list

def class_elems_list(items, klass):
    elems_list = []
    for item in items:
        _elems_list = []
        for elem in item.find_elements_by_class_name(klass):
            if isfloat(elem.text):
                _elems_list.append(float(elem.text))
            else:
                _elems_list.append(elem.text)
        elems_list.append(_elems_list)
    return elems_list
