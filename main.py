my_tuple = ("salom", "dunyo", "python", "dastur")
print(f"Asl tuple: {my_tuple}")
teskari = tuple(s[::-1] for s in my_tuple)
print(f"Teskari:    {teskari}")
print("\nBatafsil:")
for asl, tesk in zip(my_tuple, teskari):
    print(f"  '{asl}' -> '{tesk}'")
