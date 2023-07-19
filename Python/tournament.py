from enum import Enum
from typing import List, Dict


FORMAT_STR = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"


class Team:
    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.matches_played = 0
        self.won = 0
        self.lost = 0
        self.draws = 0
        self.points = 0

    def played_with_result(self, match_result: str) -> None:
        self.matches_played += 1
        if match_result == "win":
            self.won += 1
            self.points += 3
        elif match_result == "loss":
            self.lost += 1
        else:
            self.draws += 1
            self.points += 1

    def to_str(self) -> str:
        r = FORMAT_STR.format(
            self.team_name,
            str(self.matches_played),
            str(self.won),
            str(self.draws),
            str(self.lost),
            str(self.points))
        return r


def tally(rows) -> List[str]:
    match_results = [tuple(r.split(";")) for r in rows]

    teams_dict: Dict[str, Team] = {}
    # process the match results.
    for t1, t2, result in match_results:
        team1 = teams_dict.get(t1, Team(t1))
        team1.played_with_result(result)
        teams_dict[t1] = team1

        team2 = teams_dict.get(t2, Team(t2))
        team2.played_with_result(get_opposite_result(result))
        teams_dict[t2] = team2

    teams_list: List[Team] = list(teams_dict.values())
    # sort by names (secondary)
    teams_list.sort(key=lambda t: t.team_name)
    # sort by scores, descending.
    teams_list.sort(key=lambda t: t.points, reverse=True)

    result = build_table_str(teams_list)
    return result


def build_table_str(teams: List[Team]) -> List[str]:
    table: List[str] = [team.to_str() for team in teams]

    header = FORMAT_STR.format("Team", "MP", "W", "D", "L", "P")
    table.insert(0, header)
    return table


def get_opposite_result(match_result: str) -> str:
    if match_result == "win":
        return "loss"
    elif match_result == "loss":
        return "win"
    else:
        return "draw"
