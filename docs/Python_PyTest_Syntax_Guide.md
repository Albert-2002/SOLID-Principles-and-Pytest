# Complete Guide to Pytest

## 1. Basic Test Structure

### Simple Test Function

```python
# test_basic.py

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_string():
    assert "hello".upper() == "HELLO"
```

Run with: `pytest test_basic.py`

### Test Classes

```python
# test_class.py

class TestMath:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_multiplication(self):
        assert 3 * 4 == 12

class TestStrings:
    def test_concatenation(self):
        assert "hello" + " " + "world" == "hello world"
```

## 2. Assertions

### Basic Assertions

```python
# test_assertions.py

def test_equality():
    assert 5 == 5
    assert "test" == "test"

def test_inequality():
    assert 5 != 3
    assert "hello" != "world"

def test_boolean():
    assert True
    assert not False

def test_membership():
    assert 3 in [1, 2, 3, 4]
    assert "a" in "apple"

def test_identity():
    a = [1, 2, 3]
    b = a
    assert a is b

    c = [1, 2, 3]
    assert a is not c
```

### Assertion with Custom Messages

```python
# test_custom_messages.py

def test_with_message():
    x = 10
    assert x == 10, f"Expected 10, but got {x}"

def test_failing_message():
    value = 5
    # This will fail with custom message
    # assert value > 10, f"Value {value} is not greater than 10"
```

### Assertions on Types

```python
# test_types.py

def test_type_checking():
    assert isinstance(5, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2, 3], list)
    assert isinstance({"a": 1}, dict)
```

## 3. Pytest Fixtures

### Basic Fixture

```python
# test_fixtures.py
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum_with_fixture(sample_data):
    assert sum(sample_data) == 15

def test_length_with_fixture(sample_data):
    assert len(sample_data) == 5
```

### Fixture with Setup and Teardown

```python
# test_setup_teardown.py
import pytest

@pytest.fixture
def database_connection():
    # Setup
    print("\nConnecting to database...")
    connection = {"status": "connected"}

    yield connection  # Provide the fixture value

    # Teardown
    print("\nClosing database connection...")
    connection["status"] = "closed"

def test_database_query(database_connection):
    assert database_connection["status"] == "connected"
    # Perform database operations
```

### Fixture Scopes

```python
# test_fixture_scopes.py
import pytest

@pytest.fixture(scope="function")  # Default, runs for each test
def function_scope():
    print("\nFunction scope fixture")
    return "function"

@pytest.fixture(scope="class")
def class_scope():
    print("\nClass scope fixture")
    return "class"

@pytest.fixture(scope="module")
def module_scope():
    print("\nModule scope fixture")
    return "module"

@pytest.fixture(scope="session")
def session_scope():
    print("\nSession scope fixture")
    return "session"

class TestScope:
    def test_one(self, function_scope, class_scope):
        assert function_scope == "function"
        assert class_scope == "class"

    def test_two(self, function_scope, class_scope):
        assert function_scope == "function"
        assert class_scope == "class"
```

### Multiple Fixtures

```python
# test_multiple_fixtures.py
import pytest

@pytest.fixture
def user():
    return {"name": "John", "age": 30}

@pytest.fixture
def admin():
    return {"name": "Admin", "role": "superuser"}

def test_multiple_fixtures(user, admin):
    assert user["name"] == "John"
    assert admin["role"] == "superuser"
```

### Fixture Dependencies

```python
# test_fixture_dependencies.py
import pytest

@pytest.fixture
def base_url():
    return "https://api.example.com"

@pytest.fixture
def api_client(base_url):
    return {"url": base_url, "authenticated": True}

def test_api_call(api_client):
    assert api_client["url"] == "https://api.example.com"
    assert api_client["authenticated"] is True
```

### Autouse Fixtures

```python
# test_autouse.py
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("\nSetting up before test")
    yield
    print("\nTearing down after test")

def test_one():
    assert True

def test_two():
    assert 1 + 1 == 2
```

### Parametrized Fixtures

```python
# test_parametrized_fixtures.py
import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number_squared(number):
    assert number ** 2 in [1, 4, 9]
```

## 4. Parametrization

### Basic Parametrization

