
while True:
  print("""Which program do you want to run?
   1) Class code
   2) Mr. McGowan's code
   3) 
   """)
  run_this = input()
  if run_this=='1':
    exec(open("./prgrm1_class.py").read())
    break
  elif run_this=='2':
    exec(open("./prgrm2_mrM.py").read())
    break
  elif run_this=='3':
    exec(open("./prgrm4_vallat.py").read())
    break
  else:
    print("Please enter a valid response")
    continue