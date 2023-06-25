records_NYU = [
    ["a.root-servers.net", "198.41.0.4", "A"],
    ["nyu.edu", "dns.nyu.edu", "NS"],
]

records_Root = [
    ["com", "114.514.000.1", "A"],
    ["org", "114.514.000.2", "A"],
    ["edu", "114.514.000.3", "A"]
]

records_Edu = [
    ["nyu.edu", "dns.nyu.edu", "NS"],
    ["umass.edu", "dns.umass.edu", "NS"],
    ["dns.nyu.edu", "114.514.001.1", "A"],
    ["dns.umass.edu", "114.514.001.2", "A"]
]

records_UMASS = [
    ["gaia.cs.umass.edu", "114.514.010.1", "A"],
    ["cs.umass.edu", "114.514.010.2", "A"],
    ["mai.umass.edu", "114.514.010.3", "A"]
]


def query(server, name):
    if server == "Root":
        i = 1
        records = records_Root
    if server == "Edu":
        i = 2
        records = records_Edu
    if server == "UMASS":
        records = records_UMASS
    else:
        i = 0
    # target = name.rsplit(".", i)[-1]
    parts = name.rsplit(".", i)
    target = parts[-1] if len(parts) >= i+1 else name
    print(target)
    result = ""
    for record in records:
        if record[0] == target:
            result = record[1]
            break
    return result


domain = input("Input domain to resolve: ")
print(query("Root", domain))
