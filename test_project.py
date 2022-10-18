from project import prompt, parse, conversion
import pytest

def test_prompt():
    assert prompt() == ""

def test_parse():
    assert parse("10 USD to KRW") == {"currency": ["10", "usd", "krw"]}
    assert parse("10 c to f") == {"temperature": ["10", "c", "f"]}
    assert parse("10 lb to kg") == {"weight": ["10", "lb", "kg"]}
    assert parse("10 ft to in") == {"length": ["10", "ft", "in"]}
    assert parse("10 floz to ml") == {"volume": ["10", "floz", "ml"]}
    assert parse("10 mph to kmh") == {"speed": ["10", "mph", "kmh"]}
    assert parse("1.5 ft to in") == {"length": ["1.5", "ft", "in"]}
    with pytest.raises(ValueError):
        parse("10 USD to f")
    with pytest.raises(ValueError):
        parse("100lb to kg")


def test_conversion():
    #conversion on currency cannot be reliably tested since currency requires a request from an exchange rate API and the rate changes day to day
    assert conversion({"temperature": ["10", "c", "f"]}) == "10.0 C is 50 F"
    assert conversion({"weight": ["10", "lb", "kg"]}) == "10.0 lb is 4.54 kg"
    assert conversion({"volume": ["10", "floz", "ml"]}) == "10.0 floz is 295.74 ml"
    assert conversion({"speed": ["10", "mph", "kmh"]}) == "10.0 mph is 16.093 kmh"
    assert conversion({"length": ["1.5", "ft", "in"]}) == "1.5 ft is 18.0 in"
    with pytest.raises(TypeError):
        conversion("cat")
    assert conversion({"temperature": ["10", "c", "d"]}) == "10.0 C is Usage: temperature requires 3 arguments in the form of 'degrees, unit, unit'. Available units are 'f, c, k'. D"
