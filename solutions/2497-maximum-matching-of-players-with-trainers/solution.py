class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        # if I can sort these input, it's pretty easy:
            # 1) initiate two pointers, one at trainers[0] and one at players[0]
            # 2) hold a pointer each - t, p - at the next position at trainers and players
            # 3) increment t until t_j such that t_j >= p_k
            # 4) assign t_j to p_k -> i.e. k ++, numMatches ++
            # 5) repeat step 3)

        if not players:
            return 0
        if not trainers:
            return 0

        sorted_trainers = sorted(trainers)
        sorted_players = sorted(players)

        t, p = 0, 0

        t_n = len(trainers)
        p_n = len(players)

        num_matches = 0

        while t < t_n and p < p_n:
            if sorted_trainers[t] >= sorted_players[p]:
                # match player p with trainer t and increment num matches
                num_matches += 1
                p += 1
            # always move to the next trainer
            t += 1
        return num_matches


        
