
#!/usr/bin/env python3
my_list = ["192.168.0.5",5060, "up"]
print("The first itme in the list (IP):" + my_list[0])
print("The second item in the list(Port):" + str(my_list[1]))
print("The last item in the lsit(state):" + my_list[2])
new_list = [5060,"80",55,"10.20.30.1","10.20.20.1","ssh"]
print("When I {5} into IP addresses {3} or {4} I am unabel to pint ports {0} {1} or {2}.".format(*new_list))