```python
# test_parametrize.py
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### Multiple Parameters

```python
# test_multiple_params.py
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (10, 5, 15),
    (100, 200, 300),
    (-1, 1, 0)
])
def test_addition(a, b, result):
    assert a + b == result
```

### Parametrize with IDs

```python
# test_parametrize_ids.py
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16)
], ids=["two_squared", "three_squared", "four_squared"])
def test_square_with_ids(input, expected):
    assert input ** 2 == expected
```

### Multiple Parametrize Decorators

```python
# test_multiple_parametrize.py
import pytest

@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_multiplication(x, y):
    result = x * y
    assert result in [3, 4, 6, 8]
```

### Parametrize with Complex Data

```python
# test_complex_parametrize.py
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ({"a": 1, "b": 2}, 3),
    ({"a": 10, "b": 20}, 30),
    ({"a": -5, "b": 5}, 0)
])
def test_dict_sum(test_input, expected):
    assert sum(test_input.values()) == expected
```

## 5. Marks

### Skip Tests

```python
# test_skip.py
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_new_python_feature():
    assert True
```

### XFail (Expected Failures)

```python
# test_xfail.py
import pytest

@pytest.mark.xfail
def test_known_bug():
    assert 1 + 1 == 3  # Known to fail

@pytest.mark.xfail(reason="Bug #123", strict=True)
def test_strict_xfail():
    assert False  # Must fail, otherwise test fails

@pytest.mark.xfail(raises=ValueError)
def test_expected_exception():
    raise ValueError("Expected error")
```

### Custom Marks

```python
# test_custom_marks.py
import pytest

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(1)
    assert True

@pytest.mark.integration
def test_api_integration():
    assert True

@pytest.mark.unit
def test_unit_function():
    assert 2 + 2 == 4
```

Run specific marks: `pytest -m slow` or `pytest -m "not slow"`

### Multiple Marks

```python
# test_multiple_marks.py
import pytest

@pytest.mark.slow
@pytest.mark.integration
def test_full_integration():
    assert True

@pytest.mark.smoke
@pytest.mark.critical
def test_critical_feature():
    assert True
```

## 6. Exception Testing

### Testing for Exceptions

```python
# test_exceptions.py
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_zero_division():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_exception_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_exception_details():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)

    assert "Cannot divide by zero" in str(exc_info.value)
    assert exc_info.type is ValueError
```

### Testing Multiple Exceptions

```python
# test_multiple_exceptions.py
import pytest

def process_data(data):
    if not data:
        raise ValueError("Data is empty")
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    return data

def test_value_error():
    with pytest.raises(ValueError):
        process_data([])

def test_type_error():
    with pytest.raises(TypeError):
        process_data("not a list")
```

## 7. Warnings Testing

```python
# test_warnings.py
import pytest
import warnings

def legacy_function():
    warnings.warn("This function is deprecated", DeprecationWarning)
    return True

def test_warning():
    with pytest.warns(DeprecationWarning):
        legacy_function()

def test_warning_message():
    with pytest.warns(DeprecationWarning, match="deprecated"):
        legacy_function()
```

## 8. Monkeypatching

### Patching Attributes

```python
# test_monkeypatch_attr.py
import pytest

class Config:
    debug_mode = False
    api_key = "default_key"

def test_with_debug_mode(monkeypatch):
    monkeypatch.setattr(Config, "debug_mode", True)
    assert Config.debug_mode is True

def test_with_custom_api_key(monkeypatch):
    monkeypatch.setattr(Config, "api_key", "test_key_123")
    assert Config.api_key == "test_key_123"
```

### Patching Environment Variables

```python
# test_monkeypatch_env.py
import pytest
import os

def get_environment():
    return os.getenv("ENVIRONMENT", "production")

def test_development_environment(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "development")
    assert get_environment() == "development"

def test_delete_env_var(monkeypatch):
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    assert get_environment() == "production"
```

### Patching Functions

```python
# test_monkeypatch_function.py
import pytest

def external_api_call():
    return "real_api_response"

def my_function():
    return external_api_call()

def test_mocked_api(monkeypatch):
    def mock_api():
        return "mocked_response"

    monkeypatch.setattr("__main__.external_api_call", mock_api)
    assert my_function() == "mocked_response"
