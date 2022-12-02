# Disk class

# defines a class for disk objects with a definition for size
class Disk:
  def __init__(self, size):
    self.diskSize = size

# creates 4 disks of different sizes
smallestDisk = Disk(1)
smallDisk = Disk(2)
mediumDisk = Disk(3)
largeDisk = Disk(4)