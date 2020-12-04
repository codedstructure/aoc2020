import re
from utils import get_blank_sep_fields


class Passport:
    def __init__(self, fields):
        self.fields = fields

    mandatory_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    optional_fields = {'cid'}

    def valid(self):
        return (len(set(self.fields) & self.mandatory_fields)
                == len(self.mandatory_fields))

    @property
    def byr(self):
        return self.fields['byr']

    @property
    def iyr(self):
        return self.fields['iyr']

    @property
    def eyr(self):
        return self.fields['eyr']

    @property
    def hgt(self):
        return self.fields['hgt']

    @property
    def hcl(self):
        return self.fields['hcl']

    @property
    def ecl(self):
        return self.fields['ecl']

    @property
    def pid(self):
        return self.fields['pid']

    @property
    def cid(self):
        return self.fields['cid']

    def extra_valid(self):
        if not self.valid():
            return False

        if (not self.byr.isdigit()
                or len(self.byr) != 4
                or not 1920 <= int(self.byr) <= 2002):
            return False

        if (not self.iyr.isdigit()
                or len(self.iyr) != 4
                or not 2010 <= int(self.iyr) <= 2020):
            return False

        if (not self.eyr.isdigit()
                or len(self.eyr) != 4
                or not 2020 <= int(self.eyr) <= 2030):
            return False

        if not self.hgt.endswith(('cm', 'in')):
            return False
        if self.hgt.endswith('in') and not 59 <= int(self.hgt[:-2]) <= 76:
            return False
        if self.hgt.endswith('cm') and not 150 <= int(self.hgt[:-2]) <= 193:
            return False

        if not re.match(r'^#[0-9a-f]{6}$', self.hcl):
            return False

        if self.ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return False

        if not re.match(r'^[0-9]{9}$', self.pid):
            return False

        return True


def puzzle1():
    count = 0
    for fields in get_blank_sep_fields('day4'):
        if Passport(fields).valid():
            count += 1
    print(count)


def puzzle2():
    count = 0
    for fields in get_blank_sep_fields('day4'):
        if Passport(fields).extra_valid():
            count += 1
    print(count)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
