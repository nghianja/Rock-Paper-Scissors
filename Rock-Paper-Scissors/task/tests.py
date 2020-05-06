from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class RPSTest(StageTest):
    def generate(self) -> List[TestCase]:
        self.options = ["rock", "paper", "scissors"]
        cases = ["rock\npaper\npaper\nscissors\nblabla\n!exit",
                 "rock\ninvalid\n!exit",
                 "rock\nrock\nrock\nrock\n!exit"] * 10
        return [TestCase(stdin=case, attach=case) for case in cases]

    def check(self, reply: str, attach) -> CheckResult:

        reply = reply.split("\n")[:-1]
        reply = [rep for rep in reply if len(rep.strip()) != 0]

        attaches = attach.split('\n')[:-1]

        if len(reply) == 0:
            return CheckResult.wrong(
                "Looks like you didn't output anything!"
            )

        for reply_part, attach_part in zip(reply, attaches):
            try:
                if "Sorry" in reply_part:
                    result = -1
                    option = reply_part.split()[-1]
                elif "draw" in reply_part:
                    result = 0
                    if '(' not in reply_part or ')' not in reply_part:
                        return CheckResult.wrong(
                            "There are no '(' or ')' character when there is a draw"
                        )
                    start = reply_part.index('(')
                    end = reply_part.index(')')
                    option = reply_part[start + 1: end]
                elif "Well" in reply_part:
                    result = 1
                    option = reply_part.split()[-3]
                elif "Invalid input" in reply_part:
                    result = 2
                    if attach_part in self.options:
                        return CheckResult.wrong(
                            'Looks like you output "Invalid input" '
                            'in the wrong place'
                        )
                else:
                    raise IndexError

                if attach_part not in ['!exit'] + self.options:
                    if result == 2:
                        res = True
                    else:
                        return CheckResult.wrong(
                            "Looks like you didn't handle an invalid input correctly"
                        )
                else:
                    res = self.solve(
                        result,
                        attach_part.strip(),
                        option.strip()
                    )

                if res is False:
                    return CheckResult.wrong(
                        "You chose " + attach_part + ", "
                        "computer chose " + option + '. '
                        'And the answer was \"' + reply_part + '\". '
                        'That\'s wrong reply'
                    )
                if res < 0:
                    raise IndexError
            except IndexError:
                return CheckResult.wrong(
                    "Seems like your answer (\"{}\") "
                    "does not fit in given templates".format(reply_part))
        return CheckResult.correct()

    def solve(self, result, *options):
        if any(opt not in self.options for opt in options):
            return -1
        diff = self.options.index(options[0]) - self.options.index(options[1])
        if not diff:
            true_result = 0
        else:
            true_result = (-1) ** ((abs(diff) - (len(self.options) // 2) > 0) == (diff > 0))
        return true_result == result


if __name__ == '__main__':
    RPSTest("rps.game").run_tests()
