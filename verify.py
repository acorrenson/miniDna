import os.path

needed = [
  "database.m.html",
  "simulation.m.html",
  "sequence.m.html",
  "utils.m.html",
]

print("--- Starting verification ---")

error = False

for i in range(len(needed)):
  print("| verifying file " + "\033[35m" + needed[i] + "\033[0m" + "..." )
  if os.path.exists("./docs/" + needed[i]):
    print("| done -> " + "\033[92m" + u'\u2713' + "\033[0m")
  else:
    print("| missing -> " + "\033[31m" + u'\u2717' + "\033[0m")
    error = True

if error:
  print("You need to add 'miniDna' module to your PYTHONPATH before generating the doc")
else:
  print("--- Verification ends successfully ---")