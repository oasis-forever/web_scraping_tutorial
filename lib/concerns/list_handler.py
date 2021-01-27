def uniq_list(duplicate_data):
    uniq_data = []
    for datum in duplicate_data:
        if not datum in uniq_data:
            uniq_data.append(datum)
    return uniq_data
