from tkinter.messagebox import RETRY


def lbs_to_kgs(weight):
    return weight * 0.45

def kgs_to_lbs(weight):
    return weight / 0.45

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number> max:
            max = number
    return max

