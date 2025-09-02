# Módulo de criptografia usando hashlib
import hashlib

# Lista todos os algoritmos de hash suportados pelo Python + OpenSSL
print("Algoritmos disponíveis:", hashlib.algorithms_available)

# Lista apenas os algoritmos garantidos de existir em qualquer SO
print("Algoritmos garantidos:", hashlib.algorithms_guaranteed)

# Criando um objeto de hash SHA-256 (inicialmente vazio)
algorithm = hashlib.sha256()

# Hash do valor vazio (sem dados ainda)
print("SHA-256 de string vazia:", algorithm.hexdigest())

# Mensagem a ser codificada em bytes (necessário para hashing)
message = "Meu nome é Roberto, sou desenvolvedor de software.".encode()

# Atualizando o objeto SHA-256 com a mensagem
algorithm.update(message)

# Exibindo o hash SHA-256 da mensagem
print("SHA-256 da mensagem:", algorithm.hexdigest())

# Exemplo usando MD5 (apenas para fins de demonstração, inseguro em aplicações reais)
md5 = hashlib.md5()
md5.update(message)
print("MD5 da mensagem:", md5.hexdigest())



