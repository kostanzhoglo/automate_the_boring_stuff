dnd_races = ["human", "elf", "dwarf", "Gnome", "halfling", "half-orc", "half-elf", "tiefling"]

# note: LIST METHODS return NONE.  so don't assign value to a new variable using any of these.
    # instead they mutate your original variable.  it WILL be changed!

# what index position is 'x' at?  use .index()
print(dnd_races)
print(dnd_races.index("Gnome"))

# add a new value to the END of a list with .append()
dnd_races.append("celestial")
print(dnd_races)

# add a new value to a list in ANY position you like with .insert()
dnd_races.insert(-1, "dragonborn")
print(dnd_races)

# APPEND and INSERT mutate the original variable.


# delete an item from a list with .remove()
    # will only remove 1st instance of value found (in case there are multiple occurrences)
dnd_races.remove("celestial")
print(dnd_races)

    # or use DEL() statement.  This is not a list METHOD, but it works on lists.
    # you could use to del an index position, or an entire list.
del dnd_races[-1]
print(dnd_races)

# sort alphabetically
dnd_races.sort()
print(dnd_races)
# sort in reverse
dnd_races.sort(reverse=True)
print(dnd_races)

# sort correctly for both Capitalized and lower-case words
dnd_races.sort(key=str.lower)
print(dnd_races)

# reverse a list with .reverse()
dnd_races.reverse()
print(dnd_races)

