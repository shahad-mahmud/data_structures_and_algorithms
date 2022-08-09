def tower_of_hanoi(source, destination, extra, n_disks):
    if n_disks <= 0: return
    
    tower_of_hanoi(source, extra, destination, n_disks-1)
    print(f"Move disk {n_disks} from {source} to {destination}")
    tower_of_hanoi(extra, destination, source, n_disks-1)

if __name__ == "__main__":
    tower_of_hanoi('s', 'd', 'e', 4)