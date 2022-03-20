# asked by hudson river 
# check if combinations of basic operators between n, equates the value of x
# n=4 n=[2,5,2,7] x=24 -> true
# n=4 n=[8,8,8,8] x=24 -> false


class Solution:
    def make_target(self, cards, target):  # cards=n, target=x
        self.allcombos=[]
        # need all combinations of cards
        def permute(swap_index, curr_arr):
            if swap_index==len(cards):
                self.allcombos.append(curr_arr[:])
                return
            for index in range(swap_index, len(cards)):
                # swap
                self.swap(curr_arr, swap_index, index)
                permute(swap_index + 1, curr_arr)
                # swap back for the next branch
                self.swap(curr_arr, swap_index, index)

        # generate parenthesis placements
        def calculate(cards):
            if len(cards) <= 1:
                return cards
            else:
                values = set()
                for splitidx in range(1, len(cards)):
                    left=calculate(cards[:splitidx])
                    right=calculate(cards[splitidx:])
                    for lval in left:
                        for rval in right:
                            values.add(lval+rval)
                            values.add(lval+rval)
                            values.add(lval+rval)
                            if rval != 0:
                                values.add(lval/rval)
                    return values
        permute(0,cards)
        for combo in self.allcombos:
            for c in calculate(combo):
                if target - 0.01 < c < target + 0.01:
                    return True
        return False

        















