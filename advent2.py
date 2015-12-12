# Day 2 part 1
accumulator=0
for box in boxes:
    box=sorted(map(int, box.split('x')))
    accumulator+=(box[0]*box[1]*2)+(box[1]*box[2]*2)+(box[2]*box[0]*2)+(box[0]*box[1])
print accumulator


# Day 2 part 2
ribbon_length=0
for box in boxes:
    box=sorted(map(int, box.split('x')))
    ribbon_length+=(box[0]+box[0]+box[1]+box[1])+(box[0]*box[1]*box[2])
print ribbon_length
