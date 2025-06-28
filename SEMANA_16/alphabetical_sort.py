def ordered_text(text_to_analyze):
    string_as_list=list(text_to_analyze.split("-"))
    string_as_list.sort()
    new_string="-".join(string_as_list)
    return string_as_list

print(ordered_text("python-VARIABLE-function-COMPUTER-monitor"))