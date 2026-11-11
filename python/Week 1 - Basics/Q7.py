box_per_camel = 6
box_per_mule = 4
box_per_donkey = 2

total_boxes = int(input("Enter total boxes: "))

camels = total_boxes//box_per_camel
remaining_boxes = total_boxes % box_per_camel

mules = remaining_boxes // box_per_mule
remaining_boxes = remaining_boxes % box_per_mule

donkeys = remaining_boxes // box_per_donkey
donkeys = donkeys + remaining_boxes % box_per_donkey  # just in case if there is one box left. So 1 donkey needed.

print("Alibaba needs ", camels, " camels, ", mules, " mules, ", donkeys, " donkeys")