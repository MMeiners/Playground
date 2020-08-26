# Problem: given a variable number of inputs, generate a basic xml tag
# Input: variable number of arguments to a function
# Output: xml tag formatted based on number of inputs.  First arg is the tag name.  Second arg is the value in the
#         tag.  Other name-value pairs are attributes of the tag.

def make_xml_tag(tag_name: str, tag_value: str = '', **kwargs) -> str:
    """ Format the inputs into a proper xml tag string """

    tag_attributes = ''

    for attribute, value in kwargs.items():
        tag_attributes += f' {attribute}="{value}"'

    return f'<{tag_name}{tag_attributes}>{tag_value}</{tag_name}>'


print(make_xml_tag('test', 'my content', a=1, b=2, c=3))
