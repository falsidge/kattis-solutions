import sys
print("\n".join(str(abs(int.__sub__(*map(int,i.split())))) for i in sys.stdin))