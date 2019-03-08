from typing import Dict, List
import re

##############################################################################


class Cleaner():
    def __init__(self,
                 key_abbreviation: Dict[str, str] = {},
                 value_abbreviation: Dict[str, Dict[str, str]] = {},
                 necessary_keys: List[str] = [],
                 regex_book: Dict[str, str] = {}):

        self._key_abbreviation = key_abbreviation
        self._value_abbreviation = value_abbreviation
        self._necessary_keys = necessary_keys
        self._regex_book = regex_book

##############################################################################

    def clean(self, entity: Dict[str, str]) -> Dict[str, str]:
        try:
            if self._key_abbreviation:
                entity = self._clean_keys(entity)
            if self._value_abbreviation:
                entity = self._clean_values(entity)
            if self._necessary_keys:
                self._check_necessary_keys(entity)
            if self._regex_book:
                self._check_values(entity)
            return entity
        except ValueError as err:
            raise err

##############################################################################

    def _clean_keys(self, entity: Dict[str, str]) -> Dict[str, str]:

        new_entity: Dict[str, str] = {}

        for key in entity:
            if key in self._key_abbreviation:
                k = self._key_abbreviation[key]
            else:
                k = key

            new_entity[k] = entity[key]

        return new_entity

##############################################################################

    def _clean_values(self, entity: Dict[str, str]) -> Dict[str, str]:

        new_entity: Dict[str, str] = {}

        for key in entity:
            new_entity[key] = entity[key]

            if key in self._value_abbreviation:
                short_value = entity[key]
                if short_value in self._value_abbreviation[key]:
                    value = self._value_abbreviation[key][short_value]

                    new_entity[key] = value

        return new_entity

##############################################################################

    def _check_necessary_keys(self, entity: Dict[str, str]) -> None:

        for key in self._necessary_keys:
            if key not in entity:
                raise ValueError("NO NECESSARY KEY: {}".format(key))

##############################################################################

    def _check_values(self, entity: Dict[str, str]) -> None:

        for key in entity:
            value = entity[key].strip().lower()

            if value == "":
                continue

            regex = self._regex_book.get(key, None)
            if not regex:
                continue

            if not re.match(regex, value, re.DOTALL):
                raise ValueError("INVALID KEY VALUE PAIR: {}={}".format(
                    key, value))


##############################################################################
