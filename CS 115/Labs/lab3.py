'''I pledge my honor that I have abided by the Stevens Honor System. - Jonathan Joshua'''

def change(amount, coins):
    """Given an amount of money and a list of coin types (coinSystem), return the least number of coins that makes up that amount of money"""
    if amount == 0:
        return 0
    if coins == [] or amount < 0:
        return float("inf")
    useit = 1 + change(amount - coins[0], coins)
    loseit = change(amount, coins[1:])
    return min(useit, float("inf") if loseit == 0 else loseit)
