class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        scores = []
        for item in operations:
            
            if item == '+':
                score_sum = scores[-1] + scores[-2]
                scores.append(score_sum)
            elif item == 'D':
                dscore = 2 * scores[-1]
                scores.append(dscore)
            elif item == 'C':
                scores.pop()
            else:
                scores.append(int(item))
            
        
        return sum(scores)
