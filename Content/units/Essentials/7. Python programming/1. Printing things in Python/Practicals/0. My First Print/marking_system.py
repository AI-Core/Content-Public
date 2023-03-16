def check_step_1(
    your_code: str,
) -> None:
    assert len(your_code) > 0, "Your code should contain something."
    assert "print" in your_code, "Your code should contain a print statement."
    assert "This print statement was created in Python" in your_code, \
        "Your print statement should contain the phrase 'This print statement was created in Python'."
    print("\033[92m\N{heavy check mark} Well done!")
