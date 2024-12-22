from django import template

register=template.Library()
@register.filter(name='prod_col')

def prod_col(list_data,pro_col_size):
    i=0
    array=[]
    for data in list_data:
        array.append(data)
        i=i+1
        if i==pro_col_size:
            yield array
            i=0
            array=[]
    if array:
        yield array

       


