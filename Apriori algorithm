from collections import defaultdict

class Apriori:
    def __init__(self, min_support):
        self.min_support = min_support

    def _get_frequent_itemsets(self, transactions, candidate_itemsets):
        itemset_count = defaultdict(int)

        for transaction in transactions:
            for itemset in candidate_itemsets:
                if set(itemset).issubset(transaction):
                    itemset_count[tuple(itemset)] += 1

        return [itemset for itemset, count in itemset_count.items() if count >= self.min_support]

    def _generate_candidates(self, frequent_itemsets, k):
        candidates = []

        for i in range(len(frequent_itemsets)):
            for j in range(i + 1, len(frequent_itemsets)):
                # Merge two frequent itemsets if the first k-1 items are equal
                if frequent_itemsets[i][:k-1] == frequent_itemsets[j][:k-1]:
                    candidates.append(frequent_itemsets[i][:k-1] + [frequent_itemsets[j][k-1]])

        return candidates

    def fit(self, transactions):
        frequent_itemsets = []

        # Get unique items from transactions
        unique_items = set(item for transaction in transactions for item in transaction)

        # Generate frequent itemsets of size 1
        frequent_itemsets_1 = [[item] for item in unique_items]

        k = 2

        while frequent_itemsets_1:
            frequent_itemsets.extend(frequent_itemsets_1)
            candidate_itemsets = self._generate_candidates(frequent_itemsets_1, k)

            frequent_itemsets_1 = self._get_frequent_itemsets(transactions, candidate_itemsets)
            k += 1

        return frequent_itemsets

# Example usage:
transactions = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'egg'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola']
]

apriori = Apriori(min_support=2)
frequent_itemsets = apriori.fit(transactions)

print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)
