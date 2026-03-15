from logic_utils import build_new_game_state, check_guess


def test_winning_guess():
    outcome, hint = check_guess(50, 50)
    assert outcome == "Win"
    assert hint == "🎉 Correct!"


def test_guess_too_high_hint_says_go_lower():
    outcome, hint = check_guess(60, 50)
    assert outcome == "Too High"
    assert hint == "📉 Go LOWER!"


def test_guess_too_low_hint_says_go_higher():
    outcome, hint = check_guess(40, 50)
    assert outcome == "Too Low"
    assert hint == "📈 Go HIGHER!"


def test_new_game_restarts_all_state_values():
    # Simulate the app's session state before user clicks "New Game".
    session_state = {
        "secret": 99,
        "attempts": 4,
        "score": 35,
        "status": "lost",
        "history": [12, 60, 45, 30],
        "range_low": 1,
        "range_high": 100,
    }

    # This mirrors reset_game_state() in app.py, where a fresh state payload
    # replaces all game values in session state.
    new_state = build_new_game_state(difficulty="Easy", secret=7)
    for key, value in new_state.items():
        session_state[key] = value

    assert session_state["secret"] == 7
    assert session_state["attempts"] == 0
    assert session_state["score"] == 0
    assert session_state["status"] == "playing"
    assert session_state["history"] == []
    assert session_state["range_low"] == 1
    assert session_state["range_high"] == 20
