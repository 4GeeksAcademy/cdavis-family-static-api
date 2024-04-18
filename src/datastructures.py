from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generateId()
        self._members.append(member)
        return True

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, updated_member):
        for index, member in enumerate(self._members):
            if member["id"] == id:
                self._members[index] = updated_member
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    
    def get_all_members(self):
        return self._members