```

### Patching Dictionary Items

```python
# test_monkeypatch_dict.py
import pytest

config = {
    "timeout": 30,
    "retry": 3
}

def test_custom_timeout(monkeypatch):
    monkeypatch.setitem(config, "timeout", 60)
    assert config["timeout"] == 60

def test_delete_config_key(monkeypatch):
    monkeypatch.delitem(config, "retry", raising=False)
    assert "retry" not in config
```

## 9. Temporary Files and Directories

### Using tmp_path (Path object)

```python
# test_tmp_path.py
import pytest

def test_create_file(tmp_path):
    # tmp_path is a Path object
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")

    assert test_file.read_text() == "Hello, World!"
    assert test_file.exists()

def test_create_directory(tmp_path):
    test_dir = tmp_path / "subdir"
    test_dir.mkdir()

    test_file = test_dir / "file.txt"
    test_file.write_text("Content")

    assert test_file.exists()
```

### Using tmpdir (Legacy, py.path)

```python
# test_tmpdir.py
import pytest

def test_tmpdir(tmpdir):
    # tmpdir is a py.path.local object
    test_file = tmpdir.join("test.txt")
    test_file.write("Hello")

    assert test_file.read() == "Hello"
```

## 10. Capturing Output

### Capturing stdout/stderr

```python
# test_capsys.py
import pytest

def print_message():
    print("Hello, stdout!")
    print("Error message", file=sys.stderr)

def test_stdout_capture(capsys):
    print("Testing output")
    captured = capsys.readouterr()
    assert "Testing output" in captured.out

def test_stderr_capture(capsys):
    import sys
    print("Error!", file=sys.stderr)
    captured = capsys.readouterr()
    assert "Error!" in captured.err
```

### Disabling Output Capture

```python
# test_capsys_disabled.py
import pytest

def test_with_output(capsys):
    print("This will be captured")

    with capsys.disabled():
        print("This will NOT be captured and shown in terminal")

    print("This will be captured again")
```

### Capturing Binary Output

```python
# test_capfd.py
import pytest
import os

def test_capfd(capfd):
    os.write(1, b"binary output")
    captured = capfd.readouterr()
    assert b"binary output" in captured.out.encode()
```

## 11. Configuration: conftest.py

```python
# conftest.py
import pytest

# Shared fixtures across all test files
@pytest.fixture
def shared_data():
    return {"key": "value"}

@pytest.fixture(scope="session")
def database():
    # Setup
    db = {"connected": True}
    yield db
    # Teardown
    db["connected"] = False

# Hooks
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks integration tests")

def pytest_collection_modifyitems(config, items):
    # Automatically add markers based on test name
    for item in items:
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
```

## 12. Pytest Hooks

### Common Hooks

```python
# conftest.py (hooks example)
import pytest

def pytest_runtest_setup(item):
    print(f"\nSetting up {item.name}")

def pytest_runtest_teardown(item):
    print(f"\nTearing down {item.name}")

