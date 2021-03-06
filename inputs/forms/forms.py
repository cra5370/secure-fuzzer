﻿def get_form_inputs(soup):
    inputs = set()

    for input in soup.find_all('input'):
        d = { 'type' : input['type'] }
        if input.has_attr('name'): d['name'] = input['name']
        if input.has_attr('value'): d['value'] = input['value']
        inputs.add(frozenset(d.items()))

    for input in soup.find_all('select'):
        d = {
           'type' : 'select',
           'options' : tuple(o['value'] for o in input.find_all('option', recursive=False))
        }

        inputs.add(frozenset(d.items()))

    return inputs