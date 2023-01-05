def merge_sort(lst):
  # Si la liste ne contient qu'un élément, elle est déjà triée
  if len(lst) <= 1:
    return lst
  
  # Détermine le milieu de la liste
  mid = len(lst) // 2

  # Tri la première moitié de la liste
  left = merge_sort(lst[:mid])

  # Tri la seconde moitié de la liste
  right = merge_sort(lst[mid:])

  # Fusionne les deux moitiés triées
  return merge(left, right)

def merge(left, right):
  # Initialise la liste qui contiendra les éléments fusionnés
  merged = []
  # Initialise les indices des éléments à comparer dans chaque liste
  left_index = 0
  right_index = 0
  # Tant que les deux listes ne sont pas vides, compare les éléments et ajoute le plus petit à la liste fusionnée
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    else:
      merged.append(right[right_index])
      right_index += 1
  # Ajoute les éléments restants de la liste la plus longue à la liste fusionnée
  merged.extend(left[left_index:])
  merged.extend(right[right_index:])
  return merged

# Exemple d'utilisation
print(merge_sort([4, 3, 2, 1])) # [1, 2, 3, 4]
