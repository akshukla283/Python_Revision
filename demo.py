import sys
print(sys.argv)
if len(sys.argv)>1:
    add = sum(args for i in sys.argv if args.isdigit())
    print(add)