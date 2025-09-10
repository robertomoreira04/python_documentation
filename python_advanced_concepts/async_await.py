# funções assincronas em python 

import asyncio 

async def sum(a, b):
    return a + b

async def print_sum(a, b):
    result = await sum(a, b)
    print(f'Resultado é igual a {result}')

asyncio.run(print_sum(20, 40)) 


