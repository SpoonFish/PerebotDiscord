import consts
import account
import funcs.formulas as formulas
import funcs.checks as checks
import random
import math
import funcs.getter as getter

async def rest(message, acc, pre, hide):
        if acc.aurum < 25:
            await message.respond(f'You do not have enough aurum to rest! You need 25 aurum', ephemeral=hide)
            return
        acc.aurum -= 25
        acc.hp = acc.total_stats["HP"]
        acc.mp = acc.total_stats["MP"]
        await message.respond(f'You rested for 25 aurum and regained all your hp and mp', ephemeral=hide)
        account.write_file()

async def gamble(message, amount, acc, pre, hide):

        if amount == '¤':
            await message.respond(f'You need to specify an amount to gamble', ephemeral=hide)
            return
        if amount < 1:
            await message.respond(f'You need to specify an amount to gamble above 0', ephemeral=hide)
            return
        elif amount > acc.aurum:
            await message.respond(f'You do not have enough aurum to gamble that much. You only have **{acc.aurum}** aurum', ephemeral=hide)
            return
        elif amount > 1000:
            await message.respond(f'Maximum amount to gamble is 1000 aurum', ephemeral=hide)
            return
        if random.randint(1, 100) <= 45:
            acc.aurum += amount
            await message.respond(f'You gambled {amount} aurum and won **{amount}** aurum! You now have **{acc.aurum}** aurum', ephemeral=hide)
        else:
            acc.aurum -= amount
            await message.respond(f'You gambled {amount} aurum and lost it. You now have **{acc.aurum}** aurum', ephemeral=hide)
        account.write_file()

