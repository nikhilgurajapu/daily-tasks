"""Given a list of tuples representing (name, age), sort the list by age in ascending order."""
tpl_list = [("nikhil",25),("roshini",18),("chaithu",29),("chandu",22),("ramya",23)]
sorted_tpl_list = sorted(tpl_list, key=lambda list: (list[1]))
print(sorted_tpl_list)