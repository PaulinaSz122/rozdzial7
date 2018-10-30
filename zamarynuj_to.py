import pickle, shelve

print("Marynowanie list.")
variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdłuż", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortmnus"]

f = open("pickle.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nOdmarynowanie list.")
f = open("pickle.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("\nOdkładanie list na półkę.")
s = shelve.open("pickle2.dat")
s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
s["marka"] = ["Dawtona", "Klimex", "Vortmnus"]

s.sync()

print("\nPobieranie list z pliku półki:")
print("marka -", s["marka"])
print("kształt -", s["kształt"])
print("odmiana -", s["odmiana"])
s.close()
