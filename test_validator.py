from validator import validate_cnic, validate_phone, InvalidCnicError, InvalidPhoneError
import pytest

def test_valid_cnic():
    assert validate_cnic("42101-1234567-1") == True

def test_invalid_cnic():
    with pytest.raises(InvalidCnicError):
        validate_cnic("4210112345671")

def test_valid_phone():
    assert validate_phone("0300-1234567") == True

def test_invalid_phone():
    with pytest.raises(InvalidPhoneError):
        validate_phone("1300-1234567")