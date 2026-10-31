
class Solution(object):
    def findWinners(self, matches):
        # the first one is the winner
        # the second is the loser
        # if the players have zero losses, put them first
        # if the players have one loss, put them second
        # sort from smallest to greatest
        # if the losses are above 1, remove them

        losses = {}
        players = set()
        onelosses = []
        zerolosses = []

        for match in matches:
            winer = match[0]
            loser = match[1]

            players.add(winer)
            players.add(loser)

            if loser in losses:
                losses[loser] = losses[loser] + 1
            else:
                losses[loser] = 1

        for player in players:
            if player not in losses:
                zerolosses.append(player)
            elif losses[player] == 1:
                onelosses.append(player)

        onelosses.sort()
        zerolosses.sort()

        return [zerolosses, onelosses]
