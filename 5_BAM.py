'''5. Write a python Program for Bidirectional Associative Memory with two pairs of vectors.
'''

import numpy as np

def train_BAM(pattern1, pattern2):
    pattern1_transpose = pattern1.T
    pattern2_transpose = pattern2.T
    weights = np.dot(pattern1_transpose, pattern2)
    return weights

def recall_forward(input_pattern, weights):
    recalled_pattern = np.sign(np.dot(input_pattern, weights))
    return recalled_pattern

def recall_backward(input_pattern, weights):
    recalled_pattern = np.sign(np.dot(input_pattern, weights.T))
    return recalled_pattern

# Define patterns
pattern1 = np.array([[1, 1, 1, -1, -1]])  # Pattern A
pattern2 = np.array([[-1, -1, -1, 1, 1]])  # Pattern B

# Train BAM model
weights = train_BAM(pattern1, pattern2)

# Recall forward
output_pattern1 = recall_forward(pattern1, weights)
print(f"Recalled Pattern 1 (Forward): {output_pattern1}")

# Recall backward
output_pattern2 = recall_backward(pattern2, weights)
print(f"Recalled Pattern 2 (Backward): {output_pattern2}")

'''
if asked for user inputs :

print("Enter your patterns (each pattern should be a row vector):")
patterns = []
while True:
    row = input("Enter pattern row (comma-separated values), or type 'done' to finish: ").strip()
    if row.lower() == 'done':
        break
    patterns.append(list(map(int, row.split(','))))
patterns = np.array(patterns)

# Train BAM model
pattern1 = patterns[0].reshape(1, -1)
pattern2 = patterns[1].reshape(1, -1)
weights = train_BAM(pattern1, pattern2)

# Recall forward
output_pattern1 = recall_forward(patterns, weights)
print(f"Recalled Patterns (Forward): {output_pattern1}")

# Recall backward
output_pattern2 = recall_backward(patterns, weights)
print(f"Recalled Patterns (Backward): {output_pattern2}")

'''

'''

example output to enter :

Enter your patterns (each pattern should be a row vector):
Enter pattern row (comma-separated values), or type 'done' to finish: 1, 1, 1, -1, -1
Enter pattern row (comma-separated values), or type 'done' to finish: -1, -1, -1, 1, 1
Enter pattern row (comma-separated values), or type 'done' to finish: -1, 1, -1, 1, -1
Enter pattern row (comma-separated values), or type 'done' to finish: done
Recalled Patterns (Forward): [[ 1.  1.  1. -1. -1.]
 [-1. -1. -1.  1.  1.]
 [-1.  1. -1.  1. -1.]]
Recalled Patterns (Backward): [[ 1. -1. -1.]
 [ 1. -1.  1.]
 [ 1. -1. -1.]
 [-1.  1.  1.]
 [-1.  1. -1.]]

'''
