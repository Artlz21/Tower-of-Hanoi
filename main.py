import disk, towers

# initialize disks
towers.towerLeft.append(disk.largeDisk.diskSize)
towers.towerLeft.append(disk.mediumDisk.diskSize)
towers.towerLeft.append(disk.smallDisk.diskSize)
towers.towerLeft.append(disk.smallestDisk.diskSize)

# init score
score = 0

# puzzle init
gameFlag = True

# puzzle start
while gameFlag == True:
  while True:
    # input target
    source = input("Select source tower (1, 2, 3): ")
    # check if valid input
    if source == '1' or source == '2' or source == '3':
      # check if target is empty
      if source == '1':
        if len(towers.towerLeft) == 0:
          print("Tower is empty!")
        else:
          break
      elif source == '2':
        if len(towers.towerMid) == 0:
          print("Tower is empty!")
        else:
          break
      elif source == '3':
        if len(towers.towerRight) == 0:
          print("Tower is empty!")
        else:
          break
    else:
      print("Invalid Selection!")
  # input destination
  dest = input("Select destination tower (1, 2, 3): ")
  # check if valid input
  if dest == '1' or dest == '2' or dest == '3':
    pass
  else:
    print("Invalid Selection!")
  # check if target and destination are the same
  if dest == source:
    print("You can't pick the same tower!")
  else:
    # check if destination is full
    if dest == '1':
      if len(towers.towerLeft) == 4:
        print("Tower is full!")
      else:
        pass
    elif dest == '2':
      if len(towers.towerMid) == 4:
        print("Tower is full!")
      else:
        pass
    # check if valid destination (disk size compare)
      # if yes, move disk
        # increment score (moves)
      # else if no, print error message
    if dest == '1':
      if source == '2':
        temp = towers.towerMid.pop()
        towers.towerMid.append(temp)
        if len(towers.towerLeft) == 0:
          test = 5
        else:
          test = towers.towerLeft.pop()
          towers.towerLeft.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerMid.pop()
          towers.towerLeft.append(temp)
          score += 1
      elif source == '3':
        temp = towers.towerRight.pop()
        towers.towerRight.append(temp)
        if len(towers.towerLeft) == 0:
          test = 5
        else:
          test = towers.towerLeft.pop()
          towers.towerLeft.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerRight.pop()
          towers.towerLeft.append(temp)
          score += 1
      else:
        print("Invalid Move!")
    elif dest == '2':
      if source == '1':
        temp = towers.towerLeft.pop()
        towers.towerLeft.append(temp)
        if len(towers.towerMid) == 0:
          test = 5
        else:
          test = towers.towerMid.pop()
          towers.towerMid.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerLeft.pop()
          towers.towerMid.append(temp)
          score += 1
      elif source == '3':
        temp = towers.towerRight.pop()
        towers.towerRight.append(temp)
        if len(towers.towerMid) == 0:
          test = 5
        else:
          test = towers.towerMid.pop()
          towers.towerMid.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerRight.pop()
          towers.towerMid.append(temp)
          score += 1
      else:
        print("Invalid Move!")
    elif dest == '3':
      if source == '1':
        temp = towers.towerLeft.pop()
        towers.towerLeft.append(temp)
        if len(towers.towerRight) == 0:
          test = 5
        else:
          test = towers.towerRight.pop()
          towers.towerRight.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerLeft.pop()
          towers.towerRight.append(temp)
          score += 1
      elif source == '2':
        temp = towers.towerMid.pop()
        towers.towerMid.append(temp)
        if len(towers.towerRight) == 0:
          test = 5
        else:
          test = towers.towerRight.pop()
          towers.towerRight.append(test)
        if temp > test:
          print("Invalid Move!")
        else:
          towers.towerMid.pop()
          towers.towerRight.append(temp)
          score += 1
      else:
        print("Invalid Move!")
  # check if puzzle is solved
    # if yes, exit loop
  if len(towers.towerRight) == 4:
    gameFlag = False
    # else if no, continue loop (reiterate)
  else:
    # update visuals test
    print(towers.towerLeft)
    print(towers.towerMid)
    print(towers.towerRight)
# if score is perfect, print perfect score
if score == 15:
  print(f"Your score is {score}. Perfect!")
# else print score
else:
  print(f"Your score is {score}.")
# end puzzle