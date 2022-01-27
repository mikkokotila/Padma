from re import L


def dictionary_lookup(request):

    from ..utils.tokenization import tokenization
    
    from fastapi import HTTPException
    from app import tokenizer
    from app import dictionary

    '''
    search_query = request.args.get('query')
    no_of_result = request.args.get('no_of_result')
    dictionaries = request.args.get('dictionaries')
    '''

    search_query = request.query_params['query']
    
    try:
        no_of_result = request.query_params['no_of_result']
    except KeyError:
        no_of_result = None
    
    try:
        dictionaries = request.query_params['dictionaries']
    except KeyError:
        dictionaries = None

    if dictionaries != None:
        dictionaries = dictionaries.split(',')
    else:
        from app import available_dictionaries

        dictionaries = available_dictionaries

    if len(search_query) == 0:
        search_query = dictionary['Tibetan'].sample(1).values[0]

    search_query = search_query.replace(' ', '')
    search_query = search_query.replace(' ', '')

    tokens = tokenization(search_query, tokenizer)

    text = []
    source = []

    for token in tokens:

        # get the results
        results = dictionary.lookup(token)
        _dictionaries = list(set(results.keys()).intersection(dictionaries))

        texts_temp = []
        sources_temp = []

        # go through each dictionary in the results
        for _dictionary in _dictionaries:
            for result in results[_dictionary][token]:
                
                texts_temp.append(result)
                sources_temp.append(_dictionary)
    
        text.append(texts_temp)
        source.append(sources_temp)


    data = {'search_query': search_query,
            'text': text,
            'source': source, 
            'tokens': tokens}

    # if no results, return 404
    try: 
        data['text'][0]
    except:
        raise HTTPException(status_code=404)

    return data