def pytest_runtest_makereport(item, call):
    if call.when == "call":
        print(f"\nTest {item.name} {'PASSED' if call.excinfo is None else 'FAILED'}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Access test result
        if report.failed:
            print(f"\nTest {item.name} failed!")
```

## 13. Command Line Options

### Custom Command Line Options

```python
# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests: dev, staging, prod"
    )
    parser.addoption(
        "--slow",
        action="store_true",
        default=False,
        help="Run slow tests"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

# test_cmdline.py
def test_environment(env):
    assert env in ["dev", "staging", "prod"]
    print(f"\nRunning in {env} environment")
```

Run with: `pytest --env=staging` or `pytest --slow`

## 14. Test Organization

### Using Setup and Teardown Methods

```python
# test_setup_methods.py
import pytest

class TestDatabase:
    def setup_method(self):
        """Run before each test method"""
        self.connection = {"status": "connected"}
        print("\nSetup method")

    def teardown_method(self):
        """Run after each test method"""
        self.connection = None
        print("\nTeardown method")

    def test_query(self):
        assert self.connection["status"] == "connected"

    def test_insert(self):
        assert self.connection is not None

class TestAPI:
    def setup_class(cls):
        """Run once before all tests in class"""
        cls.api_key = "test_key"
        print("\nSetup class")

    def teardown_class(cls):
        """Run once after all tests in class"""
        cls.api_key = None
        print("\nTeardown class")

    def test_authentication(self):
        assert self.api_key == "test_key"
```

## 15. Doctest Integration

```python
# test_doctest.py
import pytest

def add(a, b):
    """
    Add two numbers.

    >>> add(2, 3)
    5
    >>> add(10, 20)
    30
    >>> add(-1, 1)
    0
    """
    return a + b

# Run doctests with: pytest --doctest-modules
```

## 16. Pytest-specific Assertions

### Approximate Comparisons

```python
# test_approx.py
import pytest

def test_float_comparison():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 10.0001 == pytest.approx(10, abs=0.01)
    assert 100 == pytest.approx(99, rel=0.01)  # 1% relative tolerance

def test_list_approx():
    assert [1.0, 2.0, 3.0] == pytest.approx([1.0001, 2.0001, 3.0001], abs=0.001)
```

### Checking for Substrings

```python
# test_strings.py
import pytest

def test_substring():
    text = "Hello, World!"
    assert "World" in text
    assert text.startswith("Hello")
    assert text.endswith("!")
```

## 17. Failing Tests Intentionally

```python
# test_fail.py
import pytest

def test_explicit_fail():
    if some_condition:
        pytest.fail("Test failed for specific reason")

def test_conditional_fail():
    result = perform_operation()
    if not validate(result):
        pytest.fail(f"Validation failed: {result}")
```

## 18. Test Fixtures with Parameters from CLI

```python
# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# test_browser.py
def test_browser_selection(browser):
    assert browser in ["chrome", "firefox", "safari"]
    print(f"\nRunning test with {browser}")
```

Run with: `pytest --browser=firefox`

## 19. Dependency Injection with Fixtures

```python
# test_dependency_injection.py
import pytest

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, name):
        if not self.db.connected:
            raise RuntimeError("Database not connected")
        return {"name": name, "id": 1}

@pytest.fixture
def database():
    db = Database()
    db.connect()
    yield db
    db.disconnect()

@pytest.fixture
def user_service(database):
    return UserService(database)

def test_create_user(user_service):
    user = user_service.create_user("Alice")
    assert user["name"] == "Alice"
    assert user["id"] == 1
```

## 20. Testing Asynchronous Code

```python
# test_async.py
import pytest
import asyncio

async def async_function():
    await asyncio.sleep(0.1)
    return "completed"

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == "completed"

@pytest.mark.asyncio
async def test_multiple_async():
    results = await asyncio.gather(
        async_function(),
        async_function()
    )
    assert len(results) == 2
```

Note: Requires `pytest-asyncio` plugin

## 21. Retrying Flaky Tests

```python
# test_retry.py
import pytest
import random

@pytest.mark.flaky(reruns=3)
def test_flaky():
    # Simulating flaky test
    assert random.choice([True, True, False])

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_flaky_with_delay():
    # Retry up to 5 times with 2 second delay
    assert random.choice([True, False])
```

Note: Requires `pytest-rerunfailures` plugin

## 22. Coverage with Pytest

```python
# test_coverage.py

def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")
    return price * (1 - discount_percent / 100)

def test_normal_discount():
    assert calculate_discount(100, 10) == 90

def test_no_discount():
    assert calculate_discount(100, 0) == 100

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
```

Run with: `pytest --cov=module_name --cov-report=html`

## 23. Using pytest.ini or pyproject.toml

```ini
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q --strict-markers
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks tests as slow
    integration: marks integration tests
    unit: marks unit tests
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = ["tests"]
markers = [
    "slow: marks tests as slow",
    "integration: marks integration tests"
]
```

## 24. Logging in Tests

```python
# test_logging.py
import pytest
import logging

def test_with_logging(caplog):
    logger = logging.getLogger(__name__)

    with caplog.at_level(logging.INFO):
        logger.info("Info message")
        logger.warning("Warning message")

    assert "Info message" in caplog.text
    assert "Warning message" in caplog.text
    assert len(caplog.records) == 2

