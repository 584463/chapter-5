import pytest
import assignment

def test_check_age_21():
    assert assignment.check_age_21(21) is True
    assert assignment.check_age_21(20) is False
    assert assignment.check_age_21(22) is True

def test_check_grade_level():
    assert assignment.check_grade_level("9") is True
    assert assignment.check_grade_level("10") is True
    assert assignment.check_grade_level("11") is True
    assert assignment.check_grade_level("12") is True
    assert assignment.check_grade_level("8") is False
    assert assignment.check_grade_level("13") is False

def test_check_date_of_birth():
    import datetime
    current_year = datetime.datetime.now().year
    assert assignment.check_date_of_birth("2000") is True
    assert assignment.check_date_of_birth("1899") is False
    assert assignment.check_date_of_birth(str(current_year)) is True

def test_check_the_list_of_cars():
    assert assignment.ckeck_the_list_of_cars(["Toyota", "Honda", "Ford"]) is True
    assert assignment.ckeck_the_list_of_cars(["Toyota", "Honda"]) is False
    assert assignment.ckeck_the_list_of_cars(["Toyota", "Toyota", "Honda"]) is False

def test_check_if_you_can_drive():
    assert assignment.check_if_you_can_drive("yes") is True
    assert assignment.check_if_you_can_drive("no") is True
    assert assignment.check_if_you_can_drive("maybe") is False

def test_check_weather():
    assert assignment.check_weather("sunny") is True
    assert assignment.check_weather("rainy") is True
    assert assignment.check_weather("snowy") is True
    assert assignment.check_weather("wind") is True
    assert assignment.check_weather("stormy") is False

def test_check_if_you_can_play_game():
    # This test may vary as it generates random boolean
    result = assignment.check_if_you_can_play_game("game")
    assert result in ['You can play game', False]

def test_check_study_time_or_play_time():
    assert assignment.check_study_time_or_play_time("study") is True
    assert assignment.check_study_time_or_play_time("play") is True
    assert assignment.check_study_time_or_play_time("rest") is False

def test_make_the_input_store_in_variable():
    assert assignment.make_the_input_store_in_variable("Hello") == "Hello"
    assert assignment.make_the_input_store_in_variable("123") == 123
    assert assignment.make_the_input_store_in_variable("3.14") == 3.14

def test_check_if_the_number_is_even():
    assert assignment.check_if_the_number_is_even(2) is True
    assert assignment.check_if_the_number_is_even(3) is False
    assert assignment.check_if_the_number_is_even(0) is True
