
threat = 'We are going to eat all of your children and babies and high heels'

def disemvowel(string_):
    return ''.join([x if not x in 'aeiouAEIOU' else '' for x in string_])

print(disemvowel(threat))