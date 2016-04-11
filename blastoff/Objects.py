import bbcode
import re

def updateParser():
    def render_size(name, value, options, parent, context):
        if 'size' in options:
            size = options['size'].strip()
        elif options:
            size = list(options.keys())[0].strip()
        else:
            return value
        match = re.match(r'^([0-9]+)', size, re.I)
        size = match.group() if match else 'inherit'
        return '<font size=%(size)s>%(value)s</font>' % {
            'size': size,
            'value': value,
        }
    parser = bbcode.Parser(replace_links=False)
    parser.add_simple_formatter('img', '<img src=%(value)s ></img>')
    parser.add_simple_formatter('rtl', '<div style="direction: rtl;">%(value)s</div>')
    parser.add_simple_formatter('ltr', '<div style="direction: ltr;">%(value)s</div>')
    parser.add_simple_formatter('li', '<li></li>')
    parser.add_formatter('size', render_size)
    return parser
