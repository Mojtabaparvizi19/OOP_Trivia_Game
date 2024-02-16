# Todo Type hint data


age : int
height : float
can_drive :  bool


def can_drive(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False


x = can_drive(9)
print(x)
