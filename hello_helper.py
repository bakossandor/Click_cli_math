def operation(first_num, operator, second_num):
    if operator=="+":
        return float(first_num) + float(second_num)
    elif operator=="-":
        return float(first_num) - float(second_num)
    elif operator=="/":
        if second_num=="0":
            return "Zero Division Error"
        return float(first_num) / float(second_num)
    elif operator=="*":
        return float(first_num) * float(second_num)