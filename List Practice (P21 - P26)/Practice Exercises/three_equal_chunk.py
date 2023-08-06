import math

# Three Equal Chunks

# Given a list slice it into Three Equal Chunks
# and reverse each chunk.

# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

# Output:
# Chunk-1 = [18, 55, 21]
# Chunk-2 = [22, 24, 33]
# Chunk-3 = [79, 35, 68]

# check list length
sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

def reverse_chunk(p_list):
    length = len(p_list)
    if len(p_list) < 3:
        quit
    else: 
        chunk_size = int(length / 3)
        start = 0
        end = chunk_size
        for i in range(1, 4):
            new_chunk = p_list[start : end]
            rev_chunk = list(reversed(new_chunk))
            print(f'Chunk-{i} = {rev_chunk} ')
            start = end
            end += chunk_size
            
reverse_chunk(sample_list)
        
        