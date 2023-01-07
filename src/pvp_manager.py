

class Duelist():
    def __init__(self, name: str, accepted: int) -> None:
        self.name = name
        self.accepted = accepted

class Pvp():
    def __init__(self, duelists, in_battle, turn, prize):
        self.duelists = duelists
        self.in_battle = in_battle
        self.turn = turn
        self.prize = prize


def get_pvp(name, pvp_list):
    for pvp in pvp_list:
        for duelist in pvp.duelists:
            if duelist == None:
                continue
            elif duelist.name == name:
                return pvp



def initialize_file(file):
    pvp_list = []
    with open(file, 'r', encoding = "utf-8") as f:
        line = ' '
        while line != '':
            line = f.readline().replace('\n', '')
            if line != '':
                data = line.split(',')

                duelists = data[0].split('-')
                accepted = data[1].split('-')
                in_battle = int(data[2])
                turn = int(data[3])
                prize = int(data[4])

                real_duelists = []
                for i, duelist in enumerate(duelists):
                    real_duelists.append(Duelist(duelist, int(accepted[i])))

                pvp = Pvp(real_duelists, in_battle, turn, prize)
                pvp_list.append(pvp)
    return pvp_list

pvp_list = initialize_file('assets/pvp.csv')
            
def write_file(pvp_list = pvp_list):
    with open('assets/pvp.csv', 'w', encoding = "utf-8") as f:
        for pvp in pvp_list:
            string = ''
            duelists = pvp.duelists[0].name +'-'+ pvp.duelists[1].name
            accepted = f"{pvp.duelists[0].accepted}-{pvp.duelists[1].accepted}"
            string += f'{duelists},{accepted},{pvp.in_battle},{pvp.turn},{pvp.prize}\n'
            print(string)
            f.write(string)

write_file(pvp_list)