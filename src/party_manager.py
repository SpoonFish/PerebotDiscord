

class Member():
    def __init__(self, name: str, ptype: int) -> None:
        self.name = name
        self.ptype = ptype

class Party():
    def __init__(self, leader: str = '', members: list[Member] = list[None,None,None], size: int = 0, in_battle: bool = False, waiting_on: list = [0,0,0], guild=None, channel=None) -> None:
        self.guild = guild
        self.channel = channel
        self.leader = leader
        self.members = members
        self.size = size#len(list(filter(lambda x: x != None, members)))
        self.in_battle = in_battle
        self.waiting_on = waiting_on

    def resize(self):
        self.size = 0
        for member in self.members:
            if member != None and member.ptype == 1:
                self.size += 1

def get_party(name, party_list):
    for party in party_list:
        for member in party.members:
            if member == None:
                continue
            elif member.name == name:
                return party



def initialize_file(file):
    party_list = []
    with open(file, 'r', encoding = "utf-8") as f:
        line = ' '
        while line != '':
            line = f.readline().replace('\n', '')
            if line != '':
                data = line.split(',')

                leader = data[0]

                fake_members = data[1].split('-')
                members = []
                for member in fake_members:
                    name = member[:-1]
                    if name == '':
                        members.append(None)
                        continue
                    ptype = int(member[-1])
                    members.append(Member(name, ptype))

                size = len(list(filter(lambda x: x != None, members)))

                in_battle = int(data[2])

                waiting_on = [int(x) for x in data[3].split('-')]

                party = Party(leader, members, size, in_battle, waiting_on)
                party_list.append(party)
    return party_list

party_list = initialize_file('assets/parties.csv')
            
def write_file(party_list = party_list):
    with open('assets/parties.csv', 'w', encoding = "utf-8") as f:
        for party in party_list:
            if party.in_battle == 0:
                party.resize()
            string = ''
            members = ''
            for member in party.members:
                if member == None:
                    members += '0-'
                else:
                    members += f'{member.name}{member.ptype}-'
            members = members[:-1]
            waitings = '-'.join([str(x) for x in party.waiting_on])
            string += f'{party.leader},{members},{int(party.in_battle)},{waitings}\n'
            print(string)
            f.write(string)

write_file(party_list)