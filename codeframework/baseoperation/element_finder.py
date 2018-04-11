# coding=utf-8

from codeframework.tools.logger import Logger

# 初始化日志对象logger
logger = Logger("ElementFinder")


class ElementFinder(object):

    def __init__(self):
        self.strategies = {
            'identifier': self._find_by_identifier,
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'dom': self._find_by_dom,
            'link': self._find_by_link_text,
            'partial link': self._find_by_partial_link_text,
            'css': self._find_by_css_selector,
            'jquery': self._find_by_sizzle_selector,
            'sizzle': self._find_by_sizzle_selector,
            'tag': self._find_by_tag_name,
            'scLocator': self._find_by_sc_locator,
        }

    def find(self, driver, locator, tag=None):
        assert driver is not None
        assert locator is not None and len(locator) > 0

        (prefix, criteria) = self._parse_locator(locator)
        prefix = 'default' if prefix is None else prefix
        strategy = self.strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        (tag, constraints) = self._get_tag_and_constraints(tag)
        return strategy(driver, criteria, tag, constraints)

    def _find_by_identifier(self, driver, criteria, tag, constraints):
        elements = self._normalize_result(driver.find_elements_by_id(criteria))
        elements.extend(self._normalize_result(driver.find_elements_by_name(criteria)))
        return self._filter_elements(elements, tag, constraints)

    def _find_by_id(self, driver, criteria, tag, constraints):
        return self._filter_elements(driver.find_elements_by_id(criteria), tag, constraints)

    def _find_by_name(self, driver, criteria, tag, constraints):
        return self._filter_elements(driver.find_elements_by_name(criteria), tag, constraints)

    def _find_by_xpath(self, driver, criteria, tag, constraints):
        return self._filter_elements(driver.find_elements_by_xpath(criteria), tag, constraints)

    def _find_by_dom(self, driver, criteria, tag, constraints):
        result = driver.execute_script("return %s;" % criteria)
        if result is None:
            return []
        if not isinstance(result, list):
            result = [result]
        return self._filter_elements(result, tag, constraints)

    def _find_by_sizzle_selector(self, driver, criteria, tag, constraints):
        js = "return jQuery('%s').get();" % criteria.replace("'", "\\'")
        return self._filter_elements(driver.execute_script(js), tag, constraints)

    def _find_by_link_text(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_link_text(criteria), tag, constraints)

    def _find_by_partial_link_text(self, driver, criteria, tag, constraints):
        return self._filter_elements(
            driver.find_elements_by_partial_link_text(criteria), tag, constraints)

    def _find_by_css_selector(self, driver, criteria, tag, constraints):
        return self._filter_elements(driver.find_elements_by_css_selector(criteria), tag, constraints)

    def _find_by_tag_name(self, driver, criteria, tag, constraints):
        return self._filter_elements(driver.find_elements_by_tag_name(criteria), tag, constraints)

    def _find_by_sc_locator(self, driver, criteria, tag, constraints):
        js = "return isc.AutoTest.getElement('%s')" % criteria.replace("'", "\\'")
        return self._filter_elements([driver.execute_script(js)], tag, constraints)

    def _find_by_default(self, driver, criteria, tag, constraints):
        if criteria.startswith('//'):
            return self._find_by_xpath(driver, criteria, tag, constraints)
        return self._find_by_key_attrs(driver, criteria, tag, constraints)

    def _get_tag_and_constraints(self, tag):
        if tag is None:
            return None, {}

        tag = tag.lower()
        constraints = {}
        if tag == 'link':
            tag = 'a'
        if tag == 'partial link':
            tag = 'a'
        elif tag == 'image':
            tag = 'img'
        elif tag == 'list':
            tag = 'select'
        elif tag == 'radio button':
            tag = 'input'
            constraints['type'] = 'radio'
        elif tag == 'checkbox':
            tag = 'input'
            constraints['type'] = 'checkbox'
        elif tag == 'text field':
            tag = 'input'
            constraints['type'] = 'text'
        elif tag == 'file upload':
            tag = 'input'
            constraints['type'] = 'file'
        elif tag == 'text area':
            tag = 'textarea'
        return tag, constraints

    def _element_matches(self, element, tag, constraints):
        if not element.tag_name.lower() == tag:
            return False
        for name in constraints:
            if not element.get_attribute(name) == constraints[name]:
                return False
        return True

    def _filter_elements(self, elements, tag, constraints):
        elements = self._normalize_result(elements)
        if tag is None: return elements
        return filter(
            lambda element: self._element_matches(element, tag, constraints),
            elements)

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return (prefix, criteria)

    def _normalize_result(self, elements):
        if not isinstance(elements, list):
            logger.debug("WebDriver find returned %s" % elements)
            return []
        return elements
