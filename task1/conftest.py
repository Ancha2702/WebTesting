import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
S = requests.Session()


@pytest.fixture()
def add_post_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def add_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def add_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def add_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def save_post():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def title_name():
    return f"{data['title']}"


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def btn_selector():
    return "button"


@pytest.fixture()
def error_code():
    return "401"


@pytest.fixture()
def account_name():
    return f"Hello, {data['login']}"


@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def get_description():
    return 'New TESTING1'


@pytest.fixture()
def post_title():
    return 'TestTitle'




