from selenium.webdriver.common.by import By


class SearchBlockLocator(object):
    _search_block_class_locator = "Search"
    _search_class_button_locator = "pt-search"
    _close_class_button_locator = "pt-close"
    _search_select_class_locator = "Search__select"
    _exact_match_checkbox_class_locator = "exact show"
    _search_action_class_button = "Search__btn"
    _search_input_class_edit = "Search__input"

    SEARCH_BLOCK = (By.CLASS_NAME, _search_block_class_locator)
    SEARCH_BUTTON = (By.CLASS_NAME, _search_class_button_locator)
    CLOSE_BUTTON = (By.CLASS_NAME, _close_class_button_locator)
    SEARCH_SELECT = (By.CLASS_NAME, _search_select_class_locator)
    EXACT_MATCH_CHBOX = (By.CLASS_NAME, _exact_match_checkbox_class_locator)
    SEARCH_ACTION_BUTTON = (By.CLASS_NAME, _search_action_class_button)
    SEARCH_INPUT = (By.CLASS_NAME, _search_input_class_edit)

    def get_search_button(self):
        return self.SEARCH_BUTTON

    def get_close_button(self):
        return self.CLOSE_BUTTON
