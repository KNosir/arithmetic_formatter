def arithmetic_arranger(arithmetic, true_or_false=False):
    """ i make a list and inside of list all expression ordered as list.
    numbers are also ordered by input order and result added in last part.
    """
    expression_list = []
    # First dividing experssions into list parts
    if len(arithmetic) > 5:
        raise print('Error: Too many problems')

    for i in arithmetic:

        if '+' in i:
            sign_index = i.index('+')
            first_expression = i[:sign_index]
            sign_expression = i[sign_index]
            second_expression = i[sign_index+1:]
            first_expression.strip()
            second_expression.strip()

            try:
                first_expression = int(first_expression)
                second_expression = int(second_expression)
            except:
                print('Error: Numbers must only contain digits.')

            if first_expression > 9999 or second_expression > 9999:
                raise print('Error: Numbers cannot be more than four digits')

            list_all_sign = []
            list_all_sign.append(first_expression)
            list_all_sign.append(sign_expression)
            list_all_sign.append(second_expression)

        elif '-' in i:
            sign_index = i.index('-')
            first_expression = i[:sign_index-1]
            sign_expression = i[sign_index]
            second_expression = i[sign_index+1:]
            first_expression.strip()
            second_expression.strip()

            try:
                first_expression = int(first_expression)
                second_expression = int(second_expression)
            except:
                print('Error: Numbers must only contain digits.')

            if first_expression > 9999 or second_expression > 9999:
                raise print('Error: Numbers cannot be more than four digits')

            list_all_sign = []
            list_all_sign.append(first_expression)
            list_all_sign.append(sign_expression)
            list_all_sign.append(second_expression)

        else:
            raise print("Error: Operator must be '+' or '-'.")

        expression_list.append(list_all_sign)

    # adding result of expression in last part of each inside list.
    for k in expression_list:
        if '+' in k:
            result = k[0] + k[-1]
            k.append(result)
        else:
            result = k[0] - k[-1]
            k.append(result)

    """ Now i convert int to str then i'll spaces in each string
            for looking ordered
    """
    # converting int numbers to string for display
    for m in expression_list:
        for j in m:
            index_j = m.index(j)
            pop_item = m.pop(index_j)
            pop_item = str(pop_item)
            m.insert(index_j, pop_item)
    
    
    for m in expression_list:
        
        max_number = 0
        for j in m:
            if len(j) > max_number:

                max_number = len(j)

        for k in m:
            if '+' == k or '-' == k:
                continue
            spaces_free = ' '
            index_k = m.index(k)
            k = m.pop(index_k)
            k = (max_number + 1 - int(len(k))) * spaces_free + k
            m.insert(index_k, k)
        


    first_line_print = ''
    second_line_print = ''
    line_print = ''
    result_line_print = ''

    for k, number_of_expression in zip(expression_list, range(len(expression_list))):
        first_line_print = ' ' + k[0] + first_line_print
        second_line_print = k[1] + k[2] + second_line_print
        line_print = (len(k[0]) + 1) * '-' + line_print
        result_line_print = ' ' + k[3] + result_line_print
        


        if number_of_expression == len(expression_list):
            continue

        first_line_print = '    ' + first_line_print
        second_line_print = '    ' + second_line_print
        line_print = '    ' + line_print
        result_line_print = '    ' + result_line_print


    if true_or_false:
        print(first_line_print)
        print(second_line_print)
        print(line_print)
        print(result_line_print)
    else:
        print(first_line_print)
        print(second_line_print)
        print(line_print)