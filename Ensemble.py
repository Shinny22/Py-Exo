# Définition des ensembles X et Y
X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}

# Affichage des ensembles initiaux
print("Ensemble X:", X)
print("Ensemble Y:", Y)

# Test d'appartenance de l'élément 'c' à l'ensemble X
print("'c' appartient à X:", 'c' in X)

# Test d'appartenance de l'élément 'a' à l'ensemble Y
print("'a' appartient à Y:", 'a' in Y)

# Calcul des ensembles X - Y et Y - X
difference_X_Y = X - Y
difference_Y_X = Y - X
print("X - Y:", difference_X_Y)
print("Y - X:", difference_Y_X)

# Calcul de l'union des ensembles X et Y
union_X_Y = X.union(Y)
print("Union de X et Y:", union_X_Y)

# Calcul de l'intersection des ensembles X et Y
intersection_X_Y = X.intersection(Y)
print("Intersection de X et Y:", intersection_X_Y)
