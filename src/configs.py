
import src.account as account

def write_configs(server, channel='', hidden=''):
    for serv in account.serv_list:
        if serv.name == server:
            if channel == 'all':
                serv.channel_id = channel
            elif channel != '':
                serv.channel_id = int(channel)
            if hidden != '':
                serv.ephemeral = int(hidden)
    account.write_serv_file()

    return
    with open('servers/'+server+'.csv', 'r') as f:
        for line in f:
            if line.startswith('allowed_channel'):
                if channel == '':
                    channel = line.split(' ')[1].strip()
            elif line.startswith('ephemeral'):
                if hidden == '':
                    hidden = line.split(' ')[1].strip()

    with open('servers/'+server+'.csv', 'w') as f:
        f.write('CONFIGS\n')
        f.write(f'allowed_channel: {channel}\n')
        f.write(f'ephemeral: {hidden}\n')
        f.write('%\n')

def get_config(server, config):
    if config == 'prefix':
        return '/'
    for serv in account.serv_list:
        if serv.name == server:
            if config == 'channel':
                return serv.channel_id
            elif config == 'ephemeral':
                return int(serv.ephemeral)
    return
    with open('servers/'+server+'.csv', 'r') as f:
        for line in f:
            if line.startswith(config):
                data = line.split(' ')[1].strip()
                if data.isdigit():
                    data = int(data)
                return data