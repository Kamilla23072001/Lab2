s = "Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог"
print(" ".join([x for x in s.split() if not x.startswith(("м", "М"))]))