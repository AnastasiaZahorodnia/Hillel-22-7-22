new_str = input("Tell me something:").split()
print(new_str[2::3])
# = el for el in new_str if new_str

incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
outgoing_list = []

for point_element in incoming_list:

    if isinstance(point_element, float):
        outgoing_list.append(point_element)

    elif isinstance(point_element, int) and point_element % 2 == 0:
        outgoing_list.append(point_element)

    elif isinstance(point_element, int) and point_element % 2 != 0:
        outgoing_list.append(point_element ** 2)

    elif isinstance(point_element, str) and point_element.isdigit():
        outgoing_list.append(int(point_element) * 3)

    else:
        outgoing_list.append(-1)

print(outgoing_list)