def test_log_levels(caplog):
    logger = logging.getLogger(__name__)

    logger.debug("Debug")
    logger.info("Info")
    logger.warning("Warning")

    assert caplog.records[0].levelname == "DEBUG"
    assert caplog.records[1].levelname == "INFO"
```

## 25. Mocking with unittest.mock

```python
# test_mocking.py
import pytest
from unittest.mock import Mock, MagicMock, patch, call

# Simple Mock
def test_simple_mock():
    mock = Mock()
    mock.method.return_value = 42

    result = mock.method()
    assert result == 42
    mock.method.assert_called_once()

# Mocking Functions
def external_api():
    return "real_response"

def my_function():
    return external_api()

def test_patch_function():
    with patch('__main__.external_api', return_value="mocked_response"):
        result = my_function()
        assert result == "mocked_response"

# Mocking Classes
class EmailService:
    def send(self, to, subject):
        # Actually sends email
        pass

def test_mock_class():
    with patch('__main__.EmailService') as MockEmail:
        mock_instance = MockEmail.return_value
        mock_instance.send.return_value = True

        service = EmailService()
        result = service.send("test@example.com", "Test")

        assert result is True
        mock_instance.send.assert_called_once_with("test@example.com", "Test")

# Mock with Side Effects
def test_side_effect():
    mock = Mock()
    mock.method.side_effect = [1, 2, 3]

    assert mock.method() == 1
    assert mock.method() == 2
    assert mock.method() == 3

# Checking Call Arguments
def test_call_arguments():
    mock = Mock()
    mock.method(1, 2, key="value")

    mock.method.assert_called_with(1, 2, key="value")
    assert mock.method.call_args == call(1, 2, key="value")
```

## 26. Property-based Testing

```python
# test_hypothesis.py
from hypothesis import given
from hypothesis import strategies as st
import pytest

@given(st.integers())
def test_addition_commutative(x):
    y = 5
    assert x + y == y + x

@given(st.lists(st.integers()))
def test_list_reverse(lst):
    assert list(reversed(reversed(lst))) == lst

@given(st.text(), st.text())
def test_string_concatenation(s1, s2):
    result = s1 + s2
    assert len(result) == len(s1) + len(s2)
```

Note: Requires `hypothesis` plugin

## 27. Test Profiling and Duration

```python
# test_duration.py
import pytest
import time

@pytest.mark.timeout(5)
def test_with_timeout():
    time.sleep(1)
    assert True

def test_slow_operation():
    time.sleep(2)
    assert True
```

Run with: `pytest --durations=10` to see slowest 10 tests

## 28. Parallel Test Execution

```python
# test_parallel.py

def test_one():
    assert 1 + 1 == 2

def test_two():
    assert 2 + 2 == 4

def test_three():
    assert 3 + 3 == 6
```

Run with: `pytest -n auto` (requires `pytest-xdist` plugin)

## 29. Testing with Databases

```python
# test_database.py
import pytest
import sqlite3

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    yield conn
    conn.close()

def test_insert_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                   ("Alice", "alice@example.com"))
    db_connection.commit()

    cursor.execute("SELECT * FROM users WHERE name=?", ("Alice",))
    user = cursor.fetchone()

    assert user[1] == "Alice"
    assert user[2] == "alice@example.com"
```

## 30. Advanced Fixture Techniques

### Fixture Factories

```python
# test_fixture_factory.py
import pytest

@pytest.fixture
def make_user():
    def _make_user(name, age):
        return {"name": name, "age": age}
    return _make_user

def test_multiple_users(make_user):
    user1 = make_user("Alice", 30)
    user2 = make_user("Bob", 25)

    assert user1["name"] == "Alice"
    assert user2["age"] == 25
```

### Indirect Parametrization

```python
# test_indirect.py
import pytest

@pytest.fixture
def user(request):
    name = request.param
    return {"name": name, "active": True}

@pytest.mark.parametrize("user", ["Alice", "Bob", "Charlie"], indirect=True)
def test_user_active(user):
    assert user["active"] is True
    assert user["name"] in ["Alice", "Bob", "Charlie"]
```
