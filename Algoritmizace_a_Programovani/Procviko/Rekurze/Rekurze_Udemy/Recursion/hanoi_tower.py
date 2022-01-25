
def hanoi(disk, a, b, c):
    if disk == 0:
        print(f"Disk {disk} from {a} to {c}")
        return
    
    hanoi(disk-1, a, c, b)
    print(f"Disk {disk} from {a} to {c}")
    hanoi(disk-1, b, a, c)

hanoi(5, "A", "B", "C")