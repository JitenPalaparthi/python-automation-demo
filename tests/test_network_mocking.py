from playwright.sync_api import Page, Route, expect

MOCK_PRODUCTS = [
    {"id": 91, "name": "Mocked USB Hub", "price": 799},
    {"id": 92, "name": "Mocked SSD", "price": 5599},
]


def test_mock_products_api(page: Page) -> None:
    def handle_products(route: Route) -> None:
        route.fulfill(status=200, json=MOCK_PRODUCTS)

    page.route("**/api/products", handle_products)
    page.goto("/")

    expect(page.get_by_role("heading", name="Mocked USB Hub")).to_be_visible()
    expect(page.get_by_role("heading", name="Mocked SSD")).to_be_visible()
