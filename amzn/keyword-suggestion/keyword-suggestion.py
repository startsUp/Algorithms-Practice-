 def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort the products to ensure lexicographic order when adding to output
		products.sort()
        out = []
        for i in range(len(searchWord)):
            # filter products to those that match the search word in the ith character.
			# by doing this, we ensure that at each step, we know that remaining
			# products match up to char i - 1
			products = [prod for prod in products if i < len(prod) and prod[i] == searchWord[i]]
            # add the first three matches (these will be in lexicographical order because of the initial sort
			out.append(products[:3])
        return out