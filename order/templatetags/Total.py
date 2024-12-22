from django import template

register=template.Library()

@register.simple_tag(name='Total')


def Total(cart):
    total=0
    for cart_sam in cart.added_items.all():

        total +=cart_sam.quantity*cart_sam.producte.price

    return total


       


