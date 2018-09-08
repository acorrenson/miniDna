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
  print("| verifying file " + needed[i] + "...")
  if os.path.exists("./docs/" + needed[i]):
    print("| done -> " + u'\u2713')
  else:
    print("| missing -> " + u'\u2717')
    error = True

if error:
  print("You need to add 'miniDna' module to your PYTHONPATH before generating the doc")