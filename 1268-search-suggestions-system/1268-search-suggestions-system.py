class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products, ans = sorted(products), []
    
        for i in range(1,len(searchWord)+1):
            res = [p for p in products if p[:i] == searchWord[:i]]
            ans.append(res[:3])

        return ans
        