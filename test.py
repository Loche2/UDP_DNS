target = input()
target = target.rsplit(".", 2)
target = target[-2] + '.' + target[-1]
print(target)
