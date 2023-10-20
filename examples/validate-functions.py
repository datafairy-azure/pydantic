from pydantic import validate_call
from pydantic.types import conint


@validate_call
def echo_hello(n_times: conint(gt=0, lt=11), name: str, loud: bool):
    """
    Greets someone with an echo.

    Args:
        n_times: How many echos. Min value is 1, max is 10.
        name: Name to greet
        loud: Do you want the greeting to be loud?
    """
    greeting = f"Hello {name}!"

    if loud:
        greeting = greeting.upper() + "!!"

    for i in range(n_times):
        print(greeting)


# Call this function
echo_hello(n_times=1, name="World", loud=True)  # Valid
echo_hello(n_times=10, name="World", loud=True)  # Valid

# The following will raise an error:
echo_hello(n_times=20, name="World", loud=True)  # Invalid!
echo_hello(n_times=1, name=1234, loud=True)  # Invalid!
