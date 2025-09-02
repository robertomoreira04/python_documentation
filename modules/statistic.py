import statistics

print(statistics.mean([3,2,3,8,9])) # retorna a média entre números 

print(statistics.median([1,2,3,8,9])) # retorna o número mediano 

print(statistics.median([1,2,3,7,8,9])) # se a lista for impar, soma os dois números centrais e retorna sua média 

print(statistics.mode([1,2,2,2,4,4,4])) # retorna o número que mais se repete, caso haja empate, retorna o primeiro valor mais frequente

print(statistics.multimode([1,2,2,2,4,4,4])) # retorna todos os números que mais se repetem, mesmo que seja mais de um

print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])) # calcula o desvio padrão da lista de números

