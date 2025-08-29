# set em python 
# não recupera valores por slice  print(my_set[:2]) 

my_set = {"Roberto", "Dev", "Flask", "Javascript", "Dev"}
# valores duplicados são ignorados

print(my_set)      # Saída: {'Dev', 'Flask', 'Roberto', 'Javascript'}
print(len(my_set)) # resultará em 4

other_set = {"C++", "Linux", "Rust"}

my_set.update(other_set) # traz valores de outro set 

print(my_set) # Saída: {'Roberto', 'Dev', 'Linux', 'Rust', 'Javascript', 'Flask', 'C++'}

my_set.remove("Javascript") # remove o valor




