from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_check_guess_too_high_returns_correct_outcome():
    outcome, _ = check_guess(75, 50)
    assert outcome == "Too High"


def test_check_guess_too_low_returns_correct_outcome():
    outcome, _ = check_guess(25, 50)
    assert outcome == "Too Low"