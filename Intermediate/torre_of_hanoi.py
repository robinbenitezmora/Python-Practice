import copy
import sys

TOTAL_DISKS = 5
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    '''Tower of Hanoi game'''
    towers = [copy.deepcopy(COMPLETE_TOWER), [], []]
    print("Tower of Hanoi")
    print("Move the disks from the first tower to the last tower")
    print("Press ENTER to continue...")
    input()
    print_towers(towers)
    move_disks(towers, TOTAL_DISKS, 0, 2, 1)
    print("All disks moved!")

def print_towers(towers):
    '''Print the towers'''
    for level in range(TOTAL_DISKS - 1, -1, -1):
        for tower in towers:
            if level < len(tower):
                print(f"{'*' * tower[level]:^5}", end="")
            else:
                print("     ", end="")
        print()
    print("-----" * 3)

def move_disks(towers, disks, source, target, auxiliary):
    '''Move the disks'''
    if disks == 1:
        towers[target].append(towers[source].pop())
        print_towers(towers)
        return
    move_disks(towers, disks - 1, source, auxiliary, target)
    move_disks(towers, 1, source, target, auxiliary)
    move_disks(towers, disks - 1, auxiliary, target, source)

if __name__ == '__main__':
    main()