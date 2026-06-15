'''f = open('263b72060e-d009-44ce-8f9b-1b58622df596_26.1.txt')
n = int(f.readline())
boxes = [int(s) for s in f]
boxes.sort(reverse=True)
gift = []
for box in boxes:
    if gift == []:
        gift.append(box)
    elif gift[-1] - box >= 3:
        gift.append(box)
print(len(gift),min(gift))'''

'''f = open('af78fee1-432f-44ee-a2dd-d0fa1bb1f534_26.2.txt')
n = int(f.readline())
boxes = [int(s) for s in f]
boxes.sort(reverse=True)
blocks = []
while len(boxes) != 0:
    gift = [boxes[0]]
    del boxes[0]
    for box in boxes[:]:
        if gift[-1] - box >= 5:
            gift.append(box)
            boxes.remove(box)
    blocks.append(gift)
print(len(blocks),len(blocks[0]))'''

'''f = open('a3424c6b-6358-42da-a290-cdc0a9a5e302_26.3.txt')
n = int(f.readline())
boxes = []
for s in f:
    lens, color = s.split()
    boxes.append(([int(lens),color]))
boxes.sort(reverse=True)
blocks = []
while boxes != []:
    gift = [boxes[0]]
    del boxes[0]
    for box in boxes[:]:
        if gift[-1][0] - box[0] >= 8 and gift[-1][1] != box[1]:
            gift.append(box)
            boxes.remove(box)
    blocks.append(gift)
print(len(blocks),len(blocks[0]), len(max(blocks, key=len)))'''


