new_str = input("Tell me something:").split()
print(new_str[2::3])

incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]

gen_list = [x if type(x) == float else
            x if type(x) == int and x % 2 == 0 else
            x **2 if type(x) == int and x % 2 != 0 else
            int(x)*3 if type(x) == str and x.isdigit()
            else -1 for x in incoming_list]
print(gen_list)

#outgoing_list = []
#for point_element in incoming_list:

#    if type(point_element) == float:
#        outgoing_list.append(point_element)

#    elif type(point_element) == int and point_element % 2 == 0:
#        outgoing_list.append(point_element)

#    elif type(point_element) == int and point_element % 2 != 0:
#        outgoing_list.append(point_element ** 2)

#    elif type(point_element) == str and point_element.isdigit():
#        outgoing_list.append(int(point_element) * 3)

#    else:
#        outgoing_list.append(-1)

#print(outgoing_list)