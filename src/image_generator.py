
import consts
import pygame
import discord
import time
import os
import account
import party_manager
import pvp_manager
scale = 4
pygame.init()

font = pygame.font.Font('assets/images/font.ttf', 10)

class Mon():
    def __init__(self, mon, hp, mult = 1):
        self.name = mon.name
        self.hp = hp
        self.max_hp = round(mult*consts.mob_stats[mon.name]['HP'])
        if mon.name == ' ': self.name = 'NONE'
        if self.hp < 1 and self.name != 'NONE': self.name += '_dead'
    
def generate_battle(acc, user:discord.User, spell):
    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        hp_mult = 1
    else:
        hp_mult = (party.size-1)*0.4 +1
    spell_pos = 0
    if spell != 0:
        spell
        img_spell = pygame.image.load('assets/images/spells/'+spell.name.replace(' ','_')+'.png')
        spell_pos = acc.target
        if spell.target == 'player':
            spell_pos = 4
        elif spell.target == 'multi':
            spell_pos = 5
    
    mon1 = Mon(acc.battle.enemy[0], acc.battle.e_hp[0], hp_mult)
    mon2 = Mon(acc.battle.enemy[1], acc.battle.e_hp[1], hp_mult)
    mon3 = Mon(acc.battle.enemy[2], acc.battle.e_hp[2], hp_mult)

    img1 = pygame.image.load('assets/images/mobs/'+mon1.name.replace(' ','_').replace('(','').replace(')','')+'.png')
    img2 = pygame.image.load('assets/images/mobs/'+mon2.name.replace(' ','_').replace('(','').replace(')','')+'.png')    
    img3 = pygame.image.load('assets/images/mobs/'+mon3.name.replace(' ','_').replace('(','').replace(')','')+'.png')

    hps = []
    for i, hp in enumerate(acc.battle.e_hp):
        surf = pygame.Surface((20*scale, 3*scale))
        if acc.battle.enemy[i].name != ' ':
            surf.fill((0,0,0))
            try:
                hp_percent = hp/round(hp_mult*consts.mob_stats[acc.battle.enemy[i].name]['HP'])
                if hp_percent == 0:
                    width = 0
                else:
                    width = max(1,round(18*hp_percent))

                green = 230*hp_percent
                red = 255-green

                pygame.draw.rect(surf, (red//5,green//5,25), (scale, scale, 18*scale, scale))
                pygame.draw.rect(surf, (red,green,25), (scale, scale, width*scale, scale))
            except:
                try:
                    hp_percent = hp/round(1.4*consts.mob_stats[acc.battle.enemy[i].name]['HP'])
                    if hp_percent == 0:
                        width = 0
                    else:
                        width = max(1,round(18*hp_percent))

                    green = 230*hp_percent
                    red = 255-green

                    pygame.draw.rect(surf, (red//5,green//5,25), (scale, scale, 18*scale, scale))
                    pygame.draw.rect(surf, (red,green,25), (scale, scale, width*scale, scale))
                except:
                    try:
                        hp_percent = hp/round(1.8*consts.mob_stats[acc.battle.enemy[i].name]['HP'])
                        if hp_percent == 0:
                            width = 0
                        else:
                            width = max(1,round(18*hp_percent))

                        green = 230*hp_percent
                        red = 255-green

                        pygame.draw.rect(surf, (red//5,green//5,25), (scale, scale, 18*scale, scale))
                        pygame.draw.rect(surf, (red,green,25), (scale, scale, width*scale, scale))
                    except: pass
        else:
            surf.set_alpha(0)
        hps.append(surf)




    #background.fill((255,25,52))

    boss = 0
    for i in acc.battle.enemy:
        match i.name:
            case 'alpha wolf':
                boss = 1
                background = pygame.image.load('assets/images/areas/alpha_wolf_boss.png')
            case 'alpha wolf (hard)':
                boss = 1
                background = pygame.image.load('assets/images/areas/alpha_wolf_boss.png')
            case 'alpha wolf (extreme)':
                boss = 1
                background = pygame.image.load('assets/images/areas/alpha_wolf_boss.png')


            case 'king polypus':
                boss = 1
                background = pygame.image.load('assets/images/areas/king_polypus_boss.png')
            case 'king polypus (hard)':
                boss = 1
                background = pygame.image.load('assets/images/areas/king_polypus_boss.png')
            case 'king polypus (extreme)':
                boss = 1
                background = pygame.image.load('assets/images/areas/king_polypus_boss.png')
            case 'visius ent':
                boss = 1
                background = pygame.image.load('assets/images/areas/visius_ent_boss.png')
            case 'visius ent (hard)':
                boss = 1
                background = pygame.image.load('assets/images/areas/visius_ent_boss.png')
            case 'visius ent (extreme)':
                boss = 1
                background = pygame.image.load('assets/images/areas/visius_ent_boss.png')
                
    player_hp = pygame.Surface((75*scale, 7*scale))
    player_hp.fill((0,0,0))
    hp_percent = acc.hp/acc.total_stats['HP']
    if hp_percent == 0:
        width = 0
    else:
        width = max(1,round(73*hp_percent))

    green = min(255,230*hp_percent)
    red = 255-green

    pygame.draw.rect(player_hp, (red//5,green//5,25), (scale, scale, 73*scale, 5*scale))
    pygame.draw.rect(player_hp, (red,green,25), (scale, scale, width*scale, 5*scale))

    player_mp = pygame.Surface((75*scale, 7*scale))
    player_mp.fill((0,0,0))
    mp_percent = acc.mp/acc.total_stats['MP']
    if mp_percent == 0:
        width = 0
    else:
        width = max(1,round(73*mp_percent))

    blue = min(255,(230*(mp_percent)+230)//2)
    label = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('assets/images/label.png')))

    pygame.draw.rect(player_mp, (25,25,blue//5), (scale, scale, 73*scale, 5*scale))
    pygame.draw.rect(player_mp, (25,25,blue), (scale, scale, width*scale, 5*scale))
    if not boss:
        surf = pygame.Surface((100*scale, 70*scale))
        surf.fill((40,40,40))
        surf.blit(label, (3*scale,50*scale))
        surf.blit(player_hp, (20*scale,52*scale))
        surf.blit(player_mp, (20*scale,61*scale))
        background = pygame.image.load('assets/images/areas/'+acc.area.lower().replace(' ','_').replace('\'','')+'.png')
        background.blit(hps[0], (10*scale, 16*scale))
        background.blit(img1, (10*scale, 20*scale))
        if spell_pos == 1 or spell_pos == 5:
            background.blit(img_spell, (10*scale, 20*scale))

        background.blit(hps[1], (40*scale, 6*scale))
        background.blit(img2, (40*scale, 10*scale))
        if spell_pos == 2 or spell_pos == 5:
            background.blit(img_spell, (40*scale, 10*scale))
        if spell_pos == 4:
            background.blit(img_spell, (40*scale, 30*scale))

        background.blit(hps[2], (70*scale, 16*scale))
        background.blit(img3, (70*scale, 20*scale))
        if spell_pos == 3 or spell_pos == 5:
            background.blit(img_spell, (70*scale, 20*scale))

        surf.blit(background,(0,0))
        surf = pygame.transform.scale(surf, (300*scale, 225*scale))
    else:
        surf = pygame.Surface((120*scale, 90*scale))
        surf.fill((40,40,40))
        surf.blit(player_hp, (20*scale,72*scale))
        surf.blit(player_mp, (20*scale,81*scale))
        surf.blit(label, (3*scale,70*scale))
        background.blit(hps[0], (10*scale, 26*scale))
        background.blit(img1, (10*scale, 30*scale))
        if spell_pos == 1 or spell_pos == 5:
            background.blit(img_spell, (10*scale, 30*scale))
        background.blit(hps[1], (50*scale, 6*scale))
        background.blit(img2, (40*scale, 10*scale))
        if spell_pos == 2 or spell_pos == 5:
            background.blit(img_spell, (50*scale, 20*scale))
        if spell_pos == 4:
            background.blit(img_spell, (50*scale, 50*scale))
        background.blit(hps[2], (90*scale, 26*scale))
        background.blit(img3, (90*scale, 30*scale))
        if spell_pos == 3 or spell_pos == 5:
            background.blit(img_spell, (90*scale, 30*scale))
        surf.blit(background,(0,0))
        #surf = pygame.transform.scale(surf, (360*scale, 285*scale))




    #os.remove('assets/images/battle.png')
    try:
        pygame.image.save(surf, 'assets/images/battle.png')
        file =  discord.File('assets/images/battle.png', "image.png")
    except:
        try:
            pygame.image.save(surf, 'assets/images/battle2.png')
            file =  discord.File('assets/images/battle2.png', "image.png")
        except:
            file =  discord.File('assets/images/error.png', "image.png")
    return file

    #io_object = io.BytesIO()
    #pygame.image.save(background, io_object, "PNG")
    #io_object.seek(0)
    #await channel.send(file=discord.File(io_object, 'my_file.png'))

def generate_pvp(acc, user:discord.User, spell):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    spell_pos = 0
    if spell != 0:
        spell
        img_spell = pygame.image.load('assets/images/spells/'+spell.name.replace(' ','_')+'.png')
        spell_pos = acc.target
        if spell.target == 'player':
            spell_pos = 4
        elif spell.target == 'multi':
            spell_pos = 5
    if pvp.duelists[0].name != acc.name:
        opponent = account.get_account(pvp.duelists[0].name, 0)
    else:
        opponent = account.get_account(pvp.duelists[1].name, 0)

    if opponent.hp < 1:
        img = pygame.image.load('assets/images/mobs/player_dead.png')
        opponent.hp = 0
    else:
        img = pygame.image.load('assets/images/mobs/player.png')

    hp = opponent.hp
    surf = pygame.Surface((20*scale, 3*scale))
    surf.fill((0,0,0))
    hp_percent = hp/opponent.total_stats['HP']
    if hp_percent == 0:
        width = 0
    else:
        width = max(1,round(18*hp_percent))

    green = 230*hp_percent
    red = 255-green

    pygame.draw.rect(surf, (red//5,green//5,25), (scale, scale, 18*scale, scale))
    pygame.draw.rect(surf, (red,green,25), (scale, scale, width*scale, scale))
            
    hpx = surf




    #background.fill((255,25,52))

    player_hp = pygame.Surface((75*scale, 7*scale))
    player_hp.fill((0,0,0))
    hp_percent = acc.hp/acc.total_stats['HP']
    if hp_percent == 0:
        width = 0
    else:
        width = max(1,round(73*hp_percent))

    green = min(255,230*hp_percent)
    red = 255-green

    pygame.draw.rect(player_hp, (red//5,green//5,25), (scale, scale, 73*scale, 5*scale))
    pygame.draw.rect(player_hp, (red,green,25), (scale, scale, width*scale, 5*scale))

    player_mp = pygame.Surface((75*scale, 7*scale))
    player_mp.fill((0,0,0))
    mp_percent = acc.mp/acc.total_stats['MP']
    if mp_percent == 0:
        width = 0
    else:
        width = max(1,round(73*mp_percent))

    blue = min(255,(230*(mp_percent)+230)//2)
    label = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('assets/images/label.png')))

    pygame.draw.rect(player_mp, (25,25,blue//5), (scale, scale, 73*scale, 5*scale))
    pygame.draw.rect(player_mp, (25,25,blue), (scale, scale, width*scale, 5*scale))
    surf = pygame.Surface((100*scale, 70*scale))
    surf.fill((40,40,40))
    surf.blit(label, (3*scale,50*scale))
    surf.blit(player_hp, (20*scale,52*scale))
    surf.blit(player_mp, (20*scale,61*scale))
    background = pygame.image.load('assets/images/areas/'+acc.area.lower().replace(' ','_').replace('\'','')+'.png')

    background.blit(hpx, (40*scale, 6*scale))
    background.blit(img, (40*scale, 10*scale))
    if spell_pos == 2 or spell_pos == 5:
        background.blit(img_spell, (40*scale, 10*scale))
    if spell_pos == 4:
        background.blit(img_spell, (40*scale, 30*scale))
    surf.blit(background,(0,0))
    surf = pygame.transform.scale(surf, (300*scale, 225*scale))
    




    #os.remove('assets/images/battle.png')
    pygame.image.save(surf, 'assets/images/battle.png')

    file =  discord.File('assets/images/battle.png', "image.png")
    return file

    #io_object = io.BytesIO()
    #pygame.image.save(background, io_object, "PNG")
    #io_object.seek(0)
    #await channel.send(file=discord.File(io_object, 'my_file.png'))

def generate_area(area):

    file =  discord.File('assets/images/areas/'+area.lower().replace(' ','_').replace('\'','')+'_big.png', "image.png")
    return file

def generate_icon(monster):

    file =  discord.File('assets/images/mobs/'+monster.lower().replace(' ','_').replace('(','').replace(')','')+'.png', "image.png")
    return file

def generate_map(area):

    marker = pygame.image.load('assets/images/maps/location.png')
    location = (0,0)
    if area == 'Town 1':
        location = (68*4, 120*4)
    elif area == 'Apple Orchard':
        location = (44*4, 118*4)
    elif area == 'Forest Outskirts':
        location = (99*4, 100*4)
    elif area == 'Farm':
        location = (67*4, 84*4)
    elif area == 'Beach I':
        location = (27*4, 72*4)
    elif area == 'Beach II':
        location = (58*4, 13*4)
    elif area == 'Beach III':
        location = (95*4, 15*4)
    elif area == 'Boat 1':
        location = (125*4, 133*4)
    elif area == 'Forest I':
        location = (121*4, 97*4)
    elif area == 'Forest II':
        location = (98*4, 60*4)
    elif area == 'Forest III':
        location = (138*4, 70*4)
    elif area == 'Krakow\'s Cave':
        location = (21*4, 38*4)
    if location != (0,0):
        map = pygame.image.load('assets/images/maps/island1_overworld_map.png')
        map.blit(marker, location)

        pygame.image.save(map, 'assets/images/current_map.png')
        file =  discord.File('assets/images/current_map.png', "image.png")
        return file

    
    elif area == 'Wolf Den I':
        location = (98*4, 134*4)
    elif area == 'Wolf Den II':
        location = (99*4, 78*4)
    elif area == 'Wolf Den III':
        location = (58*4, 43*4)
    if location != (0,0):
        map = pygame.image.load('assets/images/maps/island1_underground_map.png')
        map.blit(marker, location)

        pygame.image.save(map, 'assets/images/current_map.png')
        file =  discord.File('assets/images/current_map.png', "image.png")
        return file