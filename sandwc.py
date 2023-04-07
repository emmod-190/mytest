import time

print("Hallo!")
time.sleep(0.7)

print("Heute überlege ich, was ich schreiben soll...")
print("Aber ich glaube, ich habe ein wenig Hunger, ich werde zuerst ein Sandwich machen.")

sandwich_zutaten = ["Brot", "Käse", "Tomaten", "Mayonnaise", "Gurken", "Salat"]
time.sleep(1)

for zutat in sandwich_zutaten:
    time.sleep(0.4)
    print("Jetzt füge ich " + zutat + " hinzu.")
    
print("Mein Sandwich ist fertig!")
