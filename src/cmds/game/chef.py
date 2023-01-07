import consts
import account
import funcs.formulas as formulas
import funcs.checks as checks
import random
import math
import funcs.getter as getter

async def recipes(message, page, acc, pre, hide):
        if page == '':
            page = 1
        else:
            try:
                page = int(page)
            except:
                await message.respond(f'{page} is not a valid page number', ephemeral=hide)
                return
        if page > 1:
            page = 1


        body = f'```\npage {page}/1\n\n'
        i = 0
        for item in consts.chef_recipes:
            if i < (page-1)*12:
                i += 1
                continue
            if i == 12+((page-1)*12):
                break
            desc = consts.items[item]['desc']
            cost_str = ''
            for cost in consts.chef_recipes[item]:
                cost_str += f'{cost[1]} {cost[0]}, '
            body += f'{item}\n - {desc}\n - {cost_str}\n\n'
            i += 1
        body += '\n```'
        print(body)
        await message.respond(body, ephemeral=hide)

async def cook(message, item, amount, acc, pre, hide):
        if item == '':
            await message.respond(f'You need to specify an item to craft from {pre}chef-recipes', ephemeral=hide)
            return  
        i = getter.get_inv(acc, item)
        valid = 1
        body = ''
        for cost in consts.chef_recipes[item]:
            aurum = 0
            if cost[0] == 'aurum':
                aurum = 1
            if aurum and int(cost[1]*amount) > acc.aurum:
                body += f'You do not have enough **{cost[0]}** to craft {amount} **{item}**\n'
                valid = 0
            
            elif getter.get_inv(acc, cost[0]) == None:
                if not aurum:
                    body += f'You do not have any **{cost[0]}** in your inventory\n'
                    valid = 0
            elif getter.get_inv(acc, cost[0]).amount < cost[1]*amount:
                if not aurum:
                    body += f'You do not have enough **{cost[0]}** to cook {amount} **{item}**\n'
                    valid = 0
        if valid == 0:
            body+=f'Use `{pre}chef-recipes` to see what you need\n'
            body+=f'Use `{pre}whatis <item name>` to see where to find a resource\n'
            await message.respond(body, ephemeral=hide)
            return
        for cost in consts.chef_recipes[item]:
            j = 0
            for i in acc.inventory:
                if i.name == cost[0]:
                    break
                j+=1
            if cost[0] != 'aurum': 
                acc.inventory[j].amount -= cost[1]*amount
                if acc.inventory[j].amount < 1:
                    acc.inventory.pop(j)
            else: acc.aurum -= cost[1]*amount
        account.give_item(item, amount, acc)
        account.write_file()
        await message.respond(f'You cooked {amount} **{item}**!', ephemeral=hide)