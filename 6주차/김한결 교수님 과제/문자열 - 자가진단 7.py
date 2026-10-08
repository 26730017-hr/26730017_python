h, m = map(int, input().split())

if h >= 12:
    ampm = "PM"
else:
    ampm = "AM"

if h >= 13:
    h -= 12

print(f"{h:02d} : {m:02d} {ampm}")
