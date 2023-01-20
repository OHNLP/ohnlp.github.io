from pelican import signals

def filter_pg2path(page_name):
    '''
    Get the path according to page_name
    '''
    if page_name == 'index':
        # ok it's the homepage
        return '.'
    else:
        return '..'


def filter_pg2act_nav(output_file, target):
    '''
    Get the active nav item
    '''
    if output_file == target:
        return 'active'

    return ''


def add_all_filters(pelican):
    """Add (register) all filters to Pelican."""
    pelican.env.filters.update({"pg2path": filter_pg2path})
    pelican.env.filters.update({"pg2act_nav": filter_pg2act_nav})


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_all_filters)