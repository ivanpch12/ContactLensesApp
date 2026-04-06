def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_customer(user):
    return user.groups.filter(name='Customer').exists()