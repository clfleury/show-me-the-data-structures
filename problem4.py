class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class User(object):
    def __init__(self, name, key):
        self.name = name
        self.key = key

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    else:
        for subgroup in group.groups:
            if is_user_in_group(user, subgroup) == True:
                return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_user('bob')
parent.add_user('john')

child.add_group(sub_child)
parent.add_group(child)

#Examples
print(is_user_in_group('bob', parent)) #True
print(is_user_in_group('john', parent)) #True
print(is_user_in_group('mary', parent)) #False

#edge cases
print(is_user_in_group(9483948, parent)) #returns False
print(is_user_in_group(['sdfdsf', 'sfdsfdf'], parent)) #returns False