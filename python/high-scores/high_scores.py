from typing import List


def latest(scores: List[int]):
    """
    :param scores:An integer list of scores.
    :return: The last added score to the list, where last is the end of the list.
    """
    assert_exists_scores(scores)

    return scores[-1]


def personal_best(scores: List[int]):
    """
    :param scores: An integer list of scores.
    :return: This method returns the top three scores from a player. If three scores aren't available then and exception
    is raised
    """
    assert_exists_scores(scores)

    print(scores)
    scores.sort(reverse=True)
    print(scores)
    return scores[0]


def personal_top_three(scores: List[int]):
    """
    :param scores: An integer list of scores.
    :return: This method returns the top three scores from a player. If three scores aren't available then and exception
    is raised
    """
    assert_exists_scores(scores)

    if len(scores) < 3:
        scores

    scores.sort(reverse=True)
    return scores[:3]


def assert_exists_scores(scores: List[int]):
    """
    This method checks the there is 1 or more score in the list.
    :param scores: An integer list of scores.
    :return: If there are some scores this function returns. If there aren't any scores this function raises an
    exception.
    """
    if not len(scores):
        raise Exception("No scores available")
