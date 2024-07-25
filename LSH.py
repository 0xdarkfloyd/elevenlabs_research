import numpy as np

# Define the feature vectors
mimosa_stable_features = np.array([36.53258, 286.47055, 0.006881430642110973, 0.10962254489555823, 0.23388442, 1.1635059, 2111.375471239768, 1245.6204469669924, 1940.907835711859, 625.6070902853011, 0.6346163611970942, 4.095271054585651])
mimosa_variable_features = np.array([107.666015625, 0.0, 0.035560157, 0.023899402, 22.27156976318561, 12.17001492882612, 3827.7638095609095, 2300.3757454273295, 111518])

jacky_stable_features = np.array([17.879423, 180.54068, -0.0032661926663031656, 0.11338307019748853, 0.56253284, 2.8386395, 2167.783986424077, 1490.7466958581986, 1963.9484483029048, 650.7770598958132, -0.71328553026434, 3.538731521979879])
jacky_variable_features = np.array([123.046875, 0.0, 0.08746687, 0.05713356, 23.80613517804654, 12.556464310543193, 3944.874079451224, 2445.8176474432753, 123775])

# Define the hash function
def hash_function(x, p, m):
    return ((x * p) % m) // (m // 2)

# Define the LSH function
def lsh(feature_vector, p, m, num_hashes):
    hash_values = []
    for i in range(num_hashes):
        p_i = p[i]
        hash_value = 0
        for j in range(len(feature_vector)):
            hash_value += hash_function(feature_vector[j], p_i, m)
        hash_values.append(hash_value)
    return tuple(hash_values)

# Parameters for LSH
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Random projection vectors
m = 100  # Hash range
num_hashes = 3  # Number of hash functions

# Calculate LSH for stable features
mimosa_stable_lsh = lsh(mimosa_stable_features, p, m, num_hashes)
jacky_stable_lsh = lsh(jacky_stable_features, p, m, num_hashes)

# Calculate LSH for variable features
mimosa_variable_lsh = lsh(mimosa_variable_features, p, m, num_hashes)
jacky_variable_lsh = lsh(jacky_variable_features, p, m, num_hashes)

# Print the results
print("Mimosa Stable Features LSH:", mimosa_stable_lsh)
print("Jacky Stable Features LSH:", jacky_stable_lsh)
print("Mimosa Variable Features LSH:", mimosa_variable_lsh)
print("Jacky Variable Features LSH:", jacky_variable_lsh